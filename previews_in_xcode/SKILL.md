---
name: Previews in Xcode
description: Rork-Max Quality skill for Previews in Xcode. Actionable patterns and best practices for SwiftUI development.
---

# Previews in Xcode

Generate dynamic, interactive previews of your custom views.
When you create a custom `View` with SwiftUI,
Xcode can display a preview of the view’s content
that stays up-to-date as you make changes to the view’s code.
You use one of the preview macros — like `Preview(_:body:)` —
to tell Xcode what to display.
Xcode shows the preview in a canvas beside your code.
Different preview macros enable different kinds of configuration.
For example, you can add traits that affect the preview’s
appearance using the `Preview(_:traits:_:body:)` macro
or add custom viewpoints for the preview using the
`Preview(_:traits:body:cameras:)` macro. You can also check how
your view behaves inside a specific scene type. For example, in visionOS
you can use the `Preview(_:immersionStyle:traits:body:)` macro to
preview your view inside an `ImmersiveSpace`.
You typically rely on preview macros to create previews in your
code. However, if you can’t get the behavior you need using a preview
macro, you can use the `PreviewProvider` protocol and its
associated supporting types to define and configure a preview.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Previewing views in Xcode with different configurations (dark mode, device sizes)
- Adding custom views and modifiers to the Xcode Library for drag-and-drop
- Profiling view rendering performance with Instruments

## Best Practices

- Create multiple `#Preview` blocks for different states (empty, loading, error, populated)
- Use `@Previewable @State` for interactive previews with mutable state
- Profile with the SwiftUI Instruments template to find slow `body` evaluations

## Common Pitfalls

- Preview-only code leaking into production builds — use `#if DEBUG` guards
- Previews failing silently because of missing environment values or data
- Ignoring Instruments' 'View body evaluated' count — high counts signal unnecessary re-renders

## Key APIs

### Creating a preview

| API | Purpose |
|-----|---------|
| `Preview(_:body:)` | Creates a preview of a SwiftUI view. |
| `Preview(_:traits:_:body:)` | Creates a preview of a SwiftUI view using the specified traits. |
| `Preview(_:traits:body:cameras:)` | Creates a preview of a SwiftUI view using the specified traits and custom |

### Creating a preview in the context of a scene

| API | Purpose |
|-----|---------|
| `Preview(_:immersionStyle:traits:body:)` | Creates a preview of a SwiftUI view in an immersive space. |
| `Preview(_:immersionStyle:traits:body:cameras:)` | Creates a preview of a SwiftUI view in an immersive space with custom |
| `Preview(_:windowStyle:traits:body:)` | Creates a preview of a SwiftUI view in a window. |
| `Preview(_:windowStyle:traits:body:cameras:)` | Creates a preview of a SwiftUI view in a window with custom viewpoints. |

### Defining a preview

| API | Purpose |
|-----|---------|
| `Previewable()` | Tag allowing a dynamic property to appear inline in a preview. |
| `PreviewProvider` | A type that produces view previews in Xcode. |
| `PreviewPlatform` | Platforms that can run the preview. |
| `previewDisplayName(_:)` | Sets a user visible name to show in the canvas for a preview. |
| `PreviewModifier` | A type that defines an environment in which previews can appear. |
| `PreviewModifierContent` | The type-erased content of a preview. |

### Customizing a preview

| API | Purpose |
|-----|---------|
| `previewDevice(_:)` | Overrides the device for a preview. |
| `PreviewDevice` | A simulator device that runs a preview. |
| `previewLayout(_:)` | Overrides the size of the container for the preview. |
| `previewInterfaceOrientation(_:)` | Overrides the orientation of the preview. |
| `InterfaceOrientation` | The orientation of the interface from the user’s perspective. |

### Setting a context

| API | Purpose |
|-----|---------|
| `previewContext(_:)` | Declares a context for the preview. |
| `PreviewContext` | A context type for use with a preview. |
| `PreviewContextKey` | A key type for a preview context. |

### Building in debug mode

| API | Purpose |
|-----|---------|
| `DebugReplaceableView` | Erases view opaque result types in debug builds. |
