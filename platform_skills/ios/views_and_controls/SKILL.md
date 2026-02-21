---
name: IOS Views and controls
description: Apple UIKit Documentation for IOS Views and controls on ios.
---

# Views and controls

Present your content onscreen and define the interactions allowed with that content.

## Discussion

Views and controls are the visual building blocks of your app’s user interface. Use them to draw and organize your app’s content onscreen.

![A screenshot of a new event view in the Calendar app, that highlights a label, switch, and date picker.](images/com.apple.uikit/views-and-controls-1@2x.png)

Views can host other views. Embedding one view inside another creates a containment relationship between the host view (known as the *superview*) and the embedded view (known as the *subview*). View hierarchies make it easier to manage views.

You can also use views to do any of the following:

- Respond to touches and other events (either directly or in coordination with gesture recognizers).
- Draw custom content using Core Graphics or UIKit classes.
- Support drag and drop interactions.
- Respond to focus changes.
- Animate the size, position, and appearance attributes of the view.

[`UIView`](/documentation/UIKit/UIView) is the root class for all views and defines their common behavior. [`UIControl`](/documentation/UIKit/UIControl) defines additional behaviors that are specific to buttons, switches, and other views designed for user interactions.

For additional information about how to use views and controls, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/components/all-components). To see examples of UIKit controls, see [UIKit Catalog: Creating and customizing views and controls](/documentation/UIKit/uikit-catalog-creating-and-customizing-views-and-controls).

## Topics

### View fundamentals

[`UIView`](/documentation/UIKit/UIView)

An object that manages the content for a rectangular area on the screen.

[UIKit Catalog: Creating and customizing views and controls](/documentation/UIKit/uikit-catalog-creating-and-customizing-views-and-controls)

Customize your app’s user interface with views and controls.

### Container views

Organize and present large data sets using container views.

  <doc://com.apple.documentation/documentation/Xcode/autosizing-views-for-localization-in-ios>

[Collection views](/documentation/UIKit/collection-views)

Display nested views using a configurable and highly customizable layout.

[Table views](/documentation/UIKit/table-views)

Display data in a single column of customizable rows.

[`UIStackView`](/documentation/UIKit/UIStackView)

A streamlined interface for laying out a collection of views in either a column or a row.

[`UIScrollView`](/documentation/UIKit/UIScrollView)

A view that allows the scrolling and zooming of its contained views.

### Content views

[`UIActivityIndicatorView`](/documentation/UIKit/UIActivityIndicatorView)

A view that shows that a task is in progress.

[`UICalendarView`](/documentation/UIKit/UICalendarView)

A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.

[`UIContentUnavailableView`](/documentation/UIKit/UIContentUnavailableView)

A view that indicates there’s no content to display.

[`UIImageView`](/documentation/UIKit/UIImageView)

A view that displays a single image or a sequence of animated images in your interface.

[`UIPickerView`](/documentation/UIKit/UIPickerView)

A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.

[`UIProgressView`](/documentation/UIKit/UIProgressView)

A view that depicts the progress of a task over time.

### Controls

Gather input and respond to user interactions with controls.

[Responding to control-based events using target-action](/documentation/UIKit/responding-to-control-based-events-using-target-action)

Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.

[`UIControl`](/documentation/UIKit/UIControl)

The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.

[`UIButton`](/documentation/UIKit/UIButton)

A control that executes your custom code in response to user interactions.

[`UIColorWell`](/documentation/UIKit/UIColorWell)

A control that displays a color picker.

[`UIDatePicker`](/documentation/UIKit/UIDatePicker)

A control for inputting date and time values.

[`UIPageControl`](/documentation/UIKit/UIPageControl)

A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.

[`UISegmentedControl`](/documentation/UIKit/UISegmentedControl)

A horizontal control that consists of multiple segments, each segment functioning as a discrete button.

[`UISlider`](/documentation/UIKit/UISlider)

A control for selecting a single value from a continuous range of values.

[`UIStepper`](/documentation/UIKit/UIStepper)

A control for incrementing or decrementing a value.

[`UISwitch`](/documentation/UIKit/UISwitch)

A control that offers a binary choice, such as on/off.

### Text views

Display and edit text using text views.

[`UILabel`](/documentation/UIKit/UILabel)

A view that displays one or more lines of informational text.

[`UITextField`](/documentation/UIKit/UITextField)

An object that displays an editable text area in your interface.

