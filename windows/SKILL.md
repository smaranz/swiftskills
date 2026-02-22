---
name: Windows
description: Rork-Max Quality skill for Windows. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Windows


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Windows

Display user interface content in a window or a collection of windows.

## Overview

The most common way to present a view hierarchy in your app’s interface is with
a [`WindowGroup`](/documentation/SwiftUI/WindowGroup), which produces a platform-specific behavior and appearance.

![](images/com.apple.SwiftUI/windows-hero@2x.png)

On platforms that support it, people can open multiple windows from the group
simultaneously. Each window relies on the same root view definition, but
retains its own view state. On some platforms, you can also supplement your
app’s user interface with a single-instance window using the [`Window`](/documentation/SwiftUI/Window) scene
type.

Configure windows using scene modifiers that you add to the window
declaration, like [`windowStyle(_:)`](/documentation/SwiftUI/Scene/windowStyle(_:)) or [`defaultPosition(_:)`](/documentation/SwiftUI/Scene/defaultPosition(_:)).
You can also indicate how to configure new windows that you present from a view
hierarchy by adding the [`presentedWindowStyle(_:)`](/documentation/SwiftUI/View/presentedWindowStyle(_:)) view modifier to a
view in the hierarchy.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/windows>
in the Human Interface Guidelines.

## Topics

### Essentials

[Customizing window styles and state-restoration behavior in macOS](/documentation/SwiftUI/Customizing-window-styles-and-state-restoration-behavior-in-macOS)

Configure how your app’s windows look and function in macOS to provide an
engaging and more coherent experience.

[Bringing multiple windows to your SwiftUI app](/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app)

Compose rich views by reacting to state changes and customize your app’s scene presentation and behavior on iPadOS and macOS.

### Creating windows

[`WindowGroup`](/documentation/SwiftUI/WindowGroup)

A scene that presents a group of identically structured windows.

[`Window`](/documentation/SwiftUI/Window)

A scene that presents its content in a single, unique window.

[`UtilityWindow`](/documentation/SwiftUI/UtilityWindow)

A specialized window scene that provides secondary utility to the content
of the main scenes of an application.

[`WindowStyle`](/documentation/SwiftUI/WindowStyle)

A specification for the appearance and interaction of a window.

[`windowStyle(_:)`](/documentation/SwiftUI/Scene/windowStyle(_:))

Sets the style for windows created by this scene.

### Styling the associated toolbar

[`windowToolbarStyle(_:)`](/documentation/SwiftUI/Scene/windowToolbarStyle(_:))

Sets the style for the toolbar defined within this scene.

[`windowToolbarLabelStyle(_:)`](/documentation/SwiftUI/Scene/windowToolbarLabelStyle(_:))

Sets the label style of items in a toolbar and enables user customization.

[`windowToolbarLabelStyle(fixed:)`](/documentation/SwiftUI/Scene/windowToolbarLabelStyle(fixed:))

Sets the label style of items in a toolbar.

[`WindowToolbarStyle`](/documentation/SwiftUI/WindowToolbarStyle)

A specification for the appearance and behavior of a window’s toolbar.

### Opening windows

  <doc://com.apple.documentation/documentation/visionOS/presenting-windows-and-spaces>

[`supportsMultipleWindows`](/documentation/SwiftUI/EnvironmentValues/supportsMultipleWindows)

A Boolean value that indicates whether the current platform supports
opening multiple windows.

[`openWindow`](/documentation/SwiftUI/EnvironmentValues/openWindow)

A window presentation action stored in a view’s environment.

[`OpenWindowAction`](/documentation/SwiftUI/OpenWindowAction)

An action that presents a window.

[`PushWindowAction`](/documentation/SwiftUI/PushWindowAction)

An action that opens the requested window in place of the window the action
is called from.

### Closing windows

[`dismissWindow`](/documentation/SwiftUI/EnvironmentValues/dismissWindow)

A window dismissal action stored in a view’s environment.

[`DismissWindowAction`](/documentation/SwiftUI/DismissWindowAction)

An action that dismisses a window associated to a particular scene.

[`dismiss`](/documentation/SwiftUI/EnvironmentValues/dismiss)

