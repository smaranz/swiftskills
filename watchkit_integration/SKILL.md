---
name: WatchKit integration
description: Apple SwiftUI Documentation for WatchKit integration.
---

# WatchKit integration

Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.

## Overview

Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into WatchKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.

![](images/com.apple.SwiftUI/watchkit-integration-hero@2x.png)

You can also add WatchKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/designing-for-watchos>
in the Human Interface Guidelines.

## Topics

### Displaying SwiftUI views in WatchKit

[`WKHostingController`](/documentation/SwiftUI/WKHostingController)

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

[`WKUserNotificationHostingController`](/documentation/SwiftUI/WKUserNotificationHostingController)

A WatchKit user notification interface controller that hosts a SwiftUI view
hierarchy.

### Adding WatchKit views to SwiftUI view hierarchies

[`WKInterfaceObjectRepresentable`](/documentation/SwiftUI/WKInterfaceObjectRepresentable)

A view that represents a WatchKit interface object.

[`WKInterfaceObjectRepresentableContext`](/documentation/SwiftUI/WKInterfaceObjectRepresentableContext)

Contextual information about the state of the system that you use to create
and update your WatchKit interface object.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
