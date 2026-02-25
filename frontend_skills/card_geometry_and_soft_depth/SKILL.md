---
name: Card Geometry & Soft Depth
description: Rork-Max Quality elite iOS frontend skill for Card Geometry & Soft Depth. Advanced shadows and corner-radius logic. Mastering the 'continuous' squircle aesthetic.
---

# Card Geometry & Soft Depth

Advanced shadows and corner-radius logic. Mastering the 'continuous' squircle aesthetic.


## 🚀 Rork-Max Quality Snippet


```swift
RoundedRectangle(cornerRadius: 24, style: .continuous)
    .fill(.background)
    .shadow(color: .black.opacity(0.05), radius: 10, y: 5)
    .shadow(color: .black.opacity(0.1), radius: 30, y: 15)
```


## 💎 Elite Implementation Tips

- Layering: Use two shadows—one sharp and one diffuse for realism.
- Shape: Always use .continuous corner style for smooth silhouettes.
- Inner-Light: A 0.5pt white stroke on top simulates light-catching.


## When to Use

- Designing card-based layouts (feeds, dashboards, settings)
- Creating Apple-style rounded rectangles with continuous corner curves
- Building elevation hierarchy with layered shadows

## Best Practices

- Always use `.continuous` corner style for smooth squircle silhouettes
- Layer two shadows: one sharp (radius 10, y: 5, 0.05 opacity) and one diffuse (radius 30, y: 15, 0.1 opacity)
- Add a 0.5pt white top stroke to simulate light catching the edge
- Use 24–32pt corner radius for cards; 12–16pt for smaller elements

## Common Pitfalls

- `.cornerRadius()` (deprecated) doesn't support continuous curves — use `.clipShape(RoundedRectangle(cornerRadius:style:))`
- Pure black shadows look harsh — use the accent color with low opacity for a glow effect
- Inconsistent corner radii across nested elements (inner radius = outer radius − padding)
