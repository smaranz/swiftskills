---
name: Cocoa Design Patterns
description: Rork-Max Quality skill for Cocoa Design Patterns. Actionable Swift language patterns and best practices.
---

# Cocoa Design Patterns

Adopt and interoperate with Cocoa design patterns in your Swift apps.

## 🚀 Rork-Max Quality Snippet

```swift
// Delegation pattern in Swift
protocol DataSourceDelegate: AnyObject {
    func didLoadItems(_ items: [String])
    func didEncounterError(_ error: Error)
}

class DataSource {
    weak var delegate: DataSourceDelegate?

    func load() {
        Task {
            do {
                let items = try await fetchItems()
                delegate?.didLoadItems(items)
            } catch {
                delegate?.didEncounterError(error)
            }
        }
    }
}

// Modern alternative: use async/await or closures instead of delegation
class ModernDataSource {
    func load() async throws -> [String] {
        try await fetchItems()
    }
}
```

## 💎 Elite Implementation Tips

- Use `weak var delegate` to avoid retain cycles in the delegate pattern
- Prefer `async/await` over delegation for one-shot operations (network calls, file I/O)
- Keep the delegate pattern for continuous event streams (UIScrollViewDelegate, etc.)

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


