import os
import re
import urllib.request
import urllib.error
from rork_snippets import DEFAULT_RORK_TIPS

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
            
    # Platform-specific Rork Tips
    platform_tips = [
        f"Master the {platform} native feel: Use system-standard components correctly before customizing.",
        f"Ensure optimal performance for {platform}: Handle lifecycle events efficiently.",
        "Aesthetics: Keep designs clean and aligned with the platform's HIG."
    ] + DEFAULT_RORK_TIPS

    tips_md = "\n".join([f"- {tip}" for tip in platform_tips])

    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title} on {platform}. Based on official Apple {framework} Documentation.
---

# {title}

## 🚀 Rork-Max Quality Snippet

```swift
// Premium {title} Implementation for {platform}
// Focus on platform-native excellence

import SwiftUI
#if os({platform.lower() if platform.lower() != 'ipados' else 'ios'})
// {framework} specific imports
#endif

struct RorkPlatformView: View {{
    var body: some View {{
        Text("Rork Quality {platform.upper()} Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }}
}}
```

## 💎 Elite Implementation Tips

{tips_md}

## Documentation

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
