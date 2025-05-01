import os
import subprocess

REPO_URL = "https://github.com/alexmen656/spectrum/blob/main"  # <--- hier anpassen
README_PATH = "README.md"

def get_all_files(root_dir):
    file_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            # Ausschließen der README-Datei, .pyc-Dateien und Git-Ordner
            if file == README_PATH or file.endswith(".pyc") or ".git" in dirpath:
                continue
            full_path = os.path.join(dirpath, file)
            relative_path = os.path.relpath(full_path, root_dir)
            # Ersetze Leerzeichen durch %20
            relative_path = relative_path.replace(" ", "%20")
            file_paths.append(relative_path.replace("\\", "/"))
    return sorted(file_paths)

def generate_markdown_links(files):
    # Die Markdown-Dateiliste im gewünschten Format generieren
    lines = ["### Documents and Files\n"]
    for file in files:
        lines.append(f"- [{file}]({REPO_URL}/{file})")
    return "\n".join(lines)

def update_readme(content):
    # Das README öffnen und aktualisieren
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Die Dateiliste an der richtigen Stelle einfügen
    start_marker = "### Documents and Files"
    if start_marker in readme_content:
        # Wenn der Abschnitt schon existiert, ersetzen wir ihn
        readme_content = readme_content.replace(f"{start_marker}\n", f"{start_marker}\n{content}\n")
    else:
        # Wenn der Abschnitt noch nicht existiert, fügen wir ihn am Ende ein
        readme_content += f"\n{content}"

    # Die aktualisierte README-Datei speichern
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)

def commit_and_push():
    # Git-Konfiguration und Push
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
    print("✅ README.md wurde automatisch aktualisiert und die Änderungen gepusht.")
