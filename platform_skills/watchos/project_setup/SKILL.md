---
name: WATCHOS Setting up a watchOS project
description: Apple WatchKit Documentation for WATCHOS Setting up a watchOS project on watchos.
---

# Setting up a watchOS project

Create a new watchOS project or add a watch target to an existing iOS project.

## Discussion

Before you start a new watchOS project, you need to decide how you’re going to distribute that project: as a watch-only app, or as a watchOS app with an iOS app. If your app is only available on Apple Watch, create a new watch-only project. If you want a watchOS and iOS app that deliver a related experience, either create a new project that bundles the two apps, or add a watchOS target to an existing iOS project.

### Create a new project

To create a new watchOS project:

1. In Xcode, choose File > New > Project.
1. Select the watchOS tab.
1. To create a watch-only app, select “App” and click Next. To create a watchOS app bundled with an iOS app, select “iOS App with Watch App” and click Next.
1. In the project options sheet ([Figure 1](/documentation/watchkit/setting_up_a_watchos_project#3312778)), enter a product name for the project. If you plan to implement a custom notification, complication, or unit tests, select the appropriate checkboxes, and click Next.
1. Select a location for the project, and click Create.

![A screenshot showing the new project sheet with the project name set, and notifications, complications, and unit tests included.](images/com.apple.watchkit/media-3312778@2x.png)

Xcode includes the Notification Scene by default. Leave this checkbox selected even if you don’t plan on implementing notifications right away. Selecting the checkbox adds the `PushNotificationPayload.apns` file to your project, which helps you debug your notification interfaces. If you add a Notification Scene later, you must also add the `PushNotificationPayload.apns` file.

### Add a watchOS app target to an existing iOS project

You can add a watchOS target to an existing iOS project by following these steps:

1. Open your iOS app’s project in Xcode.
1. Choose File > New > Target.
1. Select the watchOS tab.
1. Select “Watch App for iOS App” and click Next.
1. In the target options sheet ([Figure 2](/documentation/watchkit/setting_up_a_watchos_project#3312779)), enter a Product Name for the project. If you plan to implement notifications or complications, select the appropriate checkboxes, and click Finish.
1. Xcode then asks you to activate the new scheme for your watch target. Click Activate.

![A screenshot showing the new target sheet with the Project Name set and the Include Notification Scene and Include Complication check boxes selected.](images/com.apple.watchkit/media-3312779@2x.png)

As when creating a new project, Xcode includes the Notification Scene by default. Leave this checkbox selected even if you don’t plan to implement notifications right away; selecting the checkbox adds the `PushNotificationPayload.apns` file to your project, which helps you debug your notification interfaces. If you add a Notification Scene later, you must also add the `PushNotificationPayload.apns` file.

### Understand the WatchKit app and WatchKit extension

Regardless of whether you add a watchOS app to an existing project or create a new project that contains both an iOS and watchOS app, Xcode automatically configures the targets for your watchOS app and adds the needed files, as in [Figure 3](/documentation/watchkit/setting_up_a_watchos_project#3295999).

Xcode divides the watchOS app into two sections:

- term WatchKit App: An app bundle that contains your watchOS app’s storyboard and any assets used by the storyboard.
- term WatchKit Extension: An extension that contains your watchOS app’s code.

![A screenshot of Xcode’s Project navigator, containing an iOS app, both the WatchKit App and WatchKit Extension, and unit tests.](images/com.apple.watchkit/media-3295999@2x.png)

Xcode sets the bundle IDs for both of the watch targets based on the container’s ID. For a watch-only app, this ID is the bundle ID for the root target. For a watchOS app with an iOS app, this ID is the iOS app’s bundle ID. The root of the WatchKit app and WatchKit extension’s bundle IDs must match the container’s bundle ID. If you change your iOS app’s bundle ID, you must update the other bundle IDs accordingly.

When developing your watchOS app, edit your app’s storyboard in the WatchKit app, and write your app’s code in the WatchKit extension. Your WatchKit extension connects to controls and views in the storyboard using [`WKInterfaceObject`](/documentation/WatchKit/WKInterfaceObject) subclasses such as [`WKInterfaceButton`](/documentation/WatchKit/WKInterfaceButton) and [`WKInterfaceLabel`](/documentation/WatchKit/WKInterfaceLabel). These interface objects act as proxies for your storyboard elements. Use the interface elements to configure the elements in code.

## Topics

### Information Property List Keys

The keys that Xcode automatically sets in the information property list file when you create a watchOS target.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKWatchKitApp>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKAppBundleIdentifier>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKCompanionAppBundleIdentifier>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKExtensionDelegateClassName>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKRunsIndependentlyOfCompanionApp>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/WKWatchOnly>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
