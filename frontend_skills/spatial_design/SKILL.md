---
name: Spatial Design
description: Rork-Max Quality elite iOS frontend skill for Spatial Design. Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.
---

# Spatial Design

Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.


## 🚀 Rork-Max Quality Snippet


#if os(visionOS)
Text("Spatial UI")
    .glassBackgroundEffect()
#else
Text("Spatial Style on iOS")
    .background(.ultraThinMaterial, in: Capsule())
#endif


## 💎 Elite Implementation Tips

- Z-Axis: Use .offset(z:) and .rotation3DEffect to mimic spatial depth.
- Interaction: Implement 'hover effects' via touch-down feedback on iOS.
- Lighting: Simulate a global light source by consistent shadow X/Y offsets.


## When to Use

- Adding depth cues (parallax, shadow, scale) to flat iOS interfaces
- Designing UI that transitions between 2D (iOS) and 3D (visionOS) contexts
- Creating hover/focus effects that simulate spatial interaction

## Best Practices

- Use `.rotation3DEffect` and `.offset(z:)` to simulate depth on iOS
- Implement touch-down scale feedback to mimic spatial hover effects
- Maintain consistent shadow offsets across all cards for a unified light source
- Use `#if os(visionOS)` to provide true spatial effects when running on Vision Pro

## Common Pitfalls

- Excessive 3D transforms cause disorientation and motion sickness
- Inconsistent shadow directions — pick one light source and stick with it
- Parallax effects without Reduce Motion support violate accessibility guidelines
