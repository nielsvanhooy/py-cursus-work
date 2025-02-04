import markdown
import re
import os

# Define paths
SOURCE_DIR = os.path.abspath(os.path.join(os.getcwd(), "../python-beginner"))  # One level up
OUTPUT_DIR = os.path.join(os.getcwd(), "result")  # "result" folder in script's directory

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_markdown_to_html(md_text):
    """Convert Markdown to HTML with Prism.js-compatible syntax highlighting."""
    # Convert markdown to HTML
    html = markdown.markdown(md_text, extensions=["fenced_code", "nl2br"])

    # Ensure <code> blocks have Prism.js class names
    html = re.sub(r'<code class="(\w+)"', r'<code class="language-\1"', html)

    # Wrap HTML in a full template with Prism.js
    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Markdown to HTML</title>
        <link rel="stylesheet" href="github-markdown-dark.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
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
                color: #1829a3;
            }}
            details p {{
                font-weight: bold
            }}
        </style>
    </head>
    <body class="markdown-body">
        <div class="markdown-content">{html}</div>

        <!-- Load Prism.js -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
        <script>Prism.highlightAll();</script>
    </body>
    </html>
    """
    return html_output

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
        # Remove '-En' from the filename (case-insensitive match)
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

    index_md_content = "# Index of Converted Pages\n\n"

    for html_file in html_files:
        # Remove '-En' from the filename and format it for display in the link
        display_name = re.sub(r'[-_]en\.html$', '', html_file, flags=re.IGNORECASE)
        display_name = display_name.replace("-", " ").title()

        index_md_content += f"- [{display_name}]({html_file})\n"

    # Write index.md
    index_md_path = os.path.join(OUTPUT_DIR, "index.md")
    with open(index_md_path, "w", encoding="utf-8") as f:
        f.write(index_md_content)

    print("✅ Created index.md")

    # Convert index.md to index.html using the convert_markdown_to_html function
    convert_index_md_to_html(index_md_path)

def convert_index_md_to_html(md_file):
    """Convert the index.md file to an HTML page with proper styling."""
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = convert_markdown_to_html(md_content)

    # Save as index.html in OUTPUT_DIR
    index_html_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Converted index.md to index.html")

# Run the script
process_markdown_files()
print("🎉 Conversion complete! Check the 'result/' folder.")
create_index_md()
print("🎉 Created and converted index page complete! Check the 'result/' folder.")
