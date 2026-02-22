---
name: Lists
description: Rork-Max Quality skill for Lists. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Lists


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Lists

Display a structured, scrollable column of information.

## Overview

Use a list to display a one-dimensional vertical collection of views.

![](images/com.apple.SwiftUI/lists-hero@2x.png)

The list is a complex container type that automatically provides scrolling when
it grows too large for the current display. You build a list by providing it
with individual views for the rows in the list, or by using a [`ForEach`](/documentation/SwiftUI/ForEach) to
enumerate a group of rows. You can also mix these strategies, blending any
number of individual views and `ForEach` constructs.

Use view modifiers to configure the appearance and behavior of a list and its
rows, headers, sections, and separators. For example, you can apply a style to
the list, add swipe gestures to individual rows, or make the list
refreshable with a pull-down gesture. You can also use the configuration
associated with [Scroll views](/documentation/SwiftUI/Scroll-views) to control the list’s implicit scrolling
behavior.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/lists-and-tables>
in the Human Interface Guidelines.

## Topics

### Creating a list

[Displaying data in lists](/documentation/SwiftUI/Displaying-Data-in-Lists)

Visualize collections of data with platform-appropriate appearance.

[`List`](/documentation/SwiftUI/List)

A container that presents rows of data arranged in a single column,
optionally providing the ability to select one or more members.

[`listStyle(_:)`](/documentation/SwiftUI/View/listStyle(_:))

Sets the style for lists within this view.

### Disclosing information progressively

[`OutlineGroup`](/documentation/SwiftUI/OutlineGroup)

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

[`DisclosureGroup`](/documentation/SwiftUI/DisclosureGroup)

A view that shows or hides another content view, based on the state of a
disclosure control.

[`disclosureGroupStyle(_:)`](/documentation/SwiftUI/View/disclosureGroupStyle(_:))

Sets the style for disclosure groups within this view.

### Configuring a list’s layout

[`listRowInsets(_:)`](/documentation/SwiftUI/View/listRowInsets(_:))

Applies an inset to the rows in a list.

[`defaultMinListRowHeight`](/documentation/SwiftUI/EnvironmentValues/defaultMinListRowHeight)

The default minimum height of rows in a list.

[`defaultMinListHeaderHeight`](/documentation/SwiftUI/EnvironmentValues/defaultMinListHeaderHeight)

The default minimum height of a header in a list.

[`listRowSpacing(_:)`](/documentation/SwiftUI/View/listRowSpacing(_:))

Sets the vertical spacing between two adjacent rows in a List.

[`listSectionSpacing(_:)`](/documentation/SwiftUI/View/listSectionSpacing(_:))

Sets the spacing between adjacent sections in a [`List`](/documentation/SwiftUI/List) to a custom
value.

[`ListSectionSpacing`](/documentation/SwiftUI/ListSectionSpacing)

The spacing options between two adjacent sections in a list.

[`listSectionMargins(_:_:)`](/documentation/SwiftUI/View/listSectionMargins(_:_:))

Set the section margins for the specific edges.

### Configuring rows

[`listItemTint(_:)`](/documentation/SwiftUI/View/listItemTint(_:))

Sets a fixed tint color for content in a list.

[`ListItemTint`](/documentation/SwiftUI/ListItemTint)

A tint effect configuration that you can apply to content in a list.

### Configuring headers

[`headerProminence(_:)`](/documentation/SwiftUI/View/headerProminence(_:))

Sets the header prominence for this view.

[`headerProminence`](/documentation/SwiftUI/EnvironmentValues/headerProminence)

The prominence to apply to section headers within a view.

[`Prominence`](/documentation/SwiftUI/Prominence)

A type indicating the prominence of a view hierarchy.

### Configuring separators

[`listRowSeparatorTint(_:edges:)`](/documentation/SwiftUI/View/listRowSeparatorTint(_:edges:))

Sets the tint color associated with a row.

[`listSectionSeparatorTint(_:edges:)`](/documentation/SwiftUI/View/listSectionSeparatorTint(_:edges:))

Sets the tint color associated with a section.

[`listRowSeparator(_:edges:)`](/documentation/SwiftUI/View/listRowSeparator(_:edges:))

