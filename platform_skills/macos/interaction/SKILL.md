---
name: MACOS Mouse, Keyboard, and Trackpad
description: Apple AppKit Documentation for MACOS Mouse, Keyboard, and Trackpad on macos.
---

# Mouse, Keyboard, and Trackpad

Handle events related to mouse, keyboard, and trackpad input.

## Discussion

The [`NSResponder`](/documentation/AppKit/NSResponder) class defines the responder chain, an ordered list of objects that respond to user events. When the user clicks the mouse button, taps on the trackpad, or presses a key, an event is generated and passed up the responder chain in search of an object that can respond to it. Any object that handles events must inherit from the [`NSResponder`](/documentation/AppKit/NSResponder) class. The core AppKit classes, [`NSApplication`](/documentation/AppKit/NSApplication), [`NSWindow`](/documentation/AppKit/NSWindow), and [`NSView`](/documentation/AppKit/NSView), inherit from [`NSResponder`](/documentation/AppKit/NSResponder).

An [`NSApplication`](/documentation/AppKit/NSApplication) object maintains a list of [`NSWindow`](/documentation/AppKit/NSWindow) objects—one for each window belonging to the app—and each [`NSWindow`](/documentation/AppKit/NSWindow) object maintains a hierarchy of [`NSView`](/documentation/AppKit/NSView) objects. This view hierarchy is used for both drawing the user interface and for handling events.

An [`NSWindow`](/documentation/AppKit/NSWindow) object handles window-level events and distributes other events to its views. An [`NSWindow`](/documentation/AppKit/NSWindow) object also has a delegate allowing you to customize its behavior.

## Topics

### Responder Objects

[`NSResponder`](/documentation/AppKit/NSResponder)

An abstract class that forms the basis of event and command processing in AppKit.

### Mouse, Keyboard, and Touch Events

[`NSEvent`](/documentation/AppKit/NSEvent)

An object that contains information about an input action, such as a mouse click or a key press.

[`NSTouch`](/documentation/AppKit/NSTouch)

A snapshot of a particular touch at an instant in time.

### Trackpad

[`NSPressureConfiguration`](/documentation/AppKit/NSPressureConfiguration)

An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.

[`NSHapticFeedbackManager`](/documentation/AppKit/NSHapticFeedbackManager)

An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad.

### Constants

[`NSEvent.EventTypeMask`](/documentation/AppKit/NSEvent/EventTypeMask)

Constants that you use to filter out specific event types from the stream of incoming events.

[`NSEvent.ButtonMask`](/documentation/AppKit/NSEvent/ButtonMask-swift.struct)

Constants you use to identify the activated tablet buttons in an event.

[`NSEvent.ModifierFlags`](/documentation/AppKit/NSEvent/ModifierFlags-swift.struct)

Flags that represent key states in an event object.

[`NSEvent.Phase`](/documentation/AppKit/NSEvent/Phase-swift.struct)

Constants that represent the possible phases during an event phase.

[`NSEvent.SwipeTrackingOptions`](/documentation/AppKit/NSEvent/SwipeTrackingOptions)

Constants that specify swipe-tracking options.

[`init(type:)`](/documentation/AppKit/NSEvent/EventTypeMask/init(type:))

Returns the event mask for the specified type.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
