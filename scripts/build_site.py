"""Build methodology.html from METHODOLOGY.md so the site carries the method, not just a link to it.

Run after editing METHODOLOGY.md:  python3 scripts/build_site.py
Requires: pip install markdown
"""
import pathlib, re, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
md = (ROOT / "METHODOLOGY.md").read_text(encoding="utf-8")
body = markdown.markdown(md, extensions=["tables", "toc", "sane_lists"],
                         extension_configs={"toc": {"slugify": lambda v, sep: re.sub(r"[^a-z0-9]+", "-", v.lower()).strip("-")}})
body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Methodology · AI Molecules in the Clinic</title>
<meta name="description" content="How the AI Molecules in the Clinic registry defines, finds and codes AI-derived molecules dosed in humans, and the limits of the count.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 16 16%22%3E%3Ccircle cx=%225%22 cy=%2211%22 r=%223%22 fill=%22%233A4BA8%22/%3E%3Ccircle cx=%2211%22 cy=%225%22 r=%223%22 fill=%22%23C2366F%22/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,500;7..72,650&family=Public+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="./">AI Molecules in the Clinic</a>
  <nav aria-label="Site"><a href="./#registry">Registry</a><a href="question.html">The question</a><a href="methodology.html" aria-current="page">Methodology</a><a href="./#corrections">Corrections</a></nav>
</header>
<main class="prose">
{body}
</main>
<footer><p>Independent analysis by John Milad. Not peer-reviewed. Data licensed CC BY 4.0, code MIT. Generated from <a href="https://github.com/JEM-Fizbit/ai-molecules-in-the-clinic/blob/main/METHODOLOGY.md">METHODOLOGY.md</a>.</p></footer>
</div>
</body>
</html>
"""
(ROOT / "methodology.html").write_text(html, encoding="utf-8")
print("wrote methodology.html")
