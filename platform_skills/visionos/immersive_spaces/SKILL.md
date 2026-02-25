---
name: VISIONOS Creating fully immersive experiences in your app
description: Rork-Max Quality skill for VISIONOS Creating fully immersive experiences in your app. Platform-native patterns and best practices for visionos development.
---

# VISIONOS Creating fully immersive experiences in your app

Build fully immersive experiences by combining spaces with
content you create using RealityKit or Metal.
A fully immersive experience replaces everything the person sees with
custom content you create. You might use this type of experience to:
- Offer a temporary transitional experience
- Create a distraction-free space for your content
- Implement a virtual reality (VR) game
- Present a virtual world to explore
With a fully immersive experience, you’re responsible for everything
that appears onscreen. The system hides passthrough video and displays
the content you provide, showing the person’s hands only when they
come into view. To achieve the best performance, use RealityKit or
Metal to create and animate your content.
Typically, you combine a fully immersive experience with other types
of experiences and provide transitions between them. When you display
a window first and then offer controls to enter your immersive
experience, you give people time to prepare for the transition. It also
gives them the option to skip the experience if they prefer to use
your app’s windows instead.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import RealityKit

struct ImmersiveEnvironment: View {
    @Environment(\.dismissImmersiveSpace) private var dismiss

    var body: some View {
        RealityView { content in
            guard let scene = try? await Entity(named: "MyScene", in: realityKitContentBundle) else {
                return
            }
            content.add(scene)
        }
        .gesture(
            TapGesture()
                .targetedToAnyEntity()
                .onEnded { value in
                    // Handle entity tap
                }
        )
    }
}
```

## 💎 Elite Implementation Tips

- Use `@Environment(\.openImmersiveSpace)` / `dismissImmersiveSpace` for lifecycle control
- Load complex scenes from Reality Composer Pro bundles with `Entity(named:in:)`
- Only one `ImmersiveSpace` can be open at a time — design transitions carefully

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


