---
name: View groupings
description: Apple SwiftUI Documentation for View groupings.
---

# View groupings

Present views in different kinds of purpose-driven containers, like forms or
control groups.

## Overview

You can create groups of views that serve different purposes.

![](images/com.apple.SwiftUI/view-groupings-hero@2x.png)

For example, a [`Group`](/documentation/SwiftUI/Group) construct treats the specified views as a unit without
imposing any additional layout or appearance characteristics.
A [`Form`](/documentation/SwiftUI/Form) presents a group of elements with a platform-specific
appearance that’s suitable for gathering input from people.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/layout>
in the Human Interface Guidelines.

## Topics

### Grouping views into a container

[Creating custom container views](/documentation/SwiftUI/Creating-custom-container-views)

Access individual subviews to compose flexible container views.

[`Group`](/documentation/SwiftUI/Group)

A type that collects multiple instances of a content type — like views,
scenes, or commands — into a single unit.

[`GroupElementsOfContent`](/documentation/SwiftUI/GroupElementsOfContent)

Transforms the subviews of a given view into a resulting content view.

[`GroupSectionsOfContent`](/documentation/SwiftUI/GroupSectionsOfContent)

Transforms the sections of a given view into a resulting content view.

### Organizing views into sections

[`Section`](/documentation/SwiftUI/Section)

A container view that you can use to add hierarchy within certain views.

[`SectionCollection`](/documentation/SwiftUI/SectionCollection)

An opaque collection representing the sections of view.

[`SectionConfiguration`](/documentation/SwiftUI/SectionConfiguration)

Specifies the contents of a section.

### Iterating over dynamic data

[`ForEach`](/documentation/SwiftUI/ForEach)

A structure that computes views on demand from an underlying collection of
identified data.

[`ForEachSectionCollection`](/documentation/SwiftUI/ForEachSectionCollection)

A collection which allows a view to be treated as a collection of its
sections in a for each loop.

[`ForEachSubviewCollection`](/documentation/SwiftUI/ForEachSubviewCollection)

A collection which allows a view to be treated as a collection of its
subviews in a for each loop.

[`DynamicViewContent`](/documentation/SwiftUI/DynamicViewContent)

A type of view that generates views from an underlying collection of data.

### Accessing a container’s subviews

[`Subview`](/documentation/SwiftUI/Subview)

An opaque value representing a subview of another view.

[`SubviewsCollection`](/documentation/SwiftUI/SubviewsCollection)

An opaque collection representing the subviews of view.

[`SubviewsCollectionSlice`](/documentation/SwiftUI/SubviewsCollectionSlice)

A slice of a SubviewsCollection.

[`containerValue(_:_:)`](/documentation/SwiftUI/View/containerValue(_:_:))

Sets a particular container value of a view.

[`ContainerValues`](/documentation/SwiftUI/ContainerValues)

A collection of container values associated with a given view.

[`ContainerValueKey`](/documentation/SwiftUI/ContainerValueKey)

A key for accessing container values.

### Grouping views into a box

[`GroupBox`](/documentation/SwiftUI/GroupBox)

A stylized view, with an optional label, that visually collects a logical
grouping of content.

[`groupBoxStyle(_:)`](/documentation/SwiftUI/View/groupBoxStyle(_:))

Sets the style for group boxes within this view.

### Grouping inputs

[`Form`](/documentation/SwiftUI/Form)

A container for grouping controls used for data entry, such as in settings
or inspectors.

[`formStyle(_:)`](/documentation/SwiftUI/View/formStyle(_:))

Sets the style for forms in a view hierarchy.

[`LabeledContent`](/documentation/SwiftUI/LabeledContent)

A container for attaching a label to a value-bearing view.

[`labeledContentStyle(_:)`](/documentation/SwiftUI/View/labeledContentStyle(_:))

Sets a style for labeled content.

### Presenting a group of controls

[`ControlGroup`](/documentation/SwiftUI/ControlGroup)

A container view that displays semantically-related controls
in a visually-appropriate manner for the context

[`controlGroupStyle(_:)`](/documentation/SwiftUI/View/controlGroupStyle(_:))

Sets the style for control groups within this view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
