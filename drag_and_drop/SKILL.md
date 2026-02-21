---
name: Drag and drop
description: Apple SwiftUI Documentation for Drag and drop.
---

# Drag and drop

Enable people to move or duplicate items by dragging them from one location to another.

## Overview

Drag and drop offers people a convenient way to move content from one part of
your app to another, or from one app to another, using an intuitive dragging
gesture. Support this feature in your app by adding view modifiers
to potential source and destination views within your app’s interface.

![](images/com.apple.SwiftUI/drag-and-drop-hero@2x.png)

In your modifiers, provide or accept types that conform to the
<doc://com.apple.documentation/documentation/CoreTransferable/Transferable>
protocol, or that inherit from the
<doc://com.apple.documentation/documentation/Foundation/NSItemProvider> class.
When possible, prefer using transferable items.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/drag-and-drop>
in the Human Interface Guidelines.

## Topics

### Essentials

[Adopting drag and drop using SwiftUI](/documentation/SwiftUI/Adopting-drag-and-drop-using-SwiftUI)

Enable drag-and-drop interactions in lists, tables and custom views.

[Making a view into a drag source](/documentation/SwiftUI/Making-a-view-into-a-drag-source)

Adopt draggable API to provide items for drag-and-drop operations.

### Configuring drag and drop behavior

[`DragConfiguration`](/documentation/SwiftUI/DragConfiguration)

The behavior of the drag, proposed by the dragging source.

[`DropConfiguration`](/documentation/SwiftUI/DropConfiguration)

Describes the behavior of the drop.

### Moving items

[`DragSession`](/documentation/SwiftUI/DragSession)

Describes the ongoing dragging session.

[`DropSession`](/documentation/SwiftUI/DropSession)

### Moving transferable items

[`draggable(_:)`](/documentation/SwiftUI/View/draggable(_:))

Activates this view as the source of a drag and drop operation.

[`draggable(_:preview:)`](/documentation/SwiftUI/View/draggable(_:preview:))

Activates this view as the source of a drag and drop operation.

[`dropDestination(for:action:isTargeted:)`](/documentation/SwiftUI/View/dropDestination(for:action:isTargeted:))

Defines the destination of a drag and drop operation that handles the
dropped content with a closure that you specify.

### Moving items using item providers

[`itemProvider(_:)`](/documentation/SwiftUI/View/itemProvider(_:))

Provides a closure that vends the drag representation to be used for a
particular data element.

[`onDrag(_:preview:)`](/documentation/SwiftUI/View/onDrag(_:preview:))

Activates this view as the source of a drag and drop operation.

[`onDrag(_:)`](/documentation/SwiftUI/View/onDrag(_:))

Activates this view as the source of a drag and drop operation.

[`onDrop(of:isTargeted:perform:)`](/documentation/SwiftUI/View/onDrop(of:isTargeted:perform:))

Defines the destination of a drag-and-drop operation that handles the
dropped content with a closure that you specify.

[`onDrop(of:delegate:)`](/documentation/SwiftUI/View/onDrop(of:delegate:))

Defines the destination of a drag and drop operation using behavior
controlled by the delegate that you provide.

[`DropDelegate`](/documentation/SwiftUI/DropDelegate)

An interface that you implement to interact with a drop operation in a view
modified to accept drops.

[`DropProposal`](/documentation/SwiftUI/DropProposal)

The behavior of a drop.

[`DropOperation`](/documentation/SwiftUI/DropOperation)

Operation types that determine how a drag and drop session resolves when the
user drops a drag item.

[`DropInfo`](/documentation/SwiftUI/DropInfo)

The current state of a drop.

### Describing preview formations

[`DragDropPreviewsFormation`](/documentation/SwiftUI/DragDropPreviewsFormation)

On macOS, describes the way the dragged previews are visually composed.
Both drag sources and drop destination can specify their desired preview formation.

### Configuring spring loading

[`springLoadingBehavior(_:)`](/documentation/SwiftUI/View/springLoadingBehavior(_:))

Sets the spring loading behavior this view.

[`springLoadingBehavior`](/documentation/SwiftUI/EnvironmentValues/springLoadingBehavior)

The behavior of spring loaded interactions for the views associated
with this environment.

[`SpringLoadingBehavior`](/documentation/SwiftUI/SpringLoadingBehavior)

The options for controlling the spring loading behavior of views.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
