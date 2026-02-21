---
name: IOS View layout
description: Apple UIKit Documentation for IOS View layout on ios.
---

# View layout

Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

## Discussion

When you design your app’s interface, you position views and other interface elements in your app’s windows and size them appropriately. However, the size and position of those views may need to change at runtime for a variety of reasons:

- The user can resize the window containing your views.
- Variations in the screen sizes of iOS devices (including differences between portrait and landscape orientations) require different layouts for each device and orientation.
- Apps on iPad must adapt to cover different amounts of screen space, ranging from a third of the screen to the entire screen.
- Language changes might require size changes for labels and other text-based views.
- Dynamic Type allows changes to the size of the text, which affects the size of the view.

[`UIStackView`](/documentation/UIKit/UIStackView) objects adjust the position of their contained views automatically when interface dimensions change. Alternatively, Auto Layout constraints let you specify the rules that determine the size and position of the views in your interface.

## Topics

### Essentials

[`UIStackView`](/documentation/UIKit/UIStackView)

A streamlined interface for laying out a collection of views in either a column or a row.

### Localization

  <doc://com.apple.documentation/documentation/Xcode/autosizing-views-for-localization-in-ios>

### Constraints

[Positioning content within layout margins](/documentation/UIKit/positioning-content-within-layout-margins)

Position views so that they aren’t crowded by other content.

[Positioning content relative to the safe area](/documentation/UIKit/positioning-content-relative-to-the-safe-area)

Position views so that they aren’t obstructed by other content.

[`NSLayoutConstraint`](/documentation/UIKit/NSLayoutConstraint)

The relationship between two user interface objects that must be satisfied by the constraint-based layout system.

[`UILayoutSupport`](/documentation/UIKit/UILayoutSupport)

A set of methods that provide layout support and access to layout anchors.

[`NSDictionaryOfVariableBindings`](/documentation/UIKit/NSDictionaryOfVariableBindings)

Creates a dictionary wherein the keys are string representations of the corresponding values’ variable names.

### Layout guides

[`UILayoutGuide`](/documentation/UIKit/UILayoutGuide)

A rectangular area that can interact with Auto Layout.

[`NSLayoutDimension`](/documentation/UIKit/NSLayoutDimension)

A factory class for creating size-based layout constraint objects using a fluent API.

### Anchors

[`NSLayoutAnchor`](/documentation/UIKit/NSLayoutAnchor)

A factory class for creating layout constraint objects using a fluent API.

[`NSLayoutXAxisAnchor`](/documentation/UIKit/NSLayoutXAxisAnchor)

A factory class for creating horizontal layout constraint objects using a fluent API.

[`NSLayoutYAxisAnchor`](/documentation/UIKit/NSLayoutYAxisAnchor)

A factory class for creating vertical layout constraint objects using a fluent API.

### Anchors

[`NSLayoutAnchor`](/documentation/UIKit/NSLayoutAnchor)

A factory class for creating layout constraint objects using a fluent API.

[`NSLayoutXAxisAnchor`](/documentation/UIKit/NSLayoutXAxisAnchor)

A factory class for creating horizontal layout constraint objects using a fluent API.

[`NSLayoutYAxisAnchor`](/documentation/UIKit/NSLayoutYAxisAnchor)

A factory class for creating vertical layout constraint objects using a fluent API.

[`NSLAYOUTANCHOR_H`](/documentation/UIKit/NSLAYOUTANCHOR_H)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
