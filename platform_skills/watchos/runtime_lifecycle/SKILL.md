---
name: WATCHOS Life cycles
description: Apple WatchKit Documentation for WATCHOS Life cycles on watchos.
---

# Life cycles

Receive and respond to life-cycle notifications.

## Discussion

The system reports changes in your app’s execution state to your SwiftUI environment and your extension delegate object. State changes correspond to major events in the lifetime of your app, such as the app launching or moving into the background. Use the state changes to trigger relevant tasks, such as loading shared resources and configuring your initial user interface. The table below shows the possible states and their implications for your app.

|State      |Description                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|Not running|The watchOS app isn’t running.                                                                                                                    |
|Inactive   |The watchOS app is running in the foreground, but isn’t receiving actions from controls or gestures.                                              |
|Active     |The watchOS app is running in the foreground and receiving actions from controls and gestures. This is the normal mode for apps running on screen.|
|Background |The system has given the watchOS app a small amount of background execution time.                                                                 |
|Suspended  |The app is in memory but isn’t executing code. The system may purge suspended apps at any time to make room for other apps.                       |

For more information, see [Handling Common State Transitions](/documentation/WatchKit/handling-common-state-transitions).

### Receive background information

When the system receives background data, it may not immediately wake the watchOS app to process that data. Instead, it may delay delivery of the data to preserve battery life.

If the app is currently running—either active and onscreen, or inactive and the frontmost app—the system immediately delivers the data to the app. If the app is in the background, the system wakes the app within 10 minutes to deliver the data.

## Topics

### Responding to life cycle events

[Handling Common State Transitions](/documentation/WatchKit/handling-common-state-transitions)

Detect and respond to common state transitions.

[Working with the watchOS app life cycle](/documentation/WatchKit/working-with-the-watchos-app-life-cycle)

Learn how the watchOS app life cycle operates and responds to life cycle notification methods.

[Handling User Activity](/documentation/WatchKit/handling-user-activity)

Detect and respond to user activity information from Handoff or a complication.

[Taking advantage of frontmost app state](/documentation/WatchKit/taking-advantage-of-frontmost-app-state)

Understand the frontmost app state, and the features it provides to your app.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
