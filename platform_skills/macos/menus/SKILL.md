---
name: MACOS Menus, Cursors, and the Dock
description: Rork-Max Quality skill for MACOS Menus, Cursors, and the Dock. Platform-native patterns and best practices for macos development.
---

# MACOS Menus, Cursors, and the Dock

Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.

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
        window.title = "Menus, Cursors, and the Dock"
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

### Menus

| API | Purpose |
|-----|---------|
| `NSMenu` | An object that manages an app’s menus. |
| `NSMenuItem` | A command item in an app menu. |
| `NSMenuItemBadge` | A control that provides additional quantitative information specific to a menu item, such as the number of available updates. |
| `NSMenuDelegate` | The optional methods implemented by delegates of [`NSMenu`](/documentation/AppKit/NSMenu) objects to manage menu display and handle some events. |

### Menu Bar Items

| API | Purpose |
|-----|---------|
| `NSStatusBar` | An object that manages a collection of status items displayed within the system-wide menu bar. |
| `NSStatusItem` | An individual element displayed in the system menu bar. |
| `NSStatusBarButton` | The appearance and behavior of an item in the systemwide menu bar. |

### Cursors

| API | Purpose |
|-----|---------|
| `NSCursor` | A pointer (also called a cursor). |
| `NSTrackingArea` | A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region. |

### The Dock

| API | Purpose |
|-----|---------|
| `NSDockTile` | The visual representation of your app’s miniaturized windows and app icon as they appear in the Dock. |
| `NSDockTilePlugIn` | A set of methods implemented by plug-ins that allow an app’s Dock tile to be customized while the app is not running. |
