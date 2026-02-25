---
name: Maintaining State in Your Apps
description: Rork-Max Quality skill for Maintaining State in Your Apps. Actionable Swift language patterns and best practices.
---

# Maintaining State in Your Apps

Use enumerations to capture and track the state of your app.
Effectively managing state, the bits of data that keep track of how the app is being
used at the moment, is an important part of a developing your app. Because enumerations
define a finite number of states, and can bundle associated values with each individual
state, you can use them to model the state of your app and its internal processes.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

@Observable
class CounterModel {
    var count = 0
    var history: [Int] = []

    func increment() {
        count += 1
        history.append(count)
    }

    func reset() {
        count = 0
        history.removeAll()
    }
}

struct CounterView: View {
    @State private var model = CounterModel()

    var body: some View {
        VStack {
            Text("\(model.count)")
                .font(.largeTitle)
            Button("Increment") { model.increment() }
            Button("Reset") { model.reset() }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `@State` for view-local state, `@Environment` for shared models injected from above
- `@Observable` classes give fine-grained updates — only views reading changed properties re-render
- Never create `@Observable` objects inside `body` — they get recreated every render

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


