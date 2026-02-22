---
name: WATCHOS Storyboard support
description: Rork-Max Quality skill for WATCHOS Storyboard support on watchos. Based on official Apple WatchKit Documentation.
---

# WATCHOS Storyboard support

## 🚀 Rork-Max Quality Snippet

```swift
// Premium WATCHOS Storyboard support Implementation for watchos
// Focus on platform-native excellence

import SwiftUI
#if os(watchos)
// WatchKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality WATCHOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the watchos native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for watchos: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Storyboard support

Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.

## Discussion

The WatchKit framework includes classes to control user interface elements that you lay out in your storyboard. Storyboard-based layouts typically require an interface controller for each scene. Each controller can manage one or more controls and subviews, such as tables, buttons, sliders, and other visual elements. Use the classes in this collection to configure your visual elements at runtime, and to respond to user interactions.

> Note:
> When you build the user interface for your watchOS app, you can design the interface in a storyboard and use WatchKit classes to connect to the interface elements, or you can use SwiftUI to declare the interface in code. Because apps built with SwiftUI have more freedom, power, and control over the user interface than apps designed in a storyboard, strongly consider using SwiftUI when creating your watchOS app. For more information, see `Building a watchOS App`.

## Topics

### User interface basics

[Building watchOS app Interfaces Using the Storyboard](/documentation/WatchKit/building-watchos-app-interfaces-using-the-storyboard)

Create the user interface for your watchOS app by nesting stacks.

[`WKInterfaceObject`](/documentation/WatchKit/WKInterfaceObject)

An object that provides information that is common to all interface objects in your watchOS app.

[`WKInterfaceController`](/documentation/WatchKit/WKInterfaceController)

A class that provides the infrastructure for managing the interface in a watchOS app.

[`WKAlertAction`](/documentation/WatchKit/WKAlertAction)

An object that encapsulates information about a button displayed in an alert or action sheet.

[`WKAccessibilityImageRegion`](/documentation/WatchKit/WKAccessibilityImageRegion)

An object that defines a portion of an image that you want to call out separately to an assistive app.

[`WKAccessibilityIsVoiceOverRunning()`](/documentation/WatchKit/WKAccessibilityIsVoiceOverRunning())

Returns a Boolean value indicating whether VoiceOver is running.

[`WKAccessibilityIsReduceMotionEnabled()`](/documentation/WatchKit/WKAccessibilityIsReduceMotionEnabled())

Returns a Boolean value indicating whether reduced motion is enabled.

### Controls

[`WKInterfaceLabel`](/documentation/WatchKit/WKInterfaceLabel)

An interface element that displays static text.

[`WKInterfaceDate`](/documentation/WatchKit/WKInterfaceDate)

A label that displays the current date or time.

[`WKInterfaceTimer`](/documentation/WatchKit/WKInterfaceTimer)

A label that displays a countdown or count-up timer.

[`WKInterfaceButton`](/documentation/WatchKit/WKInterfaceButton)

A button in the user interface of your watchOS app.

[`WKInterfaceAuthorizationAppleIDButton`](/documentation/WatchKit/WKInterfaceAuthorizationAppleIDButton)

A button that you can use to trigger a Sign in with Apple request.

[`WKInterfacePaymentButton`](/documentation/WatchKit/WKInterfacePaymentButton)

A button that you can use to trigger payments through Apple Pay.

[`WKInterfaceTextField`](/documentation/WatchKit/WKInterfaceTextField)

An interface element that displays an editable text area.

[`WKInterfaceSwitch`](/documentation/WatchKit/WKInterfaceSwitch)

An interface element that toggles between an On and Off state.

[`WKInterfaceSlider`](/documentation/WatchKit/WKInterfaceSlider)

An interface element that lets users select a single floating-point value from a range of values.

[`WKInterfaceActivityRing`](/documentation/WatchKit/WKInterfaceActivityRing)

A view that displays data from a HealthKit activity summary object.

[`WKInterfaceMap`](/documentation/WatchKit/WKInterfaceMap)

An interface element that displays a noninteractive map for the location you specify.

### Containers

[`WKInterfaceGroup`](/documentation/WatchKit/WKInterfaceGroup)

A container for one or more interface objects.

[`WKInterfaceSeparator`](/documentation/WatchKit/WKInterfaceSeparator)

An interface object that displays a visual separator within a group.

[`WKInterfaceTable`](/documentation/WatchKit/WKInterfaceTable)

An object that creates and manages the contents of a single-column table interface.

[`WKInterfacePicker`](/documentation/WatchKit/WKInterfacePicker)

An interface element that presents a scrolling list of items for the user to choose from.

### Audio

[Playing Background Audio](/documentation/WatchKit/playing-background-audio)

Enable background audio in your app to provide a seamless playback experience.

[Adding a Now Playing View](/documentation/WatchKit/adding-a-now-playing-view)

Provide a view that controls the currently playing audio from your app.

[`WKInterfaceVolumeControl`](/documentation/WatchKit/WKInterfaceVolumeControl)

An interface element that provides control of the audio volume from the watch or a paired iPhone.

  <doc://com.apple.documentation/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut>

[`WKAudioFilePlayer`](/documentation/WatchKit/WKAudioFilePlayer)

An object that controls playback of a single audio item.

[`WKAudioFileQueuePlayer`](/documentation/WatchKit/WKAudioFileQueuePlayer)

An object that controls playback of one or more audio items.

[`WKAudioFilePlayerItem`](/documentation/WatchKit/WKAudioFilePlayerItem)

An object that manages the presentation state of an audio file while it is playing.

[`WKAudioFileAsset`](/documentation/WatchKit/WKAudioFileAsset)

An object that stores a reference to an audio file and provides metadata information about that file.

### Images and movies

[`WKInterfaceImage`](/documentation/WatchKit/WKInterfaceImage)

An image that can be displayed in the interface of your watchOS app.

[`WKImage`](/documentation/WatchKit/WKImage)

A wrapper for images you use with a picker interface.

[`WKImageAnimatable`](/documentation/WatchKit/WKImageAnimatable)

A collection of methods you can use to control the playback of animated images.

[`WKInterfaceMovie`](/documentation/WatchKit/WKInterfaceMovie)

An interface element that lets you play video and audio content in your watchOS app.

[`WKInterfaceInlineMovie`](/documentation/WatchKit/WKInterfaceInlineMovie)

An interface element that displays a video’s poster image and supports inline playing of the video.

[`WKInterfaceHMCamera`](/documentation/WatchKit/WKInterfaceHMCamera)

An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.

[`WKVideoGravity`](/documentation/WatchKit/WKVideoGravity)

Constants indicating the appearance of video content.

### Graphics and games

[`WKInterfaceSKScene`](/documentation/WatchKit/WKInterfaceSKScene)

A visual WatchKit element that displays a SpriteKit scene.

[`WKInterfaceSCNScene`](/documentation/WatchKit/WKInterfaceSCNScene)

An object that lets you manage SceneKit content for display in your app.

### Event handling

[`WKCrownSequencer`](/documentation/WatchKit/WKCrownSequencer)

An object that reports the current state of the digital crown, including its rotational speed when it is in motion.

[`WKCrownDelegate`](/documentation/WatchKit/WKCrownDelegate)

A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.

[`WKGestureRecognizer`](/documentation/WatchKit/WKGestureRecognizer)

The base class for all other gesture recognizer classes.

[`WKLongPressGestureRecognizer`](/documentation/WatchKit/WKLongPressGestureRecognizer)

A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.

[`WKPanGestureRecognizer`](/documentation/WatchKit/WKPanGestureRecognizer)

A gesture recognizer that interprets a touch event that moves around the screen.

[`WKSwipeGestureRecognizer`](/documentation/WatchKit/WKSwipeGestureRecognizer)

A gesture recognizer that interprets swiping gestures in one or more directions.

[`WKTapGestureRecognizer`](/documentation/WatchKit/WKTapGestureRecognizer)

A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.

### Notifications

[`WKUserNotificationInterfaceController`](/documentation/WatchKit/WKUserNotificationInterfaceController)

An interface controller object that manages a dynamic user interface for a local or remote notification.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
