---
name: Accessible appearance
description: Rork-Max Quality skill for Accessible appearance. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Accessible appearance


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Accessible appearance

Enhance the legibility of content in your app’s interface.

## Overview

Make content easier for people to see by making it larger, giving it greater
contrast, or reducing the amount of distracting motion.

![](images/com.apple.SwiftUI/accessible-appearance-hero@2x.png)

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/accessibility#Text-display>
in the Accessibility section of the Human Interface Guidelines.

## Topics

### Managing color

[`accessibilityIgnoresInvertColors(_:)`](/documentation/SwiftUI/View/accessibilityIgnoresInvertColors(_:))

Sets whether this view should ignore the system Smart Invert setting.

[`accessibilityInvertColors`](/documentation/SwiftUI/EnvironmentValues/accessibilityInvertColors)

Whether the system preference for Invert Colors is enabled.

[`accessibilityDifferentiateWithoutColor`](/documentation/SwiftUI/EnvironmentValues/accessibilityDifferentiateWithoutColor)

Whether the system preference for Differentiate without Color is enabled.

### Enlarging content

[`accessibilityShowsLargeContentViewer()`](/documentation/SwiftUI/View/accessibilityShowsLargeContentViewer())

Adds a default large content view to be shown by
the large content viewer.

[`accessibilityShowsLargeContentViewer(_:)`](/documentation/SwiftUI/View/accessibilityShowsLargeContentViewer(_:))

Adds a custom large content view to be shown by
the large content viewer.

[`accessibilityLargeContentViewerEnabled`](/documentation/SwiftUI/EnvironmentValues/accessibilityLargeContentViewerEnabled)

Whether the Large Content Viewer is enabled.

### Improving legibility

[`accessibilityShowButtonShapes`](/documentation/SwiftUI/EnvironmentValues/accessibilityShowButtonShapes)

Whether the system preference for Show Button Shapes is enabled.

[`accessibilityReduceTransparency`](/documentation/SwiftUI/EnvironmentValues/accessibilityReduceTransparency)

Whether the system preference for Reduce Transparency is enabled.

[`legibilityWeight`](/documentation/SwiftUI/EnvironmentValues/legibilityWeight)

The font weight to apply to text.

[`LegibilityWeight`](/documentation/SwiftUI/LegibilityWeight)

The Accessibility Bold Text user setting options.

### Minimizing motion

[`accessibilityDimFlashingLights`](/documentation/SwiftUI/EnvironmentValues/accessibilityDimFlashingLights)

Whether the setting to reduce flashing or strobing lights in video
content is on. This setting can also be used to determine if UI in
playback controls should be shown to indicate upcoming content that
includes flashing or strobing lights.

[`accessibilityPlayAnimatedImages`](/documentation/SwiftUI/EnvironmentValues/accessibilityPlayAnimatedImages)

Whether the setting for playing animations in an animated image is
on. When this value is false, any presented image that contains
animation should not play automatically.

[`accessibilityReduceMotion`](/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion)

Whether the system preference for Reduce Motion is enabled.

### Using assistive access

[`accessibilityAssistiveAccessEnabled`](/documentation/SwiftUI/EnvironmentValues/accessibilityAssistiveAccessEnabled)

A Boolean value that indicates whether Assistive Access is in use.

[`AssistiveAccess`](/documentation/SwiftUI/AssistiveAccess)

A scene that presents an interface appropriate for Assistive Access on iOS
and iPadOS. On other platforms, this scene is unused.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
