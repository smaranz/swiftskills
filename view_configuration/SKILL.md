---
name: View configuration
description: Rork-Max Quality skill for View configuration. Actionable patterns and best practices for SwiftUI development.
---

# View configuration

Adjust the characteristics of views in a hierarchy.
SwiftUI enables you to tune the appearance and behavior of views using view
modifiers.
Many modifiers apply to specific kinds of views or behaviors, but
some apply more generally. For example, you can conditionally hide any view
by dynamically setting its opacity, display contextual help when people hover
over a view, or request the light or dark appearance for a view.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Creating reusable UI components with customizable appearance
- Applying consistent styling across an app using view modifiers
- Configuring view behavior like disabled state, tint, and redaction
- Building design-system components (buttons, cards, badges) with custom styles

## Best Practices

- Extract reusable view modifiers instead of duplicating modifier chains
- Use `ViewModifier` protocol for complex, reusable modifier bundles
- Prefer `.foregroundStyle()` over `.foregroundColor()` for hierarchical tinting
- Apply `.compositingGroup()` before opacity to treat a view subtree as one layer

## Common Pitfalls

- Modifier order matters — `.padding().background()` differs from `.background().padding()`
- Creating views that are too large — break them into smaller extracted views
- Using `AnyView` for type erasure when `@ViewBuilder` or generics work better

## Key APIs

### Hiding views

| API | Purpose |
|-----|---------|
| `opacity(_:)` | Sets the transparency of this view. |
| `hidden()` | Hides this view unconditionally. |

### Hiding system elements

| API | Purpose |
|-----|---------|
| `labelsHidden()` | Hides the labels of any controls contained within this view. |
| `labelsVisibility(_:)` | Controls the visibility of labels of any controls contained within this |
| `labelsVisibility` | The labels visibility set by [`labelsVisibility(_:)`](/documentation/SwiftUI/View/labelsVisibility(_:)). |
| `menuIndicator(_:)` | Sets the menu indicator visibility for controls within this view. |
| `statusBarHidden(_:)` | Sets the visibility of the status bar. |
| `persistentSystemOverlays(_:)` | Sets the preferred visibility of the non-transient system views |
| `Visibility` | The visibility of a UI element, chosen automatically based on |

### Managing view interaction

| API | Purpose |
|-----|---------|
| `disabled(_:)` | Adds a condition that controls whether users can interact with this |
| `isEnabled` | A Boolean value that indicates whether the view associated with this |
| `interactionActivityTrackingTag(_:)` | Sets a tag that you use for tracking interactivity. |
| `invalidatableContent(_:)` | Mark the receiver as their content might be invalidated. |

### Providing contextual help

| API | Purpose |
|-----|---------|
| `help(_:)` | Adds help text to a view using a text view that you provide. |

### Detecting and requesting the light or dark appearance

| API | Purpose |
|-----|---------|
| `preferredColorScheme(_:)` | Sets the preferred color scheme for this presentation. |
| `colorScheme` | The color scheme of this environment. |
| `ColorScheme` | The possible color schemes, corresponding to the light and dark appearances. |

### Getting the color scheme contrast

| API | Purpose |
|-----|---------|
| `colorSchemeContrast` | The contrast associated with the color scheme of this environment. |
| `ColorSchemeContrast` | The contrast between the app’s foreground and background colors. |

### Configuring passthrough

| API | Purpose |
|-----|---------|
| `preferredSurroundingsEffect(_:)` | Applies an effect to passthrough video. |
| `SurroundingsEffect` | Effects that the system can apply to passthrough video. |

### Redacting private content

| API | Purpose |
|-----|---------|
| `privacySensitive(_:)` | Marks the view as containing sensitive, private user data. |
| `redacted(reason:)` | Adds a reason to apply a redaction to this view hierarchy. |
| `unredacted()` | Removes any reason to apply a redaction to this view hierarchy. |
| `redactionReasons` | The current redaction reasons applied to the view hierarchy. |
| `isSceneCaptured` | The current capture state. |
| `RedactionReasons` | The reasons to apply a redaction to data displayed on screen. |
