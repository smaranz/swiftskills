---
name: AppKit integration
description: Rork-Max Quality skill for AppKit integration. Actionable patterns and best practices for SwiftUI development.
---

# AppKit integration

Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into AppKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.
You can also add AppKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.
For design guidance, see
in the Human Interface Guidelines.


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

### Displaying SwiftUI views in AppKit

| API | Purpose |
|-----|---------|
| `Unifying your app’s animations` | Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit. |
| `NSHostingController` | An AppKit view controller that hosts SwiftUI view hierarchy. |
| `NSHostingView` | An AppKit view that hosts a SwiftUI view hierarchy. |
| `NSHostingMenu` | An AppKit menu with menu items that are defined by a SwiftUI View. |
| `NSHostingSizingOptions` | Options for how hosting views and controllers reflect their |
| `NSHostingSceneRepresentation` | An AppKit type that hosts and can present SwiftUI scenes |
| `NSHostingSceneBridgingOptions` | Options for how hosting views and controllers manage aspects of the |

### Adding AppKit views to SwiftUI view hierarchies

| API | Purpose |
|-----|---------|
| `NSViewRepresentable` | A wrapper that you use to integrate an AppKit view into your SwiftUI view |
| `NSViewRepresentableContext` | Contextual information about the state of the system that you use to create |
| `NSViewControllerRepresentable` | A wrapper that you use to integrate an AppKit view controller into your |
| `NSViewControllerRepresentableContext` | Contextual information about the state of the system that you use to create |

### Adding AppKit gesture recognizers into SwiftUI view hierarchies

| API | Purpose |
|-----|---------|
| `NSGestureRecognizerRepresentable` | A wrapper for an `NSGestureRecognizer` that you use to integrate that |
| `NSGestureRecognizerRepresentableContext` | Contextual information about the state of the system that you use to create |
| `NSGestureRecognizerRepresentableCoordinateSpaceConverter` | A structure used to convert locations to and from coordinate spaces in the |
| `NSGestureRecognizerRepresentable` | — |
