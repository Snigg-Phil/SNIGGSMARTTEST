import os

REPLACEMENTS = {
    "cFos Charging Manager": "Snigg Charging Manager",
    "cFos Power Brain Controller": "Snigg Smart Controller",
    "cFos Power Brain Wallbox": "Snigg Smart Charger",
    "cFos Power Brain": "Snigg Smart Charger",
    "cFos": "Snigg",
    "Power Brain Controller": "Smart Controller",
}

def replace_terms(text):
    for old, new in REPLACEMENTS.items():
        if old in text:
            print(f"🔍 Found '{old}' → replacing with '{new}'")
        text = text.replace(old, new)
    return text

def update_docs(directory="docs"):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(root, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content = replace_terms(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Updated: {path}")

if __name__ == "__main__":
    update_docs()
