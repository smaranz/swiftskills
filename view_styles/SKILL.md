---
name: View styles
description: Rork-Max Quality skill for View styles. Actionable patterns and best practices for SwiftUI development.
---

# View styles

Apply built-in and custom appearances and behaviors to different types of views.
SwiftUI defines built-in styles for certain kinds of views and automatically
selects the appropriate style for a particular presentation context. For
example, a `Label` might appear as an icon, a string title, or both,
depending on factors like the platform, whether the view appears in a toolbar,
and so on.
You can override the automatic style by using one of the style view modifiers.
These modifiers typically propagate throughout a container view, so that you can
wrap a view hierarchy in a style modifier to affect all the views
of the given type within the hierarchy.
Any of the style protocols that define a `makeBody(configuration:)` method, like
`ToggleStyle`, also enable you to define custom styles. Create a type
that conforms to the corresponding style protocol and implement its
`makeBody(configuration:)` method. Then apply the new style using a style view
modifier exactly like a built-in style.


## 🚀 Rork-Max Quality Snippet


```swift
import SwiftUI

struct PremiumViewStyle: View {
    var body: some View {
        Text("Modern Aesthetic")
            .padding()
            .background {
                Capsule()
                    .fill(
                        LinearGradient(
                            colors: [.blue, .purple],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        )
                    )
                    .overlay {
                        Capsule()
                            .strokeBorder(.white.opacity(0.2), lineWidth: 1)
                    }
            }
            .foregroundStyle(.white)
            .shadow(color: .blue.opacity(0.3), radius: 10, x: 0, y: 5)
    }
}
```


## 💎 Elite Implementation Tips

- Always add a subtle `.strokeBorder` (0.2 to 0.5 opacity) to gradients to define edges.
- Use `foregroundStyle` instead of `foregroundColor` for modern hierarchical styling.
- Shadows should match the color of the element (with low opacity) for a 'glow' effect.


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

### Styling views with Liquid Glass

| API | Purpose |
|-----|---------|
| `Applying Liquid Glass to custom views` | Configure, combine, and morph views using Liquid Glass effects. |
| `Landmarks: Building an app with Liquid Glass` | Enhance your app experience with system-provided and custom Liquid Glass. |
| `glassEffect(_:in:)` | Applies the Liquid Glass effect to a view. |
| `interactive(_:)` | Returns a copy of the structure configured to be interactive. |
| `GlassEffectContainer` | A view that combines multiple Liquid Glass shapes into a single |
| `GlassEffectTransition` | A structure that describes changes to apply when a glass effect |
| `GlassButtonStyle` | A button style that applies glass border artwork based on the button’s |
| `GlassProminentButtonStyle` | A button style that applies prominent glass border artwork based on the button’s |

### Styling buttons

| API | Purpose |
|-----|---------|
| `buttonStyle(_:)` | Sets the style for buttons within this view to a button style with a |
| `ButtonStyle` | A type that applies standard interaction behavior and a custom appearance to |
| `ButtonStyleConfiguration` | The properties of a button. |
| `PrimitiveButtonStyle` | A type that applies custom interaction behavior and a custom appearance to |
| `PrimitiveButtonStyleConfiguration` | The properties of a button. |
| `signInWithAppleButtonStyle(_:)` | Sets the style used for displaying the control |

### Styling pickers

| API | Purpose |
|-----|---------|
| `pickerStyle(_:)` | Sets the style for pickers within this view. |
| `PickerStyle` | A type that specifies the appearance and interaction of all pickers within |
| `datePickerStyle(_:)` | Sets the style for date pickers within this view. |
| `DatePickerStyle` | A type that specifies the appearance and interaction of all date pickers |

### Styling menus

| API | Purpose |
|-----|---------|
| `menuStyle(_:)` | Sets the style for menus within this view. |
| `MenuStyle` | A type that applies standard interaction behavior and a custom appearance |
| `MenuStyleConfiguration` | A configuration of a menu. |

### Styling toggles

