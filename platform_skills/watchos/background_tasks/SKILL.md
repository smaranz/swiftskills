---
name: WATCHOS Background execution
description: Rork-Max Quality skill for WATCHOS Background execution. Platform-native patterns and best practices for watchos development.
---

# WATCHOS Background execution

Manage background sessions and tasks.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct RorkWatchView: View {
    var body: some View {
        NavigationStack {
            List {
                Text("Background execution")
                    .font(.headline)
            }
            .navigationTitle("Rork")
        }
    }
}
```

## 💎 Elite Implementation Tips

- Follow the WATCHOS Human Interface Guidelines for native feel.
- Use system-standard WatchKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building watchOS apps with glanceable, quick interactions
- Implementing complications, background refresh, and workout tracking
- Optimizing for the small screen and limited resources of Apple Watch

## Best Practices

- Keep interactions under 5 seconds — watchOS is for glances, not sessions
- Use `.digitalCrownRotation()` for scroll and value adjustment
- Schedule background refresh tasks for up-to-date complications

## Common Pitfalls

- Trying to replicate the iPhone UI on watch — design for the wrist
- Ignoring battery constraints — minimize animations and network requests
- Forgetting that watchOS apps have very limited background execution time

## Key APIs

### Background tasks

| API | Purpose |
|-----|---------|
| `Using background tasks` | Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages. |
| `Preparing to take your watchOS app’s snapshot` | Provide a timely, accurate snapshot of your app by using snapshot background tasks. |
| `WKApplicationRefreshBackgroundTask` | A task that updates your app’s state in the background. |
| `WKURLSessionRefreshBackgroundTask` | A task that responds to background URL sessions. |
| `WKWatchConnectivityRefreshBackgroundTask` | A background task used to receive background updates from the Watch Connectivity framework. |
| `WKBluetoothAlertRefreshBackgroundTask` | A task for handling timely Bluetooth alerts in the background. |
| `WKIntentDidRunRefreshBackgroundTask` | A background task used to update your app after a SiriKit intent runs. |
| `WKRelevantShortcutRefreshBackgroundTask` | A background task used to periodically donate relevant Siri shortcuts. |

### Background sessions

| API | Purpose |
|-----|---------|
| `Enabling Background Sessions` | Enable the background mode for audio, location updates, remote notifications, or workouts. |
| `Playing Background Audio` | Enable background audio in your app to provide a seamless playback experience. |
