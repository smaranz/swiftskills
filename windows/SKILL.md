---
name: Windows
description: Rork-Max Quality skill for Windows. Actionable patterns and best practices for SwiftUI development.
---

# Windows

Display user interface content in a window or a collection of windows.
The most common way to present a view hierarchy in your app’s interface is with
a `WindowGroup`, which produces a platform-specific behavior and appearance.
On platforms that support it, people can open multiple windows from the group
simultaneously. Each window relies on the same root view definition, but
retains its own view state. On some platforms, you can also supplement your
app’s user interface with a single-instance window using the `Window` scene
type.
Configure windows using scene modifiers that you add to the window
declaration, like `windowStyle(_:)` or `defaultPosition(_:)`.
You can also indicate how to configure new windows that you present from a view
hierarchy by adding the `presentedWindowStyle(_:)` view modifier to a
view in the hierarchy.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct WindowExample: View {
    @Environment(\.openWindow) private var openWindow
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Open Detail") {
            openWindow(id: "detail-panel")
        }
    }
}

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            WindowExample()
        }
        Window("Detail", id: "detail-panel") {
            DetailPanelView()
        }
        .defaultSize(width: 400, height: 300)
    }
}
```

## 💎 Elite Implementation Tips

- Use `openWindow(id:)` and `dismissWindow(id:)` environment actions for programmatic control
- Set `.defaultSize()` and `.defaultPosition()` for polished window placement
- On visionOS, use `.windowStyle(.volumetric)` for 3D content windows


## When to Use

- Defining the entry point and top-level structure of a SwiftUI app
- Managing multiple windows, scenes, or document-based workflows
- Configuring app-wide lifecycle events and state restoration
- Building multi-platform apps that adapt their structure per platform

## Best Practices

- Keep `@main` App structs thin — delegate complex logic to dedicated model objects
- Use `@Environment(\.scenePhase)` to react to foreground/background transitions
- Prefer `WindowGroup` for document-based apps and `Window` for utility panels
- Store app-level state in an `@Observable` singleton injected via `.environment()`

## Common Pitfalls

- Putting heavy initialization in the App `init()` delays launch
- Forgetting that each `WindowGroup` can spawn multiple instances on macOS/iPadOS
- Using `@StateObject` in the App struct when `@State` with `@Observable` is simpler in Swift 6

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Customizing window styles and state-restoration behavior in macOS` | Configure how your app’s windows look and function in macOS to provide an |
| `Bringing multiple windows to your SwiftUI app` | Compose rich views by reacting to state changes and customize your app’s scene presentation and behavior on iPadOS and macOS. |

### Creating windows

| API | Purpose |
|-----|---------|
| `WindowGroup` | A scene that presents a group of identically structured windows. |
| `Window` | A scene that presents its content in a single, unique window. |
| `UtilityWindow` | A specialized window scene that provides secondary utility to the content |
| `WindowStyle` | A specification for the appearance and interaction of a window. |
| `windowStyle(_:)` | Sets the style for windows created by this scene. |

### Styling the associated toolbar

| API | Purpose |
|-----|---------|
| `windowToolbarStyle(_:)` | Sets the style for the toolbar defined within this scene. |
| `windowToolbarLabelStyle(_:)` | Sets the label style of items in a toolbar and enables user customization. |
| `windowToolbarLabelStyle(fixed:)` | Sets the label style of items in a toolbar. |
| `WindowToolbarStyle` | A specification for the appearance and behavior of a window’s toolbar. |

### Opening windows

| API | Purpose |
|-----|---------|
| `supportsMultipleWindows` | A Boolean value that indicates whether the current platform supports |
| `openWindow` | A window presentation action stored in a view’s environment. |
| `OpenWindowAction` | An action that presents a window. |
| `PushWindowAction` | An action that opens the requested window in place of the window the action |

### Closing windows

| API | Purpose |
|-----|---------|
| `dismissWindow` | A window dismissal action stored in a view’s environment. |
| `DismissWindowAction` | An action that dismisses a window associated to a particular scene. |
| `dismiss` | An action that dismisses the current presentation. |
| `DismissAction` | An action that dismisses a presentation. |
| `DismissBehavior` | Programmatic window dismissal behaviors. |

