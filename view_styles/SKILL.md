---
name: View styles
description: Apple SwiftUI Documentation for View styles.
---

# View styles

Apply built-in and custom appearances and behaviors to different types of views.

## Overview

SwiftUI defines built-in styles for certain kinds of views and automatically
selects the appropriate style for a particular presentation context. For
example, a [`Label`](/documentation/SwiftUI/Label) might appear as an icon, a string title, or both,
depending on factors like the platform, whether the view appears in a toolbar,
and so on.

![](images/com.apple.SwiftUI/view-styles-hero@2x.png)

You can override the automatic style by using one of the style view modifiers.
These modifiers typically propagate throughout a container view, so that you can
wrap a view hierarchy in a style modifier to affect all the views
of the given type within the hierarchy.

Any of the style protocols that define a `makeBody(configuration:)` method, like
[`ToggleStyle`](/documentation/SwiftUI/ToggleStyle), also enable you to define custom styles. Create a type
that conforms to the corresponding style protocol and implement its
`makeBody(configuration:)` method. Then apply the new style using a style view
modifier exactly like a built-in style.

## Topics

### Styling views with Liquid Glass

[Applying Liquid Glass to custom views](/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views)

Configure, combine, and morph views using Liquid Glass effects.

[Landmarks: Building an app with Liquid Glass](/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass)

Enhance your app experience with system-provided and custom Liquid Glass.

[`glassEffect(_:in:)`](/documentation/SwiftUI/View/glassEffect(_:in:))

Applies the Liquid Glass effect to a view.

[`interactive(_:)`](/documentation/SwiftUI/Glass/interactive(_:))

Returns a copy of the structure configured to be interactive.

[`GlassEffectContainer`](/documentation/SwiftUI/GlassEffectContainer)

A view that combines multiple Liquid Glass shapes into a single
shape that can morph individual shapes into one another.

[`GlassEffectTransition`](/documentation/SwiftUI/GlassEffectTransition)

A structure that describes changes to apply when a glass effect
is added or removed from the view hierarchy.

[`GlassButtonStyle`](/documentation/SwiftUI/GlassButtonStyle)

A button style that applies glass border artwork based on the button’s
context.

[`GlassProminentButtonStyle`](/documentation/SwiftUI/GlassProminentButtonStyle)

A button style that applies prominent glass border artwork based on the button’s
context.

[`DefaultGlassEffectShape`](/documentation/SwiftUI/DefaultGlassEffectShape)

The default shape applied by glass effects, a capsule.

### Styling buttons

[`buttonStyle(_:)`](/documentation/SwiftUI/View/buttonStyle(_:))

Sets the style for buttons within this view to a button style with a
custom appearance and standard interaction behavior.

[`ButtonStyle`](/documentation/SwiftUI/ButtonStyle)

A type that applies standard interaction behavior and a custom appearance to
all buttons within a view hierarchy.

[`ButtonStyleConfiguration`](/documentation/SwiftUI/ButtonStyleConfiguration)

The properties of a button.

[`PrimitiveButtonStyle`](/documentation/SwiftUI/PrimitiveButtonStyle)

A type that applies custom interaction behavior and a custom appearance to
all buttons within a view hierarchy.

[`PrimitiveButtonStyleConfiguration`](/documentation/SwiftUI/PrimitiveButtonStyleConfiguration)

The properties of a button.

[`signInWithAppleButtonStyle(_:)`](/documentation/SwiftUI/View/signInWithAppleButtonStyle(_:))

Sets the style used for displaying the control
(see `SignInWithAppleButton.Style`).

### Styling pickers

[`pickerStyle(_:)`](/documentation/SwiftUI/View/pickerStyle(_:))

Sets the style for pickers within this view.

[`PickerStyle`](/documentation/SwiftUI/PickerStyle)

A type that specifies the appearance and interaction of all pickers within
a view hierarchy.

[`datePickerStyle(_:)`](/documentation/SwiftUI/View/datePickerStyle(_:))

Sets the style for date pickers within this view.

[`DatePickerStyle`](/documentation/SwiftUI/DatePickerStyle)

