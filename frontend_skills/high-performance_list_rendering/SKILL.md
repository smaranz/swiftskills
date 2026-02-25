---
name: High-Performance List Rendering
description: Rork-Max Quality elite iOS frontend skill for High-Performance List Rendering. Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization.
---

# High-Performance List Rendering

Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct HighPerfFeed: View {
    let items: [FeedItem]
    @State private var isLoadingMore = false

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 12) {
                ForEach(items) { item in
                    FeedRow(item: item)
                        .drawingGroup()
                }

                // Infinite scroll sentinel
                Color.clear.frame(height: 1)
                    .onAppear { loadMore() }
            }
            .padding(.horizontal)
        }
    }

    func loadMore() {
        guard !isLoadingMore else { return }
        isLoadingMore = true
        // Fetch next page...
    }
}

struct FeedRow: View {
    let item: FeedItem

    var body: some View {
        HStack(spacing: 12) {
            AsyncImage(url: item.thumbnailURL) { image in
                image.resizable().scaledToFill()
            } placeholder: {
                RoundedRectangle(cornerRadius: 8).fill(.gray.opacity(0.15))
            }
            .frame(width: 60, height: 60)
            .clipShape(RoundedRectangle(cornerRadius: 8))

            VStack(alignment: .leading, spacing: 4) {
                Text(item.title).font(.headline).lineLimit(1)
                Text(item.subtitle).font(.subheadline).foregroundStyle(.secondary).lineLimit(2)
            }
        }
        .padding(12)
        .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 12, style: .continuous))
    }
}
```

## 💎 Elite Implementation Tips

- Use `LazyVStack` inside `ScrollView` for full styling control over 100+ items
- Apply `.drawingGroup()` on static rows to flatten into Metal-backed rendering
- Add a sentinel `Color.clear.onAppear` at the bottom for infinite scroll pagination
- Use `AsyncImage` with placeholder for non-blocking image loading


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
