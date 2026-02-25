---
name: IOS Accessibility for UIKit
description: Rork-Max Quality skill for IOS Accessibility for UIKit. Platform-native patterns and best practices for ios development.
---

# IOS Accessibility for UIKit

Make your UIKit apps accessible to everyone who uses iOS and tvOS.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class AccessibleCardView: UIView {
    let titleLabel = UILabel()
    let subtitleLabel = UILabel()
    let actionButton = UIButton()

    override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = true
        accessibilityTraits = .button
        accessibilityLabel = "\(titleLabel.text ?? ""), \(subtitleLabel.text ?? "")"
        accessibilityHint = "Double-tap to view details"
    }

    override func accessibilityActivate() -> Bool {
        showDetails()
        return true
    }

    func showDetails() { }
    required init?(coder: NSCoder) { fatalError() }
}
```

## 💎 Elite Implementation Tips

- Set `isAccessibilityElement = true` and group child labels for composite views
- Override `accessibilityActivate()` to provide custom VoiceOver tap actions
- Test with Accessibility Inspector and VoiceOver — they reveal issues no other tool catches

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
| `UIAccessibility` | A set of methods that provides accessibility information about views and controls in an app’s user interface. |
| `UIAccessibilityContainer` | Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements. |
| `Supporting VoiceOver in your app` | Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision. |

### Behaviors

| API | Purpose |
|-----|---------|
| `UIAccessibilityIdentification` | Methods that associate a unique identifier with elements in your user interface. |
| `UIAccessibilityReadingContent` | Methods to implement for an object that represents content that users read, such as a book or an article. |
| `UIAccessibilityContentSizeCategoryImageAdjusting` | Methods to determine when to adjust images for different content size categories. |
| `UIAccessibilityTextualContext` | Constants that describe a named context that helps identify and classify the type of text inside an element. |

### Guided Access

| API | Purpose |
|-----|---------|
| `configureForGuidedAccess(features:enabled:completionHandler:)` | Enables or disables the specified accessibility features while using Guided Access. |
| `UIGuidedAccessAccessibilityFeature` | Constants that describe accessibility features for Guided Access. |
| `UIAccessibility.GuidedAccessError.Code` | Error codes for Guided Access. |

### Actions

| API | Purpose |
|-----|---------|
| `UIAccessibilityCustomAction` | A custom action to perform on an accessible object. |
| `UIAccessibilityCustomAction.Handler` | A closure type that defines a handler to perform for an action. |

### Elements

| API | Purpose |
|-----|---------|
| `UIAccessibilityElement` | An element that should be accessible to users with disabilities, but that isn’t accessible by default. |
| `UIScrollViewAccessibilityDelegate` | A set of methods you can implement to provide accessibility information for a scroll view. |
| `UIPickerViewAccessibilityDelegate` | A set of methods you can implement to provide accessibility information for individual components of a picker view. |

### Containers

| API | Purpose |
|-----|---------|
| `UIAccessibilityContainerDataTable` | Methods that convey information about the contents of a table. |
| `UIAccessibilityContainerDataTableCell` | Methods that provide the location of a cell in a table. |
| `UIAccessibilityContainerType` | Constants that indicate the type of content in a data-based container. |

### Navigation

| API | Purpose |
|-----|---------|
| `UIAccessibilityCustomRotor` | A context-sensitive function that helps VoiceOver users find the next instance of a related element. |
| `UIAccessibilityCustomRotorItemResult` | A target element that a custom rotor references. |
| `UIAccessibilityCustomRotorSearchPredicate` | The search parameters that help determine the next matching custom rotor item result. |

### Drag and drop support

| API | Purpose |
|-----|---------|
| `UIAccessibilityLocationDescriptor` | An accessibility descriptor for a specific geometric point of interest within a view, for use by assistive apps. |

### Notifications

| API | Purpose |
|-----|---------|
| `Notification names` | The names of notifications that the accessibility system generates. |
| `Notification dictionary keys` | Handle notifications with keys in the user info dictionary. |
| `post(notification:argument:)` | Posts a notification to assistive apps. |

### Conversions

| API | Purpose |
|-----|---------|
| `convertToScreenCoordinates(_:in:)` | Converts the specified rectangle from view coordinates to screen coordinates. |
| `convertToScreenCoordinates(_:in:)` | Converts the specified path object to screen coordinates and returns a new path object with the results. |

### Convenience functions

| API | Purpose |
|-----|---------|
| `focusedElement(using:)` | Returns the accessibility element that’s currently in focus by the specified assistive app. |
| `hearingDevicePairedEar` | The current pairing status of Made for iPhone hearing devices. |
| `UIAccessibility.HearingDeviceEar` | Constants that specify how a person is using a hearing device. |
| `registerGestureConflictWithZoom()` | Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures. |
| `requestGuidedAccessSession(enabled:completionHandler:)` | Transitions the app to or from Single App mode asynchronously. |
| `zoomFocusChanged(zoomType:toFrame:in:)` | Notifies the system when the app’s focus changes to a new location. |

### Capabilities

| API | Purpose |
|-----|---------|
| `isAssistiveTouchRunning` | A Boolean value that indicates whether AssistiveTouch is in an enabled state. |
| `isVoiceOverRunning` | A Boolean value that indicates whether VoiceOver is in an enabled state. |
| `isSwitchControlRunning` | A Boolean value that indicates whether the Switch Control setting is in an enabled state. |
| `isShakeToUndoEnabled` | A Boolean value that indicates whether the Shake to Undo setting is in an enabled state. |
| `isClosedCaptioningEnabled` | A Boolean value that indicates whether the Closed Captions + SDH setting is in an enabled state. |
| `isBoldTextEnabled` | A Boolean value that indicates whether the Bold Text setting is in an enabled state. |
| `isDarkerSystemColorsEnabled` | A Boolean value that indicates whether the Increase Contrast setting is in an enabled state. |
| `isGrayscaleEnabled` | A Boolean value that indicates whether the Color Filters and the Grayscale settings are in an enabled state. |
