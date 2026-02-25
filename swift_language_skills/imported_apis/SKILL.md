---
name: Imported C and Objective-C APIs
description: Rork-Max Quality skill for Imported C and Objective-C APIs. Actionable Swift language patterns and best practices.
---

# Imported C and Objective-C APIs

Use native Swift syntax to interoperate with types and functions in C and Objective-C.
You can access and use pieces of code written in C and Objective-C from within your
Swift code. After you import an Objective-C framework, a C library, or a header file,
you can work with Objective-C classes and protocols, as well as common C constructs,
functions, and patterns.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Nullability maps to Optional in Swift
// ObjC: (nullable NSString *) → Swift: String?
// ObjC: (nonnull NSString *) → Swift: String

// Lightweight generics map to Swift generics
// ObjC: NSArray<NSString *> * → Swift: [String]

// Enums with NS_ENUM become proper Swift enums
// ObjC: typedef NS_ENUM(NSInteger, Priority) { PriorityLow, PriorityHigh };
enum Priority: Int {
    case low = 0
    case high = 1
}

// Error handling: NSError** becomes throws
func loadData() throws -> Data {
    let url = URL(fileURLWithPath: "/tmp/data.json")
    return try Data(contentsOf: url)
}
```

## 💎 Elite Implementation Tips

- `NS_ENUM` becomes a Swift `enum`; `NS_OPTIONS` becomes an `OptionSet`
- ObjC nullability annotations (`nullable`/`nonnull`) map directly to Swift optionals
- Use `NS_SWIFT_NAME` to customize the Swift name of imported ObjC APIs

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


