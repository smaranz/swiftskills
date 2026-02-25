---
name: MACOS Views and Controls
description: Rork-Max Quality skill for MACOS Views and Controls. Platform-native patterns and best practices for macos development.
---

# MACOS Views and Controls

Present your content onscreen and handle user input and events.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class SidebarViewController: NSViewController {
    private let outlineView = NSOutlineView()

    override func loadView() {
        let scrollView = NSScrollView()
        scrollView.documentView = outlineView
        scrollView.hasVerticalScroller = true
        self.view = scrollView

        let column = NSTableColumn(identifier: .init("main"))
        outlineView.addTableColumn(column)
        outlineView.headerView = nil
        outlineView.outlineTableColumn = column
    }
}
```

## 💎 Elite Implementation Tips

- Use `NSOutlineView` for sidebar tree structures, `NSTableView` for flat data
- Wrap views in `NSScrollView` with `hasVerticalScroller = true` for scrollable content
- Use `NSSplitViewController` for resizable multi-pane macOS layouts

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

### View fundamentals

| API | Purpose |
|-----|---------|
| `NSView` | The infrastructure for drawing, printing, and handling events in an app. |
| `NSControl` | A specialized view, such as a button or text field, that notifies your app of relevant events using the target-action design pattern. |
| `NSCell` | A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](/documentation/AppKit/NSView) subclass. |
| `NSActionCell` | An active area inside a control. |

### Container views

| API | Purpose |
|-----|---------|
| `Grid View` | Arrange views in a flexible grid, and handle the layout associated with those views. |
| `NSSplitView` | A view that arranges two or more views in a linear stack running horizontally or vertically. |
| `Organize Your User Interface with a Stack View` | Group individual views in your app’s user interface into a scrollable stack view. |
| `NSStackView` | A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes. |
| `NSTabView` | A multipage interface that displays one page at a time. |
| `Scroll View` | Provide an interface for navigating content that is too large to fit in the available space. |

### Content views

| API | Purpose |
|-----|---------|
| `Browser View` | Provide a column-based interface for viewing and navigating hierarchical information. |
| `Collection View` | Display one or more subviews in a highly configurable arrangement. |
| `Outline View` | Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one. |
| `Table View` | Display custom data in rows and columns. |
| `NSTextView` | A view that draws text and handles user interactions with that text. |

### Controls

| API | Purpose |
|-----|---------|
| `NSButton` | A control that defines an area on the screen that a user clicks to trigger an action. |
| `NSColorWell` | A control that displays a color value and lets the user change that color value. |
| `Combo Box` | Display a list of values in a pop-up menu that lets the user select a value or type in a custom value. |
| `NSComboButton` | A button with a pull-down menu and a default action. |
| `Date Picker` | Display a calendar date and provide controls for editing the date value. |
| `NSImageView` | A display of image data in a frame. |
| `NSLevelIndicator` | A visual representation of a level or quantity, using discrete values. |
| `Path Control` | A display of a file system path or virtual path information. |

### Liquid Glass effects

| API | Purpose |
|-----|---------|
| `NSGlassEffectView` | A view that embeds its content view in a dynamic glass effect. |
| `NSGlassEffectView.Style` | — |
| `NSGlassEffectContainerView` | A view that efficiently merges descendant glass effect views together when they are within a specified proximity to each other. |

### Interacting with adjacent views

| API | Purpose |
|-----|---------|
| `NSBackgroundExtensionView` | A view that extends content to fill its own bounds. |

### Visual adornments

| API | Purpose |
|-----|---------|
| `NSVisualEffectView` | A view that adds translucency and vibrancy effects to the views in your interface. |
| `NSBox` | A stylized rectangular box with an optional title. |

### UI validation

| API | Purpose |
|-----|---------|
| `NSUserInterfaceValidations` | A protocol that a custom class can adopt to manage the enabled state of a UI element. |
| `NSValidatedUserInterfaceItem` | A protocol that a custom class can adopt to manage the automatic enablement of a UI control. |

### Tool tips

| API | Purpose |
|-----|---------|
| `NSViewToolTipOwner` | A set of methods for dynamically associating a tool tip with a view. |

### Related types

| API | Purpose |
|-----|---------|
| `NSRectAlignment` | Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction. |
| `NSDirectionalEdgeInsets` | The inset distances for views, taking the user interface layout direction into account. |
| `NSDirectionalRectEdge` | — |
