---
name: MACOS View Layout
description: Rork-Max Quality skill for MACOS View Layout. Platform-native patterns and best practices for macos development.
---

# MACOS View Layout

Position and size views using a stack view or Auto Layout constraints.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class ToolbarLayoutController: NSViewController {
    override func loadView() {
        let stack = NSStackView()
        stack.orientation = .vertical
        stack.spacing = 12
        stack.edgeInsets = NSEdgeInsets(top: 16, left: 16, bottom: 16, right: 16)

        let header = NSTextField(labelWithString: "Settings")
        header.font = .preferredFont(forTextStyle: .title1)
        stack.addArrangedSubview(header)

        let toggle = NSSwitch()
        toggle.state = .on
        let row = NSStackView(views: [NSTextField(labelWithString: "Dark Mode"), toggle])
        stack.addArrangedSubview(row)

        self.view = stack
    }
}
```

## 💎 Elite Implementation Tips

- Use `NSStackView` for most layouts — it handles alignment and distribution automatically
- Use `NSGridView` for two-dimensional form-style layouts (label + control grids)
- Leverage Auto Layout constraints for fine-tuned positioning beyond stack views

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

### Stack View

| API | Purpose |
|-----|---------|
| `NSStackView` | A view that arranges an array of views horizontally or vertically and updates their placement and sizing when the window size changes. |

### Auto Layout Constraints

| API | Purpose |
|-----|---------|
| `NSLayoutConstraint` | The relationship between two user interface objects that must be satisfied by the constraint-based layout system. |

### Layout Guides

| API | Purpose |
|-----|---------|
| `NSLayoutGuide` | A rectangular area that can interact with Auto Layout. |
| `NSLayoutDimension` | A factory class for creating size-based layout constraint objects using a fluent API. |
| `NSViewLayoutRegion` | — |

### Anchors

| API | Purpose |
|-----|---------|
| `NSLayoutAnchor` | A factory class for creating layout constraint objects using a fluent API. |
| `NSLayoutXAxisAnchor` | A factory class for creating horizontal layout constraint objects using a fluent API. |
| `NSLayoutYAxisAnchor` | A factory class for creating vertical layout constraint objects using a fluent API. |

### View Compression

| API | Purpose |
|-----|---------|
| `NSDictionaryOfVariableBindings` | Creates a dictionary wherein the keys are string representations of the corresponding values’ variable names. |
| `NSUserInterfaceCompression` | A protocol that describes how a UI control should redisplay when space is restricted. |
