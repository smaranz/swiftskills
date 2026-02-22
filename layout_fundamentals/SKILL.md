---
name: Layout fundamentals
description: Rork-Max Quality skill for Layout fundamentals. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Layout fundamentals


## 🚀 Rork-Max Quality Snippet


```swift
import SwiftUI

struct EliteLayout: View {
    var body: some View {
        Grid(alignment: .leading, horizontalSpacing: 20, verticalSpacing: 20) {
            GridRow {
                Color.blue.frame(height: 100).cornerRadius(12)
                Color.purple.frame(height: 100).cornerRadius(12)
            }
            GridRow {
                Color.teal.frame(height: 100).cornerRadius(12)
                    .gridCellColumns(2)
            }
        }
        .padding()
    }
}
```


## 💎 Elite Implementation Tips

- Use Apple's standard 8pt/16pt/24pt spacing tokens for consistent rhythm.\n- Leverage `Grid` and `GridRow` (iOS 16+) for precise control over complex layouts.\n- Ensure all corners have a radius between 12 and 25 for a modern 'squircle' feel.


## Documentation

# Layout fundamentals

Arrange views inside built-in layout containers like stacks and grids.

## Overview

Use layout containers to arrange the elements of your user interface.
Stacks and grids update and adjust the positions of the subviews they
contain in response to changes in content or interface dimensions.
You can nest layout containers inside other layout containers to any depth
to achieve complex layout effects.

![](images/com.apple.SwiftUI/layout-fundamentals-hero@2x.png)

To fine-tune the position, alignment, and other elements of a layout that you
build with layout container views, see [Layout adjustments](/documentation/SwiftUI/Layout-adjustments). To define
custom layout containers, see [Custom layout](/documentation/SwiftUI/Custom-layout).
For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/layout>
in the Human Interface Guidelines.

## Topics

### Choosing a layout

[Picking container views for your content](/documentation/SwiftUI/Picking-Container-Views-for-Your-Content)

Build flexible user interfaces by using stacks, grids, lists, and forms.

### Statically arranging views in one dimension

[Building layouts with stack views](/documentation/SwiftUI/Building-Layouts-with-Stack-Views)

Compose complex layouts from primitive container views.

[`HStack`](/documentation/SwiftUI/HStack)

A view that arranges its subviews in a horizontal line.

[`VStack`](/documentation/SwiftUI/VStack)

A view that arranges its subviews in a vertical line.

### Dynamically arranging views in one dimension

[Grouping data with lazy stack views](/documentation/SwiftUI/Grouping-Data-with-Lazy-Stack-Views)

Split content into logical sections inside lazy stack views.

[Creating performant scrollable stacks](/documentation/SwiftUI/Creating-Performant-Scrollable-Stacks)

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

[`LazyHStack`](/documentation/SwiftUI/LazyHStack)

A view that arranges its children in a line that grows horizontally,
creating items only as needed.

[`LazyVStack`](/documentation/SwiftUI/LazyVStack)

A view that arranges its children in a line that grows vertically,
creating items only as needed.

[`PinnedScrollableViews`](/documentation/SwiftUI/PinnedScrollableViews)

A set of view types that may be pinned to the bounds of a scroll view.

### Statically arranging views in two dimensions

[`Grid`](/documentation/SwiftUI/Grid)

A container view that arranges other views in a two dimensional layout.

[`GridRow`](/documentation/SwiftUI/GridRow)

A horizontal row in a two dimensional grid container.

[`gridCellColumns(_:)`](/documentation/SwiftUI/View/gridCellColumns(_:))

Tells a view that acts as a cell in a grid to span the specified
number of columns.

[`gridCellAnchor(_:)`](/documentation/SwiftUI/View/gridCellAnchor(_:))

Specifies a custom alignment anchor for a view that acts as a grid cell.

[`gridCellUnsizedAxes(_:)`](/documentation/SwiftUI/View/gridCellUnsizedAxes(_:))

Asks grid layouts not to offer the view extra size in the specified
axes.

[`gridColumnAlignment(_:)`](/documentation/SwiftUI/View/gridColumnAlignment(_:))

Overrides the default horizontal alignment of the grid column that
the view appears in.

### Dynamically arranging views in two dimensions

[`LazyHGrid`](/documentation/SwiftUI/LazyHGrid)

A container view that arranges its child views in a grid that
grows horizontally, creating items only as needed.

[`LazyVGrid`](/documentation/SwiftUI/LazyVGrid)

A container view that arranges its child views in a grid that
grows vertically, creating items only as needed.

[`GridItem`](/documentation/SwiftUI/GridItem)

A description of a row or a column in a lazy grid.

### Layering views

[Adding a background to your view](/documentation/SwiftUI/Adding-a-Background-to-Your-View)

Compose a background behind your view and extend it beyond the safe area insets.

[`ZStack`](/documentation/SwiftUI/ZStack)

A view that overlays its subviews, aligning them in both axes.

[`zIndex(_:)`](/documentation/SwiftUI/View/zIndex(_:))

Controls the display order of overlapping views.

[`background(alignment:content:)`](/documentation/SwiftUI/View/background(alignment:content:))

Layers the views that you specify behind this view.

[`background(_:ignoresSafeAreaEdges:)`](/documentation/SwiftUI/View/background(_:ignoresSafeAreaEdges:))

Sets the view’s background to a style.

[`background(ignoresSafeAreaEdges:)`](/documentation/SwiftUI/View/background(ignoresSafeAreaEdges:))

Sets the view’s background to the default background style.

[`background(_:in:fillStyle:)`](/documentation/SwiftUI/View/background(_:in:fillStyle:))

Sets the view’s background to an insettable shape filled with a style.

[`background(in:fillStyle:)`](/documentation/SwiftUI/View/background(in:fillStyle:))

Sets the view’s background to an insettable shape filled with the
default background style.

[`overlay(alignment:content:)`](/documentation/SwiftUI/View/overlay(alignment:content:))

Layers the views that you specify in front of this view.

[`overlay(_:ignoresSafeAreaEdges:)`](/documentation/SwiftUI/View/overlay(_:ignoresSafeAreaEdges:))

Layers the specified style in front of this view.

[`overlay(_:in:fillStyle:)`](/documentation/SwiftUI/View/overlay(_:in:fillStyle:))

Layers a shape that you specify in front of this view.

[`backgroundMaterial`](/documentation/SwiftUI/EnvironmentValues/backgroundMaterial)

The material underneath the current view.

[`containerBackground(_:for:)`](/documentation/SwiftUI/View/containerBackground(_:for:))

Sets the container background of the enclosing container using a view.

[`containerBackground(for:alignment:content:)`](/documentation/SwiftUI/View/containerBackground(for:alignment:content:))

Sets the container background of the enclosing container using a view.

[`ContainerBackgroundPlacement`](/documentation/SwiftUI/ContainerBackgroundPlacement)

The placement of a container background.

### Automatically choosing the layout that fits

[`ViewThatFits`](/documentation/SwiftUI/ViewThatFits)

A view that adapts to the available space by providing the first
child view that fits.

### Separators

[`Spacer`](/documentation/SwiftUI/Spacer)

A flexible space that expands along the major axis of its containing stack
layout, or on both axes if not contained in a stack.

[`Divider`](/documentation/SwiftUI/Divider)

A visual element that can be used to separate other content.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
