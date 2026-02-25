---
name: Input events
description: Rork-Max Quality skill for Input events. Actionable patterns and best practices for SwiftUI development.
---

# Input events

Respond to input from a hardware device, like a keyboard or a Touch Bar.
SwiftUI provides view modifiers that enable your app to listen for and react
to various kinds of user input. For example, you can create keyboard shortcuts,
respond to a form submission, or take input from the digital crown of an
Apple Watch.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct KeyboardShortcutView: View {
    @State private var events: [String] = []

    var body: some View {
        VStack {
            List(events, id: \.self) { event in
                Text(event)
            }
        }
        .onKeyPress(.return) {
            events.append("Return pressed")
            return .handled
        }
        .focusable()
        .onHover { hovering in
            events.append(hovering ? "Hover entered" : "Hover exited")
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `.onKeyPress()` for custom keyboard shortcuts on focusable views
- Use `.onHover` for pointer-aware UI on macOS and iPadOS
- Provide keyboard shortcut alternatives for all gesture-driven actions


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

### Responding to keyboard input

| API | Purpose |
|-----|---------|
| `onKeyPress(_:action:)` | Performs an action if the user presses a key on a hardware keyboard |
| `onKeyPress(phases:action:)` | Performs an action if the user presses any key on a hardware keyboard |
| `onKeyPress(_:phases:action:)` | Performs an action if the user presses a key on a hardware keyboard |
| `onKeyPress(characters:phases:action:)` | Performs an action if the user presses one or more keys on a hardware |
| `onKeyPress(keys:phases:action:)` | Performs an action if the user presses one or more keys on a hardware |

### Creating keyboard shortcuts

| API | Purpose |
|-----|---------|
| `keyboardShortcut(_:)` | Assigns a keyboard shortcut to the modified control. |
| `keyboardShortcut(_:modifiers:)` | Defines a keyboard shortcut and assigns it to the modified control. |
| `keyboardShortcut(_:modifiers:localization:)` | Defines a keyboard shortcut and assigns it to the modified control. |
| `keyboardShortcut` | The keyboard shortcut that buttons in this environment will be triggered |
| `KeyboardShortcut` | Keyboard shortcuts describe combinations of keys on a keyboard that the user |
| `KeyEquivalent` | Key equivalents consist of a letter, punctuation, or function key that can |
| `EventModifiers` | A set of key modifiers that you can add to a gesture. |

### Responding to modifier keys

| API | Purpose |
|-----|---------|
| `onModifierKeysChanged(mask:initial:_:)` | Performs an action whenever the user presses or releases a hardware |
| `modifierKeyAlternate(_:_:)` | Builds a view to use in place of the modified view when the user presses |

### Responding to hover events

| API | Purpose |
|-----|---------|
| `onHover(perform:)` | Adds an action to perform when the user moves the pointer over or away |
| `onContinuousHover(coordinateSpace:perform:)` | Adds an action to perform when the pointer enters, moves within, and |
| `hoverEffect(_:isEnabled:)` | Applies a hover effect to this view. |
| `hoverEffectDisabled(_:)` | Adds a condition that controls whether this view can display hover |
| `defaultHoverEffect(_:)` | Sets the default hover effect to use for views within this view. |
| `isHoverEffectEnabled` | A Boolean value that indicates whether the view associated with this |
| `HoverPhase` | The current hovering state and value of the pointer. |
| `HoverEffectPhaseOverride` | Options for overriding a hover effect’s current phase. |

### Modifying pointer appearance

| API | Purpose |
|-----|---------|
| `pointerStyle(_:)` | Sets the pointer style to display when the pointer is over the view. |
| `PointerStyle` | A style describing the appearance of the pointer (also called a cursor) when |
| `pointerVisibility(_:)` | Sets the visibility of the pointer when it’s over the view. |

### Changing view appearance for hover events

| API | Purpose |
|-----|---------|
| `hoverEffect(_:)` | Applies a hover effect to this view. |
| `HoverEffect` | An effect applied when the pointer hovers over a view. |
| `hoverEffect(_:in:isEnabled:)` | Applies a hover effect to this view, optionally adding it to a |
| `HoverEffectGroup` | — |
| `hoverEffect(in:isEnabled:body:)` | Applies a hover effect to this view described by the given closure. |
| `CustomHoverEffect` | A type that represents how a view should change when a pointer hovers |
| `ContentHoverEffect` | A `CustomHoverEffect` that applies effects to a view on hover using a |
| `HoverEffectGroup` | Describes a grouping of effects that activate together. |

### Responding to submission events

| API | Purpose |
|-----|---------|
| `onSubmit(of:_:)` | Adds an action to perform when the user submits a value to this view. |
| `submitScope(_:)` | Prevents submission triggers originating from this view to invoke |
| `SubmitTriggers` | A type that defines various triggers that result in the firing of a |

### Labeling a submission event

| API | Purpose |
|-----|---------|
| `submitLabel(_:)` | Sets the submit label for this view. |
| `SubmitLabel` | A semantic label describing the label of submission within a view hierarchy. |

### Responding to commands

| API | Purpose |
|-----|---------|
| `onMoveCommand(perform:)` | Adds an action to perform in response to a move command, like when the |
| `onDeleteCommand(perform:)` | Adds an action to perform in response to the system’s Delete command, |
| `pageCommand(value:in:step:)` | Steps a value through a range in response to page up or page down |
| `onExitCommand(perform:)` | Sets up an action that triggers in response to receiving the exit |
| `onPlayPauseCommand(perform:)` | Adds an action to perform in response to the system’s Play/Pause |
| `onCommand(_:perform:)` | Adds an action to perform in response to the given selector. |
| `MoveCommandDirection` | Specifies the direction of an arrow key movement. |

### Controlling hit testing

| API | Purpose |
|-----|---------|
| `allowsTightening(_:)` | Sets whether text in this view can compress the space between characters |
| `contentShape(_:eoFill:)` | Defines the content shape for hit testing. |
| `contentShape(_:_:eoFill:)` | Sets the content shape for this view. |
| `ContentShapeKinds` | A kind for the content shape of a view. |

### Interacting with the Digital Crown

| API | Purpose |
|-----|---------|
| `digitalCrownAccessory(_:)` | Specifies the visibility of Digital Crown accessory Views on Apple Watch. |
| `digitalCrownAccessory(content:)` | Places an accessory View next to the Digital Crown on Apple Watch. |
| `digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)` | Tracks Digital Crown rotations by updating the specified binding. |
| `digitalCrownRotation(_:onChange:onIdle:)` | Tracks Digital Crown rotations by updating the specified binding. |
| `digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)` | Tracks Digital Crown rotations by updating the specified binding. |
| `digitalCrownRotation(_:)` | Tracks Digital Crown rotations by updating the specified binding. |
| `digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)` | Tracks Digital Crown rotations by updating the specified binding. |
| `DigitalCrownEvent` | An event emitted when the user rotates the Digital Crown. |

### Managing Touch Bar input

| API | Purpose |
|-----|---------|
| `touchBar(content:)` | Sets the content that the Touch Bar displays. |
| `touchBar(_:)` | Sets the Touch Bar content to be shown in the Touch Bar when applicable. |
| `touchBarItemPrincipal(_:)` | Sets principal views that have special significance to this Touch Bar. |
| `touchBarCustomizationLabel(_:)` | Sets a user-visible string that identifies the view’s functionality. |
| `touchBarItemPresence(_:)` | Sets the behavior of the user-customized view. |
| `TouchBar` | A container for a view that you can show in the Touch Bar. |
| `TouchBarItemPresence` | Options that affect user customization of the Touch Bar. |

### Responding to capture events

| API | Purpose |
|-----|---------|
| `onCameraCaptureEvent(isEnabled:action:)` | Used to register an action triggered by system capture events. |
| `onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)` | Used to register actions triggered by system capture events. |
