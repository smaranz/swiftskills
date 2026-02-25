---
name: Tables
description: Rork-Max Quality skill for Tables. Actionable patterns and best practices for SwiftUI development.
---

# Tables

Display selectable, sortable data arranged in rows and columns.
Use a table to display multiple values across a collection of elements.
Each element in the collection appears in a different row of the table, while
each value for a given element appears in a different column. Narrow displays
may adapt to show only the first column of the table.
When you create a table, you provide a collection of elements, and then tell
the table how to find the needed value for each column. In simple cases,
SwiftUI infers the element for each row, but you can also specify the row
elements explicitly in more complex scenarios. With a small amount of
additional configuration, you can also make the items in the table selectable,
and the columns sortable.
Like a `List`, a table includes implicit vertical scrolling that you can
configure using the view modifiers described in Scroll views.
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

### Creating a table

| API | Purpose |
|-----|---------|
| `Building a great Mac app with SwiftUI` | Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars, and several other popular user interface elements. |
| `Table` | A container that presents rows of data arranged in one or more columns, |
| `tableStyle(_:)` | Sets the style for tables within this view. |

### Creating columns

| API | Purpose |
|-----|---------|
| `TableColumn` | A column that displays a view for each row in a table. |
| `TableColumnContent` | A type used to represent columns within a table. |
| `TableColumnAlignment` | Describes the alignment of the content of a table column. |
| `TableColumnBuilder` | A result builder that creates table column content from closures. |
| `TableColumnForEach` | A structure that computes columns on demand from an underlying collection of |

### Customizing columns

| API | Purpose |
|-----|---------|
| `tableColumnHeaders(_:)` | Controls the visibility of a `Table`’s column header views. |
| `TableColumnCustomization` | A representation of the state of the columns in a table. |
| `TableColumnCustomizationBehavior` | A set of customization behaviors of a column that a table can offer to |

### Creating rows

| API | Purpose |
|-----|---------|
| `TableRow` | A row that represents a data value in a table. |
| `TableRowContent` | A type used to represent table rows. |
| `TableHeaderRowContent` | A table row that displays a single view instead of columned content. |
| `TupleTableRowContent` | A type of table column content that creates table rows created from a |
| `TableForEachContent` | A type of table row content that creates table rows created by iterating |
| `EmptyTableRowContent` | A table row content that doesn’t produce any rows. |
| `DynamicTableRowContent` | A type of table row content that generates table rows from an underlying |
| `TableRowBuilder` | A result builder that creates table row content from closures. |

### Adding progressive disclosure

| API | Purpose |
|-----|---------|
| `DisclosureTableRow` | A kind of table row that shows or hides additional rows based on the state |
| `TableOutlineGroupContent` | An opaque table row type created by a table’s hierarchical initializers. |
