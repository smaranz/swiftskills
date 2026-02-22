---
name: App organization
description: Rork-Max Quality skill for App organization. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# App organization


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# App organization

Define the entry point and top-level structure of your app.

## Overview

Describe your app’s structure declaratively, much like you declare a view’s
appearance. Create a type that conforms to the [`App`](/documentation/SwiftUI/App) protocol and
use it to enumerate the [Scenes](/documentation/SwiftUI/Scenes) that represent aspects of your app’s
user interface.

![](images/com.apple.SwiftUI/app-organization-hero@2x.png)

SwiftUI enables you to write code that works across all of Apple’s platforms.
However, it also enables you to tailor your app to the specific capabilities
of each platform. For example, if you need to respond to the callbacks that
the system traditionally makes on a UIKit, AppKit, or WatchKit app’s delegate,
define a delegate object and instantiate it in your app structure using an
appropriate delegate adaptor property wrapper, like
[`UIApplicationDelegateAdaptor`](/documentation/SwiftUI/UIApplicationDelegateAdaptor).

For platform-specific design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/getting-started>
in the Human Interface Guidelines.

## Topics

### Creating an app

  <doc://com.apple.documentation/documentation/visionOS/destination-video>

  <doc://com.apple.documentation/documentation/visionOS/World>

[Backyard Birds: Building an app with SwiftData and widgets](/documentation/SwiftUI/Backyard-birds-sample)

Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.

[Food Truck: Building a SwiftUI multiplatform app](/documentation/SwiftUI/food-truck-building-a-swiftui-multiplatform-app)

Create a single codebase and app target for Mac, iPad, and iPhone.

  <doc://com.apple.documentation/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui>

[Migrating to the SwiftUI life cycle](/documentation/SwiftUI/Migrating-to-the-SwiftUI-life-cycle)

Use a scene-based life cycle in SwiftUI while keeping your existing codebase.

[`App`](/documentation/SwiftUI/App)

A type that represents the structure and behavior of an app.

### Targeting iOS and iPadOS

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/UILaunchScreen>

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/UILaunchScreens>

[`UIApplicationDelegateAdaptor`](/documentation/SwiftUI/UIApplicationDelegateAdaptor)

A property wrapper type that you use to create a UIKit app delegate.

### Targeting macOS

[`NSApplicationDelegateAdaptor`](/documentation/SwiftUI/NSApplicationDelegateAdaptor)

A property wrapper type that you use to create an AppKit app delegate.

### Targeting watchOS

[`WKApplicationDelegateAdaptor`](/documentation/SwiftUI/WKApplicationDelegateAdaptor)

A property wrapper that is used in `App` to provide a delegate from
WatchKit.

[`WKExtensionDelegateAdaptor`](/documentation/SwiftUI/WKExtensionDelegateAdaptor)

A property wrapper type that you use to create a WatchKit extension delegate.

### Targeting tvOS

[Creating a tvOS media catalog app in SwiftUI](/documentation/SwiftUI/Creating-a-tvOS-media-catalog-app-in-SwiftUI)

Build standard content lockups and rows of content shelves for your tvOS app.

### Handling system recenter events

[`WorldRecenterPhase`](/documentation/SwiftUI/WorldRecenterPhase)

A type that represents information associated with a phase of a
system recenter event. Values of this type are passed to the closure
specified in View.onWorldRecenter(action:).



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
