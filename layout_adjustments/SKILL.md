---
name: Layout adjustments
description: Apple SwiftUI Documentation for Layout adjustments.
---

# Layout adjustments

Make fine adjustments to alignment, spacing, padding, and other layout parameters.

## Overview

Layout containers like stacks and grids provide a great starting point for
arranging views in your app’s user interface. When you need to make fine
adjustments, use layout view modifiers. You can adjust or constrain the size,
position, and alignment of a view. You can also add padding around a view,
and indicate how the view interacts with system-defined safe areas.

![](images/com.apple.SwiftUI/layout-adjustments-hero@2x.png)

To get started with a basic layout, see [Layout fundamentals](/documentation/SwiftUI/Layout-fundamentals).
For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/layout>
in the Human Interface Guidelines.

## Topics

### Fine-tuning a layout

[Laying out a simple view](/documentation/SwiftUI/Laying-Out-a-Simple-View)

Create a view layout by adjusting the size of views.

[Inspecting view layout](/documentation/SwiftUI/Inspecting-View-Layout)

Determine the position and extent of a view using Xcode previews or
by adding temporary borders.

### Adding padding around a view

[`padding(_:)`](/documentation/SwiftUI/View/padding(_:))

Adds a different padding amount to each edge of this view.

[`padding(_:_:)`](/documentation/SwiftUI/View/padding(_:_:))

Adds an equal padding amount to specific edges of this view.

[`padding3D(_:)`](/documentation/SwiftUI/View/padding3D(_:))

Pads this view using the edge insets you specify.

[`padding3D(_:_:)`](/documentation/SwiftUI/View/padding3D(_:_:))

Pads this view using the edge insets you specify.

[`scenePadding(_:)`](/documentation/SwiftUI/View/scenePadding(_:))

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

[`scenePadding(_:edges:)`](/documentation/SwiftUI/View/scenePadding(_:edges:))

Adds a specified kind of padding to the specified edges of this view
using an amount that’s appropriate for the current scene.

[`ScenePadding`](/documentation/SwiftUI/ScenePadding)

The padding used to space a view from its containing scene.

### Influencing a view’s size

[`frame(width:height:alignment:)`](/documentation/SwiftUI/View/frame(width:height:alignment:))

Positions this view within an invisible frame with the specified size.

[`frame(depth:alignment:)`](/documentation/SwiftUI/View/frame(depth:alignment:))

Positions this view within an invisible frame with the specified depth.

[`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`](/documentation/SwiftUI/View/frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:))

Positions this view within an invisible frame having the specified size
constraints.

[`frame(minDepth:idealDepth:maxDepth:alignment:)`](/documentation/SwiftUI/View/frame(minDepth:idealDepth:maxDepth:alignment:))

Positions this view within an invisible frame having the specified depth
constraints.

[`containerRelativeFrame(_:alignment:)`](/documentation/SwiftUI/View/containerRelativeFrame(_:alignment:))

Positions this view within an invisible frame with a size relative
to the nearest container.

[`containerRelativeFrame(_:alignment:_:)`](/documentation/SwiftUI/View/containerRelativeFrame(_:alignment:_:))

Positions this view within an invisible frame with a size relative
to the nearest container.

[`containerRelativeFrame(_:count:span:spacing:alignment:)`](/documentation/SwiftUI/View/containerRelativeFrame(_:count:span:spacing:alignment:))

Positions this view within an invisible frame with a size relative
to the nearest container.

[`fixedSize()`](/documentation/SwiftUI/View/fixedSize())

Fixes this view at its ideal size.

[`fixedSize(horizontal:vertical:)`](/documentation/SwiftUI/View/fixedSize(horizontal:vertical:))

Fixes this view at its ideal size in the specified dimensions.

[`layoutPriority(_:)`](/documentation/SwiftUI/View/layoutPriority(_:))

Sets the priority by which a parent layout should apportion space to
this child.

### Adjusting a view’s position

[Making fine adjustments to a view’s position](/documentation/SwiftUI/Making-Fine-Adjustments-to-a-View-s-Position)

Shift the position of a view by applying the offset or position modifier.

[`position(_:)`](/documentation/SwiftUI/View/position(_:))

Positions the center of this view at the specified point in its parent’s
coordinate space.

[`position(x:y:)`](/documentation/SwiftUI/View/position(x:y:))

Positions the center of this view at the specified coordinates in its
parent’s coordinate space.

[`offset(_:)`](/documentation/SwiftUI/View/offset(_:))

Offset this view by the horizontal and vertical amount specified in the
offset parameter.

[`offset(x:y:)`](/documentation/SwiftUI/View/offset(x:y:))

Offset this view by the specified horizontal and vertical distances.

[`offset(z:)`](/documentation/SwiftUI/View/offset(z:))

Brings a view forward in Z by the provided distance in points.

### Aligning views

[Aligning views within a stack](/documentation/SwiftUI/Aligning-Views-Within-a-Stack)

