---
name: Using Objective-C Runtime Features in Swift
description: Rork-Max Quality skill for Using Objective-C Runtime Features in Swift. Actionable Swift language patterns and best practices.
---

# Using Objective-C Runtime Features in Swift

Use selectors and key paths to interact with dynamic Objective-C APIs.
Some Objective-C APIs—like target-action—accept method or property names as parameters,
then use those names to dynamically call or access the methods or properties. In
Swift, you use the `#selector` and `#keyPath` expressions to represent those method
or property names as selectors or key paths, respectively.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

class SettingsStore: NSObject {
    @objc dynamic var fontSize: Int = 14
    @objc dynamic var isDarkMode: Bool = false

    // KVO observation
    func observeFontSize() -> NSKeyValueObservation {
        observe(\.fontSize, options: [.new, .old]) { _, change in
            print("Font changed: \(change.oldValue ?? 0) → \(change.newValue ?? 0)")
        }
    }
}

// Usage
let store = SettingsStore()
let observation = store.observeFontSize()
store.fontSize = 18  // Triggers observer
```

## 💎 Elite Implementation Tips

- `@objc dynamic` is required for KVO — Swift properties aren't KVO-compatible by default
- Store KVO observation tokens and invalidate them to avoid leaks
- Prefer `@Observable` (Swift 6) over KVO for new SwiftUI code

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


