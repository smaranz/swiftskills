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

- Optimization: Use .drawingGroup() on static rows to flatten hierarchy.
- Lazy: Never render 50+ views in a standard VStack—always use LazyVStack.
- Smoothness: Cache thumbnails; avoid image decoding on main thread.


## When to Use

- Rendering feeds, timelines, or catalogs with 100+ items
- Displaying image-heavy content lists that must scroll at 60fps
- Building custom list styles beyond what `List` provides

## Best Practices

- Use `LazyVStack(spacing: 0)` inside `ScrollView` for full styling control
- Apply `.drawingGroup()` on static rows to flatten the view hierarchy for Metal rendering
- Cache thumbnails in memory — avoid decoding images on the main thread
- Use `.onAppear` on sentinel rows to trigger pagination/infinite scroll loading

## Common Pitfalls

- Using `VStack` for 50+ items — it renders ALL items upfront, killing performance
- Forgetting `.id()` on list items — SwiftUI can't diff correctly and re-renders everything
- Wrapping `LazyVStack` without `ScrollView` — lazy loading only works inside a scroll container
