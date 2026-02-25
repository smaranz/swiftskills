---
name: Controls and indicators
description: Rork-Max Quality skill for Controls and indicators. Actionable patterns and best practices for SwiftUI development.
---

# Controls and indicators

Display values and get user selections.
SwiftUI provides controls that enable user interaction specific to each
platform and context. For example, people can initiate events with buttons
and links, or choose among a set of discrete values with
different kinds of pickers. You can also display information to the user
with indicators like progress views and gauges.
Use these built-in controls and indicators when composing custom
views, and style them to match the needs of your app’s user interface.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Displaying text with rich formatting, markdown, or attributed strings
- Rendering images from assets, SF Symbols, or async URLs
- Building interactive controls: buttons, toggles, pickers, sliders, steppers
- Creating menus, context menus, and keyboard shortcuts

## Best Practices

- Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography
- Prefer `AsyncImage` for remote images with placeholder and error states
- Use `Label` to pair text with icons — it adapts to context (list rows, menus, toolbars)
- Support Dynamic Type by using system text styles (`.title`, `.body`, `.caption`)

## Common Pitfalls

- Hard-coding font sizes instead of using Dynamic Type styles
- Loading large images synchronously on the main thread
- Forgetting to provide accessibility labels for image-only buttons

## Key APIs

### Creating buttons

| API | Purpose |
|-----|---------|
| `Button` | A control that initiates an action. |
| `buttonStyle(_:)` | Sets the style for buttons within this view to a button style with a |
| `buttonBorderShape(_:)` | Sets the border shape for buttons in this view. |
| `buttonRepeatBehavior(_:)` | Sets whether buttons in this view should repeatedly trigger their |
| `buttonRepeatBehavior` | Whether buttons with this associated environment should repeatedly |
| `ButtonBorderShape` | A shape used to draw a button’s border. |
| `ButtonRole` | A value that describes the purpose of a button. |
| `ButtonRepeatBehavior` | The options for controlling the repeatability of button actions. |

### Creating special-purpose buttons

| API | Purpose |
|-----|---------|
| `EditButton` | A button that toggles the edit mode environment value. |
| `PasteButton` | A system button that reads items from the pasteboard and delivers it to a |
| `RenameButton` | A button that triggers a standard rename action. |

### Linking to other content

| API | Purpose |
|-----|---------|
| `Link` | A control for navigating to a URL. |
| `ShareLink` | A view that controls a sharing presentation. |
| `SharePreview` | A representation of a type to display in a share preview. |
| `TextFieldLink` | A control that requests text input from the user when pressed. |
| `HelpLink` | A button with a standard appearance that opens app-specific help |

### Getting numeric inputs

| API | Purpose |
|-----|---------|
| `Slider` | A control for selecting a value from a bounded linear range of values. |
| `Stepper` | A control that performs increment and decrement actions. |
| `Toggle` | A control that toggles between on and off states. |
| `toggleStyle(_:)` | Sets the style for toggles in a view hierarchy. |

### Choosing from a set of options

| API | Purpose |
|-----|---------|
| `Picker` | A control for selecting from a set of mutually exclusive values. |
| `pickerStyle(_:)` | Sets the style for pickers within this view. |
| `horizontalRadioGroupLayout()` | Sets the style for radio group style pickers within this view to be |
| `defaultWheelPickerItemHeight(_:)` | Sets the default wheel-style picker item height. |
| `defaultWheelPickerItemHeight` | The default height of an item in a wheel-style picker, such as a date |
| `paletteSelectionEffect(_:)` | Specifies the selection effect to apply to a palette item. |
| `PaletteSelectionEffect` | The selection effect to apply to a palette item. |

### Choosing dates

| API | Purpose |
|-----|---------|
| `DatePicker` | A control for selecting an absolute date. |
| `datePickerStyle(_:)` | Sets the style for date pickers within this view. |
| `MultiDatePicker` | A control for picking multiple dates. |
| `calendar` | The current calendar that views should use when handling dates. |
| `timeZone` | The current time zone that views should use when handling dates. |

### Choosing a color

| API | Purpose |
|-----|---------|
| `ColorPicker` | A control used to select a color from the system color picker UI. |

### Indicating a value

| API | Purpose |
|-----|---------|
| `Gauge` | A view that shows a value within a range. |
| `gaugeStyle(_:)` | Sets the style for gauges within this view. |
| `ProgressView` | A view that shows the progress toward completion of a task. |
| `progressViewStyle(_:)` | Sets the style for progress views in this view. |
| `DefaultDateProgressLabel` | The default type of the current value label when used by a date-relative |
| `DefaultButtonLabel` | The default label to use for a button. |

### Indicating missing content

| API | Purpose |
|-----|---------|
| `ContentUnavailableView` | An interface, consisting of a label and additional content, that you |

### Providing haptic feedback

| API | Purpose |
|-----|---------|
| `sensoryFeedback(_:trigger:)` | Plays the specified `feedback` when the provided `trigger` value |
| `sensoryFeedback(trigger:_:)` | Plays feedback when returned from the `feedback` closure after the |
| `sensoryFeedback(_:trigger:condition:)` | Plays the specified `feedback` when the provided `trigger` value changes |
| `SensoryFeedback` | Represents a type of haptic and/or audio feedback that can be played. |

### Sizing controls

| API | Purpose |
|-----|---------|
| `controlSize(_:)` | Sets the size for controls within this view. |
| `controlSize` | The size to apply to controls within a view. |
| `ControlSize` | The size classes, like regular or small, that you can apply to controls |
