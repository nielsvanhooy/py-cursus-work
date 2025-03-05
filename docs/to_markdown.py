import markdown
import re
import os
from bs4 import BeautifulSoup  # Required for modifying index structure
from collections import defaultdict

# Define paths
SOURCE_DIR = os.path.abspath(os.path.join(os.getcwd(), "../python-beginner"))  # One level up
OUTPUT_DIR = os.path.join(os.getcwd())  # "result" folder in script's directory

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_markdown_to_html(md_text, filename=None):
    """Convert Markdown to HTML. Special handling for index.md."""
    # Add the toc extension to support internal links
    html = markdown.markdown(md_text, extensions=["fenced_code", "nl2br", "tables", "extra", "toc"])

    # Ensure <code> blocks have Prism.js class names
    html = re.sub(r'<code class="(\w+)"', r'<code class="language-\1"', html)

    # Fix internal links by adding ids to headers
    soup = BeautifulSoup(html, "html.parser")

    # Process all headers to ensure they have proper ids for linking
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if not header.get('id'):
            # Create an id from the header text
            header_id = header.get_text().lower().replace(' ', '-')
            # Remove any special characters
            header_id = re.sub(r'[^\w-]', '', header_id)
            header['id'] = header_id

    # Fix internal links to use the proper format
    for anchor in soup.find_all('a'):
        href = anchor.get('href')
        if href and href.startswith('#'):
            # This is an internal link
            # Make sure the target exists
            target_id = href[1:]  # Remove the # character
            target = soup.find(id=target_id)
            if not target:
                # Try to find a header with similar text
                header_text = target_id.replace('-', ' ').title()
                similar_headers = soup.find_all(string=lambda text: text and header_text in text)
                if similar_headers and similar_headers[0].parent.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    # Use the parent header's id or create one
                    header = similar_headers[0].parent
                    if not header.get('id'):
                        header['id'] = target_id

    html = str(soup)

    # Apply special formatting only if processing the index page
    if filename and filename.lower() == "index.md":
        html = modify_index_structure(html)

    return wrap_html_template(html)

def modify_index_structure(html):
    """Modify the structure of index.html to separate 'Exercises' and group them by type."""
    soup = BeautifulSoup(html, "html.parser")

    exercise_items = []
    general_items = []
    cheat_sheet_items = []  # New list for cheat sheet items

    for li in soup.find_all("li"):
        item_text = li.get_text().lower()
        # Check if it's a cheat sheet item
        if "cheat sheet" in item_text:
            cheat_sheet_items.append(li)
        # Check if it's an exercise item
        elif "exercise" in item_text or "exercises" in item_text:
            exercise_items.append(li)
        else:
            general_items.append(li)

    # Group exercises by their first word
    exercise_groups = defaultdict(list)

    for item in exercise_items:
        link_text = item.find('a').get_text() if item.find('a') else item.get_text()
        # Extract the first words from filename patterns like "For Loop Exercises"
        if "For Loop" in link_text:
            group_name = "For Loop"
            exercise_groups[group_name].append(item)
        elif "Control Structures" in link_text:
            group_name = "Control Structures"
            exercise_groups[group_name].append(item)
        elif "Lists And List Methods" in link_text:
            group_name = "Lists And List Methods"
            exercise_groups[group_name].append(item)
        elif "Milestone" in link_text:
            group_name = "Milestone"
            exercise_groups[group_name].append(item)
        elif "While Loops" in link_text:
            group_name = "While Loops"
            exercise_groups[group_name].append(item)
        elif "Dictionary" in link_text:
            group_name = "Dictionaries"
            exercise_groups[group_name].append(item)
        elif "other-datastructures" in link_text:
            group_name = "Datastractures-beginner"
            exercise_groups[group_name].append(item)
        elif "Functions" in link_text:
            group_name = "Functions"
            exercise_groups[group_name].append(item)
        else:
            # Fallback for items that don't match any pattern
            exercise_groups['Other'].append(item)

    # Build HTML with separate sections
    html_content = ""

    # Add cheat sheets section first if there are any
    if cheat_sheet_items:
        html_content += f"<h2 id='cheat-sheets'>Cheat Sheets</h2><ul>{''.join(str(item) for item in cheat_sheet_items)}</ul>"

    # Add index section
    html_content += f"<h2 id='index'>Index</h2><ul>{''.join(str(item) for item in general_items)}</ul>"

    # Add exercises section with subheaders
    exercises_html = "<h2 id='exercises'>Exercises</h2>"

    # Custom order for the groups
    group_order = [
        "Milestone",
        "Control Structures",
        "For Loop",
        "Lists And List Methods",
        "While Loops",
        "Dictionaries",
        "Datastructures-beginner",
        "Functions",
        "Other"
    ]

    for group_name in group_order:
        items = exercise_groups.get(group_name, [])
        if items:  # Only add groups that have items
            # Sort items so that "Exercises.Html" comes before "Exercises 2.Html", etc.
            sorted_items = sorted(items, key=lambda item:
            '1' + str(item) if 'Exercises.Html' in str(item) else
            '2' + str(item) if 'Exercises 2.Html' in str(item) else
            '3' + str(item) if 'Exercises 3.Html' in str(item) else
            str(item))

            group_id = group_name.lower().replace(' ', '-')
            exercises_html += f"<h3 id='{group_id}' class='exercise-type'>{group_name}</h3><ul>{''.join(str(item) for item in sorted_items)}</ul>"

    return html_content + exercises_html

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
            h3.exercise-type {{
                color: #50FA7B;
                margin-left: 20px;
                font-size: 1.3em;
                margin-top: 30px;
                margin-bottom: 10px;
            }}
            /* Style for cheat sheets section heading */
            #cheat-sheets {{
                color: #FF79C6;
            }}
            /* Add smooth scrolling for internal links */
            html {{
                scroll-behavior: smooth;
            }}
            /* Add visual indication for link targets */
            :target {{
                background-color: rgba(255, 121, 198, 0.2);
                padding: 5px;
                border-radius: 3px;
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