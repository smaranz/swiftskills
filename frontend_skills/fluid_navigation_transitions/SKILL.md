---
name: Fluid Navigation Transitions
description: Rork-Max Quality elite iOS frontend skill for Fluid Navigation Transitions. Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.
---

# Fluid Navigation Transitions

Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.


## 🚀 Rork-Max Quality Snippet


```swift
struct HeroTransition: View {
    @Namespace var namespace
    @State private var isExpanded = false
    
    var body: some View {
        if !isExpanded {
            RoundedRectangle(cornerRadius: 20)
                .matchedGeometryEffect(id: "card", in: namespace)
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        } else {
            Rectangle()
                .matchedGeometryEffect(id: "card", in: namespace)
                .ignoresSafeArea()
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        }
    }
}
```


## 💎 Elite Implementation Tips

- Consistency: Ensure the namespace is passed down if moving between views.
- Smoothing: Use .geometryGroup() to resolve layout conflicts.
- Depth: Scale the background view slightly (0.95) when the hero card expands.


## When to Use

- Creating hero transitions between a thumbnail and a detail view
- Building interactive, interruptible navigation animations
- Connecting visual elements across navigation stack destinations

## Best Practices

- Use `matchedGeometryEffect(id:in:)` with a shared `@Namespace` for hero animations
- Apply `.geometryGroup()` to resolve layout conflicts during transitions
- Scale the background view to 0.95 when a hero card expands for depth
- Use `NavigationTransition.zoom` (iOS 18+) for built-in hero transitions

## Common Pitfalls

- Namespace not shared correctly — the hero effect silently fails
- Mismatched view hierarchies cause geometry effects to jump instead of interpolate
- Over-animating — subtle transitions (0.3s spring) feel better than dramatic ones
