---
name: WatchKit integration
description: Rork-Max Quality skill for WatchKit integration. Actionable patterns and best practices for SwiftUI development.
---

# WatchKit integration

Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
Integrate SwiftUI with your app’s existing content using
hosting controllers to add SwiftUI views into WatchKit interfaces. A hosting
controller wraps a set of SwiftUI views in a form
that you can then add to your storyboard-based app.
You can also add WatchKit views and view controllers to your SwiftUI interfaces.
A representable object wraps the designated view or view controller, and
facilitates communication between the wrapped object and your SwiftUI
views.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct WatchConnectivityView: View {
    @State private var heartRate: Double = 72

    var body: some View {
        VStack {
            Image(systemName: "heart.fill")
                .foregroundStyle(.red)
                .font(.largeTitle)
            Text("\(Int(heartRate)) BPM")
                .font(.system(.title, design: .rounded, weight: .bold))
        }
        .digitalCrownRotation($heartRate, from: 40, through: 200, by: 1)
    }
}
```

## 💎 Elite Implementation Tips

- Use `.digitalCrownRotation()` for scroll and value adjustment on watchOS
- Keep watch interactions under 5 seconds — design for glances, not sessions
- Use `WCSession` to send data between iPhone and Apple Watch


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

### Displaying SwiftUI views in WatchKit

| API | Purpose |
|-----|---------|
| `WKHostingController` | A WatchKit interface controller that hosts a SwiftUI view hierarchy. |
| `WKUserNotificationHostingController` | A WatchKit user notification interface controller that hosts a SwiftUI view |

### Adding WatchKit views to SwiftUI view hierarchies

| API | Purpose |
|-----|---------|
| `WKInterfaceObjectRepresentable` | A view that represents a WatchKit interface object. |
| `WKInterfaceObjectRepresentableContext` | Contextual information about the state of the system that you use to create |
