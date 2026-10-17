"""Verify self-contained resources, selection, contrast, and safe installation."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT/'skills/mobbin-site-builder'
sys.path.insert(0,str(SKILL/'scripts'))
from design_engine import read, recommend, contrast, css_tokens


class OfflineTests(unittest.TestCase):
    def brief(self, purpose='생활용품 쇼핑몰', action='구매', vibes=None):
        return dict(purpose=purpose, audience='일반 사용자',primary_action=action,vibes=vibes or ['선명'],constraints={'avoid':[]},brand={'name':'샘플'})

    def test_matching_directions_and_local_images(self):
        result = recommend(self.brief())
        self.assertEqual(result['layout']['id'],'commerce')
        self.assertEqual(result['directions'][0]['style']['id'],'bold-commerce')
        self.assertEqual(len({d['style']['silhouette'] for d in result['directions']}),3)
        for direction in result['directions']:
            self.assertTrue(direction['references'])
            for ref in direction['references']:
                self.assertTrue((SKILL/ref['local_image']).is_file())

    def test_all_references_resolve_offline(self):
        data=read('library.json')
        for ref in data:
            for s in ref.get('screens',[{'id':ref['id']}]):
                self.assertTrue((SKILL/'assets/references'/f'{s["id"]}.jpg').is_file())
            self.assertNotIn('image_url',ref)

    def test_avoids_are_respected(self):
        brief=self.brief();brief['constraints']['avoid']=['bold-commerce']
        self.assertNotIn('bold-commerce',[d['style']['id'] for d in recommend(brief)['directions']])

    def test_text_and_buttons_have_contrast(self):
        for style in read('styles.json'):
            t=style['tokens']
            for surface in (t['background'],t['surface']):
                self.assertGreaterEqual(contrast(t['text'],surface),4.5,style['id'])
                self.assertGreaterEqual(contrast(t['muted'],surface),4.5,style['id'])
            on='#ffffff' if contrast(t['accent'],'#ffffff')>=contrast(t['accent'],'#111111') else '#111111'
            self.assertGreaterEqual(contrast(t['accent'],on),4.5,style['id'])
        self.assertIn('--accent-ink:',css_tokens(read('styles.json')[0],'#ffff00'))
        with self.assertRaises(ValueError):css_tokens(read('styles.json')[0],'red; } body { display:none')

    def test_native_agent_paths_and_refusal_to_overwrite(self):
        spec=importlib.util.spec_from_file_location('installer',ROOT/'scripts/install.py')
        installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)
        with tempfile.TemporaryDirectory() as temp:
            for agent,directory in [('claude','.claude'),('codex','.agents'),('opencode','.opencode'),('grok','.grok')]:
                dest=installer.target(agent,temp)
                self.assertEqual(dest,Path(temp)/directory/'skills/mobbin-site-builder')
                installer.install(dest,text_only=True)
                self.assertTrue((dest/'SKILL.md').is_file())
                self.assertTrue((dest/'scripts/recommend.py').is_file())
                with self.assertRaises(ValueError):installer.install(dest,text_only=True)
                updated=installer.install(dest,replace=True,text_only=True)
                self.assertTrue(Path(updated['backup']).is_dir())
            foreign=Path(temp)/'foreign';foreign.mkdir()
            with self.assertRaises(ValueError):installer.install(foreign,replace=True,text_only=True)

    def test_scaffold_preserves_existing_work_and_escapes_brand(self):
        with tempfile.TemporaryDirectory() as temp:
            base=Path(temp);brief=self.brief();brief['brand']['name']='</script><script>window.INJECTED=1</script>'
            source=base/'brief.json';source.write_text(json.dumps(brief));dest=base/'site'
            cmd=[sys.executable,str(SKILL/'scripts/scaffold.py'),'--brief',str(source),'--output',str(dest)]
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertNotIn('</script>',(dest/'config.js').read_text())
            self.assertIn('\\u003c',(dest/'config.js').read_text())
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,2)


if __name__=='__main__':unittest.main()
