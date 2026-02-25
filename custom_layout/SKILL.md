---
name: Custom layout
description: Rork-Max Quality skill for Custom layout. Actionable patterns and best practices for SwiftUI development.
---

# Custom layout

Place views in custom arrangements and create animated transitions between layout types.
You can create complex view layouts using the built-in layout containers and
layout view modifiers that SwiftUI provides. However, if you need behavior
that you can’t achieve with the built-in layout tools, create a custom
layout container type using the `Layout` protocol. A container that you
define asks for the sizes of all its subviews, and then indicates where to place
the subviews within its own bounds.
You can also create animated transitions among layout types that conform
to the `Layout` procotol, including both built-in and custom layouts.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct FlowLayout: Layout {
    var spacing: CGFloat = 8

    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        var x: CGFloat = 0
        var y: CGFloat = 0
        var rowHeight: CGFloat = 0
        let maxWidth = proposal.width ?? .infinity

        for subview in subviews {
            let size = subview.sizeThatFits(.unspecified)
            if x + size.width > maxWidth && x > 0 {
                x = 0
                y += rowHeight + spacing
                rowHeight = 0
            }
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
        return CGSize(width: maxWidth, height: y + rowHeight)
    }

    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        var x = bounds.minX
        var y = bounds.minY
        var rowHeight: CGFloat = 0

        for subview in subviews {
            let size = subview.sizeThatFits(.unspecified)
            if x + size.width > bounds.maxX && x > bounds.minX {
                x = bounds.minX
                y += rowHeight + spacing
                rowHeight = 0
            }
            subview.place(at: CGPoint(x: x, y: y), proposal: .unspecified)
            x += size.width + spacing
            rowHeight = max(rowHeight, size.height)
        }
    }
}

// Usage: FlowLayout { ForEach(tags) { tag in TagView(tag) } }
```

## 💎 Elite Implementation Tips

- Implement the `Layout` protocol (iOS 16+) for custom layout algorithms
- Use `ViewThatFits` to automatically choose between layout variants based on available space
- Leverage `AnyLayout` to animate transitions between different layout types


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

### Creating a custom layout container

| API | Purpose |
|-----|---------|
| `Composing custom layouts with SwiftUI` | Arrange views in your app’s interface using layout tools that SwiftUI provides. |
| `Layout` | A type that defines the geometry of a collection of views. |
| `LayoutSubview` | A proxy that represents one subview of a layout. |
| `LayoutSubviews` | A collection of proxy values that represent the subviews of a layout view. |

### Configuring a custom layout

| API | Purpose |
|-----|---------|
| `LayoutProperties` | Layout-specific properties of a layout container. |
| `ProposedViewSize` | A proposal for the size of a view. |
| `ViewSpacing` | A collection of the geometric spacing preferences of a view. |

### Associating values with views in a custom layout

| API | Purpose |
|-----|---------|
| `layoutValue(key:value:)` | Associates a value with a custom layout property. |
| `LayoutValueKey` | A key for accessing a layout value of a layout container’s subviews. |

### Transitioning between layout types

| API | Purpose |
|-----|---------|
| `AnyLayout` | A type-erased instance of the layout protocol. |
| `HStackLayout` | A horizontal container that you can use in conditional layouts. |
| `VStackLayout` | A vertical container that you can use in conditional layouts. |
| `ZStackLayout` | An overlaying container that you can use in conditional layouts. |
| `GridLayout` | A grid that you can use in conditional layouts. |
