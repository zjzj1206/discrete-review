"""Parse Markdown math before emphasis; render locally with KaTeX at build time."""
from pathlib import Path
import json, subprocess
from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
ROOT = Path(__file__).resolve().parent

def make_markdown(texts):
    formulas = {}
    def render_math(tex, options):
        key = (tex, options["display_mode"])
        return formulas.setdefault(key, "")
    md = MarkdownIt("commonmark", {"html": False}).enable("table")
    md.use(dollarmath_plugin, allow_labels=False, allow_space=False,
           allow_digits=False, renderer=render_math)
    for text in texts:
        md.render(text)
    keys = list(formulas)
    if keys:
        result = subprocess.run(["node", str(ROOT / "render-math.mjs")],
            input=json.dumps(keys), text=True, capture_output=True, check=True)
        formulas.update(zip(keys, json.loads(result.stdout), strict=True))
    return md
