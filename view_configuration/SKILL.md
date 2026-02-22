---
name: View configuration
description: Rork-Max Quality skill for View configuration. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# View configuration


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# View configuration

Adjust the characteristics of views in a hierarchy.

## Overview

SwiftUI enables you to tune the appearance and behavior of views using view
modifiers.

![](images/com.apple.SwiftUI/view-configuration-hero@2x.png)

Many modifiers apply to specific kinds of views or behaviors, but
some apply more generally. For example, you can conditionally hide any view
by dynamically setting its opacity, display contextual help when people hover
over a view, or request the light or dark appearance for a view.

## Topics

### Hiding views

[`opacity(_:)`](/documentation/SwiftUI/View/opacity(_:))

Sets the transparency of this view.

[`hidden()`](/documentation/SwiftUI/View/hidden())

Hides this view unconditionally.

### Hiding system elements

[`labelsHidden()`](/documentation/SwiftUI/View/labelsHidden())

Hides the labels of any controls contained within this view.

[`labelsVisibility(_:)`](/documentation/SwiftUI/View/labelsVisibility(_:))

Controls the visibility of labels of any controls contained within this
view.

[`labelsVisibility`](/documentation/SwiftUI/EnvironmentValues/labelsVisibility)

The labels visibility set by [`labelsVisibility(_:)`](/documentation/SwiftUI/View/labelsVisibility(_:)).

[`menuIndicator(_:)`](/documentation/SwiftUI/View/menuIndicator(_:))

Sets the menu indicator visibility for controls within this view.

[`statusBarHidden(_:)`](/documentation/SwiftUI/View/statusBarHidden(_:))

Sets the visibility of the status bar.

[`persistentSystemOverlays(_:)`](/documentation/SwiftUI/View/persistentSystemOverlays(_:))

Sets the preferred visibility of the non-transient system views
overlaying the app.

[`Visibility`](/documentation/SwiftUI/Visibility)

The visibility of a UI element, chosen automatically based on
the platform, current context, and other factors.

### Managing view interaction

[`disabled(_:)`](/documentation/SwiftUI/View/disabled(_:))

Adds a condition that controls whether users can interact with this
view.

[`isEnabled`](/documentation/SwiftUI/EnvironmentValues/isEnabled)

A Boolean value that indicates whether the view associated with this
environment allows user interaction.

[`interactionActivityTrackingTag(_:)`](/documentation/SwiftUI/View/interactionActivityTrackingTag(_:))

Sets a tag that you use for tracking interactivity.

[`invalidatableContent(_:)`](/documentation/SwiftUI/View/invalidatableContent(_:))

Mark the receiver as their content might be invalidated.

### Providing contextual help

[`help(_:)`](/documentation/SwiftUI/View/help(_:))

Adds help text to a view using a text view that you provide.

### Detecting and requesting the light or dark appearance

[`preferredColorScheme(_:)`](/documentation/SwiftUI/View/preferredColorScheme(_:))

Sets the preferred color scheme for this presentation.

[`colorScheme`](/documentation/SwiftUI/EnvironmentValues/colorScheme)

The color scheme of this environment.

[`ColorScheme`](/documentation/SwiftUI/ColorScheme)

The possible color schemes, corresponding to the light and dark appearances.

### Getting the color scheme contrast

[`colorSchemeContrast`](/documentation/SwiftUI/EnvironmentValues/colorSchemeContrast)

The contrast associated with the color scheme of this environment.

[`ColorSchemeContrast`](/documentation/SwiftUI/ColorSchemeContrast)

The contrast between the app’s foreground and background colors.

### Configuring passthrough

[`preferredSurroundingsEffect(_:)`](/documentation/SwiftUI/View/preferredSurroundingsEffect(_:))

Applies an effect to passthrough video.

[`SurroundingsEffect`](/documentation/SwiftUI/SurroundingsEffect)

Effects that the system can apply to passthrough video.

[`BreakthroughEffect`](/documentation/SwiftUI/BreakthroughEffect)

### Redacting private content

  <doc://com.apple.documentation/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state>

[`privacySensitive(_:)`](/documentation/SwiftUI/View/privacySensitive(_:))

Marks the view as containing sensitive, private user data.

[`redacted(reason:)`](/documentation/SwiftUI/View/redacted(reason:))

Adds a reason to apply a redaction to this view hierarchy.

[`unredacted()`](/documentation/SwiftUI/View/unredacted())

Removes any reason to apply a redaction to this view hierarchy.

[`redactionReasons`](/documentation/SwiftUI/EnvironmentValues/redactionReasons)

The current redaction reasons applied to the view hierarchy.

[`isSceneCaptured`](/documentation/SwiftUI/EnvironmentValues/isSceneCaptured)

The current capture state.

[`RedactionReasons`](/documentation/SwiftUI/RedactionReasons)

The reasons to apply a redaction to data displayed on screen.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
