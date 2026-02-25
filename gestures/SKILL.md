---
name: Gestures
description: Rork-Max Quality skill for Gestures. Actionable patterns and best practices for SwiftUI development.
---

# Gestures

Define interactions from taps, clicks, and swipes to fine-grained gestures.
Respond to gestures by adding gesture modifiers to your views.
You can listen for taps, drags, pinches, and other standard gestures.
You can also compose custom gestures from individual gestures using the
`simultaneously(with:)`, `sequenced(before:)`, or
`exclusively(before:)` modifiers, or combine gestures with
keyboard modifiers using the `modifiers(_:)` modifier.
> Important: When you need a button, use a `Button` instance rather than
> a tap gesture. You can use any view as the button’s label, and the button
> type automatically provides many of the standard behaviors that users expect
> from a button, like accessibility labels and hints.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct DraggableCard: View {
    @State private var offset: CGSize = .zero
    @State private var isDragging = false

    var body: some View {
        RoundedRectangle(cornerRadius: 20, style: .continuous)
            .fill(.blue.gradient)
            .frame(width: 200, height: 120)
            .scaleEffect(isDragging ? 1.05 : 1.0)
            .offset(offset)
            .gesture(
                DragGesture()
                    .onChanged { value in
                        offset = value.translation
                        isDragging = true
                    }
                    .onEnded { _ in
                        withAnimation(.spring(response: 0.4, dampingFraction: 0.6)) {
                            offset = .zero
                            isDragging = false
                        }
                    }
            )
            .animation(.spring(response: 0.3), value: isDragging)
    }
}
```

## 💎 Elite Implementation Tips

- Use `.spring()` on `.onEnded` for natural snap-back motion
- Combine `DragGesture` with `scaleEffect` for tactile "pick up" feedback
- Use `.simultaneousGesture()` to avoid conflicts with `ScrollView` gestures


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
| `Adding interactivity with gestures` | Use gesture modifiers to add interactivity to your app. |

### Recognizing tap gestures

| API | Purpose |
|-----|---------|
| `onTapGesture(count:perform:)` | Adds an action to perform when this view recognizes a tap gesture. |
| `onTapGesture(count:coordinateSpace:perform:)` | Adds an action to perform when this view recognizes a tap gesture, |
| `TapGesture` | A gesture that recognizes one or more taps. |
| `SpatialTapGesture` | A gesture that recognizes one or more taps and reports their location. |

### Recognizing long press gestures

| API | Purpose |
|-----|---------|
| `onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)` | Adds an action to perform when this view recognizes a long press |
| `onLongPressGesture(minimumDuration:perform:onPressingChanged:)` | Adds an action to perform when this view recognizes a long press |
| `onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)` | Adds an action to perform when this view recognizes a |
| `LongPressGesture` | A gesture that succeeds when the user performs a long press. |

### Recognizing spatial events

| API | Purpose |
|-----|---------|
| `SpatialEventGesture` | A gesture that provides information about ongoing spatial events like |
| `SpatialEventCollection` | A collection of spatial input events that target a specific view. |
| `Chirality` | The chirality, or handedness, of a pose. |

### Recognizing gestures that change over time

| API | Purpose |
|-----|---------|
| `gesture(_:)` | Attaches an [`NSGestureRecognizerRepresentable`](/documentation/SwiftUI/NSGestureRecognizerRepresentable) to the view. |
| `gesture(_:isEnabled:)` | Attaches a gesture to the view with a lower precedence than gestures |
| `gesture(_:name:isEnabled:)` | Attaches a gesture to the view with a lower precedence than gestures |
| `gesture(_:including:)` | Attaches a gesture to the view with a lower precedence than gestures |
| `DragGesture` | A dragging motion that invokes an action as the drag-event sequence changes. |
| `WindowDragGesture` | A gesture that recognizes the motion of and handles dragging a window. |
| `MagnifyGesture` | A gesture that recognizes a magnification motion and tracks the amount of |
| `RotateGesture` | A gesture that recognizes a rotation motion and tracks the angle of the |

### Recognizing Apple Pencil gestures

| API | Purpose |
|-----|---------|
| `onPencilDoubleTap(perform:)` | Adds an action to perform after the user double-taps their Apple Pencil. |
| `onPencilSqueeze(perform:)` | Adds an action to perform when the user squeezes their Apple Pencil. |
| `preferredPencilDoubleTapAction` | The action that the user prefers to perform after double-tapping their |
| `preferredPencilSqueezeAction` | The action that the user prefers to perform when squeezing their Apple |
| `PencilPreferredAction` | An action that the user prefers to perform after double-tapping their |
| `PencilDoubleTapGestureValue` | Describes the value of an Apple Pencil double-tap gesture. |
| `PencilSqueezeGestureValue` | Describes the value of an Apple Pencil squeeze gesture. |
| `PencilSqueezeGesturePhase` | Describes the phase and value of an Apple Pencil squeeze gesture. |

### Combining gestures

| API | Purpose |
|-----|---------|
| `Composing SwiftUI gestures` | Combine gestures to create complex interactions. |
| `simultaneousGesture(_:including:)` | Attaches a gesture to the view to process simultaneously with gestures |
| `simultaneousGesture(_:isEnabled:)` | Attaches a gesture to the view to process simultaneously with gestures |
| `simultaneousGesture(_:name:isEnabled:)` | Attaches a gesture to the view to process simultaneously with gestures |
| `SequenceGesture` | A gesture that’s a sequence of two gestures. |
| `SimultaneousGesture` | A gesture containing two gestures that can happen at the same time with |
| `ExclusiveGesture` | A gesture that consists of two gestures where only one of them can succeed. |

### Defining custom gestures

| API | Purpose |
|-----|---------|
| `highPriorityGesture(_:including:)` | Attaches a gesture to the view with a higher precedence than gestures |
| `highPriorityGesture(_:isEnabled:)` | Attaches a gesture to the view with a higher precedence than gestures |
| `highPriorityGesture(_:name:isEnabled:)` | Attaches a gesture to the view with a higher precedence than gestures |
| `handGestureShortcut(_:isEnabled:)` | Assigns a hand gesture shortcut to the modified control. |
| `defersSystemGestures(on:)` | Sets the screen edge from which you want your gesture to take |
| `Gesture` | An instance that matches a sequence of events to a gesture, and returns a |
| `AnyGesture` | A type-erased gesture. |
| `HandActivationBehavior` | An activation behavior specific to hand-driven input. |

### Managing gesture state

| API | Purpose |
|-----|---------|
| `GestureState` | A property wrapper type that updates a property while the user performs a |
| `GestureStateGesture` | A gesture that updates the state provided by a gesture’s updating callback. |

### Handling activation events

| API | Purpose |
|-----|---------|
| `allowsWindowActivationEvents(_:)` | Configures whether gestures in this view hierarchy can handle events |

### Deprecated gestures

| API | Purpose |
|-----|---------|
| `MagnificationGesture` | A gesture that recognizes a magnification motion and tracks the amount of |
| `RotationGesture` | A gesture that recognizes a rotation motion and tracks the angle of the rotation. |
