---
name: MACOS Mouse, Keyboard, and Trackpad
description: Rork-Max Quality skill for MACOS Mouse, Keyboard, and Trackpad. Platform-native patterns and best practices for macos development.
---

# MACOS Mouse, Keyboard, and Trackpad

Handle events related to mouse, keyboard, and trackpad input.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class RorkWindowController: NSWindowController {
    convenience init() {
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 600, height: 400),
            styleMask: [.titled, .closable, .resizable, .miniaturizable],
            backing: .buffered,
            defer: false
        )
        window.title = "Mouse, Keyboard, and Trackpad"
        window.center()
        self.init(window: window)
    }
}
```

## 💎 Elite Implementation Tips

- Follow the MACOS Human Interface Guidelines for native feel.
- Use system-standard AppKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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
