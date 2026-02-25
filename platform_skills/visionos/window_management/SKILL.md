---
name: VISIONOS Positioning and sizing windows
description: Rork-Max Quality skill for VISIONOS Positioning and sizing windows. Platform-native patterns and best practices for visionos development.
---

# VISIONOS Positioning and sizing windows

Influence the initial geometry of windows that your app presents.
visionOS and macOS enable people to move and resize windows. In some cases,
your app can use scene modifiers to influence a window’s initial geometry
on these platforms, as well as to specify the strategy that the system employs
to place minimum and maximum size limitations on a window. This kind of
configuration affects both windows and volumes, which are windows with the
window style.
Your ability to configure window size and position is subject to the
following constraints:
- The system might be unable to fulfill your request. For example, if you
specify a default size that’s outside the range of the window’s resizability,
the system clamps the affected dimension to keep it in range.
- Although you can change the window’s content, you can’t directly manipulate
window position or size after the window appears. This ensures that people
have full control over their workspace.
- During state restoration, the system restores windows to their previous
position and size.
> Note: Windows in iPadOS occupy the full screen, or share the screen with
> another window in Slide Over or Split View. You can’t programmatically
> affect window geometry on that platform.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import RealityKit

struct RorkSpatialView: View {
    var body: some View {
        RealityView { content in
            let sphere = MeshResource.generateSphere(radius: 0.1)
            let material = SimpleMaterial(color: .blue, isMetallic: true)
            let entity = ModelEntity(mesh: sphere, materials: [material])
            content.add(entity)
        }
        .navigationTitle("Positioning and sizing windows")
    }
}
```

## 💎 Elite Implementation Tips

- Follow the VISIONOS Human Interface Guidelines for native feel.
- Use system-standard visionOS components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building spatial computing experiences for Apple Vision Pro
- Adding 3D content with RealityKit and volumetric windows
- Creating fully immersive experiences with `ImmersiveSpace`

## Best Practices

- Start with a window-based app, then add volumetric or immersive content
- Use `.glassBackgroundEffect()` for windows to feel native in the shared space
- Design for indirect input (eye tracking + hand pinch) as the primary interaction

## Common Pitfalls

- Assuming direct touch — visionOS primarily uses indirect gaze-and-pinch input
- Making UI elements too small for comfortable eye targeting (minimum 60pt touch targets)
- Ignoring the shared space — immersive content should not disorient the user


