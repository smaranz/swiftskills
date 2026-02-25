---
name: Synchronization
description: Rork-Max Quality skill for Synchronization. Actionable Swift language patterns and best practices.
---

# Synchronization

Build synchronization constructs using low-level, primitive operations.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Synchronization — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Synchronization.
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

## Key APIs

### Atomic Values

| API | Purpose |
|-----|---------|
| `Atomic` | An atomic value. |
| `AtomicLazyReference` | A lazily initializable atomic strong reference. |
| `WordPair` | A pair of two word sized `UInt`s. |
| `AtomicRepresentable` | A type that supports atomic operations through a separate atomic storage |
| `AtomicOptionalRepresentable` | An atomic value that also supports atomic operations when wrapped |

### Memory Ordering Semantics

| API | Purpose |
|-----|---------|
| `AtomicLoadOrdering` | Specifies the memory ordering semantics of an atomic load operation. |
| `AtomicStoreOrdering` | Specifies the memory ordering semantics of an atomic store operation. |
| `AtomicUpdateOrdering` | Specifies the memory ordering semantics of an atomic read-modify-write |
| `atomicMemoryFence(ordering:)` | Establishes a memory ordering without associating it with a |
