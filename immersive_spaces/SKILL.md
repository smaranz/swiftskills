---
name: Immersive spaces
description: Rork-Max Quality skill for Immersive spaces. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Immersive spaces


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Immersive spaces

Display unbounded content in a person’s surroundings.

## Overview

Use an immersive space in visionOS to present SwiftUI views outside of any
containers. You can include any views in a space, although you typically use
a <doc://com.apple.documentation/documentation/RealityKit/RealityView>
to present RealityKit content.

![](images/com.apple.SwiftUI/immersive-spaces-hero@2x.png)

You can request one of three styles of spaces with the
[`immersionStyle(selection:in:)`](/documentation/SwiftUI/Scene/immersionStyle(selection:in:)) scene modifier:

- The ``doc://com.apple.SwiftUI/documentation/SwiftUI/ImmersionStyle/mixed`` style blends your content with passthrough.
  This enables you to place virtual objects in a person’s surroundings.
- The ``doc://com.apple.SwiftUI/documentation/SwiftUI/ImmersionStyle/full`` style displays only your content, with
  passthrough turned off. This enables you to completely control the visual
  experience, like when you want to transport people to a new world.
- The ``doc://com.apple.SwiftUI/documentation/SwiftUI/ImmersionStyle/progressive`` style completely replaces passthrough in
  a portion of the display. You might use this style to keep people grounded
  in the real world while displaying a view into another world.

When you open an immersive space, the system continues to display all of your
app’s windows, but hides windows from other apps. The system supports displaying
only one space at a time across all apps, so your app can only open a space
if one isn’t already open.

## Topics

### Creating an immersive space

[`ImmersiveSpace`](/documentation/SwiftUI/ImmersiveSpace)

A scene that presents its content in an unbounded space.

[`ImmersiveSpaceContentBuilder`](/documentation/SwiftUI/ImmersiveSpaceContentBuilder)

A result builder for composing a collection of immersive space elements.

[`immersionStyle(selection:in:)`](/documentation/SwiftUI/Scene/immersionStyle(selection:in:))

Sets the style for an immersive space.

[`ImmersionStyle`](/documentation/SwiftUI/ImmersionStyle)

The styles that an immersive space can have.

[`immersiveSpaceDisplacement`](/documentation/SwiftUI/EnvironmentValues/immersiveSpaceDisplacement)

The displacement that the system applies to the immersive space when
moving the space away from its default position, in meters.

[`ImmersiveEnvironmentBehavior`](/documentation/SwiftUI/ImmersiveEnvironmentBehavior)

The behavior of the system-provided immersive environments when a scene is
opened by your app.

[`ProgressiveImmersionAspectRatio`](/documentation/SwiftUI/ProgressiveImmersionAspectRatio)

### Opening an immersive space

[`openImmersiveSpace`](/documentation/SwiftUI/EnvironmentValues/openImmersiveSpace)

An action that presents an immersive space.

[`OpenImmersiveSpaceAction`](/documentation/SwiftUI/OpenImmersiveSpaceAction)

An action that presents an immersive space.

### Closing the immersive space

[`dismissImmersiveSpace`](/documentation/SwiftUI/EnvironmentValues/dismissImmersiveSpace)

An immersive space dismissal action stored in a view’s environment.

[`DismissImmersiveSpaceAction`](/documentation/SwiftUI/DismissImmersiveSpaceAction)

An action that dismisses an immersive space.

### Hiding upper limbs during immersion

[`upperLimbVisibility(_:)`](/documentation/SwiftUI/Scene/upperLimbVisibility(_:))

Sets the preferred visibility of the user’s upper limbs, while an
[`ImmersiveSpace`](/documentation/SwiftUI/ImmersiveSpace) scene is presented.

[`upperLimbVisibility(_:)`](/documentation/SwiftUI/View/upperLimbVisibility(_:))

Sets the preferred visibility of the user’s upper limbs, while an
[`ImmersiveSpace`](/documentation/SwiftUI/ImmersiveSpace) scene is presented.

### Adjusting content brightness

[`immersiveContentBrightness(_:)`](/documentation/SwiftUI/Scene/immersiveContentBrightness(_:))

Sets the content brightness of an immersive space.

[`ImmersiveContentBrightness`](/documentation/SwiftUI/ImmersiveContentBrightness)

The content brightness of an immersive space.

### Responding to immersion changes

[`onImmersionChange(initial:_:)`](/documentation/SwiftUI/View/onImmersionChange(initial:_:))

Performs an action when the immersion state of your app changes.

[`ImmersionChangeContext`](/documentation/SwiftUI/ImmersionChangeContext)

A structure that represents a state of immersion of your app.

### Adding menu items to an immersive space

[`immersiveEnvironmentPicker(content:)`](/documentation/SwiftUI/View/immersiveEnvironmentPicker(content:))

Add menu items to open immersive spaces from a media player’s
environment picker.

### Handling remote immersive spaces

[`RemoteImmersiveSpace`](/documentation/SwiftUI/RemoteImmersiveSpace)

A scene that presents its content in an unbounded space on a remote device.

[`RemoteDeviceIdentifier`](/documentation/SwiftUI/RemoteDeviceIdentifier)

An opaque type that identifies a remote device displaying scene content
in a [`RemoteImmersiveSpace`](/documentation/SwiftUI/RemoteImmersiveSpace).



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
