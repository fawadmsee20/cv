import json
import codecs

try:
    with codecs.open('papers.json', 'r', encoding='utf-8') as f:
        papers = json.load(f)
except:
    with codecs.open('papers.json', 'r', encoding='utf-16le') as f:
        content = f.read().strip('\ufeff')
        papers = json.loads(content)

journals = []
conferences = []

for p in papers:
    ven = p.get('venue', '').lower()
    if 'journal' in ven or 'ieee' in ven or 'sensors' in ven or 'symmetry' in ven or 'internet of things' in ven or 'technologies' in ven or 'computers' in ven or 'authorea' in ven:
        journals.append(p)
    elif ven.strip() != '':
        conferences.append(p)

def sort_by_year(p):
    y = p.get('year', '')
    if not y: return 0
    try: return int(y)
    except: return 0

journals.sort(key=sort_by_year, reverse=True)
conferences.sort(key=sort_by_year, reverse=True)

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Publications - Fawad Khan</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="stanford-header"><div class="stanford-header-inner"><a href="index.html" class="university-brand">KENTECH Profiles</a></div></header>
  <section class="hero-wrapper"><div class="hero-inner"><div class=\"profile-photo-container\"><img src="FawadProfile.jpeg"></div><div class="profile-info"><h1 class="profile-name">Fawad Khan</h1><div class="profile-titles"><strong>PostDoc Researcher</strong><br>EnergyAI Lab, Korea Institute of Energy Technology</div></div></div></section>
  <nav class="tabs-container">
    <div class="tabs-inner" id="nav-tabs">
      <a href="index.html" class="nav-tab">Home</a>
      <a href="research.html" class="nav-tab">Research & Scholarship</a>
      <a href="teaching.html" class="nav-tab">Teaching</a>
      <a href="publications.html" class="nav-tab active">Publications</a>
      <a href="experience.html" class="nav-tab">Experience</a>
      <a href="education.html" class="nav-tab">Education</a>
      <a href="cv.html" class="nav-tab">CV</a>
    </div>
  </nav>
  <main class="main-wrapper">
    <div class="content-area">
      <h2 class="section-title">Journal Articles</h2>
      <div class="pub-list">
"""

for p in journals:
    html += f"""        <div class="pub-item">
          <div class="pub-title">{p.get('title', '')}</div>
          <div class="pub-authors">{p.get('authors', '')}</div>
          <div class="pub-venue">{p.get('venue', '')} {f"({p.get('year')})" if p.get('year') else ''}</div>
        </div>\n"""

html += """      </div>
      <h2 class="section-title">Conference Proceedings</h2>
      <div class="pub-list">
"""

for p in conferences:
    html += f"""        <div class="pub-item">
          <div class="pub-title">{p.get('title', '')}</div>
          <div class="pub-authors">{p.get('authors', '')}</div>
          <div class="pub-venue">{p.get('venue', '')} {f"({p.get('year')})" if p.get('year') else ''}</div>
        </div>\n"""

html += """      </div>
    </div>
  </main>
  <script src="app.js"></script>
</body>
</html>"""

with codecs.open('publications.html', 'w', encoding='utf-8') as f:
    f.write(html)
