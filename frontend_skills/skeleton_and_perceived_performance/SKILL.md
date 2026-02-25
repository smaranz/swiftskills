---
name: Skeleton & Perceived Performance
description: Rork-Max Quality elite iOS frontend skill for Skeleton & Perceived Performance. High-end data loading aesthetics. Using animated shimmer gradients and placeholders.
---

# Skeleton & Perceived Performance

High-end data loading aesthetics. Using animated shimmer gradients and placeholders.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct ShimmerModifier: ViewModifier {
    @State private var phase: CGFloat = -1

    func body(content: Content) -> some View {
        content.overlay {
            LinearGradient(
                colors: [.clear, .white.opacity(0.25), .clear],
                startPoint: .leading,
                endPoint: .trailing
            )
            .offset(x: phase * 300)
            .mask(content)
        }
        .onAppear {
            withAnimation(.linear(duration: 1.5).repeatForever(autoreverses: false)) {
                phase = 1
            }
        }
    }
}

struct SkeletonRow: View {
    var body: some View {
        HStack(spacing: 12) {
            RoundedRectangle(cornerRadius: 8)
                .fill(.gray.opacity(0.15))
                .frame(width: 48, height: 48)

            VStack(alignment: .leading, spacing: 6) {
                RoundedRectangle(cornerRadius: 4)
                    .fill(.gray.opacity(0.15))
                    .frame(height: 14)
                    .frame(maxWidth: 180)
                RoundedRectangle(cornerRadius: 4)
                    .fill(.gray.opacity(0.12))
                    .frame(height: 12)
                    .frame(maxWidth: 120)
            }
        }
        .modifier(ShimmerModifier())
    }
}
```

## 💎 Elite Implementation Tips

- Build a reusable `ShimmerModifier` and apply it to any placeholder shape
- Match skeleton shapes to actual content layout so the transition feels seamless
- Use system fill colors (`.gray.opacity(0.15)`) for automatic dark/light mode support
- Stagger row animations by 50–100ms offset for organic cascading reveal


## When to Use

- Showing placeholder UI while network data loads
- Replacing spinners with skeleton screens that preview the content layout
- Improving perceived performance by showing structure before data arrives

## Best Practices

- Match skeleton shapes to actual content layout (image placeholders, text lines)
- Use a linear gradient shimmer at 1.5s duration for 'just right' pacing
- Apply system colors so skeletons match dark/light mode automatically
- Stagger row animation start times by 50–100ms for an organic cascading reveal

## Common Pitfalls

- Skeleton that doesn't match final layout causes a jarring shift when content loads
- Shimmer animations without Reduce Motion support — use static placeholders as fallback
- Showing skeletons for < 200ms — flash of skeleton is worse than no skeleton
