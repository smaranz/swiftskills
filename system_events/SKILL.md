---
name: System events
description: Rork-Max Quality skill for System events. Actionable patterns and best practices for SwiftUI development.
---

# System events

React to system events, like opening a URL.
Specify view and scene modifiers to indicate how your app responds to certain
system events. For example, you can use the `onOpenURL(perform:)`
view modifier to define an action to take when your app receives a universal
link, or use the `backgroundTask(_:action:)` scene modifier to specify
an asynchronous task to carry out in response to a background
task event, like the completion of a background URL session.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct LifecycleAwareView: View {
    @Environment(\.scenePhase) private var scenePhase
    @State private var lastSaved: Date?

    var body: some View {
        ContentView()
            .onChange(of: scenePhase) { _, newPhase in
                switch newPhase {
                case .active:
                    refreshData()
                case .inactive:
                    saveState()
                case .background:
                    scheduleBackgroundTasks()
                @unknown default:
                    break
                }
            }
            .onOpenURL { url in
                handleDeepLink(url)
            }
    }

    func refreshData() { }
    func saveState() { lastSaved = .now }
    func scheduleBackgroundTasks() { }
    func handleDeepLink(_ url: URL) { }
}
```

## 💎 Elite Implementation Tips

- Use `.onChange(of: scenePhase)` to save state on `.inactive` and refresh on `.active`
- Handle deep links with `.onOpenURL` at the top-level scene
- Use `.onContinueUserActivity()` for Handoff and Spotlight integration


## When to Use

- Responding to scene phase changes (active, inactive, background)
- Handling app lifecycle events like `onOpenURL` or Handoff
- Reacting to system notifications like low memory or locale changes

## Best Practices

- Use `.onChange(of: scenePhase)` to pause/resume work when backgrounded
- Handle `onOpenURL` at the top-level scene for deep link routing
- Use `.onContinueUserActivity()` for Handoff and Spotlight integration

## Common Pitfalls

- Assuming the app is always in the foreground — save state on `.inactive`
- Blocking the main thread in lifecycle handlers delays the transition

## Key APIs

### Sending and receiving user activities

| API | Purpose |
|-----|---------|
| `Restoring your app’s state with SwiftUI` | Provide app continuity for users by preserving their current activities. |
| `userActivity(_:element:_:)` | Advertises a user activity type. |
| `userActivity(_:isActive:_:)` | Advertises a user activity type. |
| `onContinueUserActivity(_:perform:)` | Registers a handler to invoke in response to a user activity that your |

### Sending and receiving URLs

| API | Purpose |
|-----|---------|
| `openURL` | An action that opens a URL. |
| `OpenURLAction` | An action that opens a URL. |
| `onOpenURL(perform:)` | Registers a handler to invoke in response to a URL that your app |

### Handling external events

| API | Purpose |
|-----|---------|
| `handlesExternalEvents(matching:)` | Specifies the external events for which SwiftUI opens a new instance |
| `handlesExternalEvents(preferring:allowing:)` | Specifies the external events that the view’s scene handles |

### Handling background tasks

| API | Purpose |
|-----|---------|
| `backgroundTask(_:action:)` | Runs the specified action when the system provides a background task. |
| `BackgroundTask` | The kinds of background tasks that your app or extension can handle. |
| `SnapshotData` | The associated data of a snapshot background task. |
| `SnapshotResponse` | Your application’s response to a snapshot background task. |

### Importing and exporting transferable items

| API | Purpose |
|-----|---------|
| `importableFromServices(for:action:)` | Enables importing items from services, such as Continuity Camera |
| `exportableToServices(_:)` | Exports items for consumption by shortcuts, |
| `exportableToServices(_:onEdit:)` | Exports read-write items for consumption by shortcuts, |

### Importing and exporting using item providers

| API | Purpose |
|-----|---------|
| `importsItemProviders(_:onImport:)` | Enables importing item providers from services, such as Continuity Camera |
| `exportsItemProviders(_:onExport:)` | Exports a read-only item provider for consumption by shortcuts, |
| `exportsItemProviders(_:onExport:onEdit:)` | Exports a read-write item provider for consumption by shortcuts, |
