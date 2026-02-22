---
name: View fundamentals
description: Rork-Max Quality skill for View fundamentals. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# View fundamentals


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# View fundamentals

Define the visual elements of your app using a hierarchy of views.

## Overview

Views are the building blocks that you use to declare your app’s user interface.
Each view contains a description of what to display for a given state.
Every bit of your app that’s visible to the user derives from the description
in a view, and any type that conforms to the [`View`](/documentation/SwiftUI/View) protocol can act as a
view in your app.

![](images/com.apple.SwiftUI/view-fundamentals-hero@2x.png)

Compose a custom view by combining built-in views that SwiftUI provides with
other custom views that you create in your view’s [`body`](/documentation/SwiftUI/View/body-8kl5o)
computed property. Configure views using the view modifiers that SwiftUI
provides, or by defining your own view modifiers using the
[`ViewModifier`](/documentation/SwiftUI/ViewModifier) protocol and the [`modifier(_:)`](/documentation/SwiftUI/View/modifier(_:)) method.

## Topics

### Creating a view

[Declaring a custom view](/documentation/SwiftUI/Declaring-a-Custom-View)

Define views and assemble them into a view hierarchy.

[`View`](/documentation/SwiftUI/View)

A type that represents part of your app’s user interface and provides
modifiers that you use to configure views.

[`ViewBuilder`](/documentation/SwiftUI/ViewBuilder)

A custom parameter attribute that constructs views from closures.

### Modifying a view

[Configuring views](/documentation/SwiftUI/Configuring-Views)

Adjust the characteristics of a view by applying view modifiers.

[Reducing view modifier maintenance](/documentation/SwiftUI/Reducing-View-Modifier-Maintenance)

Bundle view modifiers that you regularly reuse into a custom view modifier.

[`modifier(_:)`](/documentation/SwiftUI/View/modifier(_:))

Applies a modifier to a view and returns a new view.

[`ViewModifier`](/documentation/SwiftUI/ViewModifier)

A modifier that you apply to a view or another view modifier, producing a
different version of the original value.

[`EmptyModifier`](/documentation/SwiftUI/EmptyModifier)

An empty, or identity, modifier, used during development to switch
modifiers at compile time.

[`ModifiedContent`](/documentation/SwiftUI/ModifiedContent)

A value with a modifier applied to it.

[`EnvironmentalModifier`](/documentation/SwiftUI/EnvironmentalModifier)

A modifier that must resolve to a concrete modifier in an environment before
use.

[`ManipulableModifier`](/documentation/SwiftUI/ManipulableModifier)

[`ManipulableResponderModifier`](/documentation/SwiftUI/ManipulableResponderModifier)

[`ManipulableTransformBindingModifier`](/documentation/SwiftUI/ManipulableTransformBindingModifier)

[`ManipulationGeometryModifier`](/documentation/SwiftUI/ManipulationGeometryModifier)

[`ManipulationGestureModifier`](/documentation/SwiftUI/ManipulationGestureModifier)

[`ManipulationUsingGestureStateModifier`](/documentation/SwiftUI/ManipulationUsingGestureStateModifier)

[`Manipulable`](/documentation/SwiftUI/Manipulable)

A namespace for various manipulable related types.

### Responding to view life cycle updates

[`onAppear(perform:)`](/documentation/SwiftUI/View/onAppear(perform:))

Adds an action to perform before this view appears.

[`onDisappear(perform:)`](/documentation/SwiftUI/View/onDisappear(perform:))

Adds an action to perform after this view disappears.

### Managing the view hierarchy

[`id(_:)`](/documentation/SwiftUI/View/id(_:))

Binds a view’s identity to the given proxy value.

[`tag(_:includeOptional:)`](/documentation/SwiftUI/View/tag(_:includeOptional:))

Sets the unique tag value of this view.

[`equatable()`](/documentation/SwiftUI/View/equatable())

Prevents the view from updating its child view when its new value is the
same as its old value.

### Supporting view types

[`AnyView`](/documentation/SwiftUI/AnyView)

A type-erased view.

[`EmptyView`](/documentation/SwiftUI/EmptyView)

A view that doesn’t contain any content.

[`EquatableView`](/documentation/SwiftUI/EquatableView)

A view type that compares itself against its previous value and prevents its
child updating if its new value is the same as its old value.

[`SubscriptionView`](/documentation/SwiftUI/SubscriptionView)

A view that subscribes to a publisher with an action.

[`TupleView`](/documentation/SwiftUI/TupleView)

A View created from a swift tuple of View values.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
