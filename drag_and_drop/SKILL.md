---
name: Drag and drop
description: Rork-Max Quality skill for Drag and drop. Actionable patterns and best practices for SwiftUI development.
---

# Drag and drop

Enable people to move or duplicate items by dragging them from one location to another.
Drag and drop offers people a convenient way to move content from one part of
your app to another, or from one app to another, using an intuitive dragging
gesture. Support this feature in your app by adding view modifiers
to potential source and destination views within your app’s interface.
In your modifiers, provide or accept types that conform to the
protocol, or that inherit from the
When possible, prefer using transferable items.
For design guidance, see
in the Human Interface Guidelines.


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

### Essentials

| API | Purpose |
|-----|---------|
| `Adopting drag and drop using SwiftUI` | Enable drag-and-drop interactions in lists, tables and custom views. |
| `Making a view into a drag source` | Adopt draggable API to provide items for drag-and-drop operations. |

### Configuring drag and drop behavior

| API | Purpose |
|-----|---------|
| `DragConfiguration` | The behavior of the drag, proposed by the dragging source. |
| `DropConfiguration` | Describes the behavior of the drop. |

### Moving items

| API | Purpose |
|-----|---------|
| `DragSession` | Describes the ongoing dragging session. |

### Moving transferable items

| API | Purpose |
|-----|---------|
| `draggable(_:)` | Activates this view as the source of a drag and drop operation. |
| `draggable(_:preview:)` | Activates this view as the source of a drag and drop operation. |
| `dropDestination(for:action:isTargeted:)` | Defines the destination of a drag and drop operation that handles the |

### Moving items using item providers

| API | Purpose |
|-----|---------|
| `itemProvider(_:)` | Provides a closure that vends the drag representation to be used for a |
| `onDrag(_:preview:)` | Activates this view as the source of a drag and drop operation. |
| `onDrag(_:)` | Activates this view as the source of a drag and drop operation. |
| `onDrop(of:isTargeted:perform:)` | Defines the destination of a drag-and-drop operation that handles the |
| `onDrop(of:delegate:)` | Defines the destination of a drag and drop operation using behavior |
| `DropDelegate` | An interface that you implement to interact with a drop operation in a view |
| `DropProposal` | The behavior of a drop. |
| `DropOperation` | Operation types that determine how a drag and drop session resolves when the |

### Describing preview formations

| API | Purpose |
|-----|---------|
| `DragDropPreviewsFormation` | On macOS, describes the way the dragged previews are visually composed. |

### Configuring spring loading

| API | Purpose |
|-----|---------|
| `springLoadingBehavior(_:)` | Sets the spring loading behavior this view. |
| `springLoadingBehavior` | The behavior of spring loaded interactions for the views associated |
| `SpringLoadingBehavior` | The options for controlling the spring loading behavior of views. |
