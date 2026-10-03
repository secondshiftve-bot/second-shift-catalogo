#!/usr/bin/env python3
"""Genera nube.html: la app en un solo archivo para publicarla como Artifact
de claude.ai (con base de datos en la nube). Ejecutar tras cambiar la app:
    python3 finanzas/build-nube.py
"""
import pathlib
import re

here = pathlib.Path(__file__).parent
html = (here / 'index.html').read_text(encoding='utf-8')
css = (here / 'css' / 'styles.css').read_text(encoding='utf-8')
js = (here / 'js' / 'app.js').read_text(encoding='utf-8')

body = re.search(r'<body>(.*)</body>', html, re.S).group(1)
body = body.replace('<script src="js/app.js"></script>', '').strip()
assert '</script' not in js

out = f"""<title>Second Shift Finanzas</title>
<style>
{css}
</style>
{body}
<script>
{js}
</script>
"""
(here / 'nube.html').write_text(out, encoding='utf-8')
print('nube.html generado:', len(out), 'bytes')
