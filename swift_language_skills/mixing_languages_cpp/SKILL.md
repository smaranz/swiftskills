---
name: Mixing Languages in an Xcode project
description: Rork-Max Quality skill for Mixing Languages in an Xcode project. Actionable Swift language patterns and best practices.
---

# Mixing Languages in an Xcode project

Use C++ APIs in Swift – and Swift APIs in C++ – in a single framework target, and consume the framework’s APIs in a separate app target.
> Note: This sample code project is associated with WWDC 2023 session 10172: Mix Swift and C++.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Mixing Languages in an Xcode project — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Mixing Languages in an Xcode project.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Calling Objective-C APIs from Swift or vice versa
- Integrating C/C++ libraries into a Swift project
- Migrating an existing Objective-C codebase to Swift incrementally

## Best Practices

- Use a bridging header for Objective-C → Swift; `@objc` attribute for Swift → Objective-C
- Leverage `NS_SWIFT_NAME` in Objective-C headers for clean Swift API names
- Use `async` overloads of Objective-C completion-handler APIs

## Common Pitfalls

- Objective-C generics don't fully map to Swift generics — watch for `Any` erasure
- C pointers require careful memory management — use `withUnsafe*Pointer` wrappers
- KVO from Swift requires `@objc dynamic` properties


