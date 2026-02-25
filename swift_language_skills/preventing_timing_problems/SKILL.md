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
import Foundation

// Preventing Timing Problems When Using Closures — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Preventing Timing Problems When Using Closures.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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


