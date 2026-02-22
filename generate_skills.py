import os
import re
import urllib.request
import urllib.error
from rork_snippets import get_rork_quality_section

topics = {
    # App structure
    "App-organization": "app_organization",
    "Scenes": "scenes",
    "Windows": "windows",
    "Immersive-spaces": "immersive_spaces",
    "Documents": "documents",
    "Navigation": "navigation",
    "Modal-presentations": "modal_presentations",
    "Toolbars": "toolbars",
    "Search": "search",
    "App-extensions": "app_extensions",

    # Data and storage
    "Model-data": "model_data",
    "Environment-values": "environment_values",
    "Preferences": "preferences",
    "Persistent-storage": "persistent_storage",

    # Views
    "View-fundamentals": "view_fundamentals",
    "View-configuration": "view_configuration",
    "View-styles": "view_styles",
    "Animations": "animations",
    "Text-input-and-output": "text_input_and_output",
    "Images": "images",
    "Controls-and-indicators": "controls_and_indicators",
    "Menus-and-commands": "menus_and_commands",
    "Shapes": "shapes",
    "Drawing-and-graphics": "drawing_and_graphics",

    # View layout
    "Layout-fundamentals": "layout_fundamentals",
    "Layout-adjustments": "layout_adjustments",
    "Custom-layout": "custom_layout",
    "Lists": "lists",
    "Tables": "tables",
    "View-groupings": "view_groupings",
    "Scroll-views": "scroll_views",

    # Event handling
    "Gestures": "gestures",
    "Input-events": "input_events",
    "Clipboard": "clipboard",
    "Drag-and-drop": "drag_and_drop",
    "Focus": "focus",
    "System-events": "system_events",

    # Accessibility
    "Accessibility-fundamentals": "accessibility_fundamentals",
    "Accessible-appearance": "accessible_appearance",
    "Accessible-controls": "accessible_controls",
    "Accessible-descriptions": "accessible_descriptions",
    "Accessible-navigation": "accessible_navigation",

    # Framework integration
    "AppKit-integration": "appkit_integration",
    "UIKit-integration": "uikit_integration",
    "WatchKit-integration": "watchkit_integration",
    "Technology-specific-views": "technology_specific_views",

    # Tool support
    "Previews-in-Xcode": "previews_in_xcode",
    "Xcode-library-customization": "xcode_library_customization",
    "Performance-analysis": "performance_analysis"
}

base_url = "https://docs.developer.apple.com/tutorials/data/documentation/SwiftUI/"

def cleanup_markdown(text):
    # Remove the initial JSON block
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
    return text

def create_skill(endpoint, folder_name):
    url = f"{base_url}{endpoint}.md"
    try:
        with urllib.request.urlopen(url) as response:
            md_content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e}")
        return

    md_content = cleanup_markdown(md_content)
    
    # Extract Title
    title = endpoint.replace('-', ' ').title()
    for line in md_content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break
            
    # Inject Rork Quality Section
    rork_section = get_rork_quality_section(endpoint)
    
    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title}. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# {title}

{rork_section}

## Documentation

{md_content}
"""
    
    os.makedirs(folder_name, exist_ok=True)
    with open(os.path.join(folder_name, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {folder_name}/SKILL.md")

for endpoint, folder in topics.items():
    create_skill(endpoint, folder)
