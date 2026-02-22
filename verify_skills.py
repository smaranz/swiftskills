import os

def verify_skill(path):
    with open(path, 'r') as f:
        content = f.read()
    
    checks = {
        "YAML Metadata": content.startswith("---"),
        "Rork Snippet Header": "## 🚀 Rork-Max Quality Snippet" in content,
        "Elite Tips Header": "## 💎 Elite Implementation Tips" in content,
        "Modern Description": "Rork-Max Quality" in content
    }
    
    missing = [k for k, v in checks.items() if not v]
    return missing

def run_verification():
    root_dirs = [
        "app_organization", "scenes", "windows", "immersive_spaces", "documents",
        "navigation", "modal_presentations", "toolbars", "search", "app_extensions",
        "model_data", "environment_values", "preferences", "persistent_storage",
        "view_fundamentals", "view_configuration", "view_styles", "animations",
        "text_input_and_output", "images", "controls_and_indicators", "menus_and_commands",
        "shapes", "drawing_and_graphics", "layout_fundamentals", "layout_adjustments",
        "custom_layout", "lists", "tables", "view_groupings", "scroll_views",
        "gestures", "input_events", "clipboard", "drag_and_drop", "focus",
        "system_events", "accessibility_fundamentals", "accessible_appearance",
        "accessible_controls", "accessible_descriptions", "accessible_navigation",
        "appkit_integration", "uikit_integration", "watchkit_integration",
        "technology_specific_views", "previews_in_xcode", "xcode_library_customization",
        "performance_analysis", "frontend_skills", "apple_intelligence_skills", "platform_skills"
    ]
    
    errors = []
    
    for root in root_dirs:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                if filename == "SKILL.md":
                    path = os.path.join(dirpath, filename)
                    missing = verify_skill(path)
                    if missing:
                        errors.append(f"{path}: Missing {', '.join(missing)}")
    
    if errors:
        print(f"Verification FAILED with {len(errors)} errors:")
        for err in errors[:10]:
            print(f"  - {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more.")
    else:
        print("Verification PASSED! All skills meet Rork quality standards.")

if __name__ == "__main__":
    run_verification()
