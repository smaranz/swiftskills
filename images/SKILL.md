---
name: Images
description: Rork-Max Quality skill for Images. Actionable patterns and best practices for SwiftUI development.
---

# Images

Add images and symbols to your app’s user interface.
Display images, including
images that you store in an asset catalog, and images that you store on disk,
using an `Image` view.
For images that take time to retrieve
— for example, when you load an image from a network endpoint —
load the image asynchronously using `AsyncImage`.
You can instruct that view to display a placeholder during the load operation.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct ImageShowcase: View {
    var body: some View {
        VStack(spacing: 16) {
            // SF Symbol with hierarchical rendering
            Image(systemName: "cloud.sun.rain.fill")
                .symbolRenderingMode(.hierarchical)
                .font(.system(size: 64))
                .foregroundStyle(.blue)

            // Async remote image
            AsyncImage(url: URL(string: "https://example.com/photo.jpg")) { phase in
                switch phase {
                case .success(let image):
                    image.resizable().scaledToFill()
                case .failure:
                    Image(systemName: "photo").foregroundStyle(.secondary)
                default:
                    ProgressView()
                }
            }
            .frame(width: 200, height: 200)
            .clipShape(RoundedRectangle(cornerRadius: 16))
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography
- Use `AsyncImage` with phase handling for loading, success, and error states
- Apply `.resizable()` before `.scaledToFit()` / `.scaledToFill()` — order matters

## When to Use

- Displaying text with rich formatting, markdown, or attributed strings
- Rendering images from assets, SF Symbols, or async URLs
- Building interactive controls: buttons, toggles, pickers, sliders, steppers
- Creating menus, context menus, and keyboard shortcuts

## Best Practices

- Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography
- Prefer `AsyncImage` for remote images with placeholder and error states
- Use `Label` to pair text with icons — it adapts to context (list rows, menus, toolbars)
- Support Dynamic Type by using system text styles (`.title`, `.body`, `.caption`)

## Common Pitfalls

- Hard-coding font sizes instead of using Dynamic Type styles
- Loading large images synchronously on the main thread
- Forgetting to provide accessibility labels for image-only buttons

## Key APIs

### Creating an image

| API | Purpose |
|-----|---------|
| `Image` | A view that displays an image. |

### Configuring an image

| API | Purpose |
|-----|---------|
| `Fitting images into available space` | Adjust the size and shape of images in your app’s user interface by applying view modifiers. |
| `imageScale(_:)` | Scales images within the view according to one of the relative sizes |
| `imageScale` | The image scale for this environment. |
| `Image.Scale` | A scale to apply to vector images relative to text. |
| `Image.Orientation` | The orientation of an image. |
| `Image.ResizingMode` | The modes that SwiftUI uses to resize an image to fit within |

### Loading images asynchronously

| API | Purpose |
|-----|---------|
| `AsyncImage` | A view that asynchronously loads and displays an image. |
| `AsyncImagePhase` | The current phase of the asynchronous image loading operation. |

### Setting a symbol variant

| API | Purpose |
|-----|---------|
| `symbolVariant(_:)` | Makes symbols within the view show a particular variant. |
| `symbolVariants` | The symbol variant to use in this environment. |
| `SymbolVariants` | A variant of a symbol. |

### Managing symbol effects

| API | Purpose |
|-----|---------|
| `symbolEffect(_:options:isActive:)` | Returns a new view with a symbol effect added to it. |
| `symbolEffect(_:options:value:)` | Returns a new view with a symbol effect added to it. |
| `symbolEffectsRemoved(_:)` | Returns a new view with its inherited symbol image effects |
| `SymbolEffectTransition` | Creates a transition that applies the Appear, Disappear, DrawOn or |

### Setting symbol rendering modes

| API | Purpose |
|-----|---------|
| `symbolRenderingMode(_:)` | Sets the rendering mode for symbol images within this view. |
| `symbolRenderingMode` | The current symbol rendering mode, or `nil` denoting that the |
| `SymbolRenderingMode` | A symbol rendering mode. |
| `SymbolColorRenderingMode` | A method of filling a layer in a symbol image. |
| `SymbolVariableValueMode` | A method of rendering the variable value of a symbol image. |

### Rendering images from views

| API | Purpose |
|-----|---------|
| `ImageRenderer` | An object that creates images from SwiftUI views. |
