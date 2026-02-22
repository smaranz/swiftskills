---
name: MACOS Views and Controls
description: Rork-Max Quality skill for MACOS Views and Controls on macos. Based on official Apple AppKit Documentation.
---

# MACOS Views and Controls

## 🚀 Rork-Max Quality Snippet

```swift
// Premium MACOS Views and Controls Implementation for macos
// Focus on platform-native excellence

import SwiftUI
#if os(macos)
// AppKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality MACOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the macos native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for macos: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Views and Controls

Present your content onscreen and handle user input and events.

## Discussion

Views and controls are the building blocks of your app’s user interface.

![A sample macOS app with the view broken down into label, text field, and button control elements.The window has the title New List. Beneath the title is a text field labeled name, with a text box containing the placeholder text Enter text here. Beneath that is a label titled color followed by seven selectable circles of color. In the bottom right hand corner is a enabled Cancel button followed by a disabled OK button side-by-side.](images/com.apple.appkit/media-4098514@2x.png)

Views can host other views. Embedding one view inside another creates a containment relationship between the host view (known as the *superview*) and the embedded view (known as the *subview*). View hierarchies make it easier to manage views.

You can also use views to do any of the following:

- Respond to touches and other events (either directly or in coordination with gesture recognizers).
- Draw custom content using Core Graphics.
- Respond to focus changes.
- Animate the size, position, and appearance attributes of the view using Core Animation.

Favor AppKit views and controls whenever possible. These components adapt automatically to system changes, and many support appearance customizations to support the look and feel you want in your app. When AppKit doesn’t provide the exact view or control you need, you can create a custom view.

[`NSView`](/documentation/AppKit/NSView) is the root class for all views and defines their common behavior. [`NSControl`](/documentation/AppKit/NSControl) defines additional behaviors that are specific to buttons, switches, and other views designed for user interactions.

For additional information about how to use views and controls, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/components/all-components).

## Topics

### View fundamentals

[`NSView`](/documentation/AppKit/NSView)

The infrastructure for drawing, printing, and handling events in an app.

[`NSControl`](/documentation/AppKit/NSControl)

A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern.

[`NSCell`](/documentation/AppKit/NSCell)

A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](/documentation/AppKit/NSView) subclass.

[`NSActionCell`](/documentation/AppKit/NSActionCell)

An active area inside a control.

### Container views

Use container views to arrange the views of your interface and to facilitate navigation among those views.

  <doc://com.apple.documentation/documentation/Xcode/localization-friendly-layouts-in-macos>

[Grid View](/documentation/AppKit/grid-view)

Arrange views in a flexible grid, and handle the layout associated with those views.

[`NSSplitView`](/documentation/AppKit/NSSplitView)

A view that arranges two or more views in a linear stack running horizontally or vertically.

[Organize Your User Interface with a Stack View](/documentation/AppKit/organize-your-user-interface-with-a-stack-view)

Group individual views in your app’s user interface into a scrollable stack view.

[`NSStackView`](/documentation/AppKit/NSStackView)

A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes.

[`NSTabView`](/documentation/AppKit/NSTabView)

A multipage interface that displays one page at a time.

[Scroll View](/documentation/AppKit/scroll-view)

Provide an interface for navigating content that is too large to fit in the available space.

### Content views

Use content views to organize and display your app’s data.

[Browser View](/documentation/AppKit/browser-view)

Provide a column-based interface for viewing and navigating hierarchical information.

[Collection View](/documentation/AppKit/collection-view)

Display one or more subviews in a highly configurable arrangement.

[Outline View](/documentation/AppKit/outline-view)

Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.

[Table View](/documentation/AppKit/table-view)

Display custom data in rows and columns.

[`NSTextView`](/documentation/AppKit/NSTextView)

A view that draws text and handles user interactions with that text.

### Controls

Use controls to handle specific types of user interactions. Controls are specialized views that use the target-action design pattern to notify your app of interactions with their content.

  <doc://com.apple.documentation/documentation/UIKit/responding-to-control-based-events-using-target-action>

[`NSButton`](/documentation/AppKit/NSButton)

A control that defines an area on the screen that a user clicks to trigger an action.

[`NSColorWell`](/documentation/AppKit/NSColorWell)

A control that displays a color value and lets the user change that color value.

[Combo Box](/documentation/AppKit/combo-box)

Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.

[`NSComboButton`](/documentation/AppKit/NSComboButton)

A button with a pull-down menu and a default action.

[Date Picker](/documentation/AppKit/date-picker)

Display a calendar date and provide controls for editing the date value.

[`NSImageView`](/documentation/AppKit/NSImageView)

A display of image data in a frame.

[`NSLevelIndicator`](/documentation/AppKit/NSLevelIndicator)

A visual representation of a level or quantity, using discrete values.

[Path Control](/documentation/AppKit/path-control)

A display of a file system path or virtual path information.

[`NSPopUpButton`](/documentation/AppKit/NSPopUpButton)

A control for selecting an item from a list.

[`NSProgressIndicator`](/documentation/AppKit/NSProgressIndicator)

An interface that provides visual feedback to the user about the status of an ongoing task.

[`NSRuleEditor`](/documentation/AppKit/NSRuleEditor)

An interface for configuring a rule-based list of options.

[`NSPredicateEditor`](/documentation/AppKit/NSPredicateEditor)

A defined set of rules that allows the editing of predicate objects.

[Search Field](/documentation/AppKit/search-field)

Provide a text field that is optimized for text-based search interfaces.

[`NSSegmentedControl`](/documentation/AppKit/NSSegmentedControl)

Display one or more buttons in a single horizontal group.

[Slider](/documentation/AppKit/slider)

Display a range of values from which the user selects a single value.

[`NSStepper`](/documentation/AppKit/NSStepper)

An interface with up and down arrow buttons for incrementing or decrementing a value.

[Text Field](/documentation/AppKit/text-field)

Provide a simple interface for displaying and editing text, including support for password fields and secure forms of text entry.

[Token Field](/documentation/AppKit/token-field)

Provide a text field whose text can be rendered in a visually distinct way so that users can recognize portions more easily.

[Toolbar](/documentation/AppKit/toolbar)

Provide a space for controls under a window’s title bar and above your custom content.

[`NSSwitch`](/documentation/AppKit/NSSwitch)

A control that offers a binary choice.

[`NSMatrix`](/documentation/AppKit/NSMatrix)

A legacy interface for grouping radio buttons or other types of cells together.

### Liquid Glass effects

[`NSGlassEffectView`](/documentation/AppKit/NSGlassEffectView)

A view that embeds its content view in a dynamic glass effect.

[`NSGlassEffectView.Style`](/documentation/AppKit/NSGlassEffectView/Style-swift.enum)

[`NSGlassEffectContainerView`](/documentation/AppKit/NSGlassEffectContainerView)

A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other.

### Interacting with adjacent views

[`NSBackgroundExtensionView`](/documentation/AppKit/NSBackgroundExtensionView)

A view that extends content to fill its own bounds.

### Visual adornments

Add purely decorative elements to your user interface.

[`NSVisualEffectView`](/documentation/AppKit/NSVisualEffectView)

A view that adds translucency and vibrancy effects to the views in your interface.

[`NSBox`](/documentation/AppKit/NSBox)

A stylized rectangular box with an optional title.

### UI validation

[`NSUserInterfaceValidations`](/documentation/AppKit/NSUserInterfaceValidations)

A protocol that a custom class can adopt to manage the enabled state of a UI element.

[`NSValidatedUserInterfaceItem`](/documentation/AppKit/NSValidatedUserInterfaceItem)

A protocol that a custom class can adopt to manage the automatic enablement of a UI control.

### Tool tips

[`NSViewToolTipOwner`](/documentation/AppKit/NSViewToolTipOwner)

A set of methods for dynamically associating a tool tip with a view.

### Related types

[`NSRectAlignment`](/documentation/AppKit/NSRectAlignment)

Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.

[`NSDirectionalEdgeInsets`](/documentation/AppKit/NSDirectionalEdgeInsets)

The inset distances for views, taking the user interface layout direction into account.

[`NSDirectionalRectEdge`](/documentation/AppKit/NSDirectionalRectEdge)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