### Sizing a window

| API | Purpose |
|-----|---------|
| `defaultSize(_:)` | Sets a default size for a window. |
| `defaultSize(width:height:)` | Sets a default width and height for a window. |
| `defaultSize(width:height:depth:)` | Sets a default size for a volumetric window. |
| `defaultSize(_:in:)` | Sets a default size for a volumetric window. |
| `defaultSize(width:height:depth:in:)` | Sets a default size for a volumetric window. |
| `windowResizability(_:)` | Sets the kind of resizability to use for a window. |
| `WindowResizability` | The resizability of a window. |
| `windowIdealSize(_:)` | Specifies how windows derived form this scene should determine their |

### Positioning a window

| API | Purpose |
|-----|---------|
| `defaultPosition(_:)` | Sets a default position for a window. |
| `WindowLevel` | The level of a window. |
| `windowLevel(_:)` | Sets the window level of this scene. |
| `WindowLayoutRoot` | A proxy which represents the root contents of a window. |
| `WindowPlacement` | A type which represents a preferred size and position for a window. |
| `defaultWindowPlacement(_:)` | Defines a function used for determining the default placement |
| `windowIdealPlacement(_:)` | Provides a function which determines a placement to use when windows |
| `WindowPlacementContext` | A type which represents contextual information used for sizing and |

### Configuring window visibility

| API | Purpose |
|-----|---------|
| `WindowVisibilityToggle` | A specialized button for toggling the visibility of a window. |
| `defaultLaunchBehavior(_:)` | Sets the default launch behavior for this scene. |
| `restorationBehavior(_:)` | Sets the restoration behavior for this scene. |
| `SceneLaunchBehavior` | The launch behavior for a scene. |
| `SceneRestorationBehavior` | The restoration behavior for a scene. |
| `persistentSystemOverlays(_:)` | Sets the preferred visibility of the non-transient system views |
| `windowToolbarFullScreenVisibility(_:)` | Configures the visibility of the window toolbar when the window enters |
| `WindowToolbarFullScreenVisibility` | The visibility of the window toolbar with respect to full screen mode. |

### Managing window behavior

| API | Purpose |
|-----|---------|
| `WindowManagerRole` | Options for defining how a scene’s windows behave when used within a managed |
| `windowManagerRole(_:)` | Configures the role for windows derived from `self` when |
| `WindowInteractionBehavior` | Options for enabling and disabling window interaction behaviors. |
| `windowDismissBehavior(_:)` | Configures the dismiss functionality for the window enclosing `self`. |
| `windowFullScreenBehavior(_:)` | Configures the full screen functionality for the window enclosing `self`. |
| `windowMinimizeBehavior(_:)` | Configures the minimize functionality for the window enclosing `self`. |
| `windowResizeBehavior(_:)` | Configures the resize functionality for the window enclosing `self`. |
| `windowBackgroundDragBehavior(_:)` | Configures the behavior of dragging a window by its background. |

### Interacting with volumes

| API | Purpose |
|-----|---------|
| `onVolumeViewpointChange(updateStrategy:initial:_:)` | Adds an action to perform when the viewpoint of the volume changes. |
| `supportedVolumeViewpoints(_:)` | Specifies which viewpoints are supported for the window bar and |
| `VolumeViewpointUpdateStrategy` | A type describing when the action provided to |
| `onVolumeViewpointChange(updateStrategy:initial:_:)` | called. |
| `Viewpoint3D` | A type describing what direction something is being viewed from. |
| `SquareAzimuth` | A type describing what direction something is being viewed from along |
| `WorldAlignmentBehavior` | A type representing the world alignment behavior for a scene. |
| `volumeWorldAlignment(_:)` | Specifies how a volume should be aligned when moved in the world. |

### Deprecated Types

| API | Purpose |
|-----|---------|
| `ControlActiveState` | The active appearance expected of controls in a window. |
