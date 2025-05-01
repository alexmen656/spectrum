import os
import urllib.parse

DOCUMENT_EXTENSIONS = {'.md', '.pdf', '.png'}
IGNORE_DIRS = {'.git', '__pycache__', 'node_modules'}

README_PATH = 'README.md'
SECTION_HEADER = '### Documents and Files'

def is_document(filename):
    return any(filename.lower().endswith(ext) for ext in DOCUMENT_EXTENSIONS)

def normalize_path(path):
    """Convert OS path to forward-slash path and encode properly for Markdown."""
    path = path.replace(os.sep, '/')
    return urllib.parse.quote(path, safe='/')

def generate_link(path):
    filename = os.path.basename(path)
    encoded_path = normalize_path(path)
    return f'- [{filename}]({encoded_path})\n  - Summary is missing!'

def collect_documents(base_dir='.'):
    links = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if is_document(file):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir).replace(os.sep, '/')
                links.append(generate_link(rel_path))
    return sorted(links, key=lambda x: x.lower())

def update_readme(readme_path, section_header, new_links):
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            start_idx = i
            break

    if start_idx is None:
        print(f"Section header '{section_header}' not found.")
        return

    end_idx = start_idx + 1
    while end_idx < len(lines) and not lines[end_idx].startswith("###"):
        end_idx += 1

    updated_lines = lines[:start_idx+1] + ['\n'] + [line + '\n' for line in new_links] + ['\n'] + lines[end_idx:]

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print("README.md successfully updated.")

if __name__ == "__main__":
    links = collect_documents()
    update_readme(README_PATH, SECTION_HEADER, links)
