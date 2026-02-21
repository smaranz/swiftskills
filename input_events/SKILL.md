---
name: Input events
description: Apple SwiftUI Documentation for Input events.
---

# Input events

Respond to input from a hardware device, like a keyboard or a Touch Bar.

## Overview

SwiftUI provides view modifiers that enable your app to listen for and react
to various kinds of user input. For example, you can create keyboard shortcuts,
respond to a form submission, or take input from the digital crown of an
Apple Watch.

![](images/com.apple.SwiftUI/input-events-hero@2x.png)

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/inputs>
in the Human Interface Guidelines.

## Topics

### Responding to keyboard input

[`onKeyPress(_:action:)`](/documentation/SwiftUI/View/onKeyPress(_:action:))

Performs an action if the user presses a key on a hardware keyboard
while the view has focus.

[`onKeyPress(phases:action:)`](/documentation/SwiftUI/View/onKeyPress(phases:action:))

Performs an action if the user presses any key on a hardware keyboard
while the view has focus.

[`onKeyPress(_:phases:action:)`](/documentation/SwiftUI/View/onKeyPress(_:phases:action:))

Performs an action if the user presses a key on a hardware keyboard
while the view has focus.

[`onKeyPress(characters:phases:action:)`](/documentation/SwiftUI/View/onKeyPress(characters:phases:action:))

Performs an action if the user presses one or more keys on a hardware
keyboard while the view has focus.

[`onKeyPress(keys:phases:action:)`](/documentation/SwiftUI/View/onKeyPress(keys:phases:action:))

Performs an action if the user presses one or more keys on a hardware
keyboard while the view has focus.

[`KeyPress`](/documentation/SwiftUI/KeyPress)

### Creating keyboard shortcuts

[`keyboardShortcut(_:)`](/documentation/SwiftUI/View/keyboardShortcut(_:))

Assigns a keyboard shortcut to the modified control.

[`keyboardShortcut(_:modifiers:)`](/documentation/SwiftUI/View/keyboardShortcut(_:modifiers:))

Defines a keyboard shortcut and assigns it to the modified control.

[`keyboardShortcut(_:modifiers:localization:)`](/documentation/SwiftUI/View/keyboardShortcut(_:modifiers:localization:))

Defines a keyboard shortcut and assigns it to the modified control.

[`keyboardShortcut`](/documentation/SwiftUI/EnvironmentValues/keyboardShortcut)

The keyboard shortcut that buttons in this environment will be triggered
with.

[`KeyboardShortcut`](/documentation/SwiftUI/KeyboardShortcut)

Keyboard shortcuts describe combinations of keys on a keyboard that the user
can press in order to activate a button or toggle.

[`KeyEquivalent`](/documentation/SwiftUI/KeyEquivalent)

Key equivalents consist of a letter, punctuation, or function key that can
be combined with an optional set of modifier keys to specify a keyboard
shortcut.

[`EventModifiers`](/documentation/SwiftUI/EventModifiers)

A set of key modifiers that you can add to a gesture.

### Responding to modifier keys

[`onModifierKeysChanged(mask:initial:_:)`](/documentation/SwiftUI/View/onModifierKeysChanged(mask:initial:_:))

Performs an action whenever the user presses or releases a hardware
modifier key.

[`modifierKeyAlternate(_:_:)`](/documentation/SwiftUI/View/modifierKeyAlternate(_:_:))

Builds a view to use in place of the modified view when the user presses
the modifier key(s) indicated by the given set.

### Responding to hover events

[`onHover(perform:)`](/documentation/SwiftUI/View/onHover(perform:))

Adds an action to perform when the user moves the pointer over or away
from the view’s frame.

[`onContinuousHover(coordinateSpace:perform:)`](/documentation/SwiftUI/View/onContinuousHover(coordinateSpace:perform:))

Adds an action to perform when the pointer enters, moves within, and
exits the view’s bounds.

[`hoverEffect(_:isEnabled:)`](/documentation/SwiftUI/View/hoverEffect(_:isEnabled:))

Applies a hover effect to this view.

[`hoverEffectDisabled(_:)`](/documentation/SwiftUI/View/hoverEffectDisabled(_:))

Adds a condition that controls whether this view can display hover
effects.

[`defaultHoverEffect(_:)`](/documentation/SwiftUI/View/defaultHoverEffect(_:))

Sets the default hover effect to use for views within this view.

[`isHoverEffectEnabled`](/documentation/SwiftUI/EnvironmentValues/isHoverEffectEnabled)

A Boolean value that indicates whether the view associated with this
environment allows hover effects to be displayed.

[`HoverPhase`](/documentation/SwiftUI/HoverPhase)

The current hovering state and value of the pointer.

