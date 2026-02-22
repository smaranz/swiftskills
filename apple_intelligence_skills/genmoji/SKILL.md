---
name: Apple Intelligence: NSAdaptiveImageGlyph
description: Rork-Max Quality skill for Apple Intelligence: NSAdaptiveImageGlyph. Specialized for elite Apple Intelligence integration.
---

# Apple Intelligence: NSAdaptiveImageGlyph

## 🚀 Rork-Max Quality Snippet

```swift
// Premium Apple Intelligence: NSAdaptiveImageGlyph Implementation
// Focus on low-latency, high-delight AI interactions

import SwiftUI
import AppIntents

struct RorkIntelligenceView: View {
    var body: some View {
        ContentUnavailableView {
            Label("Apple Intelligence: NSAdaptiveImageGlyph", systemImage: "sparkles")
        } description: {
            Text("Implementing elite AI features with Rork Max quality.")
        } actions: {
            Button("Explore Intents") {
                // Action logic
            }
            .buttonStyle(.borderedProminent)
        }
    }
}
```

## 💎 Elite Implementation Tips

- Ensure genmoji integration feels seamless by following the Human Interface Guidelines for Intelligence.
- Always handle fallback cases gracefully where the model might be unavailable or downloading.
- Use modern async/await patterns for all AI-triggered operations to keep the UI responsive.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# NSAdaptiveImageGlyph

A data object for an emoji-like image that can appear in attributed text.

```
class NSAdaptiveImageGlyph
```

## Overview

An [`NSAdaptiveImageGlyph`](/documentation/AppKit/NSAdaptiveImageGlyph) contains an image that automatically adapts to different sizes and resolutions. The text system creates instances of this type to represent custom emojis that people create using the system interfaces. This type manages multiple images, along with metadata describing how to adapt those images correctly to different fonts and font attributes.

Typically, you receive new [`NSAdaptiveImageGlyph`](/documentation/AppKit/NSAdaptiveImageGlyph) objects only from the text-input system. When someone creates a new emoji and inserts it into their text, TextKit creates an instance of this type to represent it. If your app examines or changes the attributes of attributed strings, preserve the <doc://com.apple.documentation/documentation/Foundation/NSAttributedString/Key/adaptiveImageGlyph> attribute when making any changes. For example, if you filter unknown attributes in a custom text-storage object, update your code to preserve this attribute. The value of the attribute is an [`NSAdaptiveImageGlyph`](/documentation/AppKit/NSAdaptiveImageGlyph) containing the emoji data. You can save the image data with the rest of your content and use the data to recreate the type later.

## Topics

### Creating an adaptive image glyph

[`init(imageContent:)`](/documentation/AppKit/NSAdaptiveImageGlyph/init(imageContent:))

Create an adaptive image glyph from the previously saved data.

[`init(coder:)`](/documentation/AppKit/NSAdaptiveImageGlyph/init(coder:))

### Getting the image data

[`imageContent`](/documentation/AppKit/NSAdaptiveImageGlyph/imageContent)

The raw data for the image.

### Getting the content metadata

[`contentIdentifier`](/documentation/AppKit/NSAdaptiveImageGlyph/contentIdentifier)

A unique identifier for this image.

[`contentDescription`](/documentation/AppKit/NSAdaptiveImageGlyph/contentDescription)

An alternate textual description of the image contents.

[`contentType`](/documentation/AppKit/NSAdaptiveImageGlyph/contentType)

The image data format to use for this image type.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
