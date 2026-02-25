---
name: Environment values
description: Rork-Max Quality skill for Environment values. Actionable patterns and best practices for SwiftUI development.
---

# Environment values

Share data throughout a view hierarchy using the environment.
Views in SwiftUI can react to configuration information that they read from the
environment using an `Environment` property wrapper.
A view inherits its environment from its container view, subject to explicit
changes from an `environment(_:_:)` view modifier, or by implicit
changes from one of the many modifiers that operate on environment values.
As a result, you can configure a entire hierarchy of views by modifying the
environment of the group’s container.
You can find many built-in environment values in the `EnvironmentValues`
structure. You can also create a custom `EnvironmentValues` property by defining
a new property in an extension to the environment values structure and applying
the `Entry()` macro to the variable declaration.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Sharing state between views without explicit prop drilling
- Persisting user preferences or small data sets across launches
- Injecting dependencies (services, repositories) into the view hierarchy
- Propagating theme, locale, or feature-flag values through the environment

## Best Practices

- Use `@Observable` (Swift 6) instead of `ObservableObject` for finer-grained updates
- Prefer `@Environment` for dependency injection over singletons
- Use `@AppStorage` for simple UserDefaults-backed preferences
- Model domain data as value types (structs) and wrap in `@Observable` classes for mutation tracking

## Common Pitfalls

- Storing large data in `@AppStorage` — it's backed by UserDefaults, not a database
- Creating `@Observable` objects inside `body` — they get recreated every render
- Using `@EnvironmentObject` when `@Environment` with `@Observable` is cleaner in iOS 17+

## Key APIs

### Accessing environment values

| API | Purpose |
|-----|---------|
| `Environment` | A property wrapper that reads a value from a view’s environment. |
| `EnvironmentValues` | A collection of environment values propagated through a view hierarchy. |

### Creating custom environment values

| API | Purpose |
|-----|---------|
| `Entry()` | Creates an environment values, transaction, container values, |
| `EnvironmentKey` | A key for accessing values in the environment. |

### Modifying the environment of a view

| API | Purpose |
|-----|---------|
| `environment(_:)` | Places an observable object in the view’s environment. |
| `environment(_:_:)` | Sets the environment value of the specified key path to the given value. |
| `transformEnvironment(_:transform:)` | Transforms the environment value of the specified key path with the |

### Modifying the environment of a scene

| API | Purpose |
|-----|---------|
| `environment(_:)` | Places an observable object in the scene’s environment. |
| `environment(_:_:)` | Sets the environment value of the specified key path to the given value. |
| `transformEnvironment(_:transform:)` | Transforms the environment value of the specified key path with the |
