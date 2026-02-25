---
name: App extensions
description: Rork-Max Quality skill for App extensions. Actionable patterns and best practices for SwiftUI development.
---

# App extensions

Extend your app’s basic functionality to other parts of the system, like
by adding a Widget.
Use SwiftUI along with WidgetKit
to add widgets to your app.
Widgets provide quick access to relevant content
from your app. Define a structure that conforms to the `Widget` protocol,
and declare a view hierarchy for the widget. Configure the views inside the
widget as you do other SwiftUI views, using view modifiers, including a
few widget-specific modifiers.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Adding widgets, watch complications, or share extensions to an app
- Exposing app functionality to Shortcuts, Siri, or Spotlight
- Implementing App Intents for system-level integration

## Best Practices

- Share data between app and extensions using App Groups and shared containers
- Keep extension targets lightweight — factor shared code into a framework
- Use `WidgetKit` timeline providers for efficient widget updates

## Common Pitfalls

- Extensions have strict memory limits — avoid loading large assets
- Forgetting to configure App Group entitlements for shared UserDefaults or files
- Over-scheduling widget timeline reloads, wasting battery

## Key APIs

### Creating widgets

| API | Purpose |
|-----|---------|
| `Widget` | The configuration and content of a widget to display on the Home screen or |
| `WidgetBundle` | A container used to expose multiple widgets from a single widget extension. |
| `LimitedAvailabilityConfiguration` | A type-erased widget configuration. |
| `WidgetConfiguration` | A type that describes a widget’s content. |
| `EmptyWidgetConfiguration` | An empty widget configuration. |

### Composing control widgets

| API | Purpose |
|-----|---------|
| `ControlWidget` | The configuration and content of a control widget to display in system spaces |
| `ControlWidgetConfiguration` | A type that describes a control widget’s content. |
| `EmptyControlWidgetConfiguration` | An empty control widget configuration. |
| `ControlWidgetConfigurationBuilder` | A custom attribute that constructs a control widget’s body. |
| `ControlWidgetTemplate` | A type that describes a control widget’s content. |
| `EmptyControlWidgetTemplate` | An empty control widget template. |
| `ControlWidgetTemplateBuilder` | A custom attribute that constructs a control widget template’s body. |
| `controlWidgetActionHint(_:)` | The action hint of the control described by the modified label. |

### Labeling a widget

| API | Purpose |
|-----|---------|
| `widgetLabel(_:)` | Returns a localized text label that displays additional content outside |
| `widgetLabel(label:)` | Creates a label for displaying additional content outside an accessory |

### Styling a widget group

| API | Purpose |
|-----|---------|
| `accessoryWidgetGroupStyle(_:)` | The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three |

### Controlling the accented group

| API | Purpose |
|-----|---------|
| `widgetAccentable(_:)` | Adds the view and all of its subviews to the accented group. |

### Managing placement in the Dynamic Island

| API | Purpose |
|-----|---------|
| `dynamicIsland(verticalPlacement:)` | Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic |
