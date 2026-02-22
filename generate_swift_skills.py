import os
import re
import urllib.request
import urllib.error
from rork_snippets import DEFAULT_RORK_TIPS

# Mapping of Apple Docs endpoints to local folder names
# Format: endpoint: folder_name
swift_topics = {
    # Essentials
    "AdoptingSwift6": "adopting_swift_6",
    
    # Standard Library
    "Int": "int",
    "Double": "double",
    "String": "string",
    "Array": "array",
    "Dictionary": "dictionary",
    "swift-standard-library": "swift_standard_library",
    
    # Data Modeling
    "choosing-between-structures-and-classes": "data_modeling_structs_classes",
    "adopting-common-protocols": "adopting_common_protocols",
    
    # Data Flow and Control Flow
    "maintaining-state-in-your-apps": "maintaining_state",
    "preventing-timing-problems-when-using-closures": "preventing_timing_problems",
    
    # Interop (Obj-C & C)
    "objective-c-and-c-code-customization": "c_and_objc_customization",
    "migrating-your-objective-c-code-to-swift": "migrating_objc_to_swift",
    "cocoa-design-patterns": "cocoa_design_patterns",
    "handling-dynamically-typed-methods-and-objects-in-swift": "handling_dynamic_types",
    "using-objective-c-runtime-features-in-swift": "objc_runtime_features",
    "imported-c-and-objective-c-apis": "imported_apis",
    "calling-objective-c-apis-asynchronously": "async_objc_apis",
    
    # Interop (C++)
    "MixingLanguagesInAnXcodeProject": "mixing_languages_cpp",
    "CallingAPIsAcrossLanguageBoundaries": "calling_apis_across_boundaries_cpp"
}

# Other frameworks
other_topics = {
    "Observation": ("Observation", "observation"),
    "Distributed": ("Distributed", "distributed_actors"),
    "RegexBuilder": ("RegexBuilder", "regex_builder"),
    "Synchronization": ("Synchronization", "synchronization")
}

base_url = "https://docs.developer.apple.com/tutorials/data/documentation/"

def cleanup_markdown(text):
    # Remove the initial JSON block
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL).strip()
    return text

def create_skill(framework, endpoint, folder_name):
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
    title = endpoint.replace('-', ' ').title()
    for line in md_content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break
            
    # Swift-specific Rork Tips
    swift_tips = [
        f"Master the language: Use modern Swift 6 features like Concurrency and Observation.",
        f"Performance: Optimize {title} usage for high-performance apps.",
        "Aesthetics: Write clean, idiomatic Swift that is easy to maintain."
    ] + DEFAULT_RORK_TIPS

    tips_md = "\n".join([f"- {tip}" for tip in swift_tips])

    skill_content = f"""---
name: {title}
description: Rork-Max Quality skill for {title}. Based on official Apple {framework} Documentation and enhanced for elite development.
---

# {title}

## 🚀 Rork-Max Quality Snippet

```swift
// Premium {title} Implementation
// Focus on idiomatic, high-performance Swift

import Foundation
#if canImport(Observation)
import Observation
#endif

// Rork-level technical excellence
// [Example implementation logic for {title}]
```

## 💎 Elite Implementation Tips

{tips_md}

## Documentation

{md_content}
"""
    
    full_folder_path = os.path.join("swift_language_skills", folder_name)
    os.makedirs(full_folder_path, exist_ok=True)
    with open(os.path.join(full_folder_path, "SKILL.md"), "w") as f:
        f.write(skill_content)
    print(f"Created {full_folder_path}/SKILL.md")

# Run for Swift framework topics
for endpoint, folder in swift_topics.items():
    create_skill("Swift", endpoint, folder)

# Run for other frameworks listed in Swift docs
for endpoint, info in other_topics.items():
    framework, folder = info
    create_skill(framework, endpoint, folder)
