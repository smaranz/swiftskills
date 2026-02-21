---
name: MACOS View Layout
description: Apple AppKit Documentation for MACOS View Layout on macos.
---

# View Layout

Position and size views using a stack view or Auto Layout constraints.

## Discussion

When you design your app’s interface, you position views and other interface elements in your app’s windows and size them appropriately. However, the size and position of those views may need to change at runtime for a few reasons:

- The user resizes the window containing your views.
- The user’s language choice requires size changes for labels and text-based views.

[`NSStackView`](/documentation/AppKit/NSStackView) objects adjust the position of their contained views automatically when interface dimensions change. Alternatively, Auto Layout constraints let you specify the rules that determine the precise size and position of the views in your interface

## Topics

### Stack View

[`NSStackView`](/documentation/AppKit/NSStackView)

A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes.

### Auto Layout Constraints

[`NSLayoutConstraint`](/documentation/AppKit/NSLayoutConstraint)

The relationship between two user interface objects that must be satisfied by the constraint-based layout system.

### Layout Guides

[`NSLayoutGuide`](/documentation/AppKit/NSLayoutGuide)

A rectangular area that can interact with Auto Layout.

[`NSLayoutDimension`](/documentation/AppKit/NSLayoutDimension)

A factory class for creating size-based layout constraint objects using a fluent API.

[`NSViewLayoutRegion`](/documentation/AppKit/NSViewLayoutRegion)

[`NSViewLayoutRegionAdaptivityAxis`](/documentation/AppKit/NSViewLayoutRegionAdaptivityAxis)

### Anchors

[`NSLayoutAnchor`](/documentation/AppKit/NSLayoutAnchor)

A factory class for creating layout constraint objects using a fluent API.

[`NSLayoutXAxisAnchor`](/documentation/AppKit/NSLayoutXAxisAnchor)

A factory class for creating horizontal layout constraint objects using a fluent API.

[`NSLayoutYAxisAnchor`](/documentation/AppKit/NSLayoutYAxisAnchor)

A factory class for creating vertical layout constraint objects using a fluent API.

### View Compression

[`NSDictionaryOfVariableBindings`](/documentation/AppKit/NSDictionaryOfVariableBindings)

Creates a dictionary wherein the keys are string representations of the corresponding values’ variable names.

[`NSUserInterfaceCompression`](/documentation/AppKit/NSUserInterfaceCompression)

A protocol that describes how a UI control should redisplay when space is restricted.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
