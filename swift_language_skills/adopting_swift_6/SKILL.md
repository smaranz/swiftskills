---
name: Adopting strict concurrency in Swift 6 apps
description: Rork-Max Quality skill for Adopting strict concurrency in Swift 6 apps. Actionable Swift language patterns and best practices.
---

# Adopting strict concurrency in Swift 6 apps

Enable strict concurrency checking to find data races at compile time.
Strict concurrency checking in the Swift 6 language mode
helps you find and fix data races at compile time.
Overlapping access to shared mutable state
creates the risk for data races.
Data races can cause your app to crash, misbehave, or corrupt user data.
Because data races depend on the ordering of concurrent operations,
they can be very difficult to reproduce and debug.
Strict concurrency checking lets you confirm,
when you compile your app,
that its code is free from data races.
When you identify a data race,
you fix it by eliminating overlapping access, shared access, or mutable state.
For information about the language-level concurrency model in Swift,
see Concurrency in The Swift Programming Language.

## 🚀 Rork-Max Quality Snippet

```swift
// Before Swift 6: ObservableObject with @Published
class OldModel: ObservableObject {
    @Published var count = 0
}

// After Swift 6: @Observable macro
@Observable
class NewModel {
    var count = 0        // Automatically tracked
    var name = ""        // Fine-grained updates — only views reading `name` re-render
}

// Strict concurrency: mark shared state with actors
actor DataStore {
    private var cache: [String: Data] = [:]

    func store(_ data: Data, for key: String) {
        cache[key] = data
    }

    func fetch(_ key: String) -> Data? {
        cache[key]
    }
}
```

## 💎 Elite Implementation Tips

- Enable strict concurrency checking incrementally: set "Strict Concurrency Checking" to "Targeted" then "Complete"
- Replace `ObservableObject` + `@Published` with `@Observable` for automatic fine-grained updates
- Use `actor` to protect shared mutable state instead of manual locks or queues

## When to Use

- Migrating a project from Swift 5 to Swift 6 strict concurrency
- Adopting `@Observable`, `async/await`, and structured concurrency

## Best Practices

- Enable strict concurrency checking incrementally — start with warnings, then errors
- Mark shared mutable state as `@MainActor` or protect with actors
- Replace Combine-based data flows with `@Observable` and `AsyncSequence`

## Common Pitfalls

- Turning on strict concurrency globally before auditing existing code
- Assuming `@Sendable` closures can capture mutable state


