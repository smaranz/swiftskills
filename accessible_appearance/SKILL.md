---
name: Accessible appearance
description: Rork-Max Quality skill for Accessible appearance. Actionable patterns and best practices for SwiftUI development.
---

# Accessible appearance

Enhance the legibility of content in your app’s interface.
Make content easier for people to see by making it larger, giving it greater
contrast, or reducing the amount of distracting motion.
For design guidance, see
in the Accessibility section of the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct AdaptiveView: View {
    @Environment(\.dynamicTypeSize) private var typeSize
    @Environment(\.colorSchemeContrast) private var contrast

    var body: some View {
        VStack {
            Text("Accessible Content")
                .font(.title)
            Text("Adapts to user preferences")
                .font(.body)
                .foregroundStyle(contrast == .increased ? .primary : .secondary)
        }
        .padding(typeSize.isAccessibilitySize ? 24 : 16)
    }
}
```

## 💎 Elite Implementation Tips

- Check `dynamicTypeSize.isAccessibilitySize` to adjust layouts for very large text
- Use semantic colors (`.primary`, `.secondary`) — they adapt to contrast settings
- Never rely on color alone to convey information — add icons or text labels


## When to Use

- Ensuring VoiceOver users can navigate and interact with all app features
- Supporting Dynamic Type, Reduce Motion, and high-contrast modes
- Providing accessible labels, hints, and traits for custom controls
- Implementing accessible drag-and-drop or custom gesture alternatives

## Best Practices

- Add `.accessibilityLabel()` to every image, icon, and custom control
- Use `.accessibilityAddTraits(.isButton)` for interactive non-button elements
- Group related elements with `.accessibilityElement(children: .combine)`
- Test with VoiceOver enabled — it reveals issues no other tool catches
- Support Dynamic Type by never hard-coding font sizes

## Common Pitfalls

- Decorative images without `.accessibilityHidden(true)` clutter VoiceOver
- Custom gestures with no accessible action alternative lock out VoiceOver users
- Using color alone to convey information (red = error) without text/shape cues

## Key APIs

### Managing color

| API | Purpose |
|-----|---------|
| `accessibilityIgnoresInvertColors(_:)` | Sets whether this view should ignore the system Smart Invert setting. |
| `accessibilityInvertColors` | Whether the system preference for Invert Colors is enabled. |
| `accessibilityDifferentiateWithoutColor` | Whether the system preference for Differentiate without Color is enabled. |

### Enlarging content

| API | Purpose |
|-----|---------|
| `accessibilityShowsLargeContentViewer()` | Adds a default large content view to be shown by |
| `accessibilityShowsLargeContentViewer(_:)` | Adds a custom large content view to be shown by |
| `accessibilityLargeContentViewerEnabled` | Whether the Large Content Viewer is enabled. |

### Improving legibility

| API | Purpose |
|-----|---------|
| `accessibilityShowButtonShapes` | Whether the system preference for Show Button Shapes is enabled. |
| `accessibilityReduceTransparency` | Whether the system preference for Reduce Transparency is enabled. |
| `legibilityWeight` | The font weight to apply to text. |
| `LegibilityWeight` | The Accessibility Bold Text user setting options. |

### Minimizing motion

| API | Purpose |
|-----|---------|
| `accessibilityDimFlashingLights` | Whether the setting to reduce flashing or strobing lights in video |
| `accessibilityPlayAnimatedImages` | Whether the setting for playing animations in an animated image is |
| `accessibilityReduceMotion` | Whether the system preference for Reduce Motion is enabled. |

### Using assistive access

| API | Purpose |
|-----|---------|
| `accessibilityAssistiveAccessEnabled` | A Boolean value that indicates whether Assistive Access is in use. |
| `AssistiveAccess` | A scene that presents an interface appropriate for Assistive Access on iOS |
