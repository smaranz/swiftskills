---
name: Accessible controls
description: Rork-Max Quality skill for Accessible controls. Actionable patterns and best practices for SwiftUI development.
---

# Accessible controls

Improve access to actions that your app can undertake.
Help people using assistive technologies to gain access to controls in
your app.
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

### Adding actions to views

| API | Purpose |
|-----|---------|
| `accessibilityAction(_:_:)` | Adds an accessibility action to the view. Actions allow assistive technologies, |
| `accessibilityActions(_:)` | Adds multiple accessibility actions to the view. |
| `accessibilityAction(named:_:)` | Adds an accessibility action to the view. Actions allow assistive technologies, |
| `accessibilityAction(action:label:)` | Adds an accessibility action to the view. Actions allow assistive technologies, |
| `accessibilityAction(intent:label:)` | Adds an accessibility action labeled by the contents of `label` to the view. |
| `accessibilityAction(_:intent:)` | Adds an accessibility action representing `actionKind` to the view. |
| `accessibilityAction(named:intent:)` | Adds an accessibility action labeled `name` to the view. Actions allow |
| `accessibilityAdjustableAction(_:)` | Adds an accessibility adjustable action to the view. Actions allow |

### Offering Quick Actions to people

| API | Purpose |
|-----|---------|
| `accessibilityQuickAction(style:content:)` | Adds a quick action to be shown by the system when active. |
| `accessibilityQuickAction(style:isActive:content:)` | Adds a quick action to be shown by the system when active. |
| `AccessibilityQuickActionStyle` | A type that describes the presentation style of an |

### Making gestures accessible

| API | Purpose |
|-----|---------|
| `accessibilityActivationPoint(_:)` | The activation point for an element is the location |
| `accessibilityActivationPoint(_:isEnabled:)` | The activation point for an element is the location |
| `accessibilityDragPoint(_:description:)` | The point an assistive technology should use to begin a drag interaction. |
| `accessibilityDragPoint(_:description:isEnabled:)` | The point an assistive technology should use to begin a drag interaction. |
| `accessibilityDropPoint(_:description:)` | The point an assistive technology should use to end a drag interaction. |
| `accessibilityDropPoint(_:description:isEnabled:)` | The point an assistive technology should use to end a drag interaction. |
| `accessibilityDirectTouch(_:options:)` | Explicitly set whether this accessibility element is a direct touch |
| `accessibilityZoomAction(_:)` | Adds an accessibility zoom action to the view. Actions allow |

### Controlling focus

| API | Purpose |
|-----|---------|
| `accessibilityFocused(_:)` | Modifies this view by binding its accessibility element’s focus state |
| `accessibilityFocused(_:equals:)` | Modifies this view by binding its accessibility element’s focus state to |
| `AccessibilityFocusState` | A property wrapper type that can read and write a value that SwiftUI updates |

### Managing interactivity

| API | Purpose |
|-----|---------|
| `accessibilityRespondsToUserInteraction(_:)` | Explicitly set whether this Accessibility element responds to user |
| `accessibilityRespondsToUserInteraction(_:isEnabled:)` | Explicitly set whether this Accessibility element responds to user |
