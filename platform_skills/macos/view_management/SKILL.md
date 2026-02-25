---
name: MACOS View Management
description: Rork-Max Quality skill for MACOS View Management. Platform-native patterns and best practices for macos development.
---

# MACOS View Management

Manage your user interface, including the size and position of views in a window.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class DocumentWindowController: NSWindowController {
    convenience init(document: NSDocument) {
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 800, height: 600),
            styleMask: [.titled, .closable, .resizable, .miniaturizable, .fullSizeContentView],
            backing: .buffered, defer: false
        )
        window.titlebarAppearsTransparent = true
        window.center()
        self.init(window: window)
        window.contentViewController = MainSplitViewController()
    }
}
```

## 💎 Elite Implementation Tips

- Use `.fullSizeContentView` with `.titlebarAppearsTransparent` for modern macOS window styling
- Set `contentViewController` instead of `contentView` for proper view controller lifecycle
- Use `NSSplitViewController` with `NSSplitViewItem` for resizable panes

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

### Content Controllers

| API | Purpose |
|-----|---------|
| `NSWindowController` | A controller that manages a window, usually a window stored in a nib file. |
| `NSViewController` | A controller that manages a view, typically loaded from a nib file. |
| `NSTitlebarAccessoryViewController` | An object that manages a custom view—known as an accessory view—in the title bar–toolbar area of a window. |

### Split View Interface

| API | Purpose |
|-----|---------|
| `NSSplitViewController` | An object that manages an array of adjacent child views, and has a split view object for managing dividers between those views. |
| `NSSplitView` | A view that arranges two or more views in a linear stack running horizontally or vertically. |
| `NSSplitViewItem` | An item in a split view controller. |

### Stack View Interface

| API | Purpose |
|-----|---------|
| `NSStackView` | A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes. |

### Tab View Interface

| API | Purpose |
|-----|---------|
| `NSTabViewController` | A container view controller that manages a tab view interface, which organizes multiple pages of content but displays only one page at a time. |
| `NSTabView` | A multipage interface that displays one page at a time. |
| `NSTabViewItem` | An item in a tab view. |

### Paged Interface

| API | Purpose |
|-----|---------|
| `NSPageController` | An object that controls swipe navigation and animations between views or view content. |

### Media Library Interface

| API | Purpose |
|-----|---------|
| `NSMediaLibraryBrowserController` | An object that configures and displays a Media Library Browser panel. |
