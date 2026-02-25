---
name: MACOS Mouse, Keyboard, and Trackpad
description: Rork-Max Quality skill for MACOS Mouse, Keyboard, and Trackpad. Platform-native patterns and best practices for macos development.
---

# MACOS Mouse, Keyboard, and Trackpad

Handle events related to mouse, keyboard, and trackpad input.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class TrackpadViewController: NSViewController {
    override func loadView() {
        let view = NSView(frame: NSRect(x: 0, y: 0, width: 400, height: 300))
        let pan = NSPanGestureRecognizer(target: self, action: #selector(handlePan))
        let magnify = NSMagnificationGestureRecognizer(target: self, action: #selector(handleZoom))
        view.addGestureRecognizer(pan)
        view.addGestureRecognizer(magnify)
        self.view = view
    }

    @objc func handlePan(_ gesture: NSPanGestureRecognizer) {
        let translation = gesture.translation(in: view)
        // Apply translation
        gesture.setTranslation(.zero, in: view)
    }

    @objc func handleZoom(_ gesture: NSMagnificationGestureRecognizer) {
        let scale = 1.0 + gesture.magnification
        // Apply scale
    }
}
```

## 💎 Elite Implementation Tips

- Support trackpad gestures (pan, magnify, rotate) for natural macOS interactions
- Use `NSEvent.addLocalMonitorForEvents` for app-wide keyboard shortcut handling
- Implement `NSMenuItemValidation` to enable/disable menu items based on state

## When to Use

- Building native macOS features with AppKit
- Implementing menu bar items, dock menus, and macOS-specific UI
- Working with NSWindow, NSViewController, and AppKit patterns

## Best Practices

- Support keyboard shortcuts and menu bar commands for every major action
- Use NSToolbar for window-level controls; avoid floating toolbars
- Support trackpad gestures and the Magic Mouse for natural interactions

## Common Pitfalls

- Ignoring the menu bar — macOS users expect all actions available via menus
- Not testing with multiple windows open simultaneously
- Forgetting to handle the app running without any windows (macOS apps don't quit on last window close)

## Key APIs

### Responder Objects

| API | Purpose |
|-----|---------|
| `NSResponder` | An abstract class that forms the basis of event and command processing in AppKit. |

### Mouse, Keyboard, and Touch Events

| API | Purpose |
|-----|---------|
| `NSEvent` | An object that contains information about an input action, such as a mouse click or a key press. |
| `NSTouch` | A snapshot of a particular touch at an instant in time. |

### Trackpad

| API | Purpose |
|-----|---------|
| `NSPressureConfiguration` | An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events. |
| `NSHapticFeedbackManager` | An object that provides access to the haptic feedback management attributes on a system with a Force Touch trackpad. |

### Constants

| API | Purpose |
|-----|---------|
| `NSEvent.EventTypeMask` | Constants that you use to filter out specific event types from the stream of incoming events. |
| `NSEvent.ButtonMask` | Constants you use to identify the activated tablet buttons in an event. |
| `NSEvent.ModifierFlags` | Flags that represent key states in an event object. |
| `NSEvent.Phase` | Constants that represent the possible phases during an event phase. |
| `NSEvent.SwipeTrackingOptions` | Constants that specify swipe-tracking options. |
| `init(type:)` | Returns the event mask for the specified type. |
