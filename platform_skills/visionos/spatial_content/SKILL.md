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

struct SpatialGallery: View {
    var body: some View {
        RealityView { content in
            let floor = ModelEntity(
                mesh: .generatePlane(width: 2, depth: 2),
                materials: [SimpleMaterial(color: .gray, isMetallic: false)]
            )
            content.add(floor)

            for i in 0..<5 {
                let sphere = ModelEntity(
                    mesh: .generateSphere(radius: 0.1),
                    materials: [SimpleMaterial(color: .blue, isMetallic: true)]
                )
                sphere.position = [Float(i) * 0.3 - 0.6, 0.2, -0.5]
                sphere.components.set(HoverEffectComponent())
                sphere.components.set(InputTargetComponent())
                sphere.generateCollisionShapes(recursive: false)
                content.add(sphere)
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Add `InputTargetComponent` + collision shapes for entities to be tappable
- Use `HoverEffectComponent` for visual feedback on gaze targeting
- Position content 1–2 meters in front of the user at eye height for comfort

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


