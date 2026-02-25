---
name: Preferences
description: Rork-Max Quality skill for Preferences. Actionable patterns and best practices for SwiftUI development.
---

# Preferences

Indicate configuration preferences from views to their container views.
Whereas you use the environment to configure the subviews of a view, you use
preferences to send configuration information from subviews toward their
container. However, unlike configuration information that flows down a view
hierarchy from one container to many subviews, a single container needs to
reconcile potentially conflicting preferences flowing up from its many subviews.
When you use the `PreferenceKey` protocol to define a custom preference, you
indicate how to merge preferences from multiple subviews. You can then set a
value for the preference on a view using the `preference(key:value:)`
view modifier. Many built-in modifiers, like `navigationTitle(_:)`,
rely on preferences to send configuration information to their container.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct SizePreferenceKey: PreferenceKey {
    static var defaultValue: CGSize = .zero
    static func reduce(value: inout CGSize, nextValue: () -> CGSize) {
        value = nextValue()
    }
}

struct DynamicHeaderView: View {
    @State private var headerHeight: CGFloat = 0

    var body: some View {
        VStack {
            HeaderContent()
                .background(
                    GeometryReader { proxy in
                        Color.clear.preference(
                            key: SizePreferenceKey.self,
                            value: proxy.size
                        )
                    }
                )
            ScrollView {
                ContentView()
            }
            .padding(.top, headerHeight)
        }
        .onPreferenceChange(SizePreferenceKey.self) { size in
            headerHeight = size.height
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `PreferenceKey` to pass data UP the view hierarchy (child → parent)
- Combine with `GeometryReader` to measure child sizes for dynamic layout
- Always implement `reduce` to handle multiple children reporting preferences


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

### Setting preferences

| API | Purpose |
|-----|---------|
| `preference(key:value:)` | Sets a value for the given preference. |
| `transformPreference(_:_:)` | Applies a transformation to a preference value. |

### Creating custom preferences

| API | Purpose |
|-----|---------|
| `PreferenceKey` | A named value produced by a view. |

### Setting preferences based on geometry

| API | Purpose |
|-----|---------|
| `anchorPreference(key:value:transform:)` | Sets a value for the specified preference key, the value is a |
| `transformAnchorPreference(key:value:transform:)` | Sets a value for the specified preference key, the value is a |

### Responding to changes in preferences

| API | Purpose |
|-----|---------|
| `onPreferenceChange(_:perform:)` | Adds an action to perform when the specified preference key’s value |

### Generating backgrounds and overlays from preferences

| API | Purpose |
|-----|---------|
| `backgroundPreferenceValue(_:_:)` | Reads the specified preference value from the view, using it to |
| `backgroundPreferenceValue(_:alignment:_:)` | Reads the specified preference value from the view, using it to |
| `overlayPreferenceValue(_:_:)` | Reads the specified preference value from the view, using it to |
| `overlayPreferenceValue(_:alignment:_:)` | Reads the specified preference value from the view, using it to |
