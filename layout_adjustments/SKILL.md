---
name: Layout adjustments
description: Rork-Max Quality skill for Layout adjustments. Actionable patterns and best practices for SwiftUI development.
---

# Layout adjustments

Make fine adjustments to alignment, spacing, padding, and other layout parameters.
Layout containers like stacks and grids provide a great starting point for
arranging views in your app’s user interface. When you need to make fine
adjustments, use layout view modifiers. You can adjust or constrain the size,
position, and alignment of a view. You can also add padding around a view,
and indicate how the view interacts with system-defined safe areas.
To get started with a basic layout, see Layout fundamentals.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Arranging views in stacks, grids, or custom layout containers
- Building responsive layouts that adapt to different screen sizes
- Creating scrollable lists, tables, or collection-style interfaces
- Implementing custom layout algorithms with the `Layout` protocol

## Best Practices

- Use `LazyVStack`/`LazyHStack` inside `ScrollView` for large data sets
- Prefer `Grid` (iOS 16+) over nested stacks for tabular 2D layouts
- Use `ViewThatFits` to automatically choose between layout variants
- Apply `.frame(maxWidth: .infinity)` for full-width sections rather than hard-coding widths

## Common Pitfalls

- Putting `LazyVStack` without a `ScrollView` — it won't scroll
- Using `List` when you want custom styling — `LazyVStack` gives more control
- Nesting `ScrollView`s in the same axis causes confusing scroll behavior
- Forgetting `.listRowInsets(EdgeInsets())` when you want edge-to-edge list content

## Key APIs

### Fine-tuning a layout

| API | Purpose |
|-----|---------|
| `Laying out a simple view` | Create a view layout by adjusting the size of views. |
| `Inspecting view layout` | Determine the position and extent of a view using Xcode previews or |

### Adding padding around a view

| API | Purpose |
|-----|---------|
| `padding(_:)` | Adds a different padding amount to each edge of this view. |
| `padding(_:_:)` | Adds an equal padding amount to specific edges of this view. |
| `padding3D(_:)` | Pads this view using the edge insets you specify. |
| `padding3D(_:_:)` | Pads this view using the edge insets you specify. |
| `scenePadding(_:)` | Adds padding to the specified edges of this view using an amount that’s |
| `scenePadding(_:edges:)` | Adds a specified kind of padding to the specified edges of this view |
| `ScenePadding` | The padding used to space a view from its containing scene. |

### Influencing a view’s size

| API | Purpose |
|-----|---------|
| `frame(width:height:alignment:)` | Positions this view within an invisible frame with the specified size. |
| `frame(depth:alignment:)` | Positions this view within an invisible frame with the specified depth. |
| `frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)` | Positions this view within an invisible frame having the specified size |
| `frame(minDepth:idealDepth:maxDepth:alignment:)` | Positions this view within an invisible frame having the specified depth |
| `containerRelativeFrame(_:alignment:)` | Positions this view within an invisible frame with a size relative |
| `containerRelativeFrame(_:alignment:_:)` | Positions this view within an invisible frame with a size relative |
| `containerRelativeFrame(_:count:span:spacing:alignment:)` | Positions this view within an invisible frame with a size relative |
| `fixedSize()` | Fixes this view at its ideal size. |

### Adjusting a view’s position

| API | Purpose |
|-----|---------|
| `Making fine adjustments to a view’s position` | Shift the position of a view by applying the offset or position modifier. |
| `position(_:)` | Positions the center of this view at the specified point in its parent’s |
| `position(x:y:)` | Positions the center of this view at the specified coordinates in its |
| `offset(_:)` | Offset this view by the horizontal and vertical amount specified in the |
| `offset(x:y:)` | Offset this view by the specified horizontal and vertical distances. |
| `offset(z:)` | Brings a view forward in Z by the provided distance in points. |

### Aligning views

| API | Purpose |
|-----|---------|
| `Aligning views within a stack` | Position views inside a stack using alignment guides. |
| `Aligning views across stacks` | Create a custom alignment and use it to align views across multiple stacks. |
| `alignmentGuide(_:computeValue:)` | Sets the view’s horizontal alignment. |
| `Alignment` | An alignment in both axes. |
| `HorizontalAlignment` | An alignment position along the horizontal axis. |
| `VerticalAlignment` | An alignment position along the vertical axis. |
| `DepthAlignment` | An alignment position along the depth axis. |
| `AlignmentID` | A type that you use to create custom alignment guides. |

### Setting margins

| API | Purpose |
|-----|---------|
| `contentMargins(_:for:)` | Configures the content margin for a provided placement. |
| `contentMargins(_:_:for:)` | Configures the content margin for a provided placement. |
| `ContentMarginPlacement` | The placement of margins. |

### Staying in the safe areas

| API | Purpose |
|-----|---------|
| `ignoresSafeArea(_:edges:)` | Expands the safe area of a view. |
| `safeAreaInset(edge:alignment:spacing:content:)` | Shows the specified content beside the modified view. |
| `safeAreaPadding(_:)` | Adds the provided insets into the safe area of this view. |
| `safeAreaPadding(_:_:)` | Adds the provided insets into the safe area of this view. |
| `SafeAreaRegions` | A set of symbolic safe area regions. |

### Setting a layout direction

| API | Purpose |
|-----|---------|
| `layoutDirectionBehavior(_:)` | Sets the behavior of this view for different layout directions. |
| `LayoutDirectionBehavior` | A description of what should happen when the layout direction changes. |
| `layoutDirection` | The layout direction associated with the current environment. |
| `LayoutDirection` | A direction in which SwiftUI can lay out content. |

### Reacting to interface characteristics

| API | Purpose |
|-----|---------|
| `isLuminanceReduced` | A Boolean value that indicates whether the display or environment currently requires |
| `displayScale` | The display scale of this environment. |
| `pixelLength` | The size of a pixel on the screen. |
| `horizontalSizeClass` | The horizontal size class of this environment. |
| `verticalSizeClass` | The vertical size class of this environment. |
| `UserInterfaceSizeClass` | A set of values that indicate the visual size available to the view. |

### Accessing edges, regions, and layouts

| API | Purpose |
|-----|---------|
| `Edge` | An enumeration to indicate one edge of a rectangle. |
| `Edge3D` | An edge or face of a 3D volume. |
| `HorizontalEdge` | An edge on the horizontal axis. |
| `VerticalEdge` | An edge on the vertical axis. |
| `EdgeInsets` | The inset distances for the sides of a rectangle. |
| `EdgeInsets3D` | The inset distances for the faces of a 3D volume. |
