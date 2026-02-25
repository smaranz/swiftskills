---
name: UIKit integration
description: Rork-Max Quality skill for UIKit integration. Actionable patterns and best practices for SwiftUI development.
---

# UIKit integration

Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into UIKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.
You can also add UIKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.
For design guidance, see the following sections in the Human Interface Guidelines:
- designing-for-ios
- designing-for-ipados
- designing-for-tvos


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Embedding UIKit views/controllers in SwiftUI with `UIViewRepresentable`
- Using SwiftUI views inside UIKit with `UIHostingController`
- Wrapping AppKit views for macOS SwiftUI apps
- Integrating MapKit, WebKit, or other framework views into SwiftUI

## Best Practices

- Use `UIViewRepresentable` / `NSViewRepresentable` for UIKit/AppKit views in SwiftUI
- Implement `Coordinator` for delegate callbacks flowing back into SwiftUI
- Keep bridge code minimal — move logic into shared `@Observable` models
- Prefer native SwiftUI equivalents when available (e.g., `Map` over `MKMapView` wrapper)

## Common Pitfalls

- Forgetting to implement `updateUIView()` — state changes won't propagate to the UIKit view
- Creating a new `UIHostingController` every time instead of updating the existing root view
- Memory leaks from strong reference cycles between Coordinator and SwiftUI state

## Key APIs

### Displaying SwiftUI views in UIKit

| API | Purpose |
|-----|---------|
| `Unifying your app’s animations` | Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit. |
| `UIHostingController` | A UIKit view controller that manages a SwiftUI view hierarchy. |
| `UIHostingControllerSizingOptions` | Options for how a hosting controller tracks its content’s size. |
| `UIHostingConfiguration` | A content configuration suitable for hosting a hierarchy of SwiftUI views. |
| `UIHostingSceneDelegate` | Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes. |

### Adding UIKit views to SwiftUI view hierarchies

| API | Purpose |
|-----|---------|
| `UIViewRepresentable` | A wrapper for a UIKit view that you use to integrate that view into your |
| `UIViewRepresentableContext` | Contextual information about the state of the system that you use to create |
| `UIViewControllerRepresentable` | A view that represents a UIKit view controller. |
| `UIViewControllerRepresentableContext` | Contextual information about the state of the system that you use to create |

### Adding UIKit gesture recognizers into SwiftUI view hierarchies

| API | Purpose |
|-----|---------|
| `UIGestureRecognizerRepresentable` | A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture |
| `UIGestureRecognizerRepresentableContext` | Contextual information about the state of the system that you use to create |
| `UIGestureRecognizerRepresentableCoordinateSpaceConverter` | A proxy structure used to convert locations to/from coordinate spaces in the |

### Hosting an ornament in UIKit

| API | Purpose |
|-----|---------|
| `UIHostingOrnament` | A model that represents an ornament suitable for being hosted in UIKit. |
| `UIOrnament` | The abstract base class that represents an ornament. |
