import requests
from bs4 import BeautifulSoup
import html2text
import re
import sys
import os

def fetch_and_convert_to_markdown(url, output_file=None, content_class='content-main'):
    """
    Fetch content from a webpage and convert it to Markdown.

    Args:
        url (str): The URL of the webpage to extract content from
        output_file (str): The filename to save the Markdown to (or None to just return the content)
        content_class (str): The CSS class containing the main content

    Returns:
        str: Markdown formatted content
    """
    print(f"Fetching content from {url}...")

    # Set up headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Fetch the webpage content
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the page title
        title = soup.title.string if soup.title else "Converted Content"
        clean_title = title.strip()

        # Find the main content container
        content_container = soup.find(class_=content_class)

        if not content_container:
            print(f"Error: Could not find content with class '{content_class}'")
            # Try to find any significant content
            content_container = soup.find('article') or soup.find('main') or soup.find('body')
            if not content_container:
                return None
            print(f"Using fallback content container: {content_container.name}")

        # Initialize HTML to text converter with appropriate settings
        h2t = html2text.HTML2Text()
        h2t.ignore_links = False
        h2t.ignore_images = False
        h2t.ignore_tables = False
        h2t.body_width = 0  # Don't wrap text
        h2t.unicode_snob = True  # Use Unicode characters instead of their ASCII approximations

        # Convert to markdown
        markdown_content = h2t.handle(str(content_container))

        # Clean up the markdown
        # Remove excessive newlines
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)

        # Improve table formatting
        markdown_content = re.sub(r'\n\[\|\s+', '\n|', markdown_content)

        # Add title at the beginning
        markdown_content = f"# {clean_title}\n\n{markdown_content}"

        # Save to file if requested
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"Successfully saved markdown to {output_file}")

        print(f"Conversion completed - {len(markdown_content)} characters extracted")
        return markdown_content

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Default URL and output file
    url = "https://www.dataquest.io/blog/python-dictionary-tutorial/"

    # Determine output filename based on URL if not provided
    default_output_file = os.path.basename(url.rstrip('/').split('/')[-1]) + ".md"
    output_file = default_output_file

    # Parse command line arguments
    if len(sys.argv) > 1:
        url = sys.argv[1]
        default_output_file = os.path.basename(url.rstrip('/').split('/')[-1]) + ".md"
        output_file = default_output_file

    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    # Perform the conversion
    markdown_content = fetch_and_convert_to_markdown(url, output_file)

    if markdown_content:
        # Print a preview
        print("\nPreview of the first 500 characters:")
        print("-" * 80)
        print(markdown_content[:500] + "...")
        print("-" * 80)
        print(f"Full content saved to {output_file}")
    else:
        print("Failed to fetch and convert the content.")

# Note: You'll need to install the following packages:
# pip install requests beautifulsoup4 html2text