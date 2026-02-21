---
name: Controls and indicators
description: Apple SwiftUI Documentation for Controls and indicators.
---

# Controls and indicators

Display values and get user selections.

## Overview

SwiftUI provides controls that enable user interaction specific to each
platform and context. For example, people can initiate events with buttons
and links, or choose among a set of discrete values with
different kinds of pickers. You can also display information to the user
with indicators like progress views and gauges.

![](images/com.apple.SwiftUI/controls-and-indicators-hero@2x.png)

Use these built-in controls and indicators when composing custom
views, and style them to match the needs of your app’s user interface.
For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/menus-and-actions>,
<doc://com.apple.documentation/design/Human-Interface-Guidelines/selection-and-input>, and
<doc://com.apple.documentation/design/Human-Interface-Guidelines/status>
in the Human Interface Guidelines.

## Topics

### Creating buttons

[`Button`](/documentation/SwiftUI/Button)

A control that initiates an action.

[`buttonStyle(_:)`](/documentation/SwiftUI/View/buttonStyle(_:))

Sets the style for buttons within this view to a button style with a
custom appearance and standard interaction behavior.

[`buttonBorderShape(_:)`](/documentation/SwiftUI/View/buttonBorderShape(_:))

Sets the border shape for buttons in this view.

[`buttonRepeatBehavior(_:)`](/documentation/SwiftUI/View/buttonRepeatBehavior(_:))

Sets whether buttons in this view should repeatedly trigger their
actions on prolonged interactions.

[`buttonRepeatBehavior`](/documentation/SwiftUI/EnvironmentValues/buttonRepeatBehavior)

Whether buttons with this associated environment should repeatedly
trigger their actions on prolonged interactions.

[`ButtonBorderShape`](/documentation/SwiftUI/ButtonBorderShape)

A shape used to draw a button’s border.

[`ButtonRole`](/documentation/SwiftUI/ButtonRole)

A value that describes the purpose of a button.

[`ButtonRepeatBehavior`](/documentation/SwiftUI/ButtonRepeatBehavior)

The options for controlling the repeatability of button actions.

[`ButtonSizing`](/documentation/SwiftUI/ButtonSizing)

The sizing behavior of `Button`s and other button-like controls.

### Creating special-purpose buttons

[`EditButton`](/documentation/SwiftUI/EditButton)

A button that toggles the edit mode environment value.

[`PasteButton`](/documentation/SwiftUI/PasteButton)

A system button that reads items from the pasteboard and delivers it to a
closure.

[`RenameButton`](/documentation/SwiftUI/RenameButton)

A button that triggers a standard rename action.

### Linking to other content

[`Link`](/documentation/SwiftUI/Link)

A control for navigating to a URL.

[`ShareLink`](/documentation/SwiftUI/ShareLink)

A view that controls a sharing presentation.

[`SharePreview`](/documentation/SwiftUI/SharePreview)

A representation of a type to display in a share preview.

[`TextFieldLink`](/documentation/SwiftUI/TextFieldLink)

A control that requests text input from the user when pressed.

[`HelpLink`](/documentation/SwiftUI/HelpLink)

A button with a standard appearance that opens app-specific help
documentation.

### Getting numeric inputs

[`Slider`](/documentation/SwiftUI/Slider)

A control for selecting a value from a bounded linear range of values.

[`Stepper`](/documentation/SwiftUI/Stepper)

A control that performs increment and decrement actions.

[`Toggle`](/documentation/SwiftUI/Toggle)

A control that toggles between on and off states.

[`toggleStyle(_:)`](/documentation/SwiftUI/View/toggleStyle(_:))

Sets the style for toggles in a view hierarchy.

### Choosing from a set of options

[`Picker`](/documentation/SwiftUI/Picker)

A control for selecting from a set of mutually exclusive values.

[`pickerStyle(_:)`](/documentation/SwiftUI/View/pickerStyle(_:))

