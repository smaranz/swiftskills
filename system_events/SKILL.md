---
name: System events
description: Rork-Max Quality skill for System events. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# System events


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# System events

React to system events, like opening a URL.

## Overview

Specify view and scene modifiers to indicate how your app responds to certain
system events. For example, you can use the [`onOpenURL(perform:)`](/documentation/SwiftUI/View/onOpenURL(perform:))
view modifier to define an action to take when your app receives a universal
link, or use the [`backgroundTask(_:action:)`](/documentation/SwiftUI/Scene/backgroundTask(_:action:)) scene modifier to specify
an asynchronous task to carry out in response to a background
task event, like the completion of a background URL session.

![](images/com.apple.SwiftUI/system-events-hero@2x.png)

## Topics

### Sending and receiving user activities

[Restoring your app’s state with SwiftUI](/documentation/SwiftUI/restoring-your-app-s-state-with-swiftui)

Provide app continuity for users by preserving their current activities.

[`userActivity(_:element:_:)`](/documentation/SwiftUI/View/userActivity(_:element:_:))

Advertises a user activity type.

[`userActivity(_:isActive:_:)`](/documentation/SwiftUI/View/userActivity(_:isActive:_:))

Advertises a user activity type.

[`onContinueUserActivity(_:perform:)`](/documentation/SwiftUI/View/onContinueUserActivity(_:perform:))

Registers a handler to invoke in response to a user activity that your
app receives.

### Sending and receiving URLs

[`openURL`](/documentation/SwiftUI/EnvironmentValues/openURL)

An action that opens a URL.

[`OpenURLAction`](/documentation/SwiftUI/OpenURLAction)

An action that opens a URL.

[`onOpenURL(perform:)`](/documentation/SwiftUI/View/onOpenURL(perform:))

Registers a handler to invoke in response to a URL that your app
receives.

### Handling external events

[`handlesExternalEvents(matching:)`](/documentation/SwiftUI/Scene/handlesExternalEvents(matching:))

Specifies the external events for which SwiftUI opens a new instance
of the modified scene.

[`handlesExternalEvents(preferring:allowing:)`](/documentation/SwiftUI/View/handlesExternalEvents(preferring:allowing:))

Specifies the external events that the view’s scene handles
if the scene is already open.

### Handling background tasks

[`backgroundTask(_:action:)`](/documentation/SwiftUI/Scene/backgroundTask(_:action:))

Runs the specified action when the system provides a background task.

[`BackgroundTask`](/documentation/SwiftUI/BackgroundTask)

The kinds of background tasks that your app or extension can handle.

[`SnapshotData`](/documentation/SwiftUI/SnapshotData)

The associated data of a snapshot background task.

[`SnapshotResponse`](/documentation/SwiftUI/SnapshotResponse)

Your application’s response to a snapshot background task.

### Importing and exporting transferable items

[`importableFromServices(for:action:)`](/documentation/SwiftUI/View/importableFromServices(for:action:))

Enables importing items from services, such as Continuity Camera
on macOS.

[`exportableToServices(_:)`](/documentation/SwiftUI/View/exportableToServices(_:))

Exports items for consumption by shortcuts,
quick actions, and services.

[`exportableToServices(_:onEdit:)`](/documentation/SwiftUI/View/exportableToServices(_:onEdit:))

Exports read-write items for consumption by shortcuts,
quick actions, and services.

### Importing and exporting using item providers

[`importsItemProviders(_:onImport:)`](/documentation/SwiftUI/View/importsItemProviders(_:onImport:))

Enables importing item providers from services, such as Continuity Camera
on macOS.

[`exportsItemProviders(_:onExport:)`](/documentation/SwiftUI/View/exportsItemProviders(_:onExport:))

Exports a read-only item provider for consumption by shortcuts,
quick actions, and services.

[`exportsItemProviders(_:onExport:onEdit:)`](/documentation/SwiftUI/View/exportsItemProviders(_:onExport:onEdit:))

Exports a read-write item provider for consumption by shortcuts,
quick actions, and services.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
