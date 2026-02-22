---
name: Model data
description: Rork-Max Quality skill for Model data. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Model data


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Model data

Manage the data that your app uses to drive its interface.

## Overview

SwiftUI offers a declarative approach to user interface design. As you compose a
hierarchy of views, you also indicate data dependencies for the views.
When the data changes, either due to an external event or because of an action
that the user performs, SwiftUI automatically updates the affected parts of the
interface. As a result, the framework automatically performs most of the work
that view controllers traditionally do.

![](images/com.apple.SwiftUI/model-data-hero@2x.png)

The framework provides tools, like state variables and bindings, for connecting
your app’s data to the user interface. These tools help you maintain a single
source of truth for every piece of data in your app, in part by reducing the
amount of glue logic you write. Select the tool that best suits the task you
need to perform:

- Manage transient UI state locally within a view by wrapping value types as
  ``doc://com.apple.SwiftUI/documentation/SwiftUI/State`` properties.
- Share a reference to a source of truth, like local state, using the
  ``doc://com.apple.SwiftUI/documentation/SwiftUI/Binding`` property wrapper.
- Connect to and observe reference model data in views by applying the
  <doc://com.apple.documentation/documentation/Observation/Observable()>
  macro to the model data type. Instantiate an observable model data type
  directly in a view using a ``doc://com.apple.SwiftUI/documentation/SwiftUI/State`` property. Share the observable model data
  with other views in the hierarchy without passing a reference using the
  ``doc://com.apple.SwiftUI/documentation/SwiftUI/Environment`` property wrapper.

### Leveraging property wrappers

SwiftUI implements many data management types, like [`State`](/documentation/SwiftUI/State) and [`Binding`](/documentation/SwiftUI/Binding),
as Swift property wrappers. Apply a property wrapper by adding an attribute with
the wrapper’s name to a property’s declaration.

```
@State private var isVisible = true // Declares isVisible as a state variable.
```

The property gains the behavior that the wrapper specifies. The state and data
flow property wrappers in SwiftUI watch for changes in your data, and automatically
update affected views as necessary. When you refer directly to the property in your
code, you access the wrapped value, which for the `isVisible` state property in
the example above is the stored Boolean.

```
if isVisible == true {
    Text("Hello") // Only renders when isVisible is true.
}
```

Alternatively, you can access a property wrapper’s projected value by prefixing
the property name with the dollar sign (`$`). SwiftUI state and data flow
property wrappers project a [`Binding`](/documentation/SwiftUI/Binding), which is a two-way connection to
the wrapped value, allowing another view to access and mutate a single source of
truth.

```
Toggle("Visible", isOn: $isVisible) // The toggle can update the stored value.
```

For more information about property wrappers, see [Property Wrappers](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID617)
in [The Swift Programming Language](https://swift.org/documentation/#the-swift-programming-language).

## Topics

### Creating and sharing view state

[Managing user interface state](/documentation/SwiftUI/Managing-User-Interface-State)

Encapsulate view-specific data within your app’s view hierarchy to make your
views reusable.

[`State`](/documentation/SwiftUI/State)

A property wrapper type that can read and write a value managed by SwiftUI.

[`Bindable`](/documentation/SwiftUI/Bindable)

A property wrapper type that supports creating bindings to the mutable
properties of observable objects.

[`Binding`](/documentation/SwiftUI/Binding)

A property wrapper type that can read and write a value owned by a source of
truth.

### Creating model data

[Managing model data in your app](/documentation/SwiftUI/Managing-model-data-in-your-app)

Create connections between your app’s data model and views.

[Migrating from the Observable Object protocol to the Observable macro](/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro)

Update your existing app to leverage the benefits of Observation in Swift.

  <doc://com.apple.documentation/documentation/Observation/Observable()>

[Monitoring data changes in your app](/documentation/SwiftUI/Monitoring-model-data-changes-in-your-app)

Show changes to data in your app’s user interface by using observable
objects.

[`StateObject`](/documentation/SwiftUI/StateObject)

A property wrapper type that instantiates an observable object.

[`ObservedObject`](/documentation/SwiftUI/ObservedObject)

A property wrapper type that subscribes to an observable object and
invalidates a view whenever the observable object changes.

  <doc://com.apple.documentation/documentation/Combine/ObservableObject>

### Responding to data changes

[`onChange(of:initial:_:)`](/documentation/SwiftUI/View/onChange(of:initial:_:))

Adds a modifier for this view that fires an action when a specific
value changes.

[`onReceive(_:perform:)`](/documentation/SwiftUI/View/onReceive(_:perform:))

Adds an action to perform when this view detects data emitted by the
given publisher.

### Distributing model data throughout your app

[`environmentObject(_:)`](/documentation/SwiftUI/View/environmentObject(_:))

Supplies an observable object to a view’s hierarchy.

[`environmentObject(_:)`](/documentation/SwiftUI/Scene/environmentObject(_:))

Supplies an `ObservableObject` to a view subhierarchy.

[`EnvironmentObject`](/documentation/SwiftUI/EnvironmentObject)

A property wrapper type for an observable object that a parent or ancestor
view supplies.

### Managing dynamic data

[`DynamicProperty`](/documentation/SwiftUI/DynamicProperty)

An interface for a stored variable that updates an external property of a
view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
