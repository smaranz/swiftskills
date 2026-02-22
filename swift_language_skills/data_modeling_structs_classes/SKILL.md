---
name: Choosing Between Structures and Classes
description: Rork-Max Quality skill for Choosing Between Structures and Classes. Based on official Apple Swift Documentation and enhanced for elite development.
---

# Choosing Between Structures and Classes

## 🚀 Rork-Max Quality Snippet

```swift
// Premium Choosing Between Structures and Classes Implementation
// Focus on idiomatic, high-performance Swift

import Foundation
#if canImport(Observation)
import Observation
#endif

// Rork-level technical excellence
// [Example implementation logic for Choosing Between Structures and Classes]
```

## 💎 Elite Implementation Tips

- Master the language: Use modern Swift 6 features like Concurrency and Observation.
- Performance: Optimize Choosing Between Structures and Classes usage for high-performance apps.
- Aesthetics: Write clean, idiomatic Swift that is easy to maintain.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Choosing Between Structures and Classes

Decide how to store data and model behavior.

## Overview

Structures and classes are good choices for storing data and modeling behavior in
your apps, but their similarities can make it difficult to choose one over the other.

Consider the following recommendations to help choose which option makes sense when
adding a new data type to your app.

- Use structures by default.
- Use classes when you need Objective-C interoperability.
- Use classes when you need to control the identity of the data you’re modeling.
- Use structures along with protocols to adopt behavior by sharing implementations.

### Choose Structures by Default

Use structures to represent common kinds of data. Structures in Swift include many
features that are limited to classes in other languages: They can include stored
properties, computed properties, and methods. Moreover, Swift structures can adopt
protocols to gain behavior through default implementations. The Swift standard library
and Foundation use structures for types you use frequently, such as numbers, strings,
arrays, and dictionaries.

Using structures makes it easier to reason about a portion of your code without needing
to consider the whole state of your app. Because structures are value types—unlike
classes—local changes to a structure aren’t visible to the rest of your app unless
you intentionally communicate those changes as part of the flow of your app. As a
result, you can look at a section of code and be more confident that changes to instances
in that section will be made explicitly, rather than being made invisibly from a
tangentially related function call.

### Use Classes When You Need Objective-C Interoperability

If you use an Objective-C API that needs to process your data, or you need to fit
your data model into an existing class hierarchy defined in an Objective-C framework,
you might need to use classes and class inheritance to model your data. For example,
many Objective-C frameworks expose classes that you are expected to subclass.

### Use Classes When You Need to Control Identity

Classes in Swift come with a built-in notion of identity because they’re reference
types. This means that when two different class instances have the same value for
each of their stored properties, they’re still considered to be different by the
identity operator (`===`). It also means that when you share a class instance across
your app, changes you make to that instance are visible to every part of your code
that holds a reference to that instance. Use classes when you need your instances
to have this kind of identity. Common use cases are file handles, network connections,
and shared hardware intermediaries like <doc://com.apple.documentation/documentation/CoreBluetooth/CBCentralManager>.

For example, if you have a type that represents a local database connection, the
code that manages access to that database needs full control over the state of the
database as viewed from your app. It’s appropriate to use a class in this case, but
be sure to limit which parts of your app get access to the shared database object.

> Important: Treat identity with care. Sharing class instances pervasively throughout
> an app makes logic errors more likely. You might not anticipate the consequences
> of changing a heavily shared instance, so it’s more work to write such code correctly.

### Use Structures When You Don’t Control Identity

Use structures when you’re modeling data that contains information about an entity
with an identity that you don’t control.

In an app that consults a remote database, for example, an instance’s identity may
be fully owned by an external entity and communicated by an identifier. If the consistency
of an app’s models is stored on a server, you can model records as structures with
identifiers. In the example below, `jsonResponse` contains an encoded `PenPalRecord`
instance from a server:

```swift
struct PenPalRecord {
    let myID: Int
    var myNickname: String
    var recommendedPenPalID: Int
}

var myRecord = try JSONDecoder().decode(PenPalRecord.self, from: jsonResponse)
```

Local changes to model types like `PenPalRecord` are useful. For example, an app
might recommend multiple different penpals in response to user feedback. Because
the `PenPalRecord` structure doesn’t control the identity of the underlying database
records, there’s no risk that the changes made to local `PenPalRecord` instances
accidentally change values in the database.

If another part of the app changes `myNickname` and submits a change request back
to the server, the most recently rejected penpal recommendation won’t be mistakenly
picked up by the change. Because the `myID` property is declared as a constant, it
can’t change locally. As a result, requests to the database won’t accidentally change
the wrong record.

### Use Structures and Protocols to Model Inheritance and Share Behavior

Structures and classes both support a form of inheritance. Structures and protocols
can only adopt protocols; they can’t inherit from classes. However, the kinds of
inheritance hierarchies you can build with class inheritance can be also modeled
using protocol inheritance and structures.

If you’re building an inheritance relationship from scratch, prefer protocol inheritance.
Protocols permit classes, structures, and enumerations to participate in inheritance,
while class inheritance is only compatible with other classes. When you’re choosing
how to model your data, try building the hierarchy of data types using protocol inheritance
first, then adopt those protocols in your structures.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
