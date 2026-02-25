---
name: Layout fundamentals
description: Rork-Max Quality skill for Layout fundamentals. Actionable patterns and best practices for SwiftUI development.
---

# Layout fundamentals

Arrange views inside built-in layout containers like stacks and grids.
Use layout containers to arrange the elements of your user interface.
Stacks and grids update and adjust the positions of the subviews they
contain in response to changes in content or interface dimensions.
You can nest layout containers inside other layout containers to any depth
to achieve complex layout effects.
To fine-tune the position, alignment, and other elements of a layout that you
build with layout container views, see Layout adjustments. To define
custom layout containers, see Custom layout.
For design guidance, see
in the Human Interface Guidelines.


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

- Use Apple's standard 8pt/16pt/24pt spacing tokens for consistent rhythm.
- Leverage `Grid` and `GridRow` (iOS 16+) for precise control over complex layouts.
- Ensure all corners have a radius between 12 and 25 for a modern 'squircle' feel.


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

### Choosing a layout

| API | Purpose |
|-----|---------|
| `Picking container views for your content` | Build flexible user interfaces by using stacks, grids, lists, and forms. |

### Statically arranging views in one dimension

| API | Purpose |
|-----|---------|
| `Building layouts with stack views` | Compose complex layouts from primitive container views. |
| `HStack` | A view that arranges its subviews in a horizontal line. |
| `VStack` | A view that arranges its subviews in a vertical line. |

### Dynamically arranging views in one dimension

| API | Purpose |
|-----|---------|
| `Grouping data with lazy stack views` | Split content into logical sections inside lazy stack views. |
| `Creating performant scrollable stacks` | Display large numbers of repeated views efficiently with scroll views, stack |
| `LazyHStack` | A view that arranges its children in a line that grows horizontally, |
| `LazyVStack` | A view that arranges its children in a line that grows vertically, |
| `PinnedScrollableViews` | A set of view types that may be pinned to the bounds of a scroll view. |

### Statically arranging views in two dimensions

| API | Purpose |
|-----|---------|
| `Grid` | A container view that arranges other views in a two dimensional layout. |
| `GridRow` | A horizontal row in a two dimensional grid container. |
| `gridCellColumns(_:)` | Tells a view that acts as a cell in a grid to span the specified |
| `gridCellAnchor(_:)` | Specifies a custom alignment anchor for a view that acts as a grid cell. |
| `gridCellUnsizedAxes(_:)` | Asks grid layouts not to offer the view extra size in the specified |
| `gridColumnAlignment(_:)` | Overrides the default horizontal alignment of the grid column that |

### Dynamically arranging views in two dimensions

| API | Purpose |
|-----|---------|
| `LazyHGrid` | A container view that arranges its child views in a grid that |
| `LazyVGrid` | A container view that arranges its child views in a grid that |
| `GridItem` | A description of a row or a column in a lazy grid. |

### Layering views

| API | Purpose |
|-----|---------|
| `Adding a background to your view` | Compose a background behind your view and extend it beyond the safe area insets. |
| `ZStack` | A view that overlays its subviews, aligning them in both axes. |
| `zIndex(_:)` | Controls the display order of overlapping views. |
| `background(alignment:content:)` | Layers the views that you specify behind this view. |
| `background(_:ignoresSafeAreaEdges:)` | Sets the view’s background to a style. |
| `background(ignoresSafeAreaEdges:)` | Sets the view’s background to the default background style. |
| `background(_:in:fillStyle:)` | Sets the view’s background to an insettable shape filled with a style. |
| `background(in:fillStyle:)` | Sets the view’s background to an insettable shape filled with the |

### Automatically choosing the layout that fits

| API | Purpose |
|-----|---------|
| `ViewThatFits` | A view that adapts to the available space by providing the first |

### Separators

| API | Purpose |
|-----|---------|
| `Spacer` | A flexible space that expands along the major axis of its containing stack |
| `Divider` | A visual element that can be used to separate other content. |
