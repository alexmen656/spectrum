import os

REPO_URL = "https://github.com/alexmen656/spectrum/blob/main"  # <--- hier anpassen
README_PATH = "README.md"

def get_all_files(root_dir):
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file == README_PATH or file.endswith(".pyc") or ".git" in dirpath:
                continue
            full_path = os.path.join(dirpath, file)
            relative_path = os.path.relpath(full_path, root_dir)
            file_paths.append(relative_path.replace("\\", "/"))
    return sorted(file_paths)

def generate_markdown_links(files):
    lines = ["## 📄 Alle Dateien im Repository:\n"]
    for file in files:
        lines.append(f"- [{file}]({REPO_URL}/{file})")
    return "\n".join(lines)

def update_readme(content):
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    repo_root = "."
    files = get_all_files(repo_root)
    markdown = generate_markdown_links(files)
    update_readme(markdown)
    print("✅ README.md wurde automatisch aktualisiert.")