| API | Purpose |
|-----|---------|
| `toggleStyle(_:)` | Sets the style for toggles in a view hierarchy. |
| `ToggleStyle` | The appearance and behavior of a toggle. |
| `ToggleStyleConfiguration` | The properties of a toggle instance. |

### Styling indicators

| API | Purpose |
|-----|---------|
| `gaugeStyle(_:)` | Sets the style for gauges within this view. |
| `GaugeStyle` | Defines the implementation of all gauge instances within a view |
| `GaugeStyleConfiguration` | The properties of a gauge instance. |
| `progressViewStyle(_:)` | Sets the style for progress views in this view. |
| `ProgressViewStyle` | A type that applies standard interaction behavior to all progress views |
| `ProgressViewStyleConfiguration` | The properties of a progress view instance. |

### Styling views that display text

| API | Purpose |
|-----|---------|
| `labelStyle(_:)` | Sets the style for labels within this view. |
| `LabelStyle` | A type that applies a custom appearance to all labels within a view. |
| `LabelStyleConfiguration` | The properties of a label. |
| `textFieldStyle(_:)` | Sets the style for text fields within this view. |
| `TextFieldStyle` | A specification for the appearance and interaction of a text field. |
| `textEditorStyle(_:)` | Sets the style for text editors within this view. |
| `TextEditorStyle` | A specification for the appearance and interaction of a text editor. |
| `TextEditorStyleConfiguration` | The properties of a text editor. |

### Styling collection views

| API | Purpose |
|-----|---------|
| `listStyle(_:)` | Sets the style for lists within this view. |
| `ListStyle` | A protocol that describes the behavior and appearance of a list. |
| `tableStyle(_:)` | Sets the style for tables within this view. |
| `TableStyle` | A type that applies a custom appearance to all tables within a view. |
| `TableStyleConfiguration` | The properties of a table. |
| `disclosureGroupStyle(_:)` | Sets the style for disclosure groups within this view. |
| `DisclosureGroupStyle` | A type that specifies the appearance and interaction of disclosure groups |

### Styling navigation views

| API | Purpose |
|-----|---------|
| `navigationSplitViewStyle(_:)` | Sets the style for navigation split views within this view. |
| `NavigationSplitViewStyle` | A type that specifies the appearance and interaction of navigation split |
| `tabViewStyle(_:)` | Sets the style for the tab view within the current environment. |
| `TabViewStyle` | A specification for the appearance and interaction of a tab view. |

### Styling groups

| API | Purpose |
|-----|---------|
| `controlGroupStyle(_:)` | Sets the style for control groups within this view. |
| `ControlGroupStyle` | Defines the implementation of all control groups within a view |
| `ControlGroupStyleConfiguration` | The properties of a control group. |
| `formStyle(_:)` | Sets the style for forms in a view hierarchy. |
| `FormStyle` | The appearance and behavior of a form. |
| `FormStyleConfiguration` | The properties of a form instance. |
| `groupBoxStyle(_:)` | Sets the style for group boxes within this view. |
| `GroupBoxStyle` | A type that specifies the appearance and interaction of all group boxes |

### Styling windows from a view inside the window

| API | Purpose |
|-----|---------|
| `presentedWindowStyle(_:)` | Sets the style for windows created by interacting with this view. |
| `presentedWindowToolbarStyle(_:)` | Sets the style for the toolbar in windows created by |

### Adding a glass background on views in visionOS

| API | Purpose |
|-----|---------|
| `glassBackgroundEffect(displayMode:)` | Fills the view’s background with an automatic glass background effect |
| `glassBackgroundEffect(in:displayMode:)` | Fills the view’s background with an automatic glass background effect |
| `GlassBackgroundDisplayMode` | The display mode of a glass background. |
| `GlassBackgroundEffect` | A specification for the appearance of a glass background. |
| `AutomaticGlassBackgroundEffect` | The automatic glass background effect. |
| `GlassBackgroundEffectConfiguration` | A configuration used to build a custom effect. |
| `FeatheredGlassBackgroundEffect` | — |
| `PlateGlassBackgroundEffect` | The plate glass background effect. |
