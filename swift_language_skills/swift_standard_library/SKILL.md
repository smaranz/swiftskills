---
name: Swift Standard Library
description: Rork-Max Quality skill for Swift Standard Library. Actionable Swift language patterns and best practices.
---

# Swift Standard Library

Solve complex problems and write high-performance, readable code.
The Swift standard library defines a base layer of functionality for writing Swift
programs, including:
- Fundamental data types such as `Int`, `Double`, and `String`
- Common data structures such as `Array`, `Dictionary`, and `Set`
- Global functions such as `print(_:separator:terminator:)` and `abs(_:)`
- Protocols, such as `Collection` and `Equatable`, that describe
common abstractions.
- Protocols, such as `CustomDebugStringConvertible` and `CustomReflectable`,
that you use to customize operations that are available to all types.
- Protocols, such as `OptionSet`, that you use to provide implementations
that would otherwise require boilerplate code.
> Note: Experiment with Swift standard library types and learn high-level concepts
> using visualizations and practical examples. Learn how the Swift standard library
> uses protocols and generics to express powerful constraints. Download the playground
> below to get started.
>
> Swift Standard Library.playground

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Result type for error handling
func fetchUser(id: Int) -> Result<User, NetworkError> {
    guard id > 0 else { return .failure(.invalidID) }
    return .success(User(id: id, name: "Rork"))
}

// Codable for JSON parsing
struct User: Codable, Identifiable {
    let id: Int
    let name: String
}

let json = #"{"id": 1, "name": "Rork"}"#.data(using: .utf8)!
let user = try JSONDecoder().decode(User.self, from: json)

// Optional chaining and nil coalescing
let displayName = user.name.isEmpty ? "Anonymous" : user.name
```

## 💎 Elite Implementation Tips

- Leverage `Codable` for JSON/Plist parsing — avoid manual dictionary access
- Use `Result<Success, Failure>` for synchronous operations that can fail
- Prefer `guard let` for early exits, `if let` for conditional binding

## When to Use

- Working with fundamental types: strings, numbers, collections
- Choosing between value types (structs/enums) and reference types (classes)
- Implementing protocols like `Codable`, `Hashable`, `Equatable`, `Comparable`

## Best Practices

- Use `Int` unless you have a specific reason for sized integers
- Prefer `[Element]` array literal syntax over `Array<Element>`
- Use `guard let` for early exits and `if let` for optional binding
- Leverage `Codable` for JSON parsing instead of manual dictionary access

## Common Pitfalls

- Floating-point equality checks — use `isApproximatelyEqual(to:)` or tolerances
- Force-unwrapping optionals (`!`) without safety checks
- String index arithmetic — Swift strings are not random-access, use `String.Index`


