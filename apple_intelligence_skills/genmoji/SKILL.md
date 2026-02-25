---
name: Apple Intelligence: Genmoji
description: Rork-Max Quality skill for Apple Intelligence: NSAdaptiveImageGlyph. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: Genmoji

Genmoji lets users create custom emoji-like images using Apple Intelligence and insert them into text. Under the hood, each Genmoji is an `NSAdaptiveImageGlyph` — a multi-resolution image that scales with the surrounding text. Standard text views render them automatically; your job is to preserve the glyph data when processing or serializing attributed strings.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

// Genmoji appear as NSAdaptiveImageGlyph in attributed strings.
// Standard UITextView handles them automatically.

class GenmojiTextViewController: UIViewController {
    let textView = UITextView()

    override func viewDidLoad() {
        super.viewDidLoad()
        textView.allowsEditingTextAttributes = true
        textView.frame = view.bounds
        textView.font = .preferredFont(forTextStyle: .body)
        view.addSubview(textView)
        // Users can insert Genmoji via the emoji keyboard — UITextView renders them natively
    }

    // When serializing text, preserve the adaptive image glyph attribute
    func saveText() -> Data? {
        try? textView.attributedText.data(
            from: NSRange(location: 0, length: textView.attributedText.length),
            documentAttributes: [.documentType: NSAttributedString.DocumentType.rtfd]
        )
    }

    // Restore text with Genmoji preserved
    func loadText(from data: Data) {
        textView.attributedText = try? NSAttributedString(
            data: data,
            options: [.documentType: NSAttributedString.DocumentType.rtfd],
            documentAttributes: nil
        )
    }
}
```

## 💎 Elite Implementation Tips

- `UITextView` and `NSTextView` render Genmoji (NSAdaptiveImageGlyph) automatically — no extra code needed
- When serializing attributed strings, use RTFD format to preserve adaptive image glyph data
- Do NOT strip unknown attributes from attributed strings — you'll lose Genmoji content
- `NSAdaptiveImageGlyph` contains multiple resolutions; the text system picks the right one for the current font size
- Available on iOS 18+, iPadOS 18+, and macOS 15+ with the emoji keyboard

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
