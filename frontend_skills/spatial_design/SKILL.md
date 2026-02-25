---
name: Spatial Design
description: Rork-Max Quality elite iOS frontend skill for Spatial Design. Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.
---

# Spatial Design

Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct SpatialCard: View {
    @State private var isHovered = false

    var body: some View {
        VStack(spacing: 12) {
            Image(systemName: "cube.fill")
                .font(.system(size: 40))
                .foregroundStyle(.blue.gradient)
            Text("Spatial Element")
                .font(.headline)
        }
        .padding(24)
        .background {
            #if os(visionOS)
            RoundedRectangle(cornerRadius: 20, style: .continuous)
                .glassBackgroundEffect()
            #else
            RoundedRectangle(cornerRadius: 20, style: .continuous)
                .fill(.ultraThinMaterial)
                .shadow(color: .black.opacity(0.08), radius: isHovered ? 20 : 12, y: isHovered ? 8 : 4)
            #endif
        }
        .scaleEffect(isHovered ? 1.03 : 1.0)
        .rotation3DEffect(.degrees(isHovered ? 3 : 0), axis: (x: 1, y: 0, z: 0))
        .animation(.spring(response: 0.35, dampingFraction: 0.7), value: isHovered)
        .onHover { isHovered = $0 }
        .onLongPressGesture(minimumDuration: 0, pressing: { pressing in
            isHovered = pressing
        }, perform: {})
    }
}
```

## 💎 Elite Implementation Tips

- Use `#if os(visionOS)` to provide true glass effects on Vision Pro, material fallback on iOS
- Simulate hover with `.onLongPressGesture(pressing:)` on touch devices
- Keep `.rotation3DEffect` subtle (2–5°) to avoid disorientation
- Maintain consistent shadow offsets across all cards for a unified light source


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
