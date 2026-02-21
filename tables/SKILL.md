---
name: Tables
description: Apple SwiftUI Documentation for Tables.
---

# Tables

Display selectable, sortable data arranged in rows and columns.

## Overview

Use a table to display multiple values across a collection of elements.
Each element in the collection appears in a different row of the table, while
each value for a given element appears in a different column. Narrow displays
may adapt to show only the first column of the table.

![](images/com.apple.SwiftUI/tables-hero@2x.png)

When you create a table, you provide a collection of elements, and then tell
the table how to find the needed value for each column. In simple cases,
SwiftUI infers the element for each row, but you can also specify the row
elements explicitly in more complex scenarios. With a small amount of
additional configuration, you can also make the items in the table selectable,
and the columns sortable.

Like a [`List`](/documentation/SwiftUI/List), a table includes implicit vertical scrolling that you can
configure using the view modifiers described in [Scroll views](/documentation/SwiftUI/Scroll-views).
For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/lists-and-tables>
in the Human Interface Guidelines.

## Topics

### Creating a table

[Building a great Mac app with SwiftUI](/documentation/SwiftUI/building-a-great-mac-app-with-swiftui)

Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars, and several other popular user interface elements.

[`Table`](/documentation/SwiftUI/Table)

A container that presents rows of data arranged in one or more columns,
optionally providing the ability to select one or more members.

[`tableStyle(_:)`](/documentation/SwiftUI/View/tableStyle(_:))

Sets the style for tables within this view.

### Creating columns

[`TableColumn`](/documentation/SwiftUI/TableColumn)

A column that displays a view for each row in a table.

[`TableColumnContent`](/documentation/SwiftUI/TableColumnContent)

A type used to represent columns within a table.

[`TableColumnAlignment`](/documentation/SwiftUI/TableColumnAlignment)

Describes the alignment of the content of a table column.

[`TableColumnBuilder`](/documentation/SwiftUI/TableColumnBuilder)

A result builder that creates table column content from closures.

[`TableColumnForEach`](/documentation/SwiftUI/TableColumnForEach)

A structure that computes columns on demand from an underlying collection of
identified data.

### Customizing columns

[`tableColumnHeaders(_:)`](/documentation/SwiftUI/View/tableColumnHeaders(_:))

Controls the visibility of a `Table`’s column header views.

[`TableColumnCustomization`](/documentation/SwiftUI/TableColumnCustomization)

A representation of the state of the columns in a table.

[`TableColumnCustomizationBehavior`](/documentation/SwiftUI/TableColumnCustomizationBehavior)

A set of customization behaviors of a column that a table can offer to
a user.

### Creating rows

[`TableRow`](/documentation/SwiftUI/TableRow)

A row that represents a data value in a table.

[`TableRowContent`](/documentation/SwiftUI/TableRowContent)

A type used to represent table rows.

[`TableHeaderRowContent`](/documentation/SwiftUI/TableHeaderRowContent)

A table row that displays a single view instead of columned content.

[`TupleTableRowContent`](/documentation/SwiftUI/TupleTableRowContent)

A type of table column content that creates table rows created from a
Swift tuple of table rows.

[`TableForEachContent`](/documentation/SwiftUI/TableForEachContent)

A type of table row content that creates table rows created by iterating
over a collection.

[`EmptyTableRowContent`](/documentation/SwiftUI/EmptyTableRowContent)

A table row content that doesn’t produce any rows.

[`DynamicTableRowContent`](/documentation/SwiftUI/DynamicTableRowContent)

A type of table row content that generates table rows from an underlying
collection of data.

[`TableRowBuilder`](/documentation/SwiftUI/TableRowBuilder)

A result builder that creates table row content from closures.

### Adding progressive disclosure

[`DisclosureTableRow`](/documentation/SwiftUI/DisclosureTableRow)

A kind of table row that shows or hides additional rows based on the state
of a disclosure control.

[`TableOutlineGroupContent`](/documentation/SwiftUI/TableOutlineGroupContent)

An opaque table row type created by a table’s hierarchical initializers.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
