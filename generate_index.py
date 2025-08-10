site_title = "UpWord Quiz"
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
html_files.sort()

links_html = "\n".join(
    f'    <li><a href="{file}">{os.path.splitext(file)[0].replace("-", " ").title()}</a></li>'
    for file in html_files
)

html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{site_title}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      max-width: 700px;
      margin: 2rem auto;
      padding: 1rem;
      background-color: #f7f7f7;
      color: #333;
    }}
    h1 {{
      color: #005aa7;
    }}
    ul {{
      padding-left: 1.2rem;
    }}
    li {{
      margin-bottom: 0.6rem;
    }}
    a {{
      text-decoration: none;
      color: #0066cc;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .note {{
      color: gray;
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>
  <h1>Welcome to {site_title}</h1>
  <p>Select a quiz below:</p>
  <ul>
{links_html}
  </ul>
  <p class="note">💡 Tous les quiz sont en anglais.</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ index.html mis à jour avec {len(html_files)} fichiers.")