An action that dismisses the current presentation.

[`DismissAction`](/documentation/SwiftUI/DismissAction)

An action that dismisses a presentation.

[`DismissBehavior`](/documentation/SwiftUI/DismissBehavior)

Programmatic window dismissal behaviors.

### Sizing a window

  <doc://com.apple.documentation/documentation/visionOS/positioning-and-sizing-windows>

[`defaultSize(_:)`](/documentation/SwiftUI/Scene/defaultSize(_:))

Sets a default size for a window.

[`defaultSize(width:height:)`](/documentation/SwiftUI/Scene/defaultSize(width:height:))

Sets a default width and height for a window.

[`defaultSize(width:height:depth:)`](/documentation/SwiftUI/Scene/defaultSize(width:height:depth:))

Sets a default size for a volumetric window.

[`defaultSize(_:in:)`](/documentation/SwiftUI/Scene/defaultSize(_:in:))

Sets a default size for a volumetric window.

[`defaultSize(width:height:depth:in:)`](/documentation/SwiftUI/Scene/defaultSize(width:height:depth:in:))

Sets a default size for a volumetric window.

[`windowResizability(_:)`](/documentation/SwiftUI/Scene/windowResizability(_:))

Sets the kind of resizability to use for a window.

[`WindowResizability`](/documentation/SwiftUI/WindowResizability)

The resizability of a window.

[`windowIdealSize(_:)`](/documentation/SwiftUI/Scene/windowIdealSize(_:))

Specifies how windows derived form this scene should determine their
size when zooming.

[`WindowIdealSize`](/documentation/SwiftUI/WindowIdealSize)

A type which defines the size a window should use when zooming.

### Positioning a window

[`defaultPosition(_:)`](/documentation/SwiftUI/Scene/defaultPosition(_:))

Sets a default position for a window.

[`WindowLevel`](/documentation/SwiftUI/WindowLevel)

The level of a window.

[`windowLevel(_:)`](/documentation/SwiftUI/Scene/windowLevel(_:))

Sets the window level of this scene.

[`WindowLayoutRoot`](/documentation/SwiftUI/WindowLayoutRoot)

A proxy which represents the root contents of a window.

[`WindowPlacement`](/documentation/SwiftUI/WindowPlacement)

A type which represents a preferred size and position for a window.

[`defaultWindowPlacement(_:)`](/documentation/SwiftUI/Scene/defaultWindowPlacement(_:))

Defines a function used for determining the default placement
of windows.

[`windowIdealPlacement(_:)`](/documentation/SwiftUI/Scene/windowIdealPlacement(_:))

Provides a function which determines a placement to use when windows
of a scene zoom.

[`WindowPlacementContext`](/documentation/SwiftUI/WindowPlacementContext)

A type which represents contextual information used for sizing and
positioning windows.

[`WindowProxy`](/documentation/SwiftUI/WindowProxy)

The proxy for an open window in the app.

[`DisplayProxy`](/documentation/SwiftUI/DisplayProxy)

A type which provides information about display hardware.

### Configuring window visibility

[`WindowVisibilityToggle`](/documentation/SwiftUI/WindowVisibilityToggle)

A specialized button for toggling the visibility of a window.

[`defaultLaunchBehavior(_:)`](/documentation/SwiftUI/Scene/defaultLaunchBehavior(_:))

Sets the default launch behavior for this scene.

[`restorationBehavior(_:)`](/documentation/SwiftUI/Scene/restorationBehavior(_:))

Sets the restoration behavior for this scene.

[`SceneLaunchBehavior`](/documentation/SwiftUI/SceneLaunchBehavior)

The launch behavior for a scene.

[`SceneRestorationBehavior`](/documentation/SwiftUI/SceneRestorationBehavior)

The restoration behavior for a scene.

[`persistentSystemOverlays(_:)`](/documentation/SwiftUI/Scene/persistentSystemOverlays(_:))

Sets the preferred visibility of the non-transient system views
overlaying the app.

[`windowToolbarFullScreenVisibility(_:)`](/documentation/SwiftUI/View/windowToolbarFullScreenVisibility(_:))

Configures the visibility of the window toolbar when the window enters
full screen mode.

