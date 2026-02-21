---
name: App extensions
description: Apple SwiftUI Documentation for App extensions.
---

# App extensions

Extend your app’s basic functionality to other parts of the system, like
by adding a Widget.

## Overview

Use SwiftUI along with <doc://com.apple.documentation/documentation/WidgetKit>
to add widgets to your app.

![](images/com.apple.SwiftUI/app-extensions-hero@2x.png)

Widgets provide quick access to relevant content
from your app. Define a structure that conforms to the [`Widget`](/documentation/SwiftUI/Widget) protocol,
and declare a view hierarchy for the widget. Configure the views inside the
widget as you do other SwiftUI views, using view modifiers, including a
few widget-specific modifiers.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/widgets>
in the Human Interface Guidelines.

## Topics

### Creating widgets

  <doc://com.apple.documentation/documentation/widgetkit/building_widgets_using_widgetkit_and_swiftui>

  <doc://com.apple.documentation/documentation/WidgetKit/Creating-a-Widget-Extension>

  <doc://com.apple.documentation/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date>

  <doc://com.apple.documentation/documentation/WidgetKit/Making-a-Configurable-Widget>

[`Widget`](/documentation/SwiftUI/Widget)

The configuration and content of a widget to display on the Home screen or
in Notification Center.

[`WidgetBundle`](/documentation/SwiftUI/WidgetBundle)

A container used to expose multiple widgets from a single widget extension.

[`LimitedAvailabilityConfiguration`](/documentation/SwiftUI/LimitedAvailabilityConfiguration)

A type-erased widget configuration.

[`WidgetConfiguration`](/documentation/SwiftUI/WidgetConfiguration)

A type that describes a widget’s content.

[`EmptyWidgetConfiguration`](/documentation/SwiftUI/EmptyWidgetConfiguration)

An empty widget configuration.

### Composing control widgets

[`ControlWidget`](/documentation/SwiftUI/ControlWidget)

The configuration and content of a control widget to display in system spaces
such as Control Center, the Lock Screen, and the Action Button.

[`ControlWidgetConfiguration`](/documentation/SwiftUI/ControlWidgetConfiguration)

A type that describes a control widget’s content.

[`EmptyControlWidgetConfiguration`](/documentation/SwiftUI/EmptyControlWidgetConfiguration)

An empty control widget configuration.

[`ControlWidgetConfigurationBuilder`](/documentation/SwiftUI/ControlWidgetConfigurationBuilder)

A custom attribute that constructs a control widget’s body.

[`ControlWidgetTemplate`](/documentation/SwiftUI/ControlWidgetTemplate)

A type that describes a control widget’s content.

[`EmptyControlWidgetTemplate`](/documentation/SwiftUI/EmptyControlWidgetTemplate)

An empty control widget template.

[`ControlWidgetTemplateBuilder`](/documentation/SwiftUI/ControlWidgetTemplateBuilder)

A custom attribute that constructs a control widget template’s body.

[`controlWidgetActionHint(_:)`](/documentation/SwiftUI/View/controlWidgetActionHint(_:))

The action hint of the control described by the modified label.

[`controlWidgetStatus(_:)`](/documentation/SwiftUI/View/controlWidgetStatus(_:))

The status of the control described by the modified label.

### Labeling a widget

[`widgetLabel(_:)`](/documentation/SwiftUI/View/widgetLabel(_:))

Returns a localized text label that displays additional content outside
the accessory family widget’s main SwiftUI view.

[`widgetLabel(label:)`](/documentation/SwiftUI/View/widgetLabel(label:))

Creates a label for displaying additional content outside an accessory
family widget’s main SwiftUI view.

### Styling a widget group

[`accessoryWidgetGroupStyle(_:)`](/documentation/SwiftUI/View/accessoryWidgetGroupStyle(_:))

The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three
content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.

### Controlling the accented group

[`widgetAccentable(_:)`](/documentation/SwiftUI/View/widgetAccentable(_:))

Adds the view and all of its subviews to the accented group.

### Managing placement in the Dynamic Island

[`dynamicIsland(verticalPlacement:)`](/documentation/SwiftUI/View/dynamicIsland(verticalPlacement:))

Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic
Island.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
