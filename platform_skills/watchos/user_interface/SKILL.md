---
name: WATCHOS Storyboard support
description: Rork-Max Quality skill for WATCHOS Storyboard support. Platform-native patterns and best practices for watchos development.
---

# WATCHOS Storyboard support

Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct RorkWatchView: View {
    var body: some View {
        NavigationStack {
            List {
                Text("Storyboard support")
                    .font(.headline)
            }
            .navigationTitle("Rork")
        }
    }
}
```

## 💎 Elite Implementation Tips

- Follow the WATCHOS Human Interface Guidelines for native feel.
- Use system-standard WatchKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building watchOS apps with glanceable, quick interactions
- Implementing complications, background refresh, and workout tracking
- Optimizing for the small screen and limited resources of Apple Watch

## Best Practices

- Keep interactions under 5 seconds — watchOS is for glances, not sessions
- Use `.digitalCrownRotation()` for scroll and value adjustment
- Schedule background refresh tasks for up-to-date complications

## Common Pitfalls

- Trying to replicate the iPhone UI on watch — design for the wrist
- Ignoring battery constraints — minimize animations and network requests
- Forgetting that watchOS apps have very limited background execution time

## Key APIs

### User interface basics

| API | Purpose |
|-----|---------|
| `Building watchOS app Interfaces Using the Storyboard` | Create the user interface for your watchOS app by nesting stacks. |
| `WKInterfaceObject` | An object that provides information that is common to all interface objects in your watchOS app. |
| `WKInterfaceController` | A class that provides the infrastructure for managing the interface in a watchOS app. |
| `WKAlertAction` | An object that encapsulates information about a button displayed in an alert or action sheet. |
| `WKAccessibilityImageRegion` | An object that defines a portion of an image that you want to call out separately to an assistive app. |
| `WKAccessibilityIsVoiceOverRunning()` | Returns a Boolean value indicating whether VoiceOver is running. |
| `WKAccessibilityIsReduceMotionEnabled()` | Returns a Boolean value indicating whether reduced motion is enabled. |

### Controls

| API | Purpose |
|-----|---------|
| `WKInterfaceLabel` | An interface element that displays static text. |
| `WKInterfaceDate` | A label that displays the current date or time. |
| `WKInterfaceTimer` | A label that displays a countdown or count-up timer. |
| `WKInterfaceButton` | A button in the user interface of your watchOS app. |
| `WKInterfaceAuthorizationAppleIDButton` | A button that you can use to trigger a Sign in with Apple request. |
| `WKInterfacePaymentButton` | A button that you can use to trigger payments through Apple Pay. |
| `WKInterfaceTextField` | An interface element that displays an editable text area. |
| `WKInterfaceSwitch` | An interface element that toggles between an On and Off state. |

### Containers

| API | Purpose |
|-----|---------|
| `WKInterfaceGroup` | A container for one or more interface objects. |
| `WKInterfaceSeparator` | An interface object that displays a visual separator within a group. |
| `WKInterfaceTable` | An object that creates and manages the contents of a single-column table interface. |
| `WKInterfacePicker` | An interface element that presents a scrolling list of items for the user to choose from. |

### Audio

| API | Purpose |
|-----|---------|
| `Playing Background Audio` | Enable background audio in your app to provide a seamless playback experience. |
| `Adding a Now Playing View` | Provide a view that controls the currently playing audio from your app. |
| `WKInterfaceVolumeControl` | An interface element that provides control of the audio volume from the watch or a paired iPhone. |
| `WKAudioFilePlayer` | An object that controls playback of a single audio item. |
| `WKAudioFileQueuePlayer` | An object that controls playback of one or more audio items. |
| `WKAudioFilePlayerItem` | An object that manages the presentation state of an audio file while it is playing. |
| `WKAudioFileAsset` | An object that stores a reference to an audio file and provides metadata information about that file. |

### Images and movies

| API | Purpose |
|-----|---------|
| `WKInterfaceImage` | An image that can be displayed in the interface of your watchOS app. |
| `WKImage` | A wrapper for images you use with a picker interface. |
| `WKImageAnimatable` | A collection of methods you can use to control the playback of animated images. |
| `WKInterfaceMovie` | An interface element that lets you play video and audio content in your watchOS app. |
| `WKInterfaceInlineMovie` | An interface element that displays a video’s poster image and supports inline playing of the video. |
| `WKInterfaceHMCamera` | An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit. |
| `WKVideoGravity` | Constants indicating the appearance of video content. |

### Graphics and games

| API | Purpose |
|-----|---------|
| `WKInterfaceSKScene` | A visual WatchKit element that displays a SpriteKit scene. |
| `WKInterfaceSCNScene` | An object that lets you manage SceneKit content for display in your app. |

### Event handling

| API | Purpose |
|-----|---------|
| `WKCrownSequencer` | An object that reports the current state of the digital crown, including its rotational speed when it is in motion. |
| `WKCrownDelegate` | A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops. |
| `WKGestureRecognizer` | The base class for all other gesture recognizer classes. |
| `WKLongPressGestureRecognizer` | A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time. |
| `WKPanGestureRecognizer` | A gesture recognizer that interprets a touch event that moves around the screen. |
| `WKSwipeGestureRecognizer` | A gesture recognizer that interprets swiping gestures in one or more directions. |
| `WKTapGestureRecognizer` | A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen. |

### Notifications

| API | Purpose |
|-----|---------|
| `WKUserNotificationInterfaceController` | An interface controller object that manages a dynamic user interface for a local or remote notification. |
