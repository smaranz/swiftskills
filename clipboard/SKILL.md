---
name: Clipboard
description: Rork-Max Quality skill for Clipboard. Actionable patterns and best practices for SwiftUI development.
---

# Clipboard

Enable people to move or duplicate items by issuing Copy and Paste commands.
When people issue standard Copy and Cut commands, they expect to move
items to the system’s Clipboard, from which they can paste the items into
another place in the same app or into another app. Your app can participate
in this activity if you add view modifiers that indicate how to respond to
the standard commands.
In your copy and paste modifiers, provide or accept types that conform to the
protocol, or that inherit from the
When possible, prefer using transferable items.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Handling tap, long press, drag, magnification, or rotation gestures
- Implementing drag-and-drop between views or apps
- Reading clipboard content or providing copy/paste support
- Processing keyboard, pencil, or game controller input events

## Best Practices

- Use `.onTapGesture` for simple taps; `DragGesture` for custom interactive motion
- Combine `.gesture()` with `.simultaneously()` or `.sequenced()` for complex interactions
- Prefer `Transferable` protocol (iOS 16+) for modern drag-and-drop and sharing
- Always provide visual feedback during gesture recognition (scale, opacity, highlight)

## Common Pitfalls

- Gesture conflicts with `ScrollView` — use `.simultaneousGesture()` or `.highPriorityGesture()`
- Forgetting minimum distance on `DragGesture` when used inside scroll views
- Not testing gestures with VoiceOver — ensure all gesture-driven actions have accessible alternatives

## Key APIs

### Copying transferable items

| API | Purpose |
|-----|---------|
| `copyable(_:)` | Specifies a list of items to copy in response to the system’s Copy |
| `cuttable(for:action:)` | Specifies an action that moves items to the Clipboard in response to |
| `pasteDestination(for:action:validator:)` | Specifies an action that adds validated items to a view in response to |

### Copying items using item providers

| API | Purpose |
|-----|---------|
| `onCopyCommand(perform:)` | Adds an action to perform in response to the system’s Copy command. |
| `onCutCommand(perform:)` | Adds an action to perform in response to the system’s Cut command. |
| `onPasteCommand(of:perform:)` | Adds an action to perform in response to the system’s Paste command. |
| `onPasteCommand(of:validator:perform:)` | Adds an action to perform in response to the system’s Paste command with |
