import os
import re
import urllib.request
import urllib.error

# Root directory for platform skills
ROOT_DIR = "platform_skills"

# Framework-to-topics mapping
# Format: Framework: [(Slug, FolderName, Platform)]
platform_mapping = {
    "UIKit": [
        ("app-and-environment", "app_and_environment", "ios"),
        ("views-and-controls", "views_and_controls", "ios"),
        ("view-controllers", "view_controllers", "ios"),
        ("view-layout", "view_layout", "ios"),
        ("touches-presses-and-gestures", "gestures", "ios"),
        ("menus-and-shortcuts", "menus", "ios"),
        ("accessibility-for-uikit", "accessibility", "ios")
    ],
    "AppKit": [
        ("app-and-environment", "app_and_environment", "macos"),
        ("views-and-controls", "views_and_controls", "macos"),
        ("view-management", "view_management", "macos"),
        ("view-layout", "view_layout", "macos"),
        ("mouse-keyboard-and-trackpad", "interaction", "macos"),
        ("menus-cursors-and-the-dock", "menus", "macos"),
        ("accessibility-for-appkit", "accessibility", "macos")
    ],
    "WatchKit": [
        ("setting-up-a-watchos-project", "project_setup", "watchos"),
        ("WKApplication", "app_lifecycle", "watchos"),
        ("background-execution", "background_tasks", "watchos"),
        ("life-cycles", "runtime_lifecycle", "watchos"),
        ("storyboard-support", "user_interface", "watchos")
    ],
    "visionOS": [
        ("creating-your-first-visionos-app", "app_construction", "visionos"),
        ("adding-3d-content-to-your-app", "spatial_content", "visionos"),
        ("creating-fully-immersive-experiences", "immersive_spaces", "visionos"),
        ("positioning-and-sizing-windows", "window_management", "visionos"),
        ("improving-accessibility-support-in-your-app", "accessibility", "visionos")
    ],
    "PencilKit": [
        ("PencilKit", "pencilkit", "ipados")
    ]
}

base_url = "https://docs.developer.apple.com/tutorials/data/documentation/"

def cleanup_markdown(text):
    # Remove the initial JSON block
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
    return text

def create_skill(framework, endpoint, folder_name, platform):
    if framework == endpoint:
        url = f"{base_url}{framework}.md"
    else:
        url = f"{base_url}{framework}/{endpoint}.md"
        
    try:
        with urllib.request.urlopen(url) as response:
            md_content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e}")
        return

    md_content = cleanup_markdown(md_content)
    
    # Extract Title
    title = f"{platform.upper()} {endpoint.replace('-', ' ').title()}"
    for line in md_content.split('\n'):
        if line.startswith('# '):
            raw_title = line[2:].strip()
            title = f"{platform.upper()} {raw_title}"
            break
            
    skill_content = f"""---
name: {title}
description: Apple {framework} Documentation for {title} on {platform}.
---

{md_content}
"""
    
    full_folder_path = os.path.join(ROOT_DIR, platform, folder_name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")

# Create root folder
os.makedirs(ROOT_DIR, exist_ok=True)

# Run for all mappings
for framework, topics in platform_mapping.items():
    for slug, folder, platform in topics:
        create_skill(framework, slug, folder, platform)
