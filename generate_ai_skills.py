import os
import re
import urllib.request
import urllib.error

# Root directory for Apple Intelligence skills
ROOT_DIR = "apple_intelligence_skills"

# Mapping of skill to DocC URL
ai_mapping = {
    "foundation_models": "https://docs.developer.apple.com/tutorials/data/documentation/foundationmodels.md",
    "app_intents": "https://docs.developer.apple.com/tutorials/data/documentation/appintents.md",
    "image_playground": "https://docs.developer.apple.com/tutorials/data/documentation/imageplayground.md",
    "writing_tools": "https://docs.developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator.md",
    "genmoji": "https://docs.developer.apple.com/tutorials/data/documentation/appkit/nsadaptiveimageglyph.md"
}

def cleanup_markdown(text):
    # Remove the initial JSON block if exists
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
    return text

def create_ai_skill(name, url):
    try:
        with urllib.request.urlopen(url) as response:
            md_content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e}")
        return

    md_content = cleanup_markdown(md_content)
    
    # Extract Title
    title = f"Apple Intelligence {name.replace('_', ' ').title()}"
    for line in md_content.split('\n'):
        if line.startswith('# '):
            raw_title = line[2:].strip()
            title = f"Apple Intelligence: {raw_title}"
            break
            
    skill_content = f"""---
name: {title}
description: Specialized skill for {title} based on official Apple Developer Documentation.
---

{md_content}
"""
    
    full_folder_path = os.path.join(ROOT_DIR, name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")

# Create root folder
os.makedirs(ROOT_DIR, exist_ok=True)

# Run for all mappings
for name, url in ai_mapping.items():
    create_ai_skill(name, url)
