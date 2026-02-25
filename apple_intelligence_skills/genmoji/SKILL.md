---
name: Apple Intelligence: NSAdaptiveImageGlyph
description: Rork-Max Quality skill for Apple Intelligence: NSAdaptiveImageGlyph. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: NSAdaptiveImageGlyph

A data object for an emoji-like image that can appear in attributed text.
```
class NSAdaptiveImageGlyph
```
An `NSAdaptiveImageGlyph` contains an image that automatically adapts to different sizes and resolutions. The text system creates instances of this type to represent custom emojis that people create using the system interfaces. This type manages multiple images, along with metadata describing how to adapt those images correctly to different fonts and font attributes.
Typically, you receive new `NSAdaptiveImageGlyph` objects only from the text-input system. When someone creates a new emoji and inserts it into their text, TextKit creates an instance of this type to represent it. If your app examines or changes the attributes of attributed strings, preserve the adaptiveImageGlyph attribute when making any changes. For example, if you filter unknown attributes in a custom text-storage object, update your code to preserve this attribute. The value of the attribute is an `NSAdaptiveImageGlyph` containing the emoji data. You can save the image data with the rest of your content and use the data to recreate the type later.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

func renderGenmoji(in attributedString: NSAttributedString) -> UIImage? {
    let renderer = UIGraphicsImageRenderer(size: CGSize(width: 300, height: 44))
    return renderer.image { context in
        attributedString.draw(in: CGRect(x: 0, y: 0, width: 300, height: 44))
    }
}
```

## 💎 Elite Implementation Tips

- Ensure genmoji integration feels seamless by following the HIG for Intelligence.
- Handle fallback cases gracefully where the model or feature may be unavailable.
- Use modern async/await patterns for all AI-triggered operations.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.

## When to Use

- Supporting user-generated emoji (Genmoji) in text rendering and input
- Handling `NSAdaptiveImageGlyph` in attributed strings

## Best Practices

- Use `NSAttributedString` with adaptive image glyph support for rich text
- Ensure Genmoji render at appropriate sizes in your text layout

## Common Pitfalls

- Stripping Genmoji when serializing text — preserve `NSAdaptiveImageGlyph` data

## Key APIs

### Creating an adaptive image glyph

| API | Purpose |
|-----|---------|
| `init(imageContent:)` | Create an adaptive image glyph from the previously saved data. |

### Getting the image data

| API | Purpose |
|-----|---------|
| `imageContent` | The raw data for the image. |

### Getting the content metadata

| API | Purpose |
|-----|---------|
| `contentIdentifier` | A unique identifier for this image. |
| `contentDescription` | An alternate textual description of the image contents. |
| `contentType` | The image data format to use for this image type. |
