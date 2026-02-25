import os
import re
import urllib.request
import urllib.error
from rork_snippets import (
    get_rork_quality_section,
    parse_apple_docs,
    format_api_reference,
    format_guidance_section,
    SWIFT_CATEGORY_GUIDANCE,
    DEFAULT_RORK_TIPS,
    RORK_SNIPPETS,
)

swift_topics = {
    "AdoptingSwift6": ("adopting_swift_6", "essentials"),
    "Int": ("int", "standard_library"),
    "Double": ("double", "standard_library"),
    "String": ("string", "standard_library"),
    "Array": ("array", "standard_library"),
    "Dictionary": ("dictionary", "standard_library"),
    "swift-standard-library": ("swift_standard_library", "standard_library"),
    "choosing-between-structures-and-classes": ("data_modeling_structs_classes", "data_modeling"),
    "adopting-common-protocols": ("adopting_common_protocols", "data_modeling"),
    "maintaining-state-in-your-apps": ("maintaining_state", "concurrency"),
    "preventing-timing-problems-when-using-closures": ("preventing_timing_problems", "concurrency"),
    "objective-c-and-c-code-customization": ("c_and_objc_customization", "interop"),
    "migrating-your-objective-c-code-to-swift": ("migrating_objc_to_swift", "interop"),
    "cocoa-design-patterns": ("cocoa_design_patterns", "interop"),
    "handling-dynamically-typed-methods-and-objects-in-swift": ("handling_dynamic_types", "interop"),
    "using-objective-c-runtime-features-in-swift": ("objc_runtime_features", "interop"),
    "imported-c-and-objective-c-apis": ("imported_apis", "interop"),
    "calling-objective-c-apis-asynchronously": ("async_objc_apis", "interop"),
    "MixingLanguagesInAnXcodeProject": ("mixing_languages_cpp", "interop"),
    "CallingAPIsAcrossLanguageBoundaries": ("calling_apis_across_boundaries_cpp", "interop"),
}

other_topics = {
    "Observation": ("Observation", "observation", "concurrency"),
    "Distributed": ("Distributed", "distributed_actors", "concurrency"),
    "RegexBuilder": ("RegexBuilder", "regex_builder", "standard_library"),
    "Synchronization": ("Synchronization", "synchronization", "concurrency"),
}

base_url = "https://docs.developer.apple.com/tutorials/data/documentation/"


def create_skill(framework, endpoint, folder_name, category):
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
    title = parsed["title"] or endpoint.replace('-', ' ').title()
    overview = parsed["overview"]
    api_reference = format_api_reference(parsed["topics"])

    # Get topic-specific snippet or generate a relevant one
    rork_data = RORK_SNIPPETS.get(endpoint, {})
    if rork_data:
        snippet = rork_data.get("snippet", "")
        tips = rork_data.get("tips", DEFAULT_RORK_TIPS)
    else:
        snippet = f"""```swift
import Foundation

// {title} — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```"""
        tips = [
            f"Use modern Swift 6 patterns when working with {title}.",
            "Prefer value types (structs/enums) unless reference semantics are needed.",
            "Leverage Swift's type system to catch errors at compile time.",
        ] + DEFAULT_RORK_TIPS

    tips_md = "\n".join([f"- {tip}" for tip in tips])

    guidance = SWIFT_CATEGORY_GUIDANCE.get(category, {})
    when_to_use = format_guidance_section("When to Use", guidance.get("when_to_use"))
    best_practices = format_guidance_section("Best Practices", guidance.get("best_practices"))
    pitfalls = format_guidance_section("Common Pitfalls", guidance.get("pitfalls"))

    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title}. Actionable Swift language patterns and best practices.
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

    full_folder_path = os.path.join("swift_language_skills", folder_name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")


for endpoint, info in swift_topics.items():
    folder, category = info
    create_skill("Swift", endpoint, folder, category)

for endpoint, info in other_topics.items():
    framework, folder, category = info
    create_skill(framework, endpoint, folder, category)
