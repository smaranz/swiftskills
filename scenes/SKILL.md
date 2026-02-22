---
name: Scenes
description: Rork-Max Quality skill for Scenes. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Scenes


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Scenes

Declare the user interface groupings that make up the parts of your app.

## Overview

A scene represents a part of your app’s user interface that has a life cycle
that the system manages. An [`App`](/documentation/SwiftUI/App) instance presents the scenes it contains,
while each [`Scene`](/documentation/SwiftUI/Scene) acts as the root element of a [`View`](/documentation/SwiftUI/View) hierarchy.

![](images/com.apple.SwiftUI/scenes-hero@2x.png)

The system presents scenes in different ways depending on the type of
scene, the platform, and the context. A scene might fill the entire display,
part of the display, a window, a tab in a window, or something else. In some
cases, your app might also be able to display more than one instance of the
scene at a time, like when a user simultaneously opens multiple windows based
on a single [`WindowGroup`](/documentation/SwiftUI/WindowGroup) declaration in your app. For more information about
the primary built-in scene types, see [Windows](/documentation/SwiftUI/Windows) and [Documents](/documentation/SwiftUI/Documents).

You configure scenes using modifiers, similar to how you configure views.
For example, you can adjust the appearance of the window that contains a
scene — if the scene happens to appear in a window — using the
[`windowStyle(_:)`](/documentation/SwiftUI/Scene/windowStyle(_:)) modifier. Similarly, you can add menu commands that
become available when the scene is in the foreground on certain platforms using
the [`commands(content:)`](/documentation/SwiftUI/Scene/commands(content:)) modifier.

## Topics

### Creating scenes

[`Scene`](/documentation/SwiftUI/Scene)

A part of an app’s user interface with a life cycle managed by the
system.

[`SceneBuilder`](/documentation/SwiftUI/SceneBuilder)

A result builder for composing a collection of scenes into a single
composite scene.

### Monitoring scene life cycle

[`scenePhase`](/documentation/SwiftUI/EnvironmentValues/scenePhase)

The current phase of the scene.

[`ScenePhase`](/documentation/SwiftUI/ScenePhase)

An indication of a scene’s operational state.

### Managing a settings window

[`Settings`](/documentation/SwiftUI/Settings)

A scene that presents an interface for viewing and modifying an app’s
settings.

[`SettingsLink`](/documentation/SwiftUI/SettingsLink)

A view that opens the Settings scene defined by an app.

[`OpenSettingsAction`](/documentation/SwiftUI/OpenSettingsAction)

An action that presents the settings scene for an app.

[`openSettings`](/documentation/SwiftUI/EnvironmentValues/openSettings)

A Settings presentation action stored in a view’s environment.

### Building a menu bar

[Building and customizing the menu bar with SwiftUI](/documentation/SwiftUI/Building-and-customizing-the-menu-bar-with-SwiftUI)

Provide a seamless, cross-platform user experience by building a native menu bar for iPadOS and macOS.

### Creating a menu bar extra

[`MenuBarExtra`](/documentation/SwiftUI/MenuBarExtra)

A scene that renders itself as a persistent control in the system menu bar.

[`menuBarExtraStyle(_:)`](/documentation/SwiftUI/Scene/menuBarExtraStyle(_:))

Sets the style for menu bar extra created by this scene.

[`MenuBarExtraStyle`](/documentation/SwiftUI/MenuBarExtraStyle)

A specification for the appearance and behavior of a menu bar extra scene.

### Creating watch notifications

[`WKNotificationScene`](/documentation/SwiftUI/WKNotificationScene)

A scene which appears in response to receiving the specified
category of remote or local notifications.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
