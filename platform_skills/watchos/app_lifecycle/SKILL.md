---
name: WATCHOS WKApplication
description: Apple WatchKit Documentation for WATCHOS WKApplication on watchos.
---

# WKApplication

The centralized point of control and coordination for apps with a single watchOS app target.

```
@MainActor class WKApplication
```

## Overview

In Xcode 13 and earlier, the system divides a watchOS app into two sections:

- term WatchKit app: An app bundle that contains your app icon. For storyboard-based apps, it also includes your storyboard and any assets used by the storyboard.
- term WatchKit extension: An extension that contains your watchOS app’s code.

In Xcode 14 and later, you can produce watchOS apps with a single watchOS app target for code, assets, extensions, and localizations. These single-target watchOS apps can run on watchOS 7 and later

Single-target watchOS apps have a single app object. While the system creates and manages this object, you can access it to perform app-level tasks such as opening URLs and getting the root interface controller of your app.

As relevant events occur within your WatchKit app, the app object notifies its delegate of those events. Your delegate object can implement the methods it needs to provide an appropriate response to life-cycle events, handle notifications, or handle Handoff–related behaviors. For more information about the methods of the delegate, see [`WKApplicationDelegate`](/documentation/WatchKit/WKApplicationDelegate).

## Topics

### Getting the app object

[`shared()`](/documentation/WatchKit/WKApplication/shared())

Returns the shared WatchKit app object.

### Accessing the app delegate

[`delegate`](/documentation/WatchKit/WKApplication/delegate)

The delegate of the WatchKit app object.

[`WKApplicationDelegate`](/documentation/WatchKit/WKApplicationDelegate)

A collection of methods that manages the app-level behavior for a single-target watchOS app.

### Opening a URL resource

[`openSystemURL(_:)`](/documentation/WatchKit/WKApplication/openSystemURL(_:))

Opens the specified system URL.

### Getting the interface controller

[`rootInterfaceController`](/documentation/WatchKit/WKApplication/rootInterfaceController)

The app’s root interface controller.

[`visibleInterfaceController`](/documentation/WatchKit/WKApplication/visibleInterfaceController)

Returns the last visible interface controller.

### Managing the app state

[`applicationState`](/documentation/WatchKit/WKApplication/applicationState)

The runtime state of the watchOS app.

[`WKApplicationState`](/documentation/WatchKit/WKApplicationState)

The running states of the Watch app.

[`isApplicationRunningInDock`](/documentation/WatchKit/WKApplication/isApplicationRunningInDock)

A Boolean value that indicates whether the app is running in the dock.

[`scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](/documentation/WatchKit/WKApplication/scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:))

Schedules a background task to refresh the app’s data.

### Managing the user interface

[`isAutorotating`](/documentation/WatchKit/WKApplication/isAutorotating)

A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.

[`isAutorotated`](/documentation/WatchKit/WKApplication/isAutorotated)

A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.

[`globalTintColor`](/documentation/WatchKit/WKApplication/globalTintColor)

The watchOS app’s global tint color.

### Managing the snapshot

[`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](/documentation/WatchKit/WKApplication/scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:))

Schedules a background task to refresh your app’s snapshot.

### Observing messages from the notification center

[`didFinishLaunchingNotification`](/documentation/WatchKit/WKApplication/didFinishLaunchingNotification)

A message indicating that the launch process finished and the extension is ready to run.

[`didBecomeActiveNotification`](/documentation/WatchKit/WKApplication/didBecomeActiveNotification)

A message indicating that the watchOS app is visible and processing events.

[`willResignActiveNotification`](/documentation/WatchKit/WKApplication/willResignActiveNotification)

A message indicating that the system is about to deactivate the watchOS app.

[`willEnterForegroundNotification`](/documentation/WatchKit/WKApplication/willEnterForegroundNotification)

A message indicating that the watchOS app is about to transition from the background to the foreground.

[`didEnterBackgroundNotification`](/documentation/WatchKit/WKApplication/didEnterBackgroundNotification)

A message indicating that the watchOS app transitioned from the foreground to the background.

### Registering for remote notifications

[`registerForRemoteNotifications()`](/documentation/WatchKit/WKApplication/registerForRemoteNotifications())

Register to receive remote notifications from the Apple Push Notification service (APNs).

[`unregisterForRemoteNotifications()`](/documentation/WatchKit/WKApplication/unregisterForRemoteNotifications())

Unregister for all remote notifications received from Apple Push Notification service (APNs).

[`isRegisteredForRemoteNotifications`](/documentation/WatchKit/WKApplication/isRegisteredForRemoteNotifications)

A Boolean value that indicates if the app has successfully registered for remote notifications.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
