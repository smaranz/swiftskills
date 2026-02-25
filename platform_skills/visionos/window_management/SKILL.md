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

struct WindowControls: View {
    @Environment(\.openWindow) private var openWindow
    @Environment(\.dismissWindow) private var dismissWindow
    @Environment(\.openImmersiveSpace) private var openSpace
    @Environment(\.dismissImmersiveSpace) private var dismissSpace

    var body: some View {
        VStack(spacing: 16) {
            Button("Open Panel") { openWindow(id: "info-panel") }
            Button("Enter Immersive") {
                Task { await openSpace(id: "immersive") }
            }
        }
        .padding()
        .glassBackgroundEffect()
    }
}
```

## 💎 Elite Implementation Tips

- Use `.glassBackgroundEffect()` for windows to feel native in the shared space
- Use `openWindow(id:)` for additional flat windows, `openImmersiveSpace` for spatial content
- Set `.defaultWindowPlacement` to control where new windows appear relative to existing ones

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


