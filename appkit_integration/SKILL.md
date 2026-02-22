---
name: AppKit integration
description: Rork-Max Quality skill for AppKit integration. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# AppKit integration


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# AppKit integration

Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.

## Overview

Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into AppKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.

![](images/com.apple.SwiftUI/appkit-integration-hero@2x.png)

You can also add AppKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/designing-for-macos>
in the Human Interface Guidelines.

## Topics

### Displaying SwiftUI views in AppKit

[Unifying your app’s animations](/documentation/SwiftUI/Unifying-your-app-s-animations)

Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.

[`NSHostingController`](/documentation/SwiftUI/NSHostingController)

An AppKit view controller that hosts SwiftUI view hierarchy.

[`NSHostingView`](/documentation/SwiftUI/NSHostingView)

An AppKit view that hosts a SwiftUI view hierarchy.

[`NSHostingMenu`](/documentation/SwiftUI/NSHostingMenu)

An AppKit menu with menu items that are defined by a SwiftUI View.

[`NSHostingSizingOptions`](/documentation/SwiftUI/NSHostingSizingOptions)

Options for how hosting views and controllers reflect their
content’s size into Auto Layout constraints.

[`NSHostingSceneRepresentation`](/documentation/SwiftUI/NSHostingSceneRepresentation)

An AppKit type that hosts and can present SwiftUI scenes

[`NSHostingSceneBridgingOptions`](/documentation/SwiftUI/NSHostingSceneBridgingOptions)

Options for how hosting views and controllers manage aspects of the
associated window.

### Adding AppKit views to SwiftUI view hierarchies

[`NSViewRepresentable`](/documentation/SwiftUI/NSViewRepresentable)

A wrapper that you use to integrate an AppKit view into your SwiftUI view
hierarchy.

[`NSViewRepresentableContext`](/documentation/SwiftUI/NSViewRepresentableContext)

Contextual information about the state of the system that you use to create
and update your AppKit view.

[`NSViewControllerRepresentable`](/documentation/SwiftUI/NSViewControllerRepresentable)

A wrapper that you use to integrate an AppKit view controller into your
SwiftUI interface.

[`NSViewControllerRepresentableContext`](/documentation/SwiftUI/NSViewControllerRepresentableContext)

Contextual information about the state of the system that you use to create
and update your AppKit view controller.

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

[`NSGestureRecognizerRepresentable`](/documentation/SwiftUI/NSGestureRecognizerRepresentable)

A wrapper for an `NSGestureRecognizer` that you use to integrate that
gesture recognizer into your SwiftUI hierarchy.

[`NSGestureRecognizerRepresentableContext`](/documentation/SwiftUI/NSGestureRecognizerRepresentableContext)

Contextual information about the state of the system that you use to create
and update a represented gesture recognizer.

[`NSGestureRecognizerRepresentableCoordinateSpaceConverter`](/documentation/SwiftUI/NSGestureRecognizerRepresentableCoordinateSpaceConverter)

A structure used to convert locations to and from coordinate spaces in the
hierarchy of the SwiftUI view associated with an
[`NSGestureRecognizerRepresentable`](/documentation/SwiftUI/NSGestureRecognizerRepresentable).



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
