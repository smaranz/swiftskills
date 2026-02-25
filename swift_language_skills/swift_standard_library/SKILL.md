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

// Swift Standard Library — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Swift Standard Library.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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


