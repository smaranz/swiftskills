---
name: Persistent storage
description: Rork-Max Quality skill for Persistent storage. Actionable patterns and best practices for SwiftUI development.
---

# Persistent storage

Store data for use across sessions of your app.
The operating system provides ways to store data when your app closes,
so that when people open your app again later, they can continue working without
interruption. The mechanism that you use depends on factors like what and how
much you need to store, whether you need serialized or random access to the
data, and so on.
You use the same kinds of storage in a SwiftUI app that you use
in any other app. For example, you can access files on disk using the
However, SwiftUI also provides conveniences that make it easier to use certain
kinds of persistent storage in a declarative environment. For example, you can
use `FetchRequest` and `FetchedResults` to interact with a Core Data model.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import SwiftData

@Model
class Bookmark {
    var title: String
    var url: URL
    var dateAdded: Date
    @Relationship(deleteRule: .cascade)
    var tags: [Tag] = []

    init(title: String, url: URL) {
        self.title = title
        self.url = url
        self.dateAdded = .now
    }
}

struct BookmarkListView: View {
    @Query(sort: \Bookmark.dateAdded, order: .reverse)
    private var bookmarks: [Bookmark]

    @Environment(\.modelContext) private var context

    var body: some View {
        List(bookmarks) { bookmark in
            VStack(alignment: .leading) {
                Text(bookmark.title).font(.headline)
                Text(bookmark.url.absoluteString).font(.caption).foregroundStyle(.secondary)
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `@Model` macro with SwiftData for declarative persistence (replaces Core Data boilerplate)
- Use `@Query` in views for automatic, live-updating fetch results
- Use `@AppStorage` for simple UserDefaults-backed preferences, SwiftData for structured data


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

### Saving state across app launches

| API | Purpose |
|-----|---------|
| `Restoring your app’s state with SwiftUI` | Provide app continuity for users by preserving their current activities. |
| `defaultAppStorage(_:)` | The default store used by `AppStorage` contained within the view. |
| `AppStorage` | A property wrapper type that reflects a value from `UserDefaults` and |
| `SceneStorage` | A property wrapper type that reads and writes to persisted, per-scene |

### Accessing Core Data

| API | Purpose |
|-----|---------|
| `Loading and displaying a large data feed` | Consume data in the background, and lower memory use by batching imports and preventing duplicate records. |
| `managedObjectContext` | — |
| `FetchRequest` | A property wrapper type that retrieves entities from a Core Data persistent |
| `FetchedResults` | A collection of results retrieved from a Core Data store. |
| `SectionedFetchRequest` | A property wrapper type that retrieves entities, grouped into sections, |
| `SectionedFetchResults` | A collection of results retrieved from a Core Data persistent store, |