A type that specifies the appearance and interaction of all date pickers
within a view hierarchy.

### Styling menus

[`menuStyle(_:)`](/documentation/SwiftUI/View/menuStyle(_:))

Sets the style for menus within this view.

[`MenuStyle`](/documentation/SwiftUI/MenuStyle)

A type that applies standard interaction behavior and a custom appearance
to all menus within a view hierarchy.

[`MenuStyleConfiguration`](/documentation/SwiftUI/MenuStyleConfiguration)

A configuration of a menu.

### Styling toggles

[`toggleStyle(_:)`](/documentation/SwiftUI/View/toggleStyle(_:))

Sets the style for toggles in a view hierarchy.

[`ToggleStyle`](/documentation/SwiftUI/ToggleStyle)

The appearance and behavior of a toggle.

[`ToggleStyleConfiguration`](/documentation/SwiftUI/ToggleStyleConfiguration)

The properties of a toggle instance.

### Styling indicators

[`gaugeStyle(_:)`](/documentation/SwiftUI/View/gaugeStyle(_:))

Sets the style for gauges within this view.

[`GaugeStyle`](/documentation/SwiftUI/GaugeStyle)

Defines the implementation of all gauge instances within a view
hierarchy.

[`GaugeStyleConfiguration`](/documentation/SwiftUI/GaugeStyleConfiguration)

The properties of a gauge instance.

[`progressViewStyle(_:)`](/documentation/SwiftUI/View/progressViewStyle(_:))

Sets the style for progress views in this view.

[`ProgressViewStyle`](/documentation/SwiftUI/ProgressViewStyle)

A type that applies standard interaction behavior to all progress views
within a view hierarchy.

[`ProgressViewStyleConfiguration`](/documentation/SwiftUI/ProgressViewStyleConfiguration)

The properties of a progress view instance.

### Styling views that display text

[`labelStyle(_:)`](/documentation/SwiftUI/View/labelStyle(_:))

Sets the style for labels within this view.

[`LabelStyle`](/documentation/SwiftUI/LabelStyle)

A type that applies a custom appearance to all labels within a view.

[`LabelStyleConfiguration`](/documentation/SwiftUI/LabelStyleConfiguration)

The properties of a label.

[`textFieldStyle(_:)`](/documentation/SwiftUI/View/textFieldStyle(_:))

Sets the style for text fields within this view.

[`TextFieldStyle`](/documentation/SwiftUI/TextFieldStyle)

A specification for the appearance and interaction of a text field.

[`textEditorStyle(_:)`](/documentation/SwiftUI/View/textEditorStyle(_:))

Sets the style for text editors within this view.

[`TextEditorStyle`](/documentation/SwiftUI/TextEditorStyle)

A specification for the appearance and interaction of a text editor.

[`TextEditorStyleConfiguration`](/documentation/SwiftUI/TextEditorStyleConfiguration)

The properties of a text editor.

### Styling collection views

[`listStyle(_:)`](/documentation/SwiftUI/View/listStyle(_:))

Sets the style for lists within this view.

[`ListStyle`](/documentation/SwiftUI/ListStyle)

A protocol that describes the behavior and appearance of a list.

[`tableStyle(_:)`](/documentation/SwiftUI/View/tableStyle(_:))

Sets the style for tables within this view.

[`TableStyle`](/documentation/SwiftUI/TableStyle)

A type that applies a custom appearance to all tables within a view.

[`TableStyleConfiguration`](/documentation/SwiftUI/TableStyleConfiguration)

The properties of a table.

[`disclosureGroupStyle(_:)`](/documentation/SwiftUI/View/disclosureGroupStyle(_:))

Sets the style for disclosure groups within this view.

[`DisclosureGroupStyle`](/documentation/SwiftUI/DisclosureGroupStyle)

A type that specifies the appearance and interaction of disclosure groups
within a view hierarchy.

### Styling navigation views

[`navigationSplitViewStyle(_:)`](/documentation/SwiftUI/View/navigationSplitViewStyle(_:))

Sets the style for navigation split views within this view.

[`NavigationSplitViewStyle`](/documentation/SwiftUI/NavigationSplitViewStyle)

