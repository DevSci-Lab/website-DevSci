import sys
import os
from bs4 import BeautifulSoup, NavigableString
from deep_translator import GoogleTranslator
import re

def translate_html(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    # Determine output filename
    # Logic: filename_en.html -> filename_es.html
    #        filename.html -> filename_es.html (if no _en suffix)
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    
    if name.endswith('_en'):
        new_name = name.replace('_en', '_es')
    else:
        # If input is already _es, we might not want to overwrite it unless explicit, 
        # but for now we assume user inputs source file (EN).
        new_name = name + '_es'
    
    output_path = os.path.join(directory, new_name + ext)

    print(f"Reading {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    translator = GoogleTranslator(source='en', target='es')

    # Regex to identify Jinja2 blocks to avoid translating them completely if they appear in text
    # However, purely structural Jinja2 is usually inside {% %} which BS4 might treat as NavigableString if inside tags
    # We will try to be careful.
    
    # We iterate over all text nodes
    for element in soup.find_all(string=True):
        if isinstance(element, NavigableString):
            if element.parent.name in ['script', 'style', 'code', 'pre']:
                continue
            
            text = element.strip()
            if not text:
                continue

            # Skip if it looks like a pure Jinja2 block {% ... %} or {{ ... }}
            if text.startswith('{%') or text.startswith('{{'):
                continue
            
            # Translate
            try:
                # Basic check to avoid translating technical strings that might break
                if len(text) > 1:
                    translated = translator.translate(text)
                    element.replace_with(translated)
            except Exception as e:
                print(f"Warning: Could not translate '{text[:20]}...': {e}")

    print(f"Saving translation to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify(formatter="html")))

    print("Done! Please review the generated file manually.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translate_site.py <path_to_html_file>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    translate_html(target_file)