[`HoverEffectPhaseOverride`](/documentation/SwiftUI/HoverEffectPhaseOverride)

Options for overriding a hover effect’s current phase.

[`OrnamentHoverContentEffect`](/documentation/SwiftUI/OrnamentHoverContentEffect)

Presents an ornament on hover using a custom effect.

[`OrnamentHoverEffect`](/documentation/SwiftUI/OrnamentHoverEffect)

Presents an ornament on hover.

### Modifying pointer appearance

[`pointerStyle(_:)`](/documentation/SwiftUI/View/pointerStyle(_:))

Sets the pointer style to display when the pointer is over the view.

[`PointerStyle`](/documentation/SwiftUI/PointerStyle)

A style describing the appearance of the pointer (also called a cursor) when
it’s hovered over a view.

[`pointerVisibility(_:)`](/documentation/SwiftUI/View/pointerVisibility(_:))

Sets the visibility of the pointer when it’s over the view.

### Changing view appearance for hover events

[`hoverEffect(_:)`](/documentation/SwiftUI/View/hoverEffect(_:))

Applies a hover effect to this view.

[`HoverEffect`](/documentation/SwiftUI/HoverEffect)

An effect applied when the pointer hovers over a view.

[`hoverEffect(_:in:isEnabled:)`](/documentation/SwiftUI/View/hoverEffect(_:in:isEnabled:))

Applies a hover effect to this view, optionally adding it to a
[`HoverEffectGroup`](/documentation/SwiftUI/HoverEffectGroup).

[`hoverEffect(in:isEnabled:body:)`](/documentation/SwiftUI/View/hoverEffect(in:isEnabled:body:))

Applies a hover effect to this view described by the given closure.

[`CustomHoverEffect`](/documentation/SwiftUI/CustomHoverEffect)

A type that represents how a view should change when a pointer hovers
over a view, or when someone looks at the view.

[`ContentHoverEffect`](/documentation/SwiftUI/ContentHoverEffect)

A `CustomHoverEffect` that applies effects to a view on hover using a
closure.

[`HoverEffectGroup`](/documentation/SwiftUI/HoverEffectGroup)

Describes a grouping of effects that activate together.

[`hoverEffectGroup()`](/documentation/SwiftUI/View/hoverEffectGroup())

Adds an implicit [`HoverEffectGroup`](/documentation/SwiftUI/HoverEffectGroup) to all effects defined on
descendant views, so that all effects added to subviews activate as a
group whenever this view or any descendant views are hovered.

[`hoverEffectGroup(_:)`](/documentation/SwiftUI/View/hoverEffectGroup(_:))

Adds a [`HoverEffectGroup`](/documentation/SwiftUI/HoverEffectGroup) to all effects defined on descendant views,
and activates the group whenever this view or any descendant views are
hovered.

[`hoverEffectGroup(id:in:behavior:)`](/documentation/SwiftUI/View/hoverEffectGroup(id:in:behavior:))

Adds a [`HoverEffectGroup`](/documentation/SwiftUI/HoverEffectGroup) to all effects defined on descendant views,
and activates the group whenever this view or any descendant views are
hovered.

[`GroupHoverEffect`](/documentation/SwiftUI/GroupHoverEffect)

A `CustomHoverEffect` that activates a named group of effects.

[`HoverEffectContent`](/documentation/SwiftUI/HoverEffectContent)

A type that describes the effects of a view for a particular hover
effect phase.

[`EmptyHoverEffectContent`](/documentation/SwiftUI/EmptyHoverEffectContent)

An empty base effect that you use to build other effects.

[`handPointerBehavior(_:)`](/documentation/SwiftUI/View/handPointerBehavior(_:))

Sets the behavior of the hand pointer while the user is interacting with
the view.

[`HandPointerBehavior`](/documentation/SwiftUI/HandPointerBehavior)

A behavior that can be applied to the hand pointer while the user is
interacting with a view.

### Responding to submission events

[`onSubmit(of:_:)`](/documentation/SwiftUI/View/onSubmit(of:_:))

Adds an action to perform when the user submits a value to this view.

[`submitScope(_:)`](/documentation/SwiftUI/View/submitScope(_:))

Prevents submission triggers originating from this view to invoke
a submission action configured by a submission modifier higher up
in the view hierarchy.

[`SubmitTriggers`](/documentation/SwiftUI/SubmitTriggers)

A type that defines various triggers that result in the firing of a
submission action.

### Labeling a submission event

[`submitLabel(_:)`](/documentation/SwiftUI/View/submitLabel(_:))

Sets the submit label for this view.

[`SubmitLabel`](/documentation/SwiftUI/SubmitLabel)

A semantic label describing the label of submission within a view hierarchy.

### Responding to commands