A type that specifies the appearance and interaction of navigation split
views within a view hierarchy.

[`tabViewStyle(_:)`](/documentation/SwiftUI/View/tabViewStyle(_:))

Sets the style for the tab view within the current environment.

[`TabViewStyle`](/documentation/SwiftUI/TabViewStyle)

A specification for the appearance and interaction of a tab view.

### Styling groups

[`controlGroupStyle(_:)`](/documentation/SwiftUI/View/controlGroupStyle(_:))

Sets the style for control groups within this view.

[`ControlGroupStyle`](/documentation/SwiftUI/ControlGroupStyle)

Defines the implementation of all control groups within a view
hierarchy.

[`ControlGroupStyleConfiguration`](/documentation/SwiftUI/ControlGroupStyleConfiguration)

The properties of a control group.

[`formStyle(_:)`](/documentation/SwiftUI/View/formStyle(_:))

Sets the style for forms in a view hierarchy.

[`FormStyle`](/documentation/SwiftUI/FormStyle)

The appearance and behavior of a form.

[`FormStyleConfiguration`](/documentation/SwiftUI/FormStyleConfiguration)

The properties of a form instance.

[`groupBoxStyle(_:)`](/documentation/SwiftUI/View/groupBoxStyle(_:))

Sets the style for group boxes within this view.

[`GroupBoxStyle`](/documentation/SwiftUI/GroupBoxStyle)

A type that specifies the appearance and interaction of all group boxes
within a view hierarchy.

[`GroupBoxStyleConfiguration`](/documentation/SwiftUI/GroupBoxStyleConfiguration)

The properties of a group box instance.

[`indexViewStyle(_:)`](/documentation/SwiftUI/View/indexViewStyle(_:))

Sets the style for the index view within the current environment.

[`IndexViewStyle`](/documentation/SwiftUI/IndexViewStyle)

Defines the implementation of all `IndexView` instances within a view
hierarchy.

[`labeledContentStyle(_:)`](/documentation/SwiftUI/View/labeledContentStyle(_:))

Sets a style for labeled content.

[`LabeledContentStyle`](/documentation/SwiftUI/LabeledContentStyle)

The appearance and behavior of a labeled content instance..

[`LabeledContentStyleConfiguration`](/documentation/SwiftUI/LabeledContentStyleConfiguration)

The properties of a labeled content instance.

### Styling windows from a view inside the window

[`presentedWindowStyle(_:)`](/documentation/SwiftUI/View/presentedWindowStyle(_:))

Sets the style for windows created by interacting with this view.

[`presentedWindowToolbarStyle(_:)`](/documentation/SwiftUI/View/presentedWindowToolbarStyle(_:))

Sets the style for the toolbar in windows created by
interacting with this view.

### Adding a glass background on views in visionOS

[`glassBackgroundEffect(displayMode:)`](/documentation/SwiftUI/View/glassBackgroundEffect(displayMode:))

Fills the view’s background with an automatic glass background effect
and container-relative rounded rectangle shape.

[`glassBackgroundEffect(in:displayMode:)`](/documentation/SwiftUI/View/glassBackgroundEffect(in:displayMode:))

Fills the view’s background with an automatic glass background effect
and a shape that you specify.

[`GlassBackgroundDisplayMode`](/documentation/SwiftUI/GlassBackgroundDisplayMode)

The display mode of a glass background.

[`GlassBackgroundEffect`](/documentation/SwiftUI/GlassBackgroundEffect)

A specification for the appearance of a glass background.

[`AutomaticGlassBackgroundEffect`](/documentation/SwiftUI/AutomaticGlassBackgroundEffect)

The automatic glass background effect.

[`GlassBackgroundEffectConfiguration`](/documentation/SwiftUI/GlassBackgroundEffectConfiguration)

A configuration used to build a custom effect.

[`FeatheredGlassBackgroundEffect`](/documentation/SwiftUI/FeatheredGlassBackgroundEffect)

[`PlateGlassBackgroundEffect`](/documentation/SwiftUI/PlateGlassBackgroundEffect)

The plate glass background effect.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
