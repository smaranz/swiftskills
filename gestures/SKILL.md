---
name: Gestures
description: Rork-Max Quality skill for Gestures. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Gestures


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Gestures

Define interactions from taps, clicks, and swipes to fine-grained gestures.

## Overview

Respond to gestures by adding gesture modifiers to your views.
You can listen for taps, drags, pinches, and other standard gestures.

![](images/com.apple.SwiftUI/gestures-hero@2x.png)

You can also compose custom gestures from individual gestures using the
[`simultaneously(with:)`](/documentation/SwiftUI/Gesture/simultaneously(with:)), [`sequenced(before:)`](/documentation/SwiftUI/Gesture/sequenced(before:)), or
[`exclusively(before:)`](/documentation/SwiftUI/Gesture/exclusively(before:)) modifiers, or combine gestures with
keyboard modifiers using the [`modifiers(_:)`](/documentation/SwiftUI/Gesture/modifiers(_:)) modifier.

> Important: When you need a button, use a ``doc://com.apple.SwiftUI/documentation/SwiftUI/Button`` instance rather than
> a tap gesture. You can use any view as the button’s label, and the button
> type automatically provides many of the standard behaviors that users expect
> from a button, like accessibility labels and hints.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/gestures>
in the Human Interface Guidelines.

## Topics

### Essentials

[Adding interactivity with gestures](/documentation/SwiftUI/Adding-Interactivity-with-Gestures)

Use gesture modifiers to add interactivity to your app.

### Recognizing tap gestures

[`onTapGesture(count:perform:)`](/documentation/SwiftUI/View/onTapGesture(count:perform:))

Adds an action to perform when this view recognizes a tap gesture.

[`onTapGesture(count:coordinateSpace:perform:)`](/documentation/SwiftUI/View/onTapGesture(count:coordinateSpace:perform:))

Adds an action to perform when this view recognizes a tap gesture,
and provides the action with the location of the interaction.

[`TapGesture`](/documentation/SwiftUI/TapGesture)

A gesture that recognizes one or more taps.

[`SpatialTapGesture`](/documentation/SwiftUI/SpatialTapGesture)

A gesture that recognizes one or more taps and reports their location.

### Recognizing long press gestures

[`onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)`](/documentation/SwiftUI/View/onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:))

Adds an action to perform when this view recognizes a long press
gesture.

[`onLongPressGesture(minimumDuration:perform:onPressingChanged:)`](/documentation/SwiftUI/View/onLongPressGesture(minimumDuration:perform:onPressingChanged:))

Adds an action to perform when this view recognizes a long press
gesture.

[`onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)`](/documentation/SwiftUI/View/onLongTouchGesture(minimumDuration:perform:onTouchingChanged:))

Adds an action to perform when this view recognizes a
remote long touch gesture. A long touch gesture is when the finger is
on the remote touch surface without actually pressing.

[`LongPressGesture`](/documentation/SwiftUI/LongPressGesture)

A gesture that succeeds when the user performs a long press.

### Recognizing spatial events

[`SpatialEventGesture`](/documentation/SwiftUI/SpatialEventGesture)

A gesture that provides information about ongoing spatial events like
clicks and touches.

[`SpatialEventCollection`](/documentation/SwiftUI/SpatialEventCollection)

A collection of spatial input events that target a specific view.

[`Chirality`](/documentation/SwiftUI/Chirality)

The chirality, or handedness, of a pose.

### Recognizing gestures that change over time

[`gesture(_:)`](/documentation/SwiftUI/View/gesture(_:))

Attaches an [`NSGestureRecognizerRepresentable`](/documentation/SwiftUI/NSGestureRecognizerRepresentable) to the view.

[`gesture(_:isEnabled:)`](/documentation/SwiftUI/View/gesture(_:isEnabled:))

Attaches a gesture to the view with a lower precedence than gestures
defined by the view.

[`gesture(_:name:isEnabled:)`](/documentation/SwiftUI/View/gesture(_:name:isEnabled:))

Attaches a gesture to the view with a lower precedence than gestures
defined by the view.

[`gesture(_:including:)`](/documentation/SwiftUI/View/gesture(_:including:))

Attaches a gesture to the view with a lower precedence than gestures
defined by the view.

[`DragGesture`](/documentation/SwiftUI/DragGesture)

A dragging motion that invokes an action as the drag-event sequence changes.

[`WindowDragGesture`](/documentation/SwiftUI/WindowDragGesture)

A gesture that recognizes the motion of and handles dragging a window.

[`MagnifyGesture`](/documentation/SwiftUI/MagnifyGesture)

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

[`RotateGesture`](/documentation/SwiftUI/RotateGesture)

A gesture that recognizes a rotation motion and tracks the angle of the
rotation.

[`RotateGesture3D`](/documentation/SwiftUI/RotateGesture3D)

A gesture that recognizes 3D rotation motion and tracks the angle and axis
of the rotation.

[`GestureMask`](/documentation/SwiftUI/GestureMask)

Options that control how adding a gesture to a view affects other gestures
recognized by the view and its subviews.

### Recognizing Apple Pencil gestures

[`onPencilDoubleTap(perform:)`](/documentation/SwiftUI/View/onPencilDoubleTap(perform:))

Adds an action to perform after the user double-taps their Apple Pencil.

