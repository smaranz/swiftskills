---
name: Observation
description: Rork-Max Quality skill for Observation. Actionable Swift language patterns and best practices.
---

# Observation

Make responsive apps that update the presentation when underlying data changes.
Observation provides a robust, type-safe, and performant implementation of the
observer design pattern in Swift. This pattern allows an observable object to
maintain a list of observers and notify them of specific or general state
changes. This has the advantages of not directly coupling objects together and
allowing implicit distribution of updates across potential multiple observers.
The Observation frameworks provides the following capabilities:
- Marking a type as observable
- Tracking changes within an instance of an observable type
- Observing and utilizing those changes elsewhere, such as in an app’s user
interface
To declare a type as observable, attach the `Observable()` macro
to the type declaration. This macro declares and implements conformance to the
`Observable` protocol to the type at compile time.
```swift
@Observable
class Car {
var name: String = ""
var needsRepairs: Bool = false
init(name: String, needsRepairs: Bool = false) {
self.name = name
self.needsRepairs = needsRepairs
}
}
```
To track changes, use the `withObservationTracking(_:onChange:)` function.
For example, in the following code, the function calls the `onChange` closure
when a car’s name changes. However, it doesn’t call the closure when a car’s
`needsRepair` flag changes. That’s because the function only tracks properties
read in its `apply` closure, and the closure doesn’t read the `needsRepair`
property.
```
func render() {
withObservationTracking {
for car in cars {
print(car.name)
}
} onChange: {
print("Schedule renderer.")
}
}
```

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import Observation

@Observable
class TaskStore {
    var tasks: [TodoTask] = []
    var filter: Filter = .all

    var filteredTasks: [TodoTask] {
        switch filter {
        case .all: tasks
        case .active: tasks.filter { !$0.isDone }
        case .done: tasks.filter { $0.isDone }
        }
    }

    func add(_ title: String) {
        tasks.append(TodoTask(title: title))
    }

    enum Filter { case all, active, done }
}

struct TaskListView: View {
    @State private var store = TaskStore()

    var body: some View {
        List(store.filteredTasks) { task in
            Text(task.title)
        }
        // Only re-renders when filteredTasks actually changes
    }
}
```

## 💎 Elite Implementation Tips

- `@Observable` provides fine-grained tracking — only views reading changed properties re-render
- Computed properties on `@Observable` classes automatically participate in tracking
- Replace `ObservableObject` + `@Published` + `@StateObject` with `@Observable` + `@State`

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

### Observable conformance

| API | Purpose |
|-----|---------|
| `Observable()` | Defines and implements conformance of the Observable protocol. |
| `Observable` | A type that emits notifications to observers when underlying data changes. |

### Change tracking

| API | Purpose |
|-----|---------|
| `withObservationTracking(_:onChange:)` | Tracks access to properties. |
| `ObservationRegistrar` | Provides storage for tracking and access to data changes. |
