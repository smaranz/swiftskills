---
name: Choosing Between Structures and Classes
description: Rork-Max Quality skill for Choosing Between Structures and Classes. Actionable Swift language patterns and best practices.
---

# Choosing Between Structures and Classes

Decide how to store data and model behavior.
Structures and classes are good choices for storing data and modeling behavior in
your apps, but their similarities can make it difficult to choose one over the other.
Consider the following recommendations to help choose which option makes sense when
adding a new data type to your app.
- Use structures by default.
- Use classes when you need Objective-C interoperability.
- Use classes when you need to control the identity of the data you’re modeling.
- Use structures along with protocols to adopt behavior by sharing implementations.

## 🚀 Rork-Max Quality Snippet

```swift
// Value type — use for most data models
struct Coordinate: Equatable, Hashable, Codable {
    var latitude: Double
    var longitude: Double

    var isValid: Bool {
        (-90...90).contains(latitude) && (-180...180).contains(longitude)
    }
}

// Reference type — use when identity matters
@Observable
class UserSession {
    var currentUser: User?
    var isAuthenticated: Bool { currentUser != nil }

    func login(user: User) {
        currentUser = user
    }
}

// Enum with associated values — perfect for state machines
enum LoadingState<T> {
    case idle
    case loading
    case loaded(T)
    case failed(Error)
}
```

## 💎 Elite Implementation Tips

- Default to structs — use classes only when identity, inheritance, or reference semantics are needed
- Use enums with associated values for state machines and result types
- Implement `Equatable`, `Hashable`, and `Codable` on types used in collections or SwiftUI

## When to Use

- Designing app data models with structs, classes, and enums
- Choosing between value semantics (struct) and reference semantics (class)
- Implementing protocol conformances for custom types

## Best Practices

- Default to structs — use classes only when identity or inheritance is needed
- Implement `Equatable` and `Hashable` for types used in collections or SwiftUI
- Use enums with associated values for state machines and API responses

## Common Pitfalls

- Using classes when structs would be simpler and safer
- Forgetting that struct mutations create new copies — this matters for large data
- Not implementing `Hashable` on types used as `ForEach` identifiers


