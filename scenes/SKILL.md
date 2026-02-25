---
name: Scenes
description: Rork-Max Quality skill for Scenes. Actionable patterns and best practices for SwiftUI development.
---

# Scenes

Declare the user interface groupings that make up the parts of your app.
A scene represents a part of your app’s user interface that has a life cycle
that the system manages. An `App` instance presents the scenes it contains,
while each `Scene` acts as the root element of a `View` hierarchy.
The system presents scenes in different ways depending on the type of
scene, the platform, and the context. A scene might fill the entire display,
part of the display, a window, a tab in a window, or something else. In some
cases, your app might also be able to display more than one instance of the
scene at a time, like when a user simultaneously opens multiple windows based
on a single `WindowGroup` declaration in your app. For more information about
the primary built-in scene types, see Windows and Documents.
You configure scenes using modifiers, similar to how you configure views.
For example, you can adjust the appearance of the window that contains a
scene — if the scene happens to appear in a window — using the
`windowStyle(_:)` modifier. Similarly, you can add menu commands that
become available when the scene is in the foreground on certain platforms using
the `commands(content:)` modifier.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


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

### Creating scenes

| API | Purpose |
|-----|---------|
| `Scene` | A part of an app’s user interface with a life cycle managed by the |
| `SceneBuilder` | A result builder for composing a collection of scenes into a single |

### Monitoring scene life cycle

| API | Purpose |
|-----|---------|
| `scenePhase` | The current phase of the scene. |
| `ScenePhase` | An indication of a scene’s operational state. |

### Managing a settings window

| API | Purpose |
|-----|---------|
| `Settings` | A scene that presents an interface for viewing and modifying an app’s |
| `SettingsLink` | A view that opens the Settings scene defined by an app. |
| `OpenSettingsAction` | An action that presents the settings scene for an app. |
| `openSettings` | A Settings presentation action stored in a view’s environment. |

### Building a menu bar

| API | Purpose |
|-----|---------|
| `Building and customizing the menu bar with SwiftUI` | Provide a seamless, cross-platform user experience by building a native menu bar for iPadOS and macOS. |

### Creating a menu bar extra

| API | Purpose |
|-----|---------|
| `MenuBarExtra` | A scene that renders itself as a persistent control in the system menu bar. |
| `menuBarExtraStyle(_:)` | Sets the style for menu bar extra created by this scene. |
| `MenuBarExtraStyle` | A specification for the appearance and behavior of a menu bar extra scene. |

### Creating watch notifications

| API | Purpose |
|-----|---------|
| `WKNotificationScene` | A scene which appears in response to receiving the specified |
