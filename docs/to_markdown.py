import markdown
import re
import os
from bs4 import BeautifulSoup  # Required for modifying index structure

# Define paths
SOURCE_DIR = os.path.abspath(os.path.join(os.getcwd(), "../python-beginner"))  # One level up
OUTPUT_DIR = os.path.join(os.getcwd())  # "result" folder in script's directory

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_markdown_to_html(md_text, filename=None):
    """Convert Markdown to HTML. Special handling for index.md."""
    html = markdown.markdown(md_text, extensions=["fenced_code", "nl2br", "tables", "extra"])

    # Ensure <code> blocks have Prism.js class names
    html = re.sub(r'<code class="(\w+)"', r'<code class="language-\1"', html)

    # Apply special formatting only if processing the index page
    if filename and filename.lower() == "index.md":
        html = modify_index_structure(html)

    return wrap_html_template(html)

def modify_index_structure(html):
    """Modify the structure of index.html to separate 'Exercises'."""
    soup = BeautifulSoup(html, "html.parser")

    exercise_items = []
    general_items = []

    for li in soup.find_all("li"):
        if "Exercise" in li.get_text() or "Exercises" in li.get_text():
            exercise_items.append(li)
        else:
            general_items.append(li)

    # Build modified HTML with separate sections
    index_html = f"<h2>Index</h2><ul>{''.join(str(item) for item in general_items)}</ul>"
    exercises_html = f"<h2>Exercises</h2><ul>{''.join(str(item) for item in exercise_items)}</ul>" if exercise_items else ""

    return index_html + exercises_html

def wrap_html_template(content):
    """Wrap content in a styled HTML template with Prism.js."""
    table_css = """
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #666;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #2d2d2d;
        }
        tr:nth-child(even) {
            background-color: #383a46;
        }
        tr:nth-child(odd) {
            background-color: #2d2d2d;
        }
    """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Python Course</title>
        <link rel="stylesheet" href="github-markdown-dark.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #44475A;
                color: white;
            }}
            pre {{
                padding: 10px;
                border-radius: 5px;
                background: #2d2d2d;
                color: #ccc;
                overflow-x: auto;
            }}
            details summary {{
                font-weight: bold;
                color: #FF79C6;
            }}
            details p {{
                font-weight: bold;
                margin-left: 40px;
            }}
            {table_css}
            .markdown-content {{
                max-width: 1000px;
                width: 90%;
                padding: 20px;
                background: #44475A;
                color: #ccc;
                border-radius: 8px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
            }}
            .markdown-body hr {{
                height: 0.50em;
                background-color: #8BE9FD;
            }}
        </style>
    </head>
    <body class="markdown-body">
        <div class="markdown-content">{content}</div>

        <!-- Load Prism.js -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
        <script>Prism.highlightAll();</script>
    </body>
    </html>
    """

def process_markdown_files():
    """Find all '*.en.md' files, convert them to HTML, and save them in 'result/'."""
    if not os.path.exists(SOURCE_DIR):
        print(f"❌ Source directory not found: {SOURCE_DIR}")
        return

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith("en.md")]

    if not files:
        print("⚠️ No matching Markdown files found.")
        return

    for file in files:
        file_name = re.sub(r'[-_]en\.md$', '', file, flags=re.IGNORECASE)
        input_path = os.path.join(SOURCE_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, f"{file_name}.html")

        with open(input_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()

        html_content = convert_markdown_to_html(markdown_text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ Converted: {file} → {output_path}")

def create_index_md():
    """Generate an index.md file linking to all converted HTML files."""
    html_files = sorted(f for f in os.listdir(OUTPUT_DIR) if f.endswith(".html") and f != "index.html")

    index_md_content = "# Index (links are clickable)\n\n"

    for html_file in html_files:
        display_name = re.sub(r'[-_]en\.html$', '', html_file, flags=re.IGNORECASE)
        display_name = display_name.replace("-", " ").title()
        index_md_content += f"- [{display_name}]({html_file})\n"

    index_md_path = os.path.join(OUTPUT_DIR, "index.md")
    with open(index_md_path, "w", encoding="utf-8") as f:
        f.write(index_md_content)

    print("✅ Created index.md")
    convert_index_md_to_html(index_md_path)

def convert_index_md_to_html(md_file):
    """Convert the index.md file to an HTML page with separate 'Exercises' section."""
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = convert_markdown_to_html(md_content, filename="index.md")

    index_html_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Converted index.md to index.html")

# Run the script
process_markdown_files()
print("🎉 Conversion complete! Check the 'result/' folder.")
create_index_md()
print("🎉 Created and converted index page complete! Check the 'result/' folder.")