[`onPencilSqueeze(perform:)`](/documentation/SwiftUI/View/onPencilSqueeze(perform:))

Adds an action to perform when the user squeezes their Apple Pencil.

[`preferredPencilDoubleTapAction`](/documentation/SwiftUI/EnvironmentValues/preferredPencilDoubleTapAction)

The action that the user prefers to perform after double-tapping their
Apple Pencil, as selected in the Settings app.

[`preferredPencilSqueezeAction`](/documentation/SwiftUI/EnvironmentValues/preferredPencilSqueezeAction)

The action that the user prefers to perform when squeezing their Apple
Pencil, as selected in the Settings app.

[`PencilPreferredAction`](/documentation/SwiftUI/PencilPreferredAction)

An action that the user prefers to perform after double-tapping their
Apple Pencil.

[`PencilDoubleTapGestureValue`](/documentation/SwiftUI/PencilDoubleTapGestureValue)

Describes the value of an Apple Pencil double-tap gesture.

[`PencilSqueezeGestureValue`](/documentation/SwiftUI/PencilSqueezeGestureValue)

Describes the value of an Apple Pencil squeeze gesture.

[`PencilSqueezeGesturePhase`](/documentation/SwiftUI/PencilSqueezeGesturePhase)

Describes the phase and value of an Apple Pencil squeeze gesture.

[`PencilHoverPose`](/documentation/SwiftUI/PencilHoverPose)

A value describing the location and distance of an Apple Pencil hovering in
the area above a view’s bounds.

### Combining gestures

[Composing SwiftUI gestures](/documentation/SwiftUI/Composing-SwiftUI-Gestures)

Combine gestures to create complex interactions.

[`simultaneousGesture(_:including:)`](/documentation/SwiftUI/View/simultaneousGesture(_:including:))

Attaches a gesture to the view to process simultaneously with gestures
defined by the view.

[`simultaneousGesture(_:isEnabled:)`](/documentation/SwiftUI/View/simultaneousGesture(_:isEnabled:))

Attaches a gesture to the view to process simultaneously with gestures
defined by the view.

[`simultaneousGesture(_:name:isEnabled:)`](/documentation/SwiftUI/View/simultaneousGesture(_:name:isEnabled:))

Attaches a gesture to the view to process simultaneously with gestures
defined by the view.

[`SequenceGesture`](/documentation/SwiftUI/SequenceGesture)

A gesture that’s a sequence of two gestures.

[`SimultaneousGesture`](/documentation/SwiftUI/SimultaneousGesture)

A gesture containing two gestures that can happen at the same time with
neither of them preceding the other.

[`ExclusiveGesture`](/documentation/SwiftUI/ExclusiveGesture)

A gesture that consists of two gestures where only one of them can succeed.

### Defining custom gestures

[`highPriorityGesture(_:including:)`](/documentation/SwiftUI/View/highPriorityGesture(_:including:))

Attaches a gesture to the view with a higher precedence than gestures
defined by the view.

[`highPriorityGesture(_:isEnabled:)`](/documentation/SwiftUI/View/highPriorityGesture(_:isEnabled:))

Attaches a gesture to the view with a higher precedence than gestures
defined by the view.

[`highPriorityGesture(_:name:isEnabled:)`](/documentation/SwiftUI/View/highPriorityGesture(_:name:isEnabled:))

Attaches a gesture to the view with a higher precedence than gestures
defined by the view.

[`handGestureShortcut(_:isEnabled:)`](/documentation/SwiftUI/View/handGestureShortcut(_:isEnabled:))

Assigns a hand gesture shortcut to the modified control.

[`defersSystemGestures(on:)`](/documentation/SwiftUI/View/defersSystemGestures(on:))

Sets the screen edge from which you want your gesture to take
precedence over the system gesture.

[`Gesture`](/documentation/SwiftUI/Gesture)

An instance that matches a sequence of events to a gesture, and returns a
stream of values for each of its states.

[`AnyGesture`](/documentation/SwiftUI/AnyGesture)

A type-erased gesture.

[`HandActivationBehavior`](/documentation/SwiftUI/HandActivationBehavior)

An activation behavior specific to hand-driven input.

[`HandGestureShortcut`](/documentation/SwiftUI/HandGestureShortcut)

Hand gesture shortcuts describe finger and wrist movements that the user can
perform in order to activate a button or toggle.

### Managing gesture state

[`GestureState`](/documentation/SwiftUI/GestureState)

A property wrapper type that updates a property while the user performs a
gesture and resets the property back to its initial state when the gesture
ends.

[`GestureStateGesture`](/documentation/SwiftUI/GestureStateGesture)

A gesture that updates the state provided by a gesture’s updating callback.

### Handling activation events

[`allowsWindowActivationEvents(_:)`](/documentation/SwiftUI/View/allowsWindowActivationEvents(_:))

Configures whether gestures in this view hierarchy can handle events
that activate the containing window.

### Deprecated gestures

[`MagnificationGesture`](/documentation/SwiftUI/MagnificationGesture)

A gesture that recognizes a magnification motion and tracks the amount of
magnification.

[`RotationGesture`](/documentation/SwiftUI/RotationGesture)

A gesture that recognizes a rotation motion and tracks the angle of the rotation.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
