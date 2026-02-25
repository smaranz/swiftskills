---
name: Objective-C and C Code Customization
description: Rork-Max Quality skill for Objective-C and C Code Customization. Actionable Swift language patterns and best practices.
---

# Objective-C and C Code Customization

Apply macros to your Objective-C APIs to customize how they’re imported into Swift.

## 🚀 Rork-Max Quality Snippet

```swift
// Exposing Swift to Objective-C
@objc class UserManager: NSObject {
    @objc dynamic var currentUser: String = ""

    @objc func fetchUsers(completion: @escaping ([String]) -> Void) {
        completion(["Alice", "Bob", "Charlie"])
    }
}

// Using Objective-C APIs from Swift
let notification = NotificationCenter.default
notification.addObserver(
    forName: UIApplication.didBecomeActiveNotification,
    object: nil, queue: .main
) { _ in
    print("App became active")
}
```

## 💎 Elite Implementation Tips

- Use `@objc` to expose Swift members to Objective-C; `@objc dynamic` for KVO
- Subclass `NSObject` for full Objective-C runtime compatibility
- Use `NS_SWIFT_NAME` in ObjC headers to customize how APIs appear in Swift

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


