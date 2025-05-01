import os
import re
import subprocess

REPO_URL = "https://github.com/alexmen656/spectrum/blob/main"
README_PATH = "README.md"

def get_all_files(root_dir):
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file == README_PATH or file.endswith(".pyc") or ".git" in dirpath:
                continue
            full_path = os.path.join(dirpath, file)
            relative_path = os.path.relpath(full_path, root_dir)
            file_paths.append((file, relative_path.replace(" ", "%20")))
    return sorted(file_paths, key=lambda x: x[0].lower())

def generate_markdown_links(files):
    lines = ["### Documents and Files\n"]
    for file_name, relative_path in files:
        lines.append(f"- [{file_name}]({REPO_URL}/{relative_path})")
    return "\n".join(lines)

def update_readme(new_section):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Regex: Suche den alten Block und ersetze ihn, sonst hänge den neuen Block an
    pattern = r"### Documents and Files\n(?:- .*\n?)*"
    if re.search(pattern, readme_content):
        updated_content = re.sub(pattern, f"{new_section}\n", readme_content)
    else:
        updated_content = readme_content.strip() + "\n\n" + new_section + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

def commit_and_push():
    subprocess.run(["git", "config", "user.name", "AlexIsKing"], check=True)
    subprocess.run(["git", "config", "user.email", "alex_is_king@control-center.eu"], check=True)
    subprocess.run(["git", "add", README_PATH], check=True)
    subprocess.run(["git", "commit", "-m", "Auto: update README with file list"], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    repo_root = "."
    files = get_all_files(repo_root)
    markdown = generate_markdown_links(files)
    update_readme(markdown)
    commit_and_push()
    print("✅ README.md wurde korrekt aktualisiert und gepusht.")
