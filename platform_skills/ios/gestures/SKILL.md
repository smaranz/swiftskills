---
name: IOS Touches, presses, and gestures
description: Rork-Max Quality skill for IOS Touches, presses, and gestures. Platform-native patterns and best practices for ios development.
---

# IOS Touches, presses, and gestures

Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class RorkViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "Touches, presses, and gestures"
        label.font = .preferredFont(forTextStyle: .largeTitle)
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }
}
```

## 💎 Elite Implementation Tips

- Follow the IOS Human Interface Guidelines for native feel.
- Use system-standard UIKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building native iOS/iPadOS features using UIKit APIs
- Implementing UIKit-specific interactions not available in SwiftUI
- Working with view controllers, navigation controllers, and UIKit lifecycle

## Best Practices

- Use SwiftUI for new views and bridge UIKit only when necessary
- Adopt modern UIKit APIs: `UICollectionViewCompositionalLayout`, diffable data sources
- Handle all size classes and trait changes for iPhone and iPad adaptivity

## Common Pitfalls

- Mixing UIKit autolayout and SwiftUI layout can cause constraint conflicts
- Forgetting to test on iPad — multitasking changes your window size
- Not adopting the UIKit scene lifecycle for multi-window support

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Using responders and the responder chain to handle events` | Learn how to handle events that propagate through your app. |
| `UIResponder` | An abstract interface for responding to and handling events. |
| `UIEvent` | An object that describes a single user interaction with your app. |

### Touches

| API | Purpose |
|-----|---------|
| `Handling touches in your view` | Use touch events directly on a view subclass if touch handling is intricately linked to the view’s content. |
| `Handling input from Apple Pencil` | Learn how to detect and respond to touches from Apple Pencil. |
| `Tracking the force of 3D Touch events` | Manipulate your content based on the force of touches. |
| `Illustrating the force, altitude, and azimuth properties of touch input` | Capture Apple Pencil and touch input in views. |
| `Leveraging touch input for drawing apps` | Capture touches as a series of strokes and render them efficiently on a drawing canvas. |
| `UITouch` | An object representing the location, size, movement, and force of a touch occurring on the screen. |

### Button presses

| API | Purpose |
|-----|---------|
| `UIPress` | An object that represents the presence or movement of a button press on the screen for a particular event. |
| `UIPressesEvent` | An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller. |

### Standard gestures

| API | Purpose |
|-----|---------|
| `Handling UIKit gestures` | Use gesture recognizers to simplify touch handling and create a consistent user experience. |
| `Coordinating multiple gesture recognizers` | Discover how to use multiple gesture recognizers on the same view. |
| `Adopting hover support for Apple Pencil` | Enhance user feedback for your iPadOS app with a hover preview for |
| `Supporting gesture interaction in your apps` | Enrich your app’s user experience by supporting standard and custom gesture interaction. |
| `UIHoverGestureRecognizer` | A continuous gesture recognizer that interprets pointer movement over a view. |
| `UILongPressGestureRecognizer` | A continuous gesture recognizer that interprets long-press gestures. |
| `UIPanGestureRecognizer` | A continuous gesture recognizer that interprets panning gestures. |
| `UIPinchGestureRecognizer` | A continuous gesture recognizer that interprets pinching gestures involving two touches. |

### Custom gestures

| API | Purpose |
|-----|---------|
| `Implementing a custom gesture recognizer` | Discover when and how to build your own gesture recognizers. |
| `UIGestureRecognizer` | The base class for concrete gesture recognizers. |
| `UIGestureRecognizerDelegate` | A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior. |
| `Supporting gesture interaction in your apps` | Enrich your app’s user experience by supporting standard and custom gesture interaction. |

### 3D Touch interactions

| API | Purpose |
|-----|---------|
| `UIPreviewInteraction` | A class that registers a view to provide a custom user experience in response to 3D Touch interactions. |
| `UIPreviewInteractionDelegate` | A set of methods for communicating the progress of a preview interaction. |
| `UIPreviewActionItem` | A set of methods that defines the styles you can apply to peek quick actions and peek quick action groups, and defines a read-only accessor for the user-visible title of a peek quick action. |
