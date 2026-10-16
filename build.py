from pathlib import Path
root = Path(__file__).resolve().parent
p = root / "src"
s = (p / "template.html").read_text().replace("__DATA__", (p / "data.json").read_text().replace("</", "<\\/"))
s = s.replace("</style>", "\n" + (p / "light.css").read_text() + "\n</style>", 1)
s = s.replace("</script>", "\n" + (p / "detail.js").read_text() + "\ntab(names[location.hash.slice(1)]?location.hash.slice(1):'overview');\n</script>")
s = s.replace('Attention is visible.<br><span style="color:var(--lime)">Intent needs a closer look.</span>', 'Whitefield Union<br><span style="color:var(--lime)">Social media performance review.</span>')
s = s.replace('A source-backed review of 64 Instagram posts, audience participation and competitive discovery journeys. Explore the evidence behind every growth decision.', '64 post records. 759 collected comments. 4,971 observed liker/post pairs. Explore publishing patterns, conversation themes and audience overlap, with the original evidence behind the findings.')
(root / "index.html").write_text(s)
print("Built index.html")
