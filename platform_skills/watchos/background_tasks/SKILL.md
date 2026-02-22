---
name: WATCHOS Background execution
description: Rork-Max Quality skill for WATCHOS Background execution on watchos. Based on official Apple WatchKit Documentation.
---

# WATCHOS Background execution

## 🚀 Rork-Max Quality Snippet

```swift
// Premium WATCHOS Background execution Implementation for watchos
// Focus on platform-native excellence

import SwiftUI
#if os(watchos)
// WatchKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality WATCHOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the watchos native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for watchos: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Background execution

Manage background sessions and tasks.

## Discussion

Apps on watchOS primarily run in the foreground to limit the impact on system resources. However, sometimes an app needs to perform an action when it’s not the foreground app. For a limited number of cases, watchOS provides options for running in the background.

### Handle background notifications

When the system launches your app in the background, you can:

- Handle background notifications from local or remote notifications with a <doc://com.apple.documentation/documentation/UserNotifications/UNUserNotificationCenterDelegate> delegate. For more information, see <doc://com.apple.documentation/documentation/UserNotifications/handling-notifications-and-notification-related-actions>.
- Receive push notifications to update your app’s complications with a <doc://com.apple.documentation/documentation/PushKit/PKPushRegistryDelegate> delegate. For more information, see <doc://com.apple.documentation/documentation/PushKit>.

### Schedule and handle background refresh tasks

A watchOS app uses a *background refresh task* to perform work in the background. If your app requires background operations, use one of the following techniques to respond to the task:

- Add a <doc://com.apple.documentation/documentation/SwiftUI/Scene/backgroundTask(_:action:)> modifier to respond to the background task in your SwiftUI scene.
- Implement your app delegate’s ``doc://com.apple.watchkit/documentation/WatchKit/WKApplicationDelegate/handle(_:)-4vdjo`` method to receive and respond to the task. You need to call the task’s ``doc://com.apple.watchkit/documentation/WatchKit/WKRefreshBackgroundTask/setTaskCompletedWithSnapshot(_:)`` method to indicate that you’re done.

In both cases, the system launches your app and gives it a few seconds of background execution time to perform the task. Complete the background task as quickly as possible. For more information, see [Using background tasks](/documentation/WatchKit/using-background-tasks).

### Start background sessions

Apps that support workouts, audio playback, or location updates can continue to run in the background until the current session ends. Your app must enable the appropriate background mode in your project’s capabilities, and then start the session while your app is running in the foreground.

- Use an <doc://com.apple.documentation/documentation/HealthKit/HKWorkoutSession> object to start and stop workouts. For more information, see <doc://com.apple.documentation/documentation/HealthKit/running-workout-sessions>.
- Use the <doc://com.apple.documentation/documentation/AVFAudio/AVAudioSession> class to play extended audio files in the background. For more information, see <doc://com.apple.watchkit/documentation/WatchKit/playing-background-audio>.
- Use a <doc://com.apple.documentation/documentation/CoreLocation/CLLocationManager> object to start a continuous background location session. For more information, see <doc://com.apple.documentation/documentation/CoreLocation/CLLocationManager/allowsBackgroundLocationUpdates>.

### Set up extended runtime sessions

Extended runtime sessions give your app additional time to run while the session is active. Extended runtime sessions provide support for the following session types:

- Self care
- Mindfulness
- Physical therapy
- Smart alarm

Extended runtime sessions let the app continue to communicate with a Bluetooth device, process data, or play sounds or haptics, even after the watch’s screen turns off. While most extended runtime sessions run your app as the frontmost app, some sessions run your app in the background. Select a session type based on the app’s intended use — not based on the features that the session provides.

For more information, see [Using extended runtime sessions](/documentation/WatchKit/using-extended-runtime-sessions).

## Topics

### Background tasks

[Using background tasks](/documentation/WatchKit/using-background-tasks)

Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.

[Preparing to take your watchOS app’s snapshot](/documentation/WatchKit/preparing-to-take-your-watchos-app-s-snapshot)

Provide a timely, accurate snapshot of your app by using snapshot background tasks.

[`WKApplicationRefreshBackgroundTask`](/documentation/WatchKit/WKApplicationRefreshBackgroundTask)

A task that updates your app’s state in the background.

[`WKURLSessionRefreshBackgroundTask`](/documentation/WatchKit/WKURLSessionRefreshBackgroundTask)

A task that responds to background URL sessions.

[`WKWatchConnectivityRefreshBackgroundTask`](/documentation/WatchKit/WKWatchConnectivityRefreshBackgroundTask)

A background task used to receive background updates from the Watch Connectivity framework.

[`WKBluetoothAlertRefreshBackgroundTask`](/documentation/WatchKit/WKBluetoothAlertRefreshBackgroundTask)

A task for handling timely Bluetooth alerts in the background.

[`WKIntentDidRunRefreshBackgroundTask`](/documentation/WatchKit/WKIntentDidRunRefreshBackgroundTask)

A background task used to update your app after a SiriKit intent runs.

[`WKRelevantShortcutRefreshBackgroundTask`](/documentation/WatchKit/WKRelevantShortcutRefreshBackgroundTask)

A background task used to periodically donate relevant Siri shortcuts.

[`WKSnapshotRefreshBackgroundTask`](/documentation/WatchKit/WKSnapshotRefreshBackgroundTask)

A background task used to update your app’s user interface in preparation for a snapshot.

[`WKRefreshBackgroundTask`](/documentation/WatchKit/WKRefreshBackgroundTask)

The abstract superclass for WatchKit’s background task classes.

### Background sessions

[Enabling Background Sessions](/documentation/WatchKit/enabling-background-sessions)

Enable the background mode for audio, location updates, remote notifications, or workouts.

[Playing Background Audio](/documentation/WatchKit/playing-background-audio)

Enable background audio in your app to provide a seamless playback experience.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKBackgroundModes>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/UIBackgroundModes>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