[`UITextView`](/documentation/UIKit/UITextView)

A scrollable, multiline text region.

[Drag and drop customization](/documentation/UIKit/drag-and-drop-customization)

Extend the standard drag and drop support for text views to include custom types of content.

### Search field

[`UISearchTextField`](/documentation/UIKit/UISearchTextField)

A view for displaying and editing text and search tokens.

[`UISearchToken`](/documentation/UIKit/UISearchToken)

Search criteria in a search text field, represented by text and an optional icon.

[`UISearchTextFieldDelegate`](/documentation/UIKit/UISearchTextFieldDelegate)

The interface for the delegate of a search field.

### Visual effects

[`UIVisualEffect`](/documentation/UIKit/UIVisualEffect)

An initializer for visual effect views and blur and vibrancy effect objects.

[`UIVisualEffectView`](/documentation/UIKit/UIVisualEffectView)

An object that implements some complex visual effects.

[`UIVibrancyEffect`](/documentation/UIKit/UIVibrancyEffect)

An object that amplifies and adjusts the color of the content layered behind a visual effect view.

[`UIBlurEffect`](/documentation/UIKit/UIBlurEffect)

An object that applies a blurring effect to the content layered behind a visual effect view.

### Bars

Manage the items displayed on navigation bars, tab bars, search bars, and toolbars.

[`UIBarItem`](/documentation/UIKit/UIBarItem)

An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.

[`UIBarButtonItem`](/documentation/UIKit/UIBarButtonItem)

A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.

[`UIBarButtonItemGroup`](/documentation/UIKit/UIBarButtonItemGroup)

A group of one or more bar button items for placement on a navigation bar or shortcuts bar.

[`UINavigationBar`](/documentation/UIKit/UINavigationBar)

Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.

[`UISearchBar`](/documentation/UIKit/UISearchBar)

A specialized view for receiving search-related information from the user.

[`UIToolbar`](/documentation/UIKit/UIToolbar)

A control that displays one or more buttons along an edge of your interface.

[`UITabBar`](/documentation/UIKit/UITabBar)

A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.

[`UITabBarItem`](/documentation/UIKit/UITabBarItem)

An object that describes an item in a tab bar.

[`UIBarPositioning`](/documentation/UIKit/UIBarPositioning)

A set of methods for defining the positioning of bars in iOS apps.

[`UIBarPositioningDelegate`](/documentation/UIKit/UIBarPositioningDelegate)

A set of methods that support the positioning of a bar that conforms to the [`UIBarPositioning`](/documentation/UIKit/UIBarPositioning) protocol.

### Content viewer

[`UILargeContentViewerInteraction`](/documentation/UIKit/UILargeContentViewerInteraction)

An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.

[`UILargeContentViewerInteractionDelegate`](/documentation/UIKit/UILargeContentViewerInteractionDelegate)

An object that customizes the behavior of the large content viewer interactions.

[`UILargeContentViewerItem`](/documentation/UIKit/UILargeContentViewerItem)

Methods that provide details about how to display your custom content in the large content viewer.

### Private Click Measurement (PCM)

[`UIEventAttributionView`](/documentation/UIKit/UIEventAttributionView)

An overlay view that verifies user interaction for Web AdAttributionKit.

[`UIEventAttribution`](/documentation/UIKit/UIEventAttribution)

An object that contains event attribution information for Web AdAttributionKit.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint>

### SwiftUI

[Using SwiftUI with UIKit](/documentation/UIKit/using-swiftui-with-uikit)

Learn how to incorporate SwiftUI views into a UIKit app.

### Related types

[`UIOffset`](/documentation/UIKit/UIOffset)

A structure that specifies an amount to offset a position.

[`UIAxis`](/documentation/UIKit/UIAxis)

A structure that specifies the layout axes.

[`UIEdgeInsets`](/documentation/UIKit/UIEdgeInsets)

The inset distances for views.

[`NSDirectionalEdgeInsets`](/documentation/UIKit/NSDirectionalEdgeInsets)

The inset distances for views, taking the user interface layout direction into account.

[`NSDirectionalRectEdge`](/documentation/UIKit/NSDirectionalRectEdge)

Constants that specify an edge or a set of edges, taking the user interface layout direction into account.

[`NSRectAlignment`](/documentation/UIKit/NSRectAlignment)

Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.

[UIKit macros](/documentation/UIKit/uikit-macros)

Macros that UIKit defines.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
