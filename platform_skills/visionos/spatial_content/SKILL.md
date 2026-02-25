---
name: VISIONOS Adding 3D content to your app
description: Rork-Max Quality skill for VISIONOS Adding 3D content to your app. Platform-native patterns and best practices for visionos development.
---

# VISIONOS Adding 3D content to your app

Add depth and dimension to your visionOS app and discover how
to incorporate your app’s content into a person’s surroundings.
A device with a stereoscopic display lets people experience
3D content in a way that feels more real. Content appears to have
real depth, and people can view it from different
angles, making it seem like it’s there in front of them.
When building an app for visionOS, think about ways you might add
depth to your app’s interface. The system provides several
ways to display 3D content, including in your existing
windows, in a volume, and in an immersive space. Choose the options
that work best for your app and the content you offer.

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
        .navigationTitle("Adding 3D content to your app")
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


