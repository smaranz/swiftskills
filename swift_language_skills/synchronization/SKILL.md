---
name: Synchronization
description: Rork-Max Quality skill for Synchronization. Actionable Swift language patterns and best practices.
---

# Synchronization

Build synchronization constructs using low-level, primitive operations.

## 🚀 Rork-Max Quality Snippet

```swift
import Synchronization

// Mutex for protecting shared state (Swift 6+)
let counter = Mutex(0)

func incrementSafely() {
    counter.withLock { value in
        value += 1
    }
}

// Atomic values for lock-free operations
let flag = Atomic<Bool>(false)

func toggle() {
    let oldValue = flag.exchange(true, ordering: .releasing)
    print("Was: \(oldValue)")
}

// Actor — the preferred Swift concurrency primitive
actor BankAccount {
    private var balance: Decimal = 0

    func deposit(_ amount: Decimal) { balance += amount }
    func withdraw(_ amount: Decimal) -> Bool {
        guard balance >= amount else { return false }
        balance -= amount
        return true
    }
}
```

## 💎 Elite Implementation Tips

- Prefer `actor` for high-level shared state protection in Swift concurrency
- Use `Mutex` from the Synchronization module for low-level, non-async critical sections
- Use `Atomic` for simple flag/counter operations that don't need locking

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
