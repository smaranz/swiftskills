---
name: Accessibility fundamentals
description: Rork-Max Quality skill for Accessibility fundamentals. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Accessibility fundamentals


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Accessibility fundamentals

Make your SwiftUI apps accessible to everyone, including people with
disabilities.

## Overview

Like all Apple UI frameworks, SwiftUI comes with built-in
accessibility support. The framework introspects common elements like
navigation views, lists, text fields, sliders, buttons, and so on, and
provides basic accessibility labels and values by default. You
don’t have to do any extra work to enable these standard accessibility
features.

![](images/com.apple.SwiftUI/accessibility-fundamentals-hero@2x.png)

SwiftUI also provides tools to help you enhance the accessibility
of your app. To find out what enhancements you need, try using your app
with accessibility features like VoiceOver, Voice Control, and Switch
Control, or get feedback from users of your app that regularly use
these features. Then use the accessibility view modifiers that SwiftUI
provides to improve the experience. For example, you can explicitly add
accessibility labels to elements in your UI using the
[`accessibilityLabel(_:)`](/documentation/SwiftUI/View/accessibilityLabel(_:)) or the
[`accessibilityValue(_:)`](/documentation/SwiftUI/View/accessibilityValue(_:)) view modifier.

Customize your use of accessibility modifiers for all the platforms that your
app runs on. For example, you may need to adjust the
accessibility elements for a companion Apple Watch app that shares a common
code base with an iOS app. If you integrate AppKit or UIKit controls in
SwiftUI, expose any accessibility labels and make them accessible from your
[`NSViewRepresentable`](/documentation/SwiftUI/NSViewRepresentable) or [`UIViewRepresentable`](/documentation/SwiftUI/UIViewRepresentable) views, or provide custom
accessibility information if the underlying accessibility labels aren’t
available.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/accessibility>
in the Human Interface Guidelines.

## Topics

### Essentials

[Creating accessible views](/documentation/SwiftUI/creating-accessible-views)

Make your app accessible to everyone by applying accessibility modifiers to your SwiftUI views.

### Creating accessible elements

[`accessibilityElement(children:)`](/documentation/SwiftUI/View/accessibilityElement(children:))

Creates a new accessibility element, or modifies the
[`AccessibilityChildBehavior`](/documentation/SwiftUI/AccessibilityChildBehavior) of the existing accessibility element.

[`accessibilityChildren(children:)`](/documentation/SwiftUI/View/accessibilityChildren(children:))

Replaces the existing accessibility element’s children with one or
more new synthetic accessibility elements.

[`accessibilityRepresentation(representation:)`](/documentation/SwiftUI/View/accessibilityRepresentation(representation:))

Replaces one or more accessibility elements for this view with new
accessibility elements.

[`AccessibilityChildBehavior`](/documentation/SwiftUI/AccessibilityChildBehavior)

Defines the behavior for the child elements of the new parent element.

### Identifying elements

[`accessibilityIdentifier(_:)`](/documentation/SwiftUI/View/accessibilityIdentifier(_:))

Uses the string you specify to identify the view.

[`accessibilityIdentifier(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityIdentifier(_:isEnabled:))

Uses the string you specify to identify the view.

### Hiding elements

[`accessibilityHidden(_:)`](/documentation/SwiftUI/View/accessibilityHidden(_:))

Specifies whether to hide this view from system accessibility features.

[`accessibilityHidden(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityHidden(_:isEnabled:))

Specifies whether to hide this view from system accessibility features.

### Supporting types

[`AccessibilityTechnologies`](/documentation/SwiftUI/AccessibilityTechnologies)

Accessibility technologies available to the system.

[`AccessibilityAttachmentModifier`](/documentation/SwiftUI/AccessibilityAttachmentModifier)

A view modifier that adds accessibility properties to the view



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
