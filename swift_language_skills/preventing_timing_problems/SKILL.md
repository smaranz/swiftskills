---
name: Preventing Timing Problems When Using Closures
description: Rork-Max Quality skill for Preventing Timing Problems When Using Closures. Actionable Swift language patterns and best practices.
---

# Preventing Timing Problems When Using Closures

Understand how different API calls to your closures can affect your app.
Many of the APIs you use in Swift take a closure—or a function passed as an instance—as
a parameter. Because closures can contain code that interacts with multiple parts
of an app, it’s important to understand the different ways closures can be called
by the APIs you pass them to. Closures you pass to APIs can be called synchronously
(immediately) or asynchronously (sometime later). They may be called once, many times,
or never.
> Important: Making false assumptions about when a closure is called can lead to
> data inconsistency and app crashes.

## 🚀 Rork-Max Quality Snippet

```swift
// Capture semantics in closures
class DataLoader {
    var items: [String] = []

    func loadAsync() {
        // Capture `self` weakly to avoid retain cycles
        Task { [weak self] in
            let data = await fetchFromNetwork()
            self?.items = data  // Safe — self may be nil
        }
    }

    // Value-type capture for safety
    func processItems() {
        let currentItems = items  // Capture the value, not the reference
        DispatchQueue.global().async {
            for item in currentItems {
                process(item)
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `[weak self]` in escaping closures to prevent retain cycles
- Capture value types before the closure to avoid race conditions on mutable state
- Prefer `async/await` over completion handlers to eliminate callback timing issues

## When to Use

- Performing network requests, file I/O, or database queries off the main thread
- Managing shared mutable state safely with actors
- Running multiple independent tasks in parallel with `TaskGroup`

## Best Practices

- Use `async/await` instead of completion handlers
- Mark UI-updating code as `@MainActor` to ensure it runs on the main thread
- Use `Task { }` to bridge from synchronous to asynchronous contexts
- Prefer structured concurrency (`async let`, `TaskGroup`) over unstructured `Task`

## Common Pitfalls

- Blocking the main actor with synchronous work disguised as async
- Creating unbounded numbers of `Task` instances without cancellation
- Capturing `self` strongly in long-lived tasks causing memory leaks


