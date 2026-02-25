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

- Over-scroll: Use the minY > 0 check to implement 'stretchy' headers.
- Opacity: Fade in a compact title as the header scrolls out of view.
- Blur: Increase material blur radius as content scrolls underneath.


## When to Use

- Building stretchy hero image headers that expand on over-scroll
- Creating parallax depth effects in scrollable content
- Fading in compact titles as full headers scroll out of view

## Best Practices

- Use `GeometryReader` + `.frame(in: .global).minY` to detect over-scroll distance
- Implement negative offset for parallax: content moves slower than the scroll
- Fade in a compact navigation title by mapping scroll offset to opacity (0→1)
- Use `scrollTargetBehavior(.paging)` for snap-to-position scroll effects (iOS 17+)

## Common Pitfalls

- GeometryReader inside LazyVStack recalculates on every scroll frame — profile performance
- Stretchy headers without clipping overflow into safe area and status bar
- Testing only in one orientation — parallax ratios may need adjustment for landscape
