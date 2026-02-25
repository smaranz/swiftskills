---
name: Immersive spaces
description: Rork-Max Quality skill for Immersive spaces. Actionable patterns and best practices for SwiftUI development.
---

# Immersive spaces

Display unbounded content in a person’s surroundings.
Use an immersive space in visionOS to present SwiftUI views outside of any
containers. You can include any views in a space, although you typically use
a RealityView
to present RealityKit content.
You can request one of three styles of spaces with the
`immersionStyle(selection:in:)` scene modifier:
- The `mixed` style blends your content with passthrough.
This enables you to place virtual objects in a person’s surroundings.
- The `full` style displays only your content, with
passthrough turned off. This enables you to completely control the visual
experience, like when you want to transport people to a new world.
- The `progressive` style completely replaces passthrough in
a portion of the display. You might use this style to keep people grounded
in the real world while displaying a view into another world.
When you open an immersive space, the system continues to display all of your
app’s windows, but hides windows from other apps. The system supports displaying
only one space at a time across all apps, so your app can only open a space
if one isn’t already open.


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

### Creating an immersive space

| API | Purpose |
|-----|---------|
| `ImmersiveSpace` | A scene that presents its content in an unbounded space. |
| `ImmersiveSpaceContentBuilder` | A result builder for composing a collection of immersive space elements. |
| `immersionStyle(selection:in:)` | Sets the style for an immersive space. |
| `ImmersionStyle` | The styles that an immersive space can have. |
| `immersiveSpaceDisplacement` | The displacement that the system applies to the immersive space when |
| `ImmersiveEnvironmentBehavior` | The behavior of the system-provided immersive environments when a scene is |

### Opening an immersive space

| API | Purpose |
|-----|---------|
| `openImmersiveSpace` | An action that presents an immersive space. |
| `OpenImmersiveSpaceAction` | An action that presents an immersive space. |

### Closing the immersive space

| API | Purpose |
|-----|---------|
| `dismissImmersiveSpace` | An immersive space dismissal action stored in a view’s environment. |
| `DismissImmersiveSpaceAction` | An action that dismisses an immersive space. |

### Hiding upper limbs during immersion

| API | Purpose |
|-----|---------|
| `upperLimbVisibility(_:)` | Sets the preferred visibility of the user’s upper limbs, while an |
| `ImmersiveSpace` | — |
| `upperLimbVisibility(_:)` | Sets the preferred visibility of the user’s upper limbs, while an |

### Adjusting content brightness

| API | Purpose |
|-----|---------|
| `immersiveContentBrightness(_:)` | Sets the content brightness of an immersive space. |
| `ImmersiveContentBrightness` | The content brightness of an immersive space. |

### Responding to immersion changes

| API | Purpose |
|-----|---------|
| `onImmersionChange(initial:_:)` | Performs an action when the immersion state of your app changes. |
| `ImmersionChangeContext` | A structure that represents a state of immersion of your app. |

### Adding menu items to an immersive space

| API | Purpose |
|-----|---------|
| `immersiveEnvironmentPicker(content:)` | Add menu items to open immersive spaces from a media player’s |

### Handling remote immersive spaces

| API | Purpose |
|-----|---------|
| `RemoteImmersiveSpace` | A scene that presents its content in an unbounded space on a remote device. |
| `RemoteDeviceIdentifier` | An opaque type that identifies a remote device displaying scene content |
