---
name: Mixing Languages in an Xcode project
description: Rork-Max Quality skill for Mixing Languages in an Xcode project. Actionable Swift language patterns and best practices.
---

# Mixing Languages in an Xcode project

Use C++ APIs in Swift – and Swift APIs in C++ – in a single framework target, and consume the framework’s APIs in a separate app target.
> Note: This sample code project is associated with WWDC 2023 session 10172: Mix Swift and C++.

## 🚀 Rork-Max Quality Snippet

```swift
// Swift can directly call C++ code through Swift/C++ interop (Swift 5.9+)
// In your target's build settings, enable "C++ Interoperability"

// C++ header (MathLib.hpp):
// int fibonacci(int n);
// struct Point { double x; double y; double distance() const; };

// Swift usage:
import MathLib

let result = fibonacci(10)  // Call C++ function directly
var point = Point(x: 3.0, y: 4.0)
let distance = point.distance()  // Call C++ method
```

## 💎 Elite Implementation Tips

- Enable "C++ and Objective-C Interoperability" in build settings for direct C++ access
- C++ value types with trivial move/copy map to Swift value types automatically
- Use a bridging header for ObjC/C, and module maps for C++ framework imports

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


