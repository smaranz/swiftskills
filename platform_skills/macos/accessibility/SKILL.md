---
name: MACOS Accessibility for AppKit
description: Rork-Max Quality skill for MACOS Accessibility for AppKit. Platform-native patterns and best practices for macos development.
---

# MACOS Accessibility for AppKit

Make your AppKit apps accessible to everyone who uses macOS.

## 🚀 Rork-Max Quality Snippet

```swift
import AppKit

class AccessibleCustomView: NSView {
    override func isAccessibilityElement() -> Bool { true }
    override func accessibilityRole() -> NSAccessibility.Role? { .button }
    override func accessibilityLabel() -> String? { "Custom Action" }
    override func accessibilityHelp() -> String? { "Performs the custom action" }

    override func accessibilityPerformPress() -> Bool {
        performAction()
        return true
    }

    func performAction() { }
}
```

## 💎 Elite Implementation Tips

- Override `accessibilityRole()` to tell VoiceOver what the element IS
- Override `accessibilityPerformPress()` for custom VoiceOver action handling
- Test with Accessibility Inspector (Xcode → Open Developer Tool → Accessibility Inspector)

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

### AppKit Elements

| API | Purpose |
|-----|---------|
| `NSAccessibilityProtocol` | The complete list of properties and methods for accessible elements. |
| `NSAccessibility` | A namespace for accessibility symbols for AppKit apps. |

### Custom View Subclasses

| API | Purpose |
|-----|---------|
| `Custom Controls` | Support accessibility for custom user interface elements by adopting a role-specific protocol and implementing its methods. |
| `Accessibility Functions` | Global accessibility functions for custom views and controls. |

### Custom Elements

| API | Purpose |
|-----|---------|
| `NSAccessibilityElement` | The basic infrastructure necessary for interacting with an assistive app. |

### Accessibility Types

| API | Purpose |
|-----|---------|
| `NSAccessibility.Action` | Constants that describe types of actions. |
| `NSAccessibility.AnnotationAttributeKey` | Keys for annotation attributes. |
| `NSAccessibilityAnnotationPosition` | Constants that specify the position where the annotation applies. |
| `NSAccessibility.Attribute` | Constants that describe attributes. |
| `NSAccessibility.FontAttributeKey` | Keys for font attributes. |
| `NSAccessibilityOrientation` | Values that indicate the orientation of accessibility elements, such as scroll bars and split views. |
| `NSAccessibility.OrientationValue` | Values that indicate the orientation of user interface elements, such as scroll bars and split views. |
| `NSAccessibility.ParameterizedAttribute` | Values that describe parameterized attributes. |