[`WindowToolbarFullScreenVisibility`](/documentation/SwiftUI/WindowToolbarFullScreenVisibility)

The visibility of the window toolbar with respect to full screen mode.

### Managing window behavior

[`WindowManagerRole`](/documentation/SwiftUI/WindowManagerRole)

Options for defining how a scene’s windows behave when used within a managed
window context, such as full screen mode and Stage Manager.

[`windowManagerRole(_:)`](/documentation/SwiftUI/Scene/windowManagerRole(_:))

Configures the role for windows derived from `self` when
participating in a managed window context, such as full screen or
Stage Manager.

[`WindowInteractionBehavior`](/documentation/SwiftUI/WindowInteractionBehavior)

Options for enabling and disabling window interaction behaviors.

[`windowDismissBehavior(_:)`](/documentation/SwiftUI/View/windowDismissBehavior(_:))

Configures the dismiss functionality for the window enclosing `self`.

[`windowFullScreenBehavior(_:)`](/documentation/SwiftUI/View/windowFullScreenBehavior(_:))

Configures the full screen functionality for the window enclosing `self`.

[`windowMinimizeBehavior(_:)`](/documentation/SwiftUI/View/windowMinimizeBehavior(_:))

Configures the minimize functionality for the window enclosing `self`.

[`windowResizeBehavior(_:)`](/documentation/SwiftUI/View/windowResizeBehavior(_:))

Configures the resize functionality for the window enclosing `self`.

[`windowBackgroundDragBehavior(_:)`](/documentation/SwiftUI/Scene/windowBackgroundDragBehavior(_:))

Configures the behavior of dragging a window by its background.

### Interacting with volumes

[`onVolumeViewpointChange(updateStrategy:initial:_:)`](/documentation/SwiftUI/View/onVolumeViewpointChange(updateStrategy:initial:_:))

Adds an action to perform when the viewpoint of the volume changes.

[`supportedVolumeViewpoints(_:)`](/documentation/SwiftUI/View/supportedVolumeViewpoints(_:))

Specifies which viewpoints are supported for the window bar and
ornaments in a volume.

[`VolumeViewpointUpdateStrategy`](/documentation/SwiftUI/VolumeViewpointUpdateStrategy)

A type describing when the action provided to
[`onVolumeViewpointChange(updateStrategy:initial:_:)`](/documentation/SwiftUI/View/onVolumeViewpointChange(updateStrategy:initial:_:)) should be
called.

[`Viewpoint3D`](/documentation/SwiftUI/Viewpoint3D)

A type describing what direction something is being viewed from.

[`SquareAzimuth`](/documentation/SwiftUI/SquareAzimuth)

A type describing what direction something is being viewed from along
the horizontal plane and snapped to 4 directions.

[`WorldAlignmentBehavior`](/documentation/SwiftUI/WorldAlignmentBehavior)

A type representing the world alignment behavior for a scene.

[`volumeWorldAlignment(_:)`](/documentation/SwiftUI/Scene/volumeWorldAlignment(_:))

Specifies how a volume should be aligned when moved in the world.

[`WorldScalingBehavior`](/documentation/SwiftUI/WorldScalingBehavior)

Specifies the scaling behavior a window should have within the world.

[`defaultWorldScaling(_:)`](/documentation/SwiftUI/Scene/defaultWorldScaling(_:))

Specify the world scaling behavior for the window.

[`WorldScalingCompensation`](/documentation/SwiftUI/WorldScalingCompensation)

Indicates whether returned metrics will take dynamic scaling into account.

[`worldTrackingLimitations`](/documentation/SwiftUI/EnvironmentValues/worldTrackingLimitations)

The current limitations of the device tracking the user’s surroundings.

[`WorldTrackingLimitation`](/documentation/SwiftUI/WorldTrackingLimitation)

A structure to represent limitations of tracking the user’s surroundings.

[`SurfaceSnappingInfo`](/documentation/SwiftUI/SurfaceSnappingInfo)

A type representing information about the window scenes snap state.

### Deprecated Types

[`ControlActiveState`](/documentation/SwiftUI/ControlActiveState)

The active appearance expected of controls in a window.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
