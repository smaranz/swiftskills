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
import Foundation

// Choosing Between Structures and Classes — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Choosing Between Structures and Classes.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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