Sets the display mode for the separator associated with this specific row.

[`listSectionSeparator(_:edges:)`](/documentation/SwiftUI/View/listSectionSeparator(_:edges:))

Sets whether to hide the separator associated with a list section.

### Configuring backgrounds

[`listRowBackground(_:)`](/documentation/SwiftUI/View/listRowBackground(_:))

Places a custom background view behind a list row item.

[`alternatingRowBackgrounds(_:)`](/documentation/SwiftUI/View/alternatingRowBackgrounds(_:))

Overrides whether lists and tables in this view have alternating row
backgrounds.

[`AlternatingRowBackgroundBehavior`](/documentation/SwiftUI/AlternatingRowBackgroundBehavior)

The styling of views with respect to alternating row backgrounds.

[`backgroundProminence`](/documentation/SwiftUI/EnvironmentValues/backgroundProminence)

The prominence of the background underneath views associated with this
environment.

[`BackgroundProminence`](/documentation/SwiftUI/BackgroundProminence)

The prominence of backgrounds underneath other views.

### Displaying a badge on a list item

[`badge(_:)`](/documentation/SwiftUI/View/badge(_:))

Generates a badge for the view from an integer value.

[`badgeProminence(_:)`](/documentation/SwiftUI/View/badgeProminence(_:))

Specifies the prominence of badges created by this view.

[`badgeProminence`](/documentation/SwiftUI/EnvironmentValues/badgeProminence)

The prominence to apply to badges associated with this environment.

[`BadgeProminence`](/documentation/SwiftUI/BadgeProminence)

The visual prominence of a badge.

### Configuring interaction

[`swipeActions(edge:allowsFullSwipe:content:)`](/documentation/SwiftUI/View/swipeActions(edge:allowsFullSwipe:content:))

Adds custom swipe actions to a row in a list.

[`selectionDisabled(_:)`](/documentation/SwiftUI/View/selectionDisabled(_:))

Adds a condition that controls whether users can select this view.

[`listRowHoverEffect(_:)`](/documentation/SwiftUI/View/listRowHoverEffect(_:))

Requests that the containing list row use the provided hover effect.

[`listRowHoverEffectDisabled(_:)`](/documentation/SwiftUI/View/listRowHoverEffectDisabled(_:))

Requests that the containing list row have its hover effect disabled.

### Refreshing a list’s content

[`refreshable(action:)`](/documentation/SwiftUI/View/refreshable(action:))

Marks this view as refreshable.

[`refresh`](/documentation/SwiftUI/EnvironmentValues/refresh)

A refresh action stored in a view’s environment.

[`RefreshAction`](/documentation/SwiftUI/RefreshAction)

An action that initiates a refresh operation.

### Editing a list

[`moveDisabled(_:)`](/documentation/SwiftUI/View/moveDisabled(_:))

Adds a condition for whether the view’s view hierarchy is movable.

[`deleteDisabled(_:)`](/documentation/SwiftUI/View/deleteDisabled(_:))

Adds a condition for whether the view’s view hierarchy is deletable.

[`editMode`](/documentation/SwiftUI/EnvironmentValues/editMode)

An indication of whether the user can edit the contents of a view
associated with this environment.

[`EditMode`](/documentation/SwiftUI/EditMode)

A mode that indicates whether the user can edit a view’s content.

[`EditActions`](/documentation/SwiftUI/EditActions)

A set of edit actions on a collection of data that a view can offer
to a user.

[`EditableCollectionContent`](/documentation/SwiftUI/EditableCollectionContent)

An opaque wrapper view that adds editing capabilities to a row in a list.

[`IndexedIdentifierCollection`](/documentation/SwiftUI/IndexedIdentifierCollection)

A collection wrapper that iterates over the indices and identifiers of a
collection together.

### Configuring a section index

[`listSectionIndexVisibility(_:)`](/documentation/SwiftUI/View/listSectionIndexVisibility(_:))

Changes the visibility of the list section index.

[`sectionIndexLabel(_:)`](/documentation/SwiftUI/View/sectionIndexLabel(_:))

Sets the label that is used in a section index to point to this
section, typically only a single character long.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
