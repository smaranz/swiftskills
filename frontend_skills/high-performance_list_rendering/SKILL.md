---
name: High-Performance List Rendering
description: Rork-Max Quality elite iOS frontend skill for High-Performance List Rendering. Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization.
---

# High-Performance List Rendering

Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization.


## 🚀 Rork-Max Quality Snippet


```swift
LazyVStack(spacing: 0) {
    ForEach(items) { item in
        RowView(item: item)
            .drawingGroup()
    }
}
```


## 💎 Elite Implementation Tips

- Optimization: Use .drawingGroup() on static rows to flatten hierarchy.\n- Lazy: Never render 50+ views in a standard VStack—always use LazyVStack.\n- Smoothness: Cache thumbnails; avoid image decoding on main thread.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
