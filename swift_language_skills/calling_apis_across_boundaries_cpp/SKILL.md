---
name: Calling APIs Across Language Boundaries
description: Rork-Max Quality skill for Calling APIs Across Language Boundaries. Actionable Swift language patterns and best practices.
---

# Calling APIs Across Language Boundaries

Use a variety of C++ APIs in Swift – and vice-versa – across multiple targets and frameworks in an Xcode project.
> Note: This sample code project is associated with WWDC 2023 sessions 10172: Mix Swift and C++ and 10268: Meet mergeable libraries.

## 🚀 Rork-Max Quality Snippet

```swift
// Calling Swift from C++ and C++ from Swift

// Swift class exposed to C++
@_expose(Cxx)
public struct SwiftPoint {
    public var x: Double
    public var y: Double

    public func magnitude() -> Double {
        (x * x + y * y).squareRoot()
    }
}

// C++ code can now use:
// auto point = SwiftModule::SwiftPoint::init(3.0, 4.0);
// auto mag = point.magnitude();
```

## 💎 Elite Implementation Tips

- Use `@_expose(Cxx)` to make Swift types available to C++ code
- Swift value types map to C++ structs; Swift classes become reference-counted pointers
- Test cross-language calls with unit tests on both sides to catch ABI mismatches

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


