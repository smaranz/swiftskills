---
name: UIKit integration
description: Apple SwiftUI Documentation for UIKit integration.
---

# UIKit integration

Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.

## Overview

Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into UIKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.

![](images/com.apple.SwiftUI/uikit-integration-hero@2x.png)

You can also add UIKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.

For design guidance, see the following sections in the Human Interface Guidelines:

- <doc://com.apple.documentation/design/Human-Interface-Guidelines/designing-for-ios>
- <doc://com.apple.documentation/design/Human-Interface-Guidelines/designing-for-ipados>
- <doc://com.apple.documentation/design/Human-Interface-Guidelines/designing-for-tvos>

## Topics

### Displaying SwiftUI views in UIKit

  <doc://com.apple.documentation/documentation/UIKit/using-swiftui-with-uikit>

[Unifying your app’s animations](/documentation/SwiftUI/Unifying-your-app-s-animations)

Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.

[`UIHostingController`](/documentation/SwiftUI/UIHostingController)

A UIKit view controller that manages a SwiftUI view hierarchy.

[`UIHostingControllerSizingOptions`](/documentation/SwiftUI/UIHostingControllerSizingOptions)

Options for how a hosting controller tracks its content’s size.

[`UIHostingConfiguration`](/documentation/SwiftUI/UIHostingConfiguration)

A content configuration suitable for hosting a hierarchy of SwiftUI views.

[`UIHostingSceneDelegate`](/documentation/SwiftUI/UIHostingSceneDelegate)

Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.

### Adding UIKit views to SwiftUI view hierarchies

[`UIViewRepresentable`](/documentation/SwiftUI/UIViewRepresentable)

A wrapper for a UIKit view that you use to integrate that view into your
SwiftUI view hierarchy.

[`UIViewRepresentableContext`](/documentation/SwiftUI/UIViewRepresentableContext)

Contextual information about the state of the system that you use to create
and update your UIKit view.

[`UIViewControllerRepresentable`](/documentation/SwiftUI/UIViewControllerRepresentable)

A view that represents a UIKit view controller.

[`UIViewControllerRepresentableContext`](/documentation/SwiftUI/UIViewControllerRepresentableContext)

Contextual information about the state of the system that you use to create
and update your UIKit view controller.

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

[`UIGestureRecognizerRepresentable`](/documentation/SwiftUI/UIGestureRecognizerRepresentable)

A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture
recognizer into your SwiftUI hierarchy.

[`UIGestureRecognizerRepresentableContext`](/documentation/SwiftUI/UIGestureRecognizerRepresentableContext)

Contextual information about the state of the system that you use to create
and update a represented gesture recognizer.

[`UIGestureRecognizerRepresentableCoordinateSpaceConverter`](/documentation/SwiftUI/UIGestureRecognizerRepresentableCoordinateSpaceConverter)

A proxy structure used to convert locations to/from coordinate spaces in the
hierarchy of the SwiftUI view associated with a
[`UIGestureRecognizerRepresentable`](/documentation/SwiftUI/UIGestureRecognizerRepresentable).

### Sharing configuration information

[`UITraitBridgedEnvironmentKey`](/documentation/SwiftUI/UITraitBridgedEnvironmentKey)

### Hosting an ornament in UIKit

[`UIHostingOrnament`](/documentation/SwiftUI/UIHostingOrnament)

A model that represents an ornament suitable for being hosted in UIKit.

[`UIOrnament`](/documentation/SwiftUI/UIOrnament)

The abstract base class that represents an ornament.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
