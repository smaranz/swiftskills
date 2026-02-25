---
name: Accessible navigation
description: Rork-Max Quality skill for Accessible navigation. Actionable patterns and best practices for SwiftUI development.
---

# Accessible navigation

Enable users to navigate to specific user interface elements using rotors.
An accessibility rotor is a shortcut that enables users
to quickly navigate to specific elements of the user interface,
and, optionally, to specific ranges of text within those elements.
The system automatically provides rotors for many navigable elements,
but you can supply additional rotors for specific purposes, or
replace system rotors when they don’t automatically pick
up off-screen elements, like those far down in a `LazyVStack` or a `List`.
For design guidance, see
in the Accessibility section of the Human Interface Guidelines.


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

### Working with rotors

| API | Purpose |
|-----|---------|
| `accessibilityRotor(_:entries:)` | Create an Accessibility Rotor with the specified user-visible label, |
| `accessibilityRotor(_:entries:entryID:entryLabel:)` | Create an Accessibility Rotor with the specified user-visible label |
| `accessibilityRotor(_:entries:entryLabel:)` | Create an Accessibility Rotor with the specified user-visible label |
| `accessibilityRotor(_:textRanges:)` | Create an Accessibility Rotor with the specified user-visible label |

### Creating rotors

| API | Purpose |
|-----|---------|
| `AccessibilityRotorContent` | Content within an accessibility rotor. |
| `AccessibilityRotorContentBuilder` | Result builder you use to generate rotor entry content. |
| `AccessibilityRotorEntry` | A struct representing an entry in an Accessibility Rotor. |

### Replacing system rotors

| API | Purpose |
|-----|---------|
| `AccessibilitySystemRotor` | Designates a Rotor that replaces one of the automatic, system-provided |

### Configuring rotors

| API | Purpose |
|-----|---------|
| `accessibilityRotorEntry(id:in:)` | Defines an explicit identifier tying an Accessibility element for this |
| `accessibilityLinkedGroup(id:in:)` | Links multiple accessibility elements so that the user can quickly |
| `accessibilitySortPriority(_:)` | Sets the sort priority order for this view’s accessibility element, |
