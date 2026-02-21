---
name: Environment values
description: Apple SwiftUI Documentation for Environment values.
---

# Environment values

Share data throughout a view hierarchy using the environment.

## Overview

Views in SwiftUI can react to configuration information that they read from the
environment using an [`Environment`](/documentation/SwiftUI/Environment) property wrapper.

![](images/com.apple.SwiftUI/environment-values-hero@2x.png)

A view inherits its environment from its container view, subject to explicit
changes from an [`environment(_:_:)`](/documentation/SwiftUI/View/environment(_:_:)) view modifier, or by implicit
changes from one of the many modifiers that operate on environment values.
As a result, you can configure a entire hierarchy of views by modifying the
environment of the group’s container.

You can find many built-in environment values in the [`EnvironmentValues`](/documentation/SwiftUI/EnvironmentValues)
structure. You can also create a custom [`EnvironmentValues`](/documentation/SwiftUI/EnvironmentValues) property by defining
a new property in an extension to the environment values structure and applying
the [`Entry()`](/documentation/SwiftUI/Entry()) macro to the variable declaration.

## Topics

### Accessing environment values

[`Environment`](/documentation/SwiftUI/Environment)

A property wrapper that reads a value from a view’s environment.

[`EnvironmentValues`](/documentation/SwiftUI/EnvironmentValues)

A collection of environment values propagated through a view hierarchy.

### Creating custom environment values

[`Entry()`](/documentation/SwiftUI/Entry())

Creates an environment values, transaction, container values,
or focused values entry.

[`EnvironmentKey`](/documentation/SwiftUI/EnvironmentKey)

A key for accessing values in the environment.

### Modifying the environment of a view

[`environment(_:)`](/documentation/SwiftUI/View/environment(_:))

Places an observable object in the view’s environment.

[`environment(_:_:)`](/documentation/SwiftUI/View/environment(_:_:))

Sets the environment value of the specified key path to the given value.

[`transformEnvironment(_:transform:)`](/documentation/SwiftUI/View/transformEnvironment(_:transform:))

Transforms the environment value of the specified key path with the
given function.

### Modifying the environment of a scene

[`environment(_:)`](/documentation/SwiftUI/Scene/environment(_:))

Places an observable object in the scene’s environment.

[`environment(_:_:)`](/documentation/SwiftUI/Scene/environment(_:_:))

Sets the environment value of the specified key path to the given value.

[`transformEnvironment(_:transform:)`](/documentation/SwiftUI/Scene/transformEnvironment(_:transform:))

Transforms the environment value of the specified key path with the
given function.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