[`onMoveCommand(perform:)`](/documentation/SwiftUI/View/onMoveCommand(perform:))

Adds an action to perform in response to a move command, like when the
user presses an arrow key on a Mac keyboard, or taps the edge of the
Siri Remote when controlling an Apple TV.

[`onDeleteCommand(perform:)`](/documentation/SwiftUI/View/onDeleteCommand(perform:))

Adds an action to perform in response to the system’s Delete command,
or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.

[`pageCommand(value:in:step:)`](/documentation/SwiftUI/View/pageCommand(value:in:step:))

Steps a value through a range in response to page up or page down
commands.

[`onExitCommand(perform:)`](/documentation/SwiftUI/View/onExitCommand(perform:))

Sets up an action that triggers in response to receiving the exit
command while the view has focus.

[`onPlayPauseCommand(perform:)`](/documentation/SwiftUI/View/onPlayPauseCommand(perform:))

Adds an action to perform in response to the system’s Play/Pause
command.

[`onCommand(_:perform:)`](/documentation/SwiftUI/View/onCommand(_:perform:))

Adds an action to perform in response to the given selector.

[`MoveCommandDirection`](/documentation/SwiftUI/MoveCommandDirection)

Specifies the direction of an arrow key movement.

### Controlling hit testing

[`allowsTightening(_:)`](/documentation/SwiftUI/View/allowsTightening(_:))

Sets whether text in this view can compress the space between characters
when necessary to fit text in a line.

[`contentShape(_:eoFill:)`](/documentation/SwiftUI/View/contentShape(_:eoFill:))

Defines the content shape for hit testing.

[`contentShape(_:_:eoFill:)`](/documentation/SwiftUI/View/contentShape(_:_:eoFill:))

Sets the content shape for this view.

[`ContentShapeKinds`](/documentation/SwiftUI/ContentShapeKinds)

A kind for the content shape of a view.

### Interacting with the Digital Crown

[`digitalCrownAccessory(_:)`](/documentation/SwiftUI/View/digitalCrownAccessory(_:))

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

[`digitalCrownAccessory(content:)`](/documentation/SwiftUI/View/digitalCrownAccessory(content:))

Places an accessory View next to the Digital Crown on Apple Watch.

[`digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)`](/documentation/SwiftUI/View/digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:))

Tracks Digital Crown rotations by updating the specified binding.

[`digitalCrownRotation(_:onChange:onIdle:)`](/documentation/SwiftUI/View/digitalCrownRotation(_:onChange:onIdle:))

Tracks Digital Crown rotations by updating the specified binding.

[`digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)`](/documentation/SwiftUI/View/digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:))

Tracks Digital Crown rotations by updating the specified binding.

[`digitalCrownRotation(_:)`](/documentation/SwiftUI/View/digitalCrownRotation(_:))

Tracks Digital Crown rotations by updating the specified binding.

[`digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)`](/documentation/SwiftUI/View/digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:))

Tracks Digital Crown rotations by updating the specified binding.

[`DigitalCrownEvent`](/documentation/SwiftUI/DigitalCrownEvent)

An event emitted when the user rotates the Digital Crown.

[`DigitalCrownRotationalSensitivity`](/documentation/SwiftUI/DigitalCrownRotationalSensitivity)

The amount of Digital Crown rotation needed to move between two integer
numbers.

### Managing Touch Bar input

[`touchBar(content:)`](/documentation/SwiftUI/View/touchBar(content:))

Sets the content that the Touch Bar displays.

[`touchBar(_:)`](/documentation/SwiftUI/View/touchBar(_:))

Sets the Touch Bar content to be shown in the Touch Bar when applicable.

[`touchBarItemPrincipal(_:)`](/documentation/SwiftUI/View/touchBarItemPrincipal(_:))

Sets principal views that have special significance to this Touch Bar.

[`touchBarCustomizationLabel(_:)`](/documentation/SwiftUI/View/touchBarCustomizationLabel(_:))

Sets a user-visible string that identifies the view’s functionality.

[`touchBarItemPresence(_:)`](/documentation/SwiftUI/View/touchBarItemPresence(_:))

Sets the behavior of the user-customized view.

[`TouchBar`](/documentation/SwiftUI/TouchBar)

A container for a view that you can show in the Touch Bar.

[`TouchBarItemPresence`](/documentation/SwiftUI/TouchBarItemPresence)

Options that affect user customization of the Touch Bar.

### Responding to capture events

[`onCameraCaptureEvent(isEnabled:action:)`](/documentation/SwiftUI/View/onCameraCaptureEvent(isEnabled:action:))

Used to register an action triggered by system capture events.

[`onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)`](/documentation/SwiftUI/View/onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:))

Used to register actions triggered by system capture events.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
