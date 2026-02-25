---
name: View groupings
description: Rork-Max Quality skill for View groupings. Actionable patterns and best practices for SwiftUI development.
---

# View groupings

Present views in different kinds of purpose-driven containers, like forms or
control groups.
You can create groups of views that serve different purposes.
For example, a `Group` construct treats the specified views as a unit without
imposing any additional layout or appearance characteristics.
A `Form` presents a group of elements with a platform-specific
appearance that’s suitable for gathering input from people.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct DashboardView: View {
    var body: some View {
        ScrollView {
            VStack(spacing: 16) {
                GroupBox("Today's Summary") {
                    LabeledContent("Steps", value: "8,432")
                    LabeledContent("Calories", value: "1,230")
                    LabeledContent("Distance", value: "4.2 km")
                }

                DisclosureGroup("Advanced Settings") {
                    Toggle("Dark Mode", isOn: .constant(true))
                    Toggle("Notifications", isOn: .constant(false))
                }
                .padding()
                .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 12))
            }
            .padding()
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `GroupBox` for visually grouped, labeled sections
- Use `DisclosureGroup` for collapsible detail sections
- `LabeledContent` pairs a label with a value — great for settings and info rows


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

### Grouping views into a container

| API | Purpose |
|-----|---------|
| `Creating custom container views` | Access individual subviews to compose flexible container views. |
| `Group` | A type that collects multiple instances of a content type — like views, |
| `GroupElementsOfContent` | Transforms the subviews of a given view into a resulting content view. |
| `GroupSectionsOfContent` | Transforms the sections of a given view into a resulting content view. |

### Organizing views into sections

| API | Purpose |
|-----|---------|
| `Section` | A container view that you can use to add hierarchy within certain views. |
| `SectionCollection` | An opaque collection representing the sections of view. |
| `SectionConfiguration` | Specifies the contents of a section. |

### Iterating over dynamic data

| API | Purpose |
|-----|---------|
| `ForEach` | A structure that computes views on demand from an underlying collection of |
| `ForEachSectionCollection` | A collection which allows a view to be treated as a collection of its |
| `ForEachSubviewCollection` | A collection which allows a view to be treated as a collection of its |
| `DynamicViewContent` | A type of view that generates views from an underlying collection of data. |

### Accessing a container’s subviews

| API | Purpose |
|-----|---------|
| `Subview` | An opaque value representing a subview of another view. |
| `SubviewsCollection` | An opaque collection representing the subviews of view. |
| `SubviewsCollectionSlice` | A slice of a SubviewsCollection. |
| `containerValue(_:_:)` | Sets a particular container value of a view. |
| `ContainerValues` | A collection of container values associated with a given view. |
| `ContainerValueKey` | A key for accessing container values. |

### Grouping views into a box

| API | Purpose |
|-----|---------|
| `GroupBox` | A stylized view, with an optional label, that visually collects a logical |
| `groupBoxStyle(_:)` | Sets the style for group boxes within this view. |

### Grouping inputs

| API | Purpose |
|-----|---------|
| `Form` | A container for grouping controls used for data entry, such as in settings |
| `formStyle(_:)` | Sets the style for forms in a view hierarchy. |
| `LabeledContent` | A container for attaching a label to a value-bearing view. |
| `labeledContentStyle(_:)` | Sets a style for labeled content. |

### Presenting a group of controls

| API | Purpose |
|-----|---------|
| `ControlGroup` | A container view that displays semantically-related controls |
| `controlGroupStyle(_:)` | Sets the style for control groups within this view. |
