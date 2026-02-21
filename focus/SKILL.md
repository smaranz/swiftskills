---
name: Focus
description: Apple SwiftUI Documentation for Focus.
---

# Focus

Identify and control which visible object responds to user interaction.

## Overview

Focus indicates which element in the display receives the next input.
Use view modifiers to indicate which views can receive focus, to detect
which view has focus, and to programmatically control focus state.

![](images/com.apple.SwiftUI/focus-hero@2x.png)

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/focus-and-selection>
in the Human Interface Guidelines.

## Topics

### Essentials

[Focus Cookbook: Supporting and enhancing focus-driven interactions in your SwiftUI app](/documentation/SwiftUI/Focus-Cookbook-sample)

Create custom focusable views with key-press handlers that accelerate keyboard input and support movement, and control focus programmatically.

### Indicating that a view can receive focus

[`focusable(_:)`](/documentation/SwiftUI/View/focusable(_:))

Specifies if the view is focusable.

[`focusable(_:interactions:)`](/documentation/SwiftUI/View/focusable(_:interactions:))

Specifies if the view is focusable, and if so, what focus-driven
interactions it supports.

[`FocusInteractions`](/documentation/SwiftUI/FocusInteractions)

Values describe different focus interactions that a view can support.

### Managing focus state

[`focused(_:equals:)`](/documentation/SwiftUI/View/focused(_:equals:))

Modifies this view by binding its focus state to the given state value.

[`focused(_:)`](/documentation/SwiftUI/View/focused(_:))

Modifies this view by binding its focus state to the given Boolean state
value.

[`isFocused`](/documentation/SwiftUI/EnvironmentValues/isFocused)

Returns whether the nearest focusable ancestor has focus.

[`FocusState`](/documentation/SwiftUI/FocusState)

A property wrapper type that can read and write a value that SwiftUI updates
as the placement of focus within the scene changes.

[`FocusedValue`](/documentation/SwiftUI/FocusedValue)

A property wrapper for observing values from the focused view or one of its
ancestors.

[`Entry()`](/documentation/SwiftUI/Entry())

Creates an environment values, transaction, container values,
or focused values entry.

[`FocusedValueKey`](/documentation/SwiftUI/FocusedValueKey)

A protocol for identifier types used when publishing and observing focused
values.

[`FocusedBinding`](/documentation/SwiftUI/FocusedBinding)

A convenience property wrapper for observing and automatically unwrapping
state bindings from the focused view or one of its ancestors.

[`searchFocused(_:)`](/documentation/SwiftUI/View/searchFocused(_:))

Modifies this view by binding the focus state of the search field
associated with the nearest searchable modifier to the given
Boolean value.

[`searchFocused(_:equals:)`](/documentation/SwiftUI/View/searchFocused(_:equals:))

Modifies this view by binding the focus state of the search field
associated with the nearest searchable modifier to the given value.

### Exposing value types to focused views

[`focusedValue(_:)`](/documentation/SwiftUI/View/focusedValue(_:))

Sets the focused value for the given object type.

[`focusedValue(_:_:)`](/documentation/SwiftUI/View/focusedValue(_:_:))

Modifies this view by injecting a value that you provide for use by
other views whose state depends on the focused view hierarchy.

[`focusedSceneValue(_:)`](/documentation/SwiftUI/View/focusedSceneValue(_:))

Sets the focused value for the given object type at a scene-wide scope.

[`focusedSceneValue(_:_:)`](/documentation/SwiftUI/View/focusedSceneValue(_:_:))

Modifies this view by injecting a value that you provide for use by
other views whose state depends on the focused scene.

[`FocusedValues`](/documentation/SwiftUI/FocusedValues)

A collection of state exported by the focused scene or view and its ancestors.

### Exposing reference types to focused views

[`focusedObject(_:)`](/documentation/SwiftUI/View/focusedObject(_:))

Creates a new view that exposes the provided object to other views whose
whose state depends on the focused view hierarchy.

[`focusedSceneObject(_:)`](/documentation/SwiftUI/View/focusedSceneObject(_:))

Creates a new view that exposes the provided object to other views whose
whose state depends on the active scene.

[`FocusedObject`](/documentation/SwiftUI/FocusedObject)

A property wrapper type for an observable object supplied by the focused
view or one of its ancestors.

### Setting focus scope

[`focusScope(_:)`](/documentation/SwiftUI/View/focusScope(_:))

Creates a focus scope that SwiftUI uses to limit default focus
preferences.

[`focusSection()`](/documentation/SwiftUI/View/focusSection())

Indicates that the view’s frame and cohort of focusable descendants
should be used to guide focus movement.

### Controlling default focus

[`prefersDefaultFocus(_:in:)`](/documentation/SwiftUI/View/prefersDefaultFocus(_:in:))

Indicates that the view should receive focus by default for a given
namespace.

[`defaultFocus(_:_:priority:)`](/documentation/SwiftUI/View/defaultFocus(_:_:priority:))

Defines a region of the window in which default focus is evaluated by
assigning a value to a given focus state binding.

[`DefaultFocusEvaluationPriority`](/documentation/SwiftUI/DefaultFocusEvaluationPriority)

Prioritizations for default focus preferences when evaluating where
to move focus in different circumstances.

### Resetting focus

[`resetFocus`](/documentation/SwiftUI/EnvironmentValues/resetFocus)

An action that requests the focus system to reevaluate default focus.

[`ResetFocusAction`](/documentation/SwiftUI/ResetFocusAction)

An environment value that provides the ability to reevaluate default
focus.

### Configuring effects

[`focusEffectDisabled(_:)`](/documentation/SwiftUI/View/focusEffectDisabled(_:))

Adds a condition that controls whether this view can display focus
effects, such as a default focus ring or hover effect.

[`isFocusEffectEnabled`](/documentation/SwiftUI/EnvironmentValues/isFocusEffectEnabled)

A Boolean value that indicates whether the view associated with this
environment allows focus effects to be displayed.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
