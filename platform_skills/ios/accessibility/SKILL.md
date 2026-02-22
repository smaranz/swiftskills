---
name: IOS Accessibility for UIKit
description: Rork-Max Quality skill for IOS Accessibility for UIKit on ios. Based on official Apple UIKit Documentation.
---

# IOS Accessibility for UIKit

## 🚀 Rork-Max Quality Snippet

```swift
// Premium IOS Accessibility for UIKit Implementation for ios
// Focus on platform-native excellence

import SwiftUI
#if os(ios)
// UIKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality IOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the ios native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for ios: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Accessibility for UIKit

Make your UIKit apps accessible to everyone who uses iOS and tvOS.

## Discussion

Making your app accessible means making it usable by everyone. By designing your app with accessibility in mind, you make it possible for everyone to enjoy your app. For more information, see <doc://com.apple.documentation/documentation/Accessibility>.

UIKit controls and views come with built-in accessibility, providing an accessible user experience by default. Typically, you don’t need to do extra work to enable the standard accessibility features.

In some cases, you might want to modify the default values to better represent your app, to provide additional context, or to modify the user’s flow through the app. UIKit makes these customizations straightforward, involving a few lines of code or Interface Builder adjustments as you define your user interface. For more information about customizing accessibility for UIKit elements, see <doc://com.apple.documentation/documentation/UIKit/uiaccessibility-protocol>.

If your app contains custom user interface elements that don’t inherit from [`UIView`](/documentation/UIKit/UIView) or one of the other UIKit classes with built-in accessibility, make those elements accessible by subclassing [`UIAccessibilityElement`](/documentation/UIKit/UIAccessibilityElement).

If you build your app with SwiftUI, see <doc://com.apple.documentation/documentation/SwiftUI/View-Accessibility>.

## Topics

### Essentials

[UIAccessibility](/documentation/UIKit/uiaccessibility-protocol)

A set of methods that provides accessibility information about views and controls in an app’s user interface.

[UIAccessibilityContainer](/documentation/UIKit/uiaccessibilitycontainer)

Provide a set of methods that view subclasses use to make subcomponents accessible as separate elements.

[Supporting VoiceOver in your app](/documentation/UIKit/supporting-voiceover-in-your-app)

Add VoiceOver support to make your iOS app more accessible to users who are blind or have low vision.

### Behaviors

  <doc://com.apple.documentation/documentation/ObjectiveC/uiaccessibilityfocus>

[`UIAccessibilityIdentification`](/documentation/UIKit/UIAccessibilityIdentification)

Methods that associate a unique identifier with elements in your user interface.

[`UIAccessibilityReadingContent`](/documentation/UIKit/UIAccessibilityReadingContent)

Methods to implement for an object that represents content that users read, such as a book or an article.

[`UIAccessibilityContentSizeCategoryImageAdjusting`](/documentation/UIKit/UIAccessibilityContentSizeCategoryImageAdjusting)

Methods to determine when to adjust images for different content size categories.

[`UIAccessibilityTextualContext`](/documentation/UIKit/UIAccessibilityTextualContext)

Constants that describe a named context that helps identify and classify the type of text inside an element.

### Guided Access

[`configureForGuidedAccess(features:enabled:completionHandler:)`](/documentation/UIKit/UIAccessibility/configureForGuidedAccess(features:enabled:completionHandler:))

Enables or disables the specified accessibility features while using Guided Access.

[`UIGuidedAccessAccessibilityFeature`](/documentation/UIKit/UIGuidedAccessAccessibilityFeature)

Constants that describe accessibility features for Guided Access.

[`UIAccessibility.GuidedAccessError.Code`](/documentation/UIKit/UIAccessibility/GuidedAccessError/Code)

Error codes for Guided Access.

### Actions

  <doc://com.apple.documentation/documentation/ObjectiveC/uiaccessibilityaction>

[`UIAccessibilityCustomAction`](/documentation/UIKit/UIAccessibilityCustomAction)

A custom action to perform on an accessible object.

[`UIAccessibilityCustomAction.Handler`](/documentation/UIKit/UIAccessibilityCustomAction/Handler)

A closure type that defines a handler to perform for an action.

  <doc://com.apple.documentation/documentation/Accessibility/delivering_an_exceptional_accessibility_experience>

### Elements

[`UIAccessibilityElement`](/documentation/UIKit/UIAccessibilityElement)

An element that should be accessible to users with disabilities, but that isn’t accessible by default.

[`UIScrollViewAccessibilityDelegate`](/documentation/UIKit/UIScrollViewAccessibilityDelegate)

A set of methods you can implement to provide accessibility information for a scroll view.

[`UIPickerViewAccessibilityDelegate`](/documentation/UIKit/UIPickerViewAccessibilityDelegate)

A set of methods you can implement to provide accessibility information for individual components of a picker view.

### Containers

[`UIAccessibilityContainerDataTable`](/documentation/UIKit/UIAccessibilityContainerDataTable)

Methods that convey information about the contents of a table.

[`UIAccessibilityContainerDataTableCell`](/documentation/UIKit/UIAccessibilityContainerDataTableCell)

Methods that provide the location of a cell in a table.

[`UIAccessibilityContainerType`](/documentation/UIKit/UIAccessibilityContainerType)

Constants that indicate the type of content in a data-based container.

### Navigation

[`UIAccessibilityCustomRotor`](/documentation/UIKit/UIAccessibilityCustomRotor)

A context-sensitive function that helps VoiceOver users find the next instance of a related element.

[`UIAccessibilityCustomRotorItemResult`](/documentation/UIKit/UIAccessibilityCustomRotorItemResult)

A target element that a custom rotor references.

[`UIAccessibilityCustomRotorSearchPredicate`](/documentation/UIKit/UIAccessibilityCustomRotorSearchPredicate)

The search parameters that help determine the next matching custom rotor item result.

### Drag and drop support

[`UIAccessibilityLocationDescriptor`](/documentation/UIKit/UIAccessibilityLocationDescriptor)

An accessibility descriptor for a specific geometric point of interest within a view, for use by assistive apps.

### Notifications

[Notification names](/documentation/UIKit/notification-names)

The names of notifications that the accessibility system generates.

[Notification dictionary keys](/documentation/UIKit/notification-dictionary-keys)

Handle notifications with keys in the user info dictionary.

[`post(notification:argument:)`](/documentation/UIKit/UIAccessibility/post(notification:argument:))

Posts a notification to assistive apps.

### Conversions

[`convertToScreenCoordinates(_:in:)`](/documentation/UIKit/UIAccessibility/convertToScreenCoordinates(_:in:)-9ziiu)

Converts the specified rectangle from view coordinates to screen coordinates.

[`convertToScreenCoordinates(_:in:)`](/documentation/UIKit/UIAccessibility/convertToScreenCoordinates(_:in:)-6dx4a)

Converts the specified path object to screen coordinates and returns a new path object with the results.

### Convenience functions

[`focusedElement(using:)`](/documentation/UIKit/UIAccessibility/focusedElement(using:))

Returns the accessibility element that’s currently in focus by the specified assistive app.

[`hearingDevicePairedEar`](/documentation/UIKit/UIAccessibility/hearingDevicePairedEar)

The current pairing status of Made for iPhone hearing devices.

[`UIAccessibility.HearingDeviceEar`](/documentation/UIKit/UIAccessibility/HearingDeviceEar)

Constants that specify how a person is using a hearing device.

[`registerGestureConflictWithZoom()`](/documentation/UIKit/UIAccessibility/registerGestureConflictWithZoom())

Warns users that app-specific gestures conflict with the system-defined Zoom accessibility gestures.

[`requestGuidedAccessSession(enabled:completionHandler:)`](/documentation/UIKit/UIAccessibility/requestGuidedAccessSession(enabled:completionHandler:))

Transitions the app to or from Single App mode asynchronously.

[`zoomFocusChanged(zoomType:toFrame:in:)`](/documentation/UIKit/UIAccessibility/zoomFocusChanged(zoomType:toFrame:in:))

Notifies the system when the app’s focus changes to a new location.

### Capabilities

[`isAssistiveTouchRunning`](/documentation/UIKit/UIAccessibility/isAssistiveTouchRunning)

A Boolean value that indicates whether AssistiveTouch is in an enabled state.

[`isVoiceOverRunning`](/documentation/UIKit/UIAccessibility/isVoiceOverRunning)

A Boolean value that indicates whether VoiceOver is in an enabled state.

[`isSwitchControlRunning`](/documentation/UIKit/UIAccessibility/isSwitchControlRunning)

A Boolean value that indicates whether the Switch Control setting is in an enabled state.

[`isShakeToUndoEnabled`](/documentation/UIKit/UIAccessibility/isShakeToUndoEnabled)

A Boolean value that indicates whether the Shake to Undo setting is in an enabled state.

[`isClosedCaptioningEnabled`](/documentation/UIKit/UIAccessibility/isClosedCaptioningEnabled)

A Boolean value that indicates whether the Closed Captions + SDH setting is in an enabled state.

[`isBoldTextEnabled`](/documentation/UIKit/UIAccessibility/isBoldTextEnabled)

A Boolean value that indicates whether the Bold Text setting is in an enabled state.

[`isDarkerSystemColorsEnabled`](/documentation/UIKit/UIAccessibility/isDarkerSystemColorsEnabled)

A Boolean value that indicates whether the Increase Contrast setting is in an enabled state.

[`isGrayscaleEnabled`](/documentation/UIKit/UIAccessibility/isGrayscaleEnabled)

A Boolean value that indicates whether the Color Filters and the Grayscale settings are in an enabled state.

[`isGuidedAccessEnabled`](/documentation/UIKit/UIAccessibility/isGuidedAccessEnabled)

A Boolean value that indicates whether the Guided Access setting is in an enabled state.

[`isInvertColorsEnabled`](/documentation/UIKit/UIAccessibility/isInvertColorsEnabled)

A Boolean value that indicates whether the Classic Invert setting is in an enabled state.

[`isMonoAudioEnabled`](/documentation/UIKit/UIAccessibility/isMonoAudioEnabled)

A Boolean value that indicates whether the Mono Audio setting is in an enabled state.

[`isReduceMotionEnabled`](/documentation/UIKit/UIAccessibility/isReduceMotionEnabled)

A Boolean value that indicates whether the Reduce Motion setting is in an enabled state.

[`isReduceTransparencyEnabled`](/documentation/UIKit/UIAccessibility/isReduceTransparencyEnabled)

A Boolean value that indicates whether the Reduce Transparency setting is in an enabled state.

[`isSpeakScreenEnabled`](/documentation/UIKit/UIAccessibility/isSpeakScreenEnabled)

A Boolean value that indicates whether the Speak Screen setting is in an enabled state.

[`isSpeakSelectionEnabled`](/documentation/UIKit/UIAccessibility/isSpeakSelectionEnabled)

A Boolean value that indicates whether the Speak Selection setting is in an enabled state.

[`isOnOffSwitchLabelsEnabled`](/documentation/UIKit/UIAccessibility/isOnOffSwitchLabelsEnabled)

A Boolean value that indicates whether the On/Off Labels setting is in an enabled state.

[`isVideoAutoplayEnabled`](/documentation/UIKit/UIAccessibility/isVideoAutoplayEnabled)

A Boolean value that indicates whether the Auto-Play Video Previews setting is in an enabled state.

[`buttonShapesEnabled`](/documentation/UIKit/UIAccessibility/buttonShapesEnabled)

A Boolean value that indicates whether the Button Shapes setting is in an enabled state.

[`prefersCrossFadeTransitions`](/documentation/UIKit/UIAccessibility/prefersCrossFadeTransitions)

A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.

[`shouldDifferentiateWithoutColor`](/documentation/UIKit/UIAccessibility/shouldDifferentiateWithoutColor)

A Boolean value that indicates whether the Differentiate Without Color setting is in an enabled state.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
