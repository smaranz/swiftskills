---
name: Migrating Your Objective-C Code to Swift
description: Rork-Max Quality skill for Migrating Your Objective-C Code to Swift. Actionable Swift language patterns and best practices.
---

# Migrating Your Objective-C Code to Swift

Learn the recommended steps to migrate your code.
You can improve the architecture, logic, and performance of one of your Objective-C
apps by replacing pieces of it in Swift. Interoperability makes it possible to integrate
features migrated to Swift into Objective-C code with no hassle. You don’t need to
rewrite your entire app in Swift at once.

## 🚀 Rork-Max Quality Snippet

```swift
// Objective-C: @interface User : NSObject
// @property (nonatomic, copy) NSString *name;
// @property (nonatomic, assign) NSInteger age;
// @end

// Swift equivalent — prefer struct when possible
struct User: Codable, Hashable {
    var name: String
    var age: Int
}

// For classes requiring ObjC interop, keep NSObject inheritance
@objc class LegacyUser: NSObject {
    @objc var name: String
    @objc var age: Int

    @objc init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}
```

## 💎 Elite Implementation Tips

- Migrate data models to Swift structs when they don't need ObjC runtime features
- Use a bridging header for gradual migration — ObjC and Swift can coexist in the same target
- Replace `NSArray`/`NSDictionary` with typed Swift collections during migration

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