Position views inside a stack using alignment guides.

[Aligning views across stacks](/documentation/SwiftUI/Aligning-Views-Across-Stacks)

Create a custom alignment and use it to align views across multiple stacks.

[`alignmentGuide(_:computeValue:)`](/documentation/SwiftUI/View/alignmentGuide(_:computeValue:))

Sets the view’s horizontal alignment.

[`Alignment`](/documentation/SwiftUI/Alignment)

An alignment in both axes.

[`HorizontalAlignment`](/documentation/SwiftUI/HorizontalAlignment)

An alignment position along the horizontal axis.

[`VerticalAlignment`](/documentation/SwiftUI/VerticalAlignment)

An alignment position along the vertical axis.

[`DepthAlignment`](/documentation/SwiftUI/DepthAlignment)

An alignment position along the depth axis.

[`AlignmentID`](/documentation/SwiftUI/AlignmentID)

A type that you use to create custom alignment guides.

[`ViewDimensions`](/documentation/SwiftUI/ViewDimensions)

A view’s size and alignment guides in its own coordinate space.

[`ViewDimensions3D`](/documentation/SwiftUI/ViewDimensions3D)

A view’s 3D size and alignment guides in its own coordinate space.

[`SpatialContainer`](/documentation/SwiftUI/SpatialContainer)

A layout container that aligns overlapping content in 3D space.

### Setting margins

[`contentMargins(_:for:)`](/documentation/SwiftUI/View/contentMargins(_:for:))

Configures the content margin for a provided placement.

[`contentMargins(_:_:for:)`](/documentation/SwiftUI/View/contentMargins(_:_:for:))

Configures the content margin for a provided placement.

[`ContentMarginPlacement`](/documentation/SwiftUI/ContentMarginPlacement)

The placement of margins.

### Staying in the safe areas

[`ignoresSafeArea(_:edges:)`](/documentation/SwiftUI/View/ignoresSafeArea(_:edges:))

Expands the safe area of a view.

[`safeAreaInset(edge:alignment:spacing:content:)`](/documentation/SwiftUI/View/safeAreaInset(edge:alignment:spacing:content:))

Shows the specified content beside the modified view.

[`safeAreaPadding(_:)`](/documentation/SwiftUI/View/safeAreaPadding(_:))

Adds the provided insets into the safe area of this view.

[`safeAreaPadding(_:_:)`](/documentation/SwiftUI/View/safeAreaPadding(_:_:))

Adds the provided insets into the safe area of this view.

[`SafeAreaRegions`](/documentation/SwiftUI/SafeAreaRegions)

A set of symbolic safe area regions.

### Setting a layout direction

[`layoutDirectionBehavior(_:)`](/documentation/SwiftUI/View/layoutDirectionBehavior(_:))

Sets the behavior of this view for different layout directions.

[`LayoutDirectionBehavior`](/documentation/SwiftUI/LayoutDirectionBehavior)

A description of what should happen when the layout direction changes.

[`layoutDirection`](/documentation/SwiftUI/EnvironmentValues/layoutDirection)

The layout direction associated with the current environment.

[`LayoutDirection`](/documentation/SwiftUI/LayoutDirection)

A direction in which SwiftUI can lay out content.

[`LayoutRotationUnaryLayout`](/documentation/SwiftUI/LayoutRotationUnaryLayout)

### Reacting to interface characteristics

[`isLuminanceReduced`](/documentation/SwiftUI/EnvironmentValues/isLuminanceReduced)

A Boolean value that indicates whether the display or environment currently requires
reduced luminance.

[`displayScale`](/documentation/SwiftUI/EnvironmentValues/displayScale)

The display scale of this environment.

[`pixelLength`](/documentation/SwiftUI/EnvironmentValues/pixelLength)

The size of a pixel on the screen.

[`horizontalSizeClass`](/documentation/SwiftUI/EnvironmentValues/horizontalSizeClass)

The horizontal size class of this environment.

[`verticalSizeClass`](/documentation/SwiftUI/EnvironmentValues/verticalSizeClass)

The vertical size class of this environment.

[`UserInterfaceSizeClass`](/documentation/SwiftUI/UserInterfaceSizeClass)

A set of values that indicate the visual size available to the view.

### Accessing edges, regions, and layouts

[`Edge`](/documentation/SwiftUI/Edge)

An enumeration to indicate one edge of a rectangle.

[`Edge3D`](/documentation/SwiftUI/Edge3D)

An edge or face of a 3D volume.

[`HorizontalEdge`](/documentation/SwiftUI/HorizontalEdge)

An edge on the horizontal axis.

[`VerticalEdge`](/documentation/SwiftUI/VerticalEdge)

An edge on the vertical axis.

[`EdgeInsets`](/documentation/SwiftUI/EdgeInsets)

The inset distances for the sides of a rectangle.

[`EdgeInsets3D`](/documentation/SwiftUI/EdgeInsets3D)

The inset distances for the faces of a 3D volume.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
