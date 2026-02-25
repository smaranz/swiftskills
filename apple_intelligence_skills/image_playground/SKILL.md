---
name: Apple Intelligence: Image Playground
description: Rork-Max Quality skill for Apple Intelligence: Image Playground. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: Image Playground

Present a system interface to generate images based on descriptive information.
Use the `ImagePlayground` framework to generate custom images using
system-supported styles. To generate images, you specify a text
description of what you want, an optional image, and the style you want
the image to adopt. Use that information to present a system sheet from your
SwiftUI view, or present a system view controller from your UIKit or AppKit interface.
The system interface manages all interactions with the person, and upon
success delivers an image for you to incorporate into your content.
You can also use a programmatic interface to generate images without
interactions.

## 🚀 Rork-Max Quality Snippet

```swift
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
```

## 💎 Elite Implementation Tips

- Check `@Environment(\.supportsImagePlayground)` before showing the generate button — not all devices support it
- Use `.imagePlaygroundSheet(isPresented:concepts:)` with pre-filled concepts to guide generation toward relevant results
- The sheet returns a file URL — load it with `UIImage(contentsOfFile:)` or `Image(nsImage:)` on macOS
- Use `ImageCreator` for programmatic generation without UI (headless batch processing)
- Available on iOS 18.1+, iPadOS 18.1+, and macOS 15.1+ with Apple Intelligence enabled
- All image generation runs on-device — no data is sent to Apple servers

## When to Use

- Letting users generate images from text descriptions within your app
- Adding AI-generated stickers, avatars, or illustrations

## Best Practices

- Present the Image Playground sheet for the best user experience
- Provide suggested concepts to guide generation toward relevant results

## Common Pitfalls

- Not checking device capability — Image Playground requires Apple Intelligence hardware

## Key APIs

### UIKit and AppKit presentation

| API | Purpose |
|-----|---------|
| `ImagePlaygroundViewController` | Displays a standard system interface to generate images from |

### Programmatic creation

| API | Purpose |
|-----|---------|
| `ImageCreator` | Generates images programmatically from the description and style information |

### Platform support

| API | Purpose |
|-----|---------|
| `ImagePlaygroundConcept` | Text elements that specify the content to include in the image. |
| `ImagePlaygroundStyle` | Style options that determine the appearance of generated images. |
