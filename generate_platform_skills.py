import os
import re
import urllib.request
import urllib.error
from rork_snippets import (
    parse_apple_docs,
    format_api_reference,
    format_guidance_section,
    PLATFORM_CATEGORY_GUIDANCE,
    DEFAULT_RORK_TIPS,
    RORK_SNIPPETS,
)

ROOT_DIR = "platform_skills"

platform_mapping = {
    "UIKit": [
        ("app-and-environment", "app_and_environment", "ios"),
        ("views-and-controls", "views_and_controls", "ios"),
        ("view-controllers", "view_controllers", "ios"),
        ("view-layout", "view_layout", "ios"),
        ("touches-presses-and-gestures", "gestures", "ios"),
        ("menus-and-shortcuts", "menus", "ios"),
        ("accessibility-for-uikit", "accessibility", "ios"),
    ],
    "AppKit": [
        ("app-and-environment", "app_and_environment", "macos"),
        ("views-and-controls", "views_and_controls", "macos"),
        ("view-management", "view_management", "macos"),
        ("view-layout", "view_layout", "macos"),
        ("mouse-keyboard-and-trackpad", "interaction", "macos"),
        ("menus-cursors-and-the-dock", "menus", "macos"),
        ("accessibility-for-appkit", "accessibility", "macos"),
    ],
    "WatchKit": [
        ("setting-up-a-watchos-project", "project_setup", "watchos"),
        ("WKApplication", "app_lifecycle", "watchos"),
        ("background-execution", "background_tasks", "watchos"),
        ("life-cycles", "runtime_lifecycle", "watchos"),
        ("storyboard-support", "user_interface", "watchos"),
    ],
    "visionOS": [
        ("creating-your-first-visionos-app", "app_construction", "visionos"),
        ("adding-3d-content-to-your-app", "spatial_content", "visionos"),
        ("creating-fully-immersive-experiences", "immersive_spaces", "visionos"),
        ("positioning-and-sizing-windows", "window_management", "visionos"),
        ("improving-accessibility-support-in-your-app", "accessibility", "visionos"),
    ],
    "PencilKit": [
        ("PencilKit", "pencilkit", "ipados"),
    ],
}

# Platform-specific snippet templates
PLATFORM_SNIPPETS = {
    "ios": """```swift
import UIKit

class RorkViewController: UIViewController {{
    override func viewDidLoad() {{
        super.viewDidLoad()

        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "{title}"
        label.font = .preferredFont(forTextStyle: .largeTitle)
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }}
}}
```""",
    "macos": """```swift
import AppKit

class RorkWindowController: NSWindowController {{
    convenience init() {{
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 600, height: 400),
            styleMask: [.titled, .closable, .resizable, .miniaturizable],
            backing: .buffered,
            defer: false
        )
        window.title = "{title}"
        window.center()
        self.init(window: window)
    }}
}}
```""",
    "watchos": """```swift
import SwiftUI

struct RorkWatchView: View {{
    var body: some View {{
        NavigationStack {{
            List {{
                Text("{title}")
                    .font(.headline)
            }}
            .navigationTitle("Rork")
        }}
    }}
}}
```""",
    "visionos": """```swift
import SwiftUI
import RealityKit

struct RorkSpatialView: View {{
    var body: some View {{
        RealityView {{ content in
            let sphere = MeshResource.generateSphere(radius: 0.1)
            let material = SimpleMaterial(color: .blue, isMetallic: true)
            let entity = ModelEntity(mesh: sphere, materials: [material])
            content.add(entity)
        }}
        .navigationTitle("{title}")
    }}
}}
```""",
    "ipados": """```swift
import PencilKit

class RorkCanvasViewController: UIViewController {{
    let canvasView = PKCanvasView()

    override func viewDidLoad() {{
        super.viewDidLoad()
        canvasView.drawingPolicy = .anyInput
        canvasView.tool = PKInkingTool(.pen, color: .systemBlue, width: 5)
        canvasView.frame = view.bounds
        canvasView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(canvasView)
    }}
}}
```""",
}

base_url = "https://docs.developer.apple.com/tutorials/data/documentation/"


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

    parsed = parse_apple_docs(md_content)

    raw_title = parsed["title"] or endpoint.replace('-', ' ').title()
    title = f"{platform.upper()} {raw_title}"
    overview = parsed["overview"]
    api_reference = format_api_reference(parsed["topics"])

    snippet_template = PLATFORM_SNIPPETS.get(platform, PLATFORM_SNIPPETS["ios"])
    snippet = snippet_template.format(title=raw_title)

    guidance = PLATFORM_CATEGORY_GUIDANCE.get(platform, {})
    platform_tips = [
        f"Follow the {platform.upper()} Human Interface Guidelines for native feel.",
        f"Use system-standard {framework} components before building custom ones.",
        "Support Dynamic Type and accessibility features from the start.",
    ] + DEFAULT_RORK_TIPS

    tips_md = "\n".join(f"- {tip}" for tip in platform_tips)

    when_to_use = format_guidance_section("When to Use", guidance.get("when_to_use"))
    best_practices = format_guidance_section("Best Practices", guidance.get("best_practices"))
    pitfalls = format_guidance_section("Common Pitfalls", guidance.get("pitfalls"))

    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title}. Platform-native patterns and best practices for {platform} development.
---

# {title}

{overview}

## 🚀 Rork-Max Quality Snippet

{snippet}

## 💎 Elite Implementation Tips

{tips_md}

{when_to_use}

{best_practices}

{pitfalls}

{api_reference}
"""

    full_folder_path = os.path.join(ROOT_DIR, platform, folder_name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")


os.makedirs(ROOT_DIR, exist_ok=True)

for framework, topics in platform_mapping.items():
    for slug, folder, platform in topics:
        create_skill(framework, slug, folder, platform)
