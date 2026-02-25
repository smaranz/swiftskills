---
name: VISIONOS Improving accessibility support in your visionOS app
description: Rork-Max Quality skill for VISIONOS Improving accessibility support in your visionOS app. Platform-native patterns and best practices for visionos development.
---

# VISIONOS Improving accessibility support in your visionOS app

Update your code to ensure everyone can access your app’s content in
visionOS.
visionOS is an immersive platform that supports people of all abilities.
Even though experiences incorporate stunning visual content and hand-
and eye-tracking technologies, people can engage with content
in other ways. In fact, the platform supports people in many
different situations, including those who are blind, have low vision,
have limited mobility, or have limb differences. With the help of
assistive technologies, people can interact with all of your
app’s content.
During development, enable VoiceOver and other assistive features
and test your app’s accessibility support. Make sure people can
navigate your app’s interface intuitively, and that all of the
necessary elements are present. Improve the descriptive information
for those elements to communicate their intended purpose. And make
sure your app adapts to changing conditions, such as changes to
the Dynamic Type setting while your app is running.
For general information about supporting accessibility, see
guidance, see Human Interface Guidelines > Accessibility.

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
        .navigationTitle("Improving accessibility support in your visionOS app")
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


