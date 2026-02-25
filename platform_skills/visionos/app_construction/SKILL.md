---
name: VISIONOS Creating your first visionOS app
description: Rork-Max Quality skill for VISIONOS Creating your first visionOS app. Platform-native patterns and best practices for visionos development.
---

# VISIONOS Creating your first visionOS app

Build a new visionOS app using SwiftUI and add platform-specific features.
If you’re new to visionOS, start with a new Xcode project to learn about the platform
features, and to familiarize yourself with visionOS content and techniques. When you
build an app for visionOS, SwiftUI is an excellent choice because it gives you full
access to visionOS features. Although you can also use UIKit to build portions of
your app, you need to use SwiftUI for many features that are unique to the platform.
> Note: Developing for visionOS requires a Mac with Apple silicon.
In any SwiftUI app, you place content onscreen using scenes. A scene contains
the views and controls to display onscreen. Scenes also define the appearance
of those views and controls when they appear onscreen. In visionOS, you can include
both 2D and 3D views in the same scene, and you can present those views in a
window or as part of the person’s surroundings.
Start with a new Xcode project and add features to familiarize yourself with
visionOS content and techniques. Run your app in Simulator to verify your content
looks like you expect, and run it on device to see your 3D content come to life.
Organize your content around one or more scenes, which manage your app’s interface.
Each scene contains the views and controls you want to display, and the scene type
determines whether your content adopts a 2D or 3D appearance. SwiftUI adds 3D
scene types specifically for visionOS, and also adds 3D elements and layout options
for all scene types.

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
        .navigationTitle("Creating your first visionOS app")
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


