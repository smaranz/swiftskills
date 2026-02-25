---
name: Skeleton & Perceived Performance
description: Rork-Max Quality elite iOS frontend skill for Skeleton & Perceived Performance. High-end data loading aesthetics. Using animated shimmer gradients and placeholders.
---

# Skeleton & Perceived Performance

High-end data loading aesthetics. Using animated shimmer gradients and placeholders.


## 🚀 Rork-Max Quality Snippet


```swift
RoundedRectangle(cornerRadius: 12)
    .fill(.gray.opacity(0.1))
    .overlay(
        LinearGradient(colors: [.clear, .white.opacity(0.2), .clear], startPoint: .leading, endPoint: .trailing)
            .offset(x: -100 + phase * 200)
    )
```


## 💎 Elite Implementation Tips

- Animation: Linear shine animations at 1.5s duration feel 'just right'.
- Colors: Use the system theme so skeleton matches dark/light mode.
- Stagger: Offset row animation start times for an organic feel.


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
