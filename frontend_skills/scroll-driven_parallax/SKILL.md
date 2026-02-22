---
name: Scroll-Driven Parallax
description: Rork-Max Quality elite iOS frontend skill for Scroll-Driven Parallax. Sticky headers with dynamic opacity, scale, and stretchy effects.
---

# Scroll-Driven Parallax

Sticky headers with dynamic opacity, scale, and stretchy effects.


## 🚀 Rork-Max Quality Snippet


```swift
ScrollView {
    GeometryReader { proxy in
        Image("header")
            .offset(y: proxy.frame(in: .global).minY > 0 ? -proxy.frame(in: .global).minY : 0)
    }
}
```


## 💎 Elite Implementation Tips

- Over-scroll: Use the minY > 0 check to implement 'stretchy' headers.\n- Opacity: Fade in a compact title as the header scrolls out of view.\n- Blur: Increase material blur radius as content scrolls underneath.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
