---
name: WATCHOS WKApplication
description: Rork-Max Quality skill for WATCHOS WKApplication. Platform-native patterns and best practices for watchos development.
---

# WATCHOS WKApplication

The centralized point of control and coordination for apps with a single watchOS app target.
```
@MainActor class WKApplication
```
In Xcode 13 and earlier, the system divides a watchOS app into two sections:
- term WatchKit app: An app bundle that contains your app icon. For storyboard-based apps, it also includes your storyboard and any assets used by the storyboard.
- term WatchKit extension: An extension that contains your watchOS app’s code.
In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later
Single-target watchOS apps have a single app object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.
As relevant events occur within your WatchKit app, the app object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life-cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see `WKApplicationDelegate`.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct RorkWatchView: View {
    var body: some View {
        NavigationStack {
            List {
                Text("WKApplication")
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

### Getting the app object

| API | Purpose |
|-----|---------|
| `shared()` | Returns the shared WatchKit app object. |

### Accessing the app delegate

| API | Purpose |
|-----|---------|
| `delegate` | The delegate of the WatchKit app object. |
| `WKApplicationDelegate` | A collection of methods that manages the app-level behavior for a single-target watchOS app. |

### Opening a URL resource

| API | Purpose |
|-----|---------|
| `openSystemURL(_:)` | Opens the specified system URL. |

### Getting the interface controller

| API | Purpose |
|-----|---------|
| `rootInterfaceController` | The app’s root interface controller. |
| `visibleInterfaceController` | Returns the last visible interface controller. |

### Managing the app state

| API | Purpose |
|-----|---------|
| `applicationState` | The runtime state of the watchOS app. |
| `WKApplicationState` | The running states of the Watch app. |
| `isApplicationRunningInDock` | A Boolean value that indicates whether the app is running in the dock. |
| `scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)` | Schedules a background task to refresh the app’s data. |

### Managing the user interface

| API | Purpose |
|-----|---------|
| `isAutorotating` | A Boolean value that determines whether the interface automatically rotates when the user flips their wrist. |
| `isAutorotated` | A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer. |
| `globalTintColor` | The watchOS app’s global tint color. |

### Managing the snapshot

| API | Purpose |
|-----|---------|
| `scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)` | Schedules a background task to refresh your app’s snapshot. |

### Observing messages from the notification center

| API | Purpose |
|-----|---------|
| `didFinishLaunchingNotification` | A message indicating that the launch process finished and the extension is ready to run. |
| `didBecomeActiveNotification` | A message indicating that the watchOS app is visible and processing events. |
| `willResignActiveNotification` | A message indicating that the system is about to deactivate the watchOS app. |
| `willEnterForegroundNotification` | A message indicating that the watchOS app is about to transition from the background to the foreground. |
| `didEnterBackgroundNotification` | A message indicating that the watchOS app transitioned from the foreground to the background. |

### Registering for remote notifications

| API | Purpose |
|-----|---------|
| `registerForRemoteNotifications()` | Register to receive remote notifications from the Apple Push Notification service (APNs). |
| `unregisterForRemoteNotifications()` | Unregister for all remote notifications received from Apple Push Notification service (APNs). |
| `isRegisteredForRemoteNotifications` | A Boolean value that indicates if the app has successfully registered for remote notifications. |
