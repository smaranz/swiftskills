---
name: Previews in Xcode
description: Apple SwiftUI Documentation for Previews in Xcode.
---

# Previews in Xcode

Generate dynamic, interactive previews of your custom views.

## Overview

When you create a custom [`View`](/documentation/SwiftUI/View) with SwiftUI,
Xcode can display a preview of the view’s content
that stays up-to-date as you make changes to the view’s code.
You use one of the preview macros — like [`Preview(_:body:)`](/documentation/SwiftUI/Preview(_:body:)) —
to tell Xcode what to display.
Xcode shows the preview in a canvas beside your code.

![](images/com.apple.SwiftUI/previews-in-xcode-hero@2x.png)

Different preview macros enable different kinds of configuration.
For example, you can add traits that affect the preview’s
appearance using the [`Preview(_:traits:_:body:)`](/documentation/SwiftUI/Preview(_:traits:_:body:)) macro
or add custom viewpoints for the preview using the
[`Preview(_:traits:body:cameras:)`](/documentation/SwiftUI/Preview(_:traits:body:cameras:)) macro. You can also check how
your view behaves inside a specific scene type. For example, in visionOS
you can use the [`Preview(_:immersionStyle:traits:body:)`](/documentation/SwiftUI/Preview(_:immersionStyle:traits:body:)) macro to
preview your view inside an [`ImmersiveSpace`](/documentation/SwiftUI/ImmersiveSpace).

You typically rely on preview macros to create previews in your
code. However, if you can’t get the behavior you need using a preview
macro, you can use the [`PreviewProvider`](/documentation/SwiftUI/PreviewProvider) protocol and its
associated supporting types to define and configure a preview.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/Xcode/previewing-your-apps-interface-in-xcode>

### Creating a preview

[`Preview(_:body:)`](/documentation/SwiftUI/Preview(_:body:))

Creates a preview of a SwiftUI view.

[`Preview(_:traits:_:body:)`](/documentation/SwiftUI/Preview(_:traits:_:body:))

Creates a preview of a SwiftUI view using the specified traits.

[`Preview(_:traits:body:cameras:)`](/documentation/SwiftUI/Preview(_:traits:body:cameras:))

Creates a preview of a SwiftUI view using the specified traits and custom
viewpoints.

### Creating a preview in the context of a scene

[`Preview(_:immersionStyle:traits:body:)`](/documentation/SwiftUI/Preview(_:immersionStyle:traits:body:))

Creates a preview of a SwiftUI view in an immersive space.

[`Preview(_:immersionStyle:traits:body:cameras:)`](/documentation/SwiftUI/Preview(_:immersionStyle:traits:body:cameras:))

Creates a preview of a SwiftUI view in an immersive space with custom
viewpoints.

[`Preview(_:windowStyle:traits:body:)`](/documentation/SwiftUI/Preview(_:windowStyle:traits:body:))

Creates a preview of a SwiftUI view in a window.

[`Preview(_:windowStyle:traits:body:cameras:)`](/documentation/SwiftUI/Preview(_:windowStyle:traits:body:cameras:))

Creates a preview of a SwiftUI view in a window with custom viewpoints.

### Defining a preview

[`Previewable()`](/documentation/SwiftUI/Previewable())

Tag allowing a dynamic property to appear inline in a preview.

[`PreviewProvider`](/documentation/SwiftUI/PreviewProvider)

A type that produces view previews in Xcode.

[`PreviewPlatform`](/documentation/SwiftUI/PreviewPlatform)

Platforms that can run the preview.

[`previewDisplayName(_:)`](/documentation/SwiftUI/View/previewDisplayName(_:))

Sets a user visible name to show in the canvas for a preview.

[`PreviewModifier`](/documentation/SwiftUI/PreviewModifier)

A type that defines an environment in which previews can appear.

[`PreviewModifierContent`](/documentation/SwiftUI/PreviewModifierContent)

The type-erased content of a preview.

### Customizing a preview

[`previewDevice(_:)`](/documentation/SwiftUI/View/previewDevice(_:))

Overrides the device for a preview.

[`PreviewDevice`](/documentation/SwiftUI/PreviewDevice)

A simulator device that runs a preview.

[`previewLayout(_:)`](/documentation/SwiftUI/View/previewLayout(_:))

Overrides the size of the container for the preview.

[`previewInterfaceOrientation(_:)`](/documentation/SwiftUI/View/previewInterfaceOrientation(_:))

Overrides the orientation of the preview.

[`InterfaceOrientation`](/documentation/SwiftUI/InterfaceOrientation)

The orientation of the interface from the user’s perspective.

### Setting a context

[`previewContext(_:)`](/documentation/SwiftUI/View/previewContext(_:))

Declares a context for the preview.

[`PreviewContext`](/documentation/SwiftUI/PreviewContext)

A context type for use with a preview.

[`PreviewContextKey`](/documentation/SwiftUI/PreviewContextKey)

A key type for a preview context.

### Building in debug mode

[`DebugReplaceableView`](/documentation/SwiftUI/DebugReplaceableView)

Erases view opaque result types in debug builds.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
