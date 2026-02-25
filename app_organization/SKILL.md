---
name: App organization
description: Rork-Max Quality skill for App organization. Actionable patterns and best practices for SwiftUI development.
---

# App organization

Define the entry point and top-level structure of your app.
Describe your app’s structure declaratively, much like you declare a view’s
appearance. Create a type that conforms to the `App` protocol and
use it to enumerate the Scenes that represent aspects of your app’s
user interface.
SwiftUI enables you to write code that works across all of Apple’s platforms.
However, it also enables you to tailor your app to the specific capabilities
of each platform. For example, if you need to respond to the callbacks that
the system traditionally makes on a UIKit, AppKit, or WatchKit app’s delegate,
define a delegate object and instantiate it in your app structure using an
appropriate delegate adaptor property wrapper, like
`UIApplicationDelegateAdaptor`.
For platform-specific design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Defining the entry point and top-level structure of a SwiftUI app
- Managing multiple windows, scenes, or document-based workflows
- Configuring app-wide lifecycle events and state restoration
- Building multi-platform apps that adapt their structure per platform

## Best Practices

- Keep `@main` App structs thin — delegate complex logic to dedicated model objects
- Use `@Environment(\.scenePhase)` to react to foreground/background transitions
- Prefer `WindowGroup` for document-based apps and `Window` for utility panels
- Store app-level state in an `@Observable` singleton injected via `.environment()`

## Common Pitfalls

- Putting heavy initialization in the App `init()` delays launch
- Forgetting that each `WindowGroup` can spawn multiple instances on macOS/iPadOS
- Using `@StateObject` in the App struct when `@State` with `@Observable` is simpler in Swift 6

## Key APIs

### Creating an app

| API | Purpose |
|-----|---------|
| `Backyard Birds: Building an app with SwiftData and widgets` | Create an app with persistent data, interactive widgets, and an all new in-app purchase experience. |
| `Food Truck: Building a SwiftUI multiplatform app` | Create a single codebase and app target for Mac, iPad, and iPhone. |
| `Migrating to the SwiftUI life cycle` | Use a scene-based life cycle in SwiftUI while keeping your existing codebase. |
| `App` | A type that represents the structure and behavior of an app. |

### Targeting iOS and iPadOS

| API | Purpose |
|-----|---------|
| `UIApplicationDelegateAdaptor` | A property wrapper type that you use to create a UIKit app delegate. |

### Targeting macOS

| API | Purpose |
|-----|---------|
| `NSApplicationDelegateAdaptor` | A property wrapper type that you use to create an AppKit app delegate. |

### Targeting watchOS

| API | Purpose |
|-----|---------|
| `WKApplicationDelegateAdaptor` | A property wrapper that is used in `App` to provide a delegate from |
| `WKExtensionDelegateAdaptor` | A property wrapper type that you use to create a WatchKit extension delegate. |

### Targeting tvOS

| API | Purpose |
|-----|---------|
| `Creating a tvOS media catalog app in SwiftUI` | Build standard content lockups and rows of content shelves for your tvOS app. |

### Handling system recenter events

| API | Purpose |
|-----|---------|
| `WorldRecenterPhase` | A type that represents information associated with a phase of a |
