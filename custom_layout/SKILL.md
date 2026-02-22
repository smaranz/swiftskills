---
name: Custom layout
description: Rork-Max Quality skill for Custom layout. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Custom layout


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Custom layout

Place views in custom arrangements and create animated transitions between layout types.

## Overview

You can create complex view layouts using the built-in layout containers and
layout view modifiers that SwiftUI provides. However, if you need behavior
that you can’t achieve with the built-in layout tools, create a custom
layout container type using the [`Layout`](/documentation/SwiftUI/Layout) protocol. A container that you
define asks for the sizes of all its subviews, and then indicates where to place
the subviews within its own bounds.

![](images/com.apple.SwiftUI/custom-layout-hero@2x.png)

You can also create animated transitions among layout types that conform
to the [`Layout`](/documentation/SwiftUI/Layout) procotol, including both built-in and custom layouts.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/layout>
in the Human Interface Guidelines.

## Topics

### Creating a custom layout container

[Composing custom layouts with SwiftUI](/documentation/SwiftUI/composing-custom-layouts-with-swiftui)

Arrange views in your app’s interface using layout tools that SwiftUI provides.

[`Layout`](/documentation/SwiftUI/Layout)

A type that defines the geometry of a collection of views.

[`LayoutSubview`](/documentation/SwiftUI/LayoutSubview)

A proxy that represents one subview of a layout.

[`LayoutSubviews`](/documentation/SwiftUI/LayoutSubviews)

A collection of proxy values that represent the subviews of a layout view.

### Configuring a custom layout

[`LayoutProperties`](/documentation/SwiftUI/LayoutProperties)

Layout-specific properties of a layout container.

[`ProposedViewSize`](/documentation/SwiftUI/ProposedViewSize)

A proposal for the size of a view.

[`ViewSpacing`](/documentation/SwiftUI/ViewSpacing)

A collection of the geometric spacing preferences of a view.

### Associating values with views in a custom layout

[`layoutValue(key:value:)`](/documentation/SwiftUI/View/layoutValue(key:value:))

Associates a value with a custom layout property.

[`LayoutValueKey`](/documentation/SwiftUI/LayoutValueKey)

A key for accessing a layout value of a layout container’s subviews.

### Transitioning between layout types

[`AnyLayout`](/documentation/SwiftUI/AnyLayout)

A type-erased instance of the layout protocol.

[`HStackLayout`](/documentation/SwiftUI/HStackLayout)

A horizontal container that you can use in conditional layouts.

[`VStackLayout`](/documentation/SwiftUI/VStackLayout)

A vertical container that you can use in conditional layouts.

[`ZStackLayout`](/documentation/SwiftUI/ZStackLayout)

An overlaying container that you can use in conditional layouts.

[`GridLayout`](/documentation/SwiftUI/GridLayout)

A grid that you can use in conditional layouts.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
