import os
import re
import urllib.request
import urllib.error
from rork_snippets import (
    parse_apple_docs,
    format_api_reference,
    format_guidance_section,
    AI_CATEGORY_GUIDANCE,
    DEFAULT_RORK_TIPS,
)

ROOT_DIR = "apple_intelligence_skills"

ai_mapping = {
    "foundation_models": {
        "url": "https://docs.developer.apple.com/tutorials/data/documentation/foundationmodels.md",
        "snippet": """```swift
import FoundationModels
import SwiftUI

@Generable
struct MovieRecommendation {
    var title: String
    var genre: String
    var reason: String
}

struct SmartRecommendationView: View {
    @State private var recommendation: MovieRecommendation?
    @State private var isLoading = false

    var body: some View {
        VStack(spacing: 20) {
            if let rec = recommendation {
                VStack(alignment: .leading, spacing: 8) {
                    Text(rec.title).font(.title2.bold())
                    Text(rec.genre).font(.subheadline).foregroundStyle(.secondary)
                    Text(rec.reason).font(.body)
                }
                .padding()
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
            }

            Button("Get Recommendation") {
                Task { await generateRecommendation() }
            }
            .buttonStyle(.borderedProminent)
            .disabled(isLoading)
        }
    }

    func generateRecommendation() async {
        isLoading = true
        defer { isLoading = false }
        let session = LanguageModelSession()
        recommendation = try? await session.respond(
            to: "Suggest a movie for a rainy evening",
            generating: MovieRecommendation.self
        )
    }
}
```""",
    },
    "app_intents": {
        "url": "https://docs.developer.apple.com/tutorials/data/documentation/appintents.md",
        "snippet": """```swift
import AppIntents

struct OpenFavoriteIntent: AppIntent {
    static var title: LocalizedStringResource = "Open Favorite"
    static var description = IntentDescription("Opens your favorite item in the app.")

    @Parameter(title: "Item Name")
    var itemName: String

    func perform() async throws -> some IntentResult & ProvidesDialog {
        .result(dialog: "Opening \\(itemName)!")
    }
}

struct AppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: OpenFavoriteIntent(),
            phrases: ["Open my favorite in \\(.applicationName)"],
            shortTitle: "Open Favorite",
            systemImageName: "star.fill"
        )
    }
}
```""",
    },
    "image_playground": {
        "url": "https://docs.developer.apple.com/tutorials/data/documentation/imageplayground.md",
        "snippet": """```swift
import ImagePlayground
import SwiftUI

struct PlaygroundView: View {
    @State private var showPlayground = false
    @State private var generatedImage: Image?

    var body: some View {
        VStack {
            if let image = generatedImage {
                image
                    .resizable()
                    .scaledToFit()
                    .clipShape(RoundedRectangle(cornerRadius: 16))
            }

            Button("Create Image") { showPlayground = true }
                .buttonStyle(.borderedProminent)
        }
        .imagePlaygroundSheet(isPresented: $showPlayground) { url in
            generatedImage = Image(uiImage: UIImage(contentsOfFile: url.path)!)
        }
    }
}
```""",
    },
    "writing_tools": {
        "url": "https://docs.developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator.md",
        "snippet": """```swift
import UIKit

class RorkTextViewController: UIViewController, UIWritingToolsCoordinatorDelegate {
    let textView = UITextView()

    override func viewDidLoad() {
        super.viewDidLoad()
        textView.frame = view.bounds
        textView.font = .preferredFont(forTextStyle: .body)
        textView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(textView)
        // Writing Tools are enabled by default on UITextView
    }
}
```""",
    },
    "genmoji": {
        "url": "https://docs.developer.apple.com/tutorials/data/documentation/appkit/nsadaptiveimageglyph.md",
        "snippet": """```swift
import UIKit

func renderGenmoji(in attributedString: NSAttributedString) -> UIImage? {
    let renderer = UIGraphicsImageRenderer(size: CGSize(width: 300, height: 44))
    return renderer.image { context in
        attributedString.draw(in: CGRect(x: 0, y: 0, width: 300, height: 44))
    }
}
```""",
    },
}


def create_ai_skill(name, config):
    url = config["url"]
    snippet = config["snippet"]

    try:
        with urllib.request.urlopen(url) as response:
            md_content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e}")
        return

    parsed = parse_apple_docs(md_content)

    raw_title = parsed["title"] or name.replace('_', ' ').title()
    title = f"Apple Intelligence: {raw_title}"
    overview = parsed["overview"]
    api_reference = format_api_reference(parsed["topics"])

    guidance = AI_CATEGORY_GUIDANCE.get(name, {})
    ai_tips = [
        f"Ensure {name.replace('_', ' ')} integration feels seamless by following the HIG for Intelligence.",
        "Handle fallback cases gracefully where the model or feature may be unavailable.",
        "Use modern async/await patterns for all AI-triggered operations.",
    ] + [
        "Always check for `@Observable` (Swift 6) compatibility for optimal performance.",
        "Prioritize SF Symbols with hierarchical rendering for all iconography.",
    ]
    tips_md = "\n".join(f"- {tip}" for tip in ai_tips)

    when_to_use = format_guidance_section("When to Use", guidance.get("when_to_use"))
    best_practices_section = format_guidance_section("Best Practices", guidance.get("best_practices"))
    pitfalls = format_guidance_section("Common Pitfalls", guidance.get("pitfalls"))

    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title}. Patterns and best practices for Apple Intelligence integration.
---

# {title}

{overview}

## 🚀 Rork-Max Quality Snippet

{snippet}

## 💎 Elite Implementation Tips

{tips_md}

{when_to_use}

{best_practices_section}

{pitfalls}

{api_reference}
"""

    full_folder_path = os.path.join(ROOT_DIR, name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")


os.makedirs(ROOT_DIR, exist_ok=True)

for name, config in ai_mapping.items():
    create_ai_skill(name, config)
