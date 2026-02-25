---
name: Accessibility fundamentals
description: Rork-Max Quality skill for Accessibility fundamentals. Actionable patterns and best practices for SwiftUI development.
---

# Accessibility fundamentals

Make your SwiftUI apps accessible to everyone, including people with
disabilities.
Like all Apple UI frameworks, SwiftUI comes with built-in
accessibility support. The framework introspects common elements like
navigation views, lists, text fields, sliders, buttons, and so on, and
provides basic accessibility labels and values by default. You
don’t have to do any extra work to enable these standard accessibility
features.
SwiftUI also provides tools to help you enhance the accessibility
of your app. To find out what enhancements you need, try using your app
with accessibility features like VoiceOver, Voice Control, and Switch
Control, or get feedback from users of your app that regularly use
these features. Then use the accessibility view modifiers that SwiftUI
provides to improve the experience. For example, you can explicitly add
accessibility labels to elements in your UI using the
`accessibilityLabel(_:)` or the
`accessibilityValue(_:)` view modifier.
Customize your use of accessibility modifiers for all the platforms that your
app runs on. For example, you may need to adjust the
accessibility elements for a companion Apple Watch app that shares a common
code base with an iOS app. If you integrate AppKit or UIKit controls in
SwiftUI, expose any accessibility labels and make them accessible from your
`NSViewRepresentable` or `UIViewRepresentable` views, or provide custom
accessibility information if the underlying accessibility labels aren’t
available.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


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

### Essentials

| API | Purpose |
|-----|---------|
| `Creating accessible views` | Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views. |

### Creating accessible elements

| API | Purpose |
|-----|---------|
| `accessibilityElement(children:)` | Creates a new accessibility element, or modifies the |
| `AccessibilityChildBehavior` | — |
| `accessibilityChildren(children:)` | Replaces the existing accessibility element’s children with one or |
| `accessibilityRepresentation(representation:)` | Replaces one or more accessibility elements for this view with new |
| `AccessibilityChildBehavior` | Defines the behavior for the child elements of the new parent element. |

### Identifying elements

| API | Purpose |
|-----|---------|
| `accessibilityIdentifier(_:)` | Uses the string you specify to identify the view. |
| `accessibilityIdentifier(_:isEnabled:)` | Uses the string you specify to identify the view. |

### Hiding elements

| API | Purpose |
|-----|---------|
| `accessibilityHidden(_:)` | Specifies whether to hide this view from system accessibility features. |
| `accessibilityHidden(_:isEnabled:)` | Specifies whether to hide this view from system accessibility features. |

### Supporting types

| API | Purpose |
|-----|---------|
| `AccessibilityTechnologies` | Accessibility technologies available to the system. |
| `AccessibilityAttachmentModifier` | A view modifier that adds accessibility properties to the view |
