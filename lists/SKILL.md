---
name: Lists
description: Rork-Max Quality skill for Lists. Actionable patterns and best practices for SwiftUI development.
---

# Lists

Display a structured, scrollable column of information.
Use a list to display a one-dimensional vertical collection of views.
The list is a complex container type that automatically provides scrolling when
it grows too large for the current display. You build a list by providing it
with individual views for the rows in the list, or by using a `ForEach` to
enumerate a group of rows. You can also mix these strategies, blending any
number of individual views and `ForEach` constructs.
Use view modifiers to configure the appearance and behavior of a list and its
rows, headers, sections, and separators. For example, you can apply a style to
the list, add swipe gestures to individual rows, or make the list
refreshable with a pull-down gesture. You can also use the configuration
associated with Scroll views to control the list’s implicit scrolling
behavior.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct TaskListView: View {
    @State private var tasks: [TaskItem] = TaskItem.samples

    var body: some View {
        List {
            ForEach($tasks) { $task in
                HStack {
                    Image(systemName: task.isDone ? "checkmark.circle.fill" : "circle")
                        .foregroundStyle(task.isDone ? .green : .secondary)
                        .onTapGesture { task.isDone.toggle() }
                    Text(task.title)
                        .strikethrough(task.isDone)
                }
            }
            .onDelete { tasks.remove(atOffsets: $0) }
            .onMove { tasks.move(fromOffsets: $0, toOffset: $1) }
        }
        .listStyle(.insetGrouped)
    }
}
```

## 💎 Elite Implementation Tips

- Use `.listStyle(.insetGrouped)` for modern card-style lists on iOS
- Support `.onDelete` and `.onMove` for swipe-to-delete and drag-to-reorder
- Use `List(selection:)` with `EditButton()` for multi-select mode


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

### Creating a list

| API | Purpose |
|-----|---------|
| `Displaying data in lists` | Visualize collections of data with platform-appropriate appearance. |
| `List` | A container that presents rows of data arranged in a single column, |
| `listStyle(_:)` | Sets the style for lists within this view. |

### Disclosing information progressively

| API | Purpose |
|-----|---------|
| `OutlineGroup` | A structure that computes views and disclosure groups on demand from an |
| `DisclosureGroup` | A view that shows or hides another content view, based on the state of a |
| `disclosureGroupStyle(_:)` | Sets the style for disclosure groups within this view. |

### Configuring a list’s layout

| API | Purpose |
|-----|---------|
| `listRowInsets(_:)` | Applies an inset to the rows in a list. |
| `defaultMinListRowHeight` | The default minimum height of rows in a list. |
| `defaultMinListHeaderHeight` | The default minimum height of a header in a list. |
| `listRowSpacing(_:)` | Sets the vertical spacing between two adjacent rows in a List. |
| `listSectionSpacing(_:)` | Sets the spacing between adjacent sections in a [`List`](/documentation/SwiftUI/List) to a custom |
| `ListSectionSpacing` | The spacing options between two adjacent sections in a list. |
| `listSectionMargins(_:_:)` | Set the section margins for the specific edges. |

### Configuring rows

| API | Purpose |
|-----|---------|
| `listItemTint(_:)` | Sets a fixed tint color for content in a list. |
| `ListItemTint` | A tint effect configuration that you can apply to content in a list. |

### Configuring headers

| API | Purpose |
|-----|---------|
| `headerProminence(_:)` | Sets the header prominence for this view. |
| `headerProminence` | The prominence to apply to section headers within a view. |
| `Prominence` | A type indicating the prominence of a view hierarchy. |

### Configuring separators

| API | Purpose |
|-----|---------|
| `listRowSeparatorTint(_:edges:)` | Sets the tint color associated with a row. |
| `listSectionSeparatorTint(_:edges:)` | Sets the tint color associated with a section. |
| `listRowSeparator(_:edges:)` | Sets the display mode for the separator associated with this specific row. |
| `listSectionSeparator(_:edges:)` | Sets whether to hide the separator associated with a list section. |

### Configuring backgrounds

| API | Purpose |
|-----|---------|
| `listRowBackground(_:)` | Places a custom background view behind a list row item. |
| `alternatingRowBackgrounds(_:)` | Overrides whether lists and tables in this view have alternating row |
| `AlternatingRowBackgroundBehavior` | The styling of views with respect to alternating row backgrounds. |
| `backgroundProminence` | The prominence of the background underneath views associated with this |
| `BackgroundProminence` | The prominence of backgrounds underneath other views. |

### Displaying a badge on a list item

| API | Purpose |
|-----|---------|
| `badge(_:)` | Generates a badge for the view from an integer value. |
| `badgeProminence(_:)` | Specifies the prominence of badges created by this view. |
| `badgeProminence` | The prominence to apply to badges associated with this environment. |
| `BadgeProminence` | The visual prominence of a badge. |

### Configuring interaction

| API | Purpose |
|-----|---------|
| `swipeActions(edge:allowsFullSwipe:content:)` | Adds custom swipe actions to a row in a list. |
| `selectionDisabled(_:)` | Adds a condition that controls whether users can select this view. |
| `listRowHoverEffect(_:)` | Requests that the containing list row use the provided hover effect. |
| `listRowHoverEffectDisabled(_:)` | Requests that the containing list row have its hover effect disabled. |

### Refreshing a list’s content

| API | Purpose |
|-----|---------|
| `refreshable(action:)` | Adds an asynchronous handler that can update the data the view |
| `refresh` | A refresh action stored in a view’s environment. |
| `RefreshAction` | An action that initiates a refresh operation. |

### Editing a list

| API | Purpose |
|-----|---------|
| `moveDisabled(_:)` | Adds a condition for whether the view’s view hierarchy is movable. |
| `deleteDisabled(_:)` | Adds a condition for whether the view’s view hierarchy is deletable. |
| `editMode` | An indication of whether the user can edit the contents of a view |
| `EditMode` | A mode that indicates whether the user can edit a view’s content. |
| `EditActions` | A set of edit actions on a collection of data that a view can offer |
| `EditableCollectionContent` | An opaque wrapper view that adds editing capabilities to a row in a list. |
| `IndexedIdentifierCollection` | A collection wrapper that iterates over the indices and identifiers of a |

### Configuring a section index

| API | Purpose |
|-----|---------|
| `listSectionIndexVisibility(_:)` | Changes the visibility of the list section index. |
| `sectionIndexLabel(_:)` | Sets the label that is used in a section index to point to this |