Sets the style for pickers within this view.

[`horizontalRadioGroupLayout()`](/documentation/SwiftUI/View/horizontalRadioGroupLayout())

Sets the style for radio group style pickers within this view to be
horizontally positioned with the radio buttons inside the layout.

[`defaultWheelPickerItemHeight(_:)`](/documentation/SwiftUI/View/defaultWheelPickerItemHeight(_:))

Sets the default wheel-style picker item height.

[`defaultWheelPickerItemHeight`](/documentation/SwiftUI/EnvironmentValues/defaultWheelPickerItemHeight)

The default height of an item in a wheel-style picker, such as a date
picker.

[`paletteSelectionEffect(_:)`](/documentation/SwiftUI/View/paletteSelectionEffect(_:))

Specifies the selection effect to apply to a palette item.

[`PaletteSelectionEffect`](/documentation/SwiftUI/PaletteSelectionEffect)

The selection effect to apply to a palette item.

### Choosing dates

[`DatePicker`](/documentation/SwiftUI/DatePicker)

A control for selecting an absolute date.

[`datePickerStyle(_:)`](/documentation/SwiftUI/View/datePickerStyle(_:))

Sets the style for date pickers within this view.

[`MultiDatePicker`](/documentation/SwiftUI/MultiDatePicker)

A control for picking multiple dates.

[`calendar`](/documentation/SwiftUI/EnvironmentValues/calendar)

The current calendar that views should use when handling dates.

[`timeZone`](/documentation/SwiftUI/EnvironmentValues/timeZone)

The current time zone that views should use when handling dates.

### Choosing a color

[`ColorPicker`](/documentation/SwiftUI/ColorPicker)

A control used to select a color from the system color picker UI.

### Indicating a value

[`Gauge`](/documentation/SwiftUI/Gauge)

A view that shows a value within a range.

[`gaugeStyle(_:)`](/documentation/SwiftUI/View/gaugeStyle(_:))

Sets the style for gauges within this view.

[`ProgressView`](/documentation/SwiftUI/ProgressView)

A view that shows the progress toward completion of a task.

[`progressViewStyle(_:)`](/documentation/SwiftUI/View/progressViewStyle(_:))

Sets the style for progress views in this view.

[`DefaultDateProgressLabel`](/documentation/SwiftUI/DefaultDateProgressLabel)

The default type of the current value label when used by a date-relative
progress view.

[`DefaultButtonLabel`](/documentation/SwiftUI/DefaultButtonLabel)

The default label to use for a button.

### Indicating missing content

[`ContentUnavailableView`](/documentation/SwiftUI/ContentUnavailableView)

An interface, consisting of a label and additional content, that you
display when the content of your app is unavailable to users.

### Providing haptic feedback

[`sensoryFeedback(_:trigger:)`](/documentation/SwiftUI/View/sensoryFeedback(_:trigger:))

Plays the specified `feedback` when the provided `trigger` value
changes.

[`sensoryFeedback(trigger:_:)`](/documentation/SwiftUI/View/sensoryFeedback(trigger:_:))

Plays feedback when returned from the `feedback` closure after the
provided `trigger` value changes.

[`sensoryFeedback(_:trigger:condition:)`](/documentation/SwiftUI/View/sensoryFeedback(_:trigger:condition:))

Plays the specified `feedback` when the provided `trigger` value changes
and the `condition` closure returns `true`.

[`SensoryFeedback`](/documentation/SwiftUI/SensoryFeedback)

Represents a type of haptic and/or audio feedback that can be played.

### Sizing controls

[`controlSize(_:)`](/documentation/SwiftUI/View/controlSize(_:))

Sets the size for controls within this view.

[`controlSize`](/documentation/SwiftUI/EnvironmentValues/controlSize)

The size to apply to controls within a view.

[`ControlSize`](/documentation/SwiftUI/ControlSize)

The size classes, like regular or small, that you can apply to controls
within a view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
