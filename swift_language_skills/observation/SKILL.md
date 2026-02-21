---
name: Observation
description: Apple Observation Documentation for Observation.
---

# Observation

Make responsive apps that update the presentation when underlying data changes.

## Overview

Observation provides a robust, type-safe, and performant implementation of the
observer design pattern in Swift. This pattern allows an observable object to
maintain a list of observers and notify them of specific or general state
changes. This has the advantages of not directly coupling objects together and
allowing implicit distribution of updates across potential multiple observers.

The Observation frameworks provides the following capabilities:

- Marking a type as observable
- Tracking changes within an instance of an observable type
- Observing and utilizing those changes elsewhere, such as in an app’s user
  interface

To declare a type as observable, attach the [`Observable()`](/documentation/Observation/Observable()) macro
to the type declaration. This macro declares and implements conformance to the
[`Observable`](/documentation/Observation/Observable) protocol to the type at compile time.

```swift
@Observable
class Car {
    var name: String = ""
    var needsRepairs: Bool = false
    
    init(name: String, needsRepairs: Bool = false) {
        self.name = name
        self.needsRepairs = needsRepairs
    }
}
```

To track changes, use the [`withObservationTracking(_:onChange:)`](/documentation/Observation/withObservationTracking(_:onChange:)) function.
For example, in the following code, the function calls the `onChange` closure
when a car’s name changes. However, it doesn’t call the closure when a car’s
`needsRepair` flag changes. That’s because the function only tracks properties
read in its `apply` closure, and the closure doesn’t read the `needsRepair`
property.

```
func render() {
    withObservationTracking {
        for car in cars {
            print(car.name)
        }
    } onChange: {
        print("Schedule renderer.")
    }
}
```

## Topics

### Observable conformance

[`Observable()`](/documentation/Observation/Observable())

Defines and implements conformance of the Observable protocol.

[`Observable`](/documentation/Observation/Observable)

A type that emits notifications to observers when underlying data changes.

### Fine-tuning

### Change tracking

[`withObservationTracking(_:onChange:)`](/documentation/Observation/withObservationTracking(_:onChange:))

Tracks access to properties.

[`ObservationRegistrar`](/documentation/Observation/ObservationRegistrar)

Provides storage for tracking and access to data changes.

### Observation in SwiftUI

  <doc://com.apple.documentation/documentation/SwiftUI/Managing-model-data-in-your-app>

  <doc://com.apple.documentation/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
