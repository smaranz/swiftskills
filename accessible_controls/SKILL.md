---
name: Accessible controls
description: Apple SwiftUI Documentation for Accessible controls.
---

# Accessible controls

Improve access to actions that your app can undertake.

## Overview

Help people using assistive technologies to gain access to controls in
your app.

![](images/com.apple.SwiftUI/accessible-controls-hero@2x.png)

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/accessibility#Buttons-and-controls>
in the Accessibility section of the Human Interface Guidelines.

## Topics

### Adding actions to views

[`accessibilityAction(_:_:)`](/documentation/SwiftUI/View/accessibilityAction(_:_:))

Adds an accessibility action to the view. Actions allow assistive technologies,
such as the VoiceOver, to interact with the view by invoking the action.

[`accessibilityActions(_:)`](/documentation/SwiftUI/View/accessibilityActions(_:))

Adds multiple accessibility actions to the view.

[`accessibilityAction(named:_:)`](/documentation/SwiftUI/View/accessibilityAction(named:_:))

Adds an accessibility action to the view. Actions allow assistive technologies,
such as the VoiceOver, to interact with the view by invoking the action.

[`accessibilityAction(action:label:)`](/documentation/SwiftUI/View/accessibilityAction(action:label:))

Adds an accessibility action to the view. Actions allow assistive technologies,
such as the VoiceOver, to interact with the view by invoking the action.

[`accessibilityAction(intent:label:)`](/documentation/SwiftUI/View/accessibilityAction(intent:label:))

Adds an accessibility action labeled by the contents of `label` to the view.
Actions allow assistive technologies, such as the VoiceOver, to interact
with the view by invoking the action. When the action is performed, the
`intent` will be invoked.

[`accessibilityAction(_:intent:)`](/documentation/SwiftUI/View/accessibilityAction(_:intent:))

Adds an accessibility action representing `actionKind` to the view.
Actions allow assistive technologies, such as the VoiceOver, to interact
with the view by invoking the action. When the action is performed,
the `intent` will be invoked.

[`accessibilityAction(named:intent:)`](/documentation/SwiftUI/View/accessibilityAction(named:intent:))

Adds an accessibility action labeled `name` to the view. Actions allow
assistive technologies, such as the VoiceOver, to interact with the view
by invoking the action. When the action is performed, the `intent` will
be invoked.

[`accessibilityAdjustableAction(_:)`](/documentation/SwiftUI/View/accessibilityAdjustableAction(_:))

Adds an accessibility adjustable action to the view. Actions allow
assistive technologies, such as the VoiceOver, to interact with the
view by invoking the action.

[`accessibilityScrollAction(_:)`](/documentation/SwiftUI/View/accessibilityScrollAction(_:))

Adds an accessibility scroll action to the view. Actions allow
assistive technologies, such as the VoiceOver, to interact with the
view by invoking the action.

[`accessibilityActions(category:_:)`](/documentation/SwiftUI/View/accessibilityActions(category:_:))

Adds multiple accessibility actions to the view with a specific
category. Actions allow assistive technologies, such as VoiceOver,
to interact with the view by invoking the action and are grouped by
their category. When multiple action modifiers with an equal category
are applied to the view, the actions are combined together.

[`AccessibilityActionKind`](/documentation/SwiftUI/AccessibilityActionKind)

The structure that defines the kinds of available accessibility actions.

[`AccessibilityAdjustmentDirection`](/documentation/SwiftUI/AccessibilityAdjustmentDirection)

A directional indicator you use when making an accessibility adjustment.

[`AccessibilityActionCategory`](/documentation/SwiftUI/AccessibilityActionCategory)

Designates an accessibility action category that is provided and named
by the system.

### Offering Quick Actions to people

[`accessibilityQuickAction(style:content:)`](/documentation/SwiftUI/View/accessibilityQuickAction(style:content:))

Adds a quick action to be shown by the system when active.

[`accessibilityQuickAction(style:isActive:content:)`](/documentation/SwiftUI/View/accessibilityQuickAction(style:isActive:content:))

Adds a quick action to be shown by the system when active.

[`AccessibilityQuickActionStyle`](/documentation/SwiftUI/AccessibilityQuickActionStyle)

A type that describes the presentation style of an
accessibility quick action.

### Making gestures accessible

[`accessibilityActivationPoint(_:)`](/documentation/SwiftUI/View/accessibilityActivationPoint(_:))

The activation point for an element is the location
assistive technologies use to initiate gestures.

[`accessibilityActivationPoint(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityActivationPoint(_:isEnabled:))

The activation point for an element is the location
assistive technologies use to initiate gestures.

[`accessibilityDragPoint(_:description:)`](/documentation/SwiftUI/View/accessibilityDragPoint(_:description:))

The point an assistive technology should use to begin a drag interaction.

[`accessibilityDragPoint(_:description:isEnabled:)`](/documentation/SwiftUI/View/accessibilityDragPoint(_:description:isEnabled:))

The point an assistive technology should use to begin a drag interaction.

[`accessibilityDropPoint(_:description:)`](/documentation/SwiftUI/View/accessibilityDropPoint(_:description:))

The point an assistive technology should use to end a drag interaction.

[`accessibilityDropPoint(_:description:isEnabled:)`](/documentation/SwiftUI/View/accessibilityDropPoint(_:description:isEnabled:))

The point an assistive technology should use to end a drag interaction.

[`accessibilityDirectTouch(_:options:)`](/documentation/SwiftUI/View/accessibilityDirectTouch(_:options:))

Explicitly set whether this accessibility element is a direct touch
area. Direct touch areas passthrough touch events to the app rather
than being handled through an assistive technology, such as VoiceOver.
The modifier accepts an optional `AccessibilityDirectTouchOptions`
option set to customize the functionality of the direct touch area.

[`accessibilityZoomAction(_:)`](/documentation/SwiftUI/View/accessibilityZoomAction(_:))

Adds an accessibility zoom action to the view. Actions allow
assistive technologies, such as VoiceOver, to interact with the
view by invoking the action.

[`AccessibilityDirectTouchOptions`](/documentation/SwiftUI/AccessibilityDirectTouchOptions)

An option set that defines the functionality of a view’s direct touch area.

[`AccessibilityZoomGestureAction`](/documentation/SwiftUI/AccessibilityZoomGestureAction)

Position and direction information of a zoom gesture that someone performs
with an assistive technology like VoiceOver.

### Controlling focus

[`accessibilityFocused(_:)`](/documentation/SwiftUI/View/accessibilityFocused(_:))

Modifies this view by binding its accessibility element’s focus state
to the given boolean state value.

[`accessibilityFocused(_:equals:)`](/documentation/SwiftUI/View/accessibilityFocused(_:equals:))

Modifies this view by binding its accessibility element’s focus state to
the given state value.

[`AccessibilityFocusState`](/documentation/SwiftUI/AccessibilityFocusState)

A property wrapper type that can read and write a value that SwiftUI updates
as the focus of any active accessibility technology, such as VoiceOver,
changes.

### Managing interactivity

[`accessibilityRespondsToUserInteraction(_:)`](/documentation/SwiftUI/View/accessibilityRespondsToUserInteraction(_:))

Explicitly set whether this Accessibility element responds to user
interaction and would thus be interacted with by technologies such as
Switch Control, Voice Control or Full Keyboard Access.

[`accessibilityRespondsToUserInteraction(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityRespondsToUserInteraction(_:isEnabled:))

Explicitly set whether this Accessibility element responds to user
interaction and would thus be interacted with by technologies such as
Switch Control, Voice Control or Full Keyboard Access.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
