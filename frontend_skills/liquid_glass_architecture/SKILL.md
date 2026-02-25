---
name: Liquid Glass Architecture
description: Rork-Max Quality elite iOS frontend skill for Liquid Glass Architecture. Depth, translucency, and material hierarchies. Mastering .ultraThinMaterial and layered shadows.
---

# Liquid Glass Architecture

Depth, translucency, and material hierarchies. Mastering .ultraThinMaterial and layered shadows.


## 🚀 Rork-Max Quality Snippet


```swift
struct LiquidGlassView: View {
    var body: some View {
        ZStack {
            MeshGradient(width: 3, height: 3, points: [
                [0, 0], [0.5, 0], [1, 0],
                [0, 0.5], [0.8, 0.5], [1, 0.5],
                [0, 1], [0.5, 1], [1, 1]
            ], colors: [.blue, .purple, .teal, .indigo, .blue, .blue, .purple, .teal, .blue])
            .ignoresSafeArea()
            
            RoundedRectangle(cornerRadius: 32)
                .fill(.ultraThinMaterial)
                .overlay(
                    RoundedRectangle(cornerRadius: 32)
                        .stroke(.white.opacity(0.2), lineWidth: 1)
                )
                .shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)
                .padding(20)
        }
    }
}
```


## 💎 Elite Implementation Tips

- Hierarchy: Use varying material thicknesses (.ultraThin vs .regular) to create depth planes.
- Stroke: A 1pt white stroke at 0.2 opacity is the secret to crisp 'glass' edges.
- Visual: MeshGradients provide the 'liquid' feel behind glass layers.


## When to Use

- Creating frosted-glass card overlays on vibrant backgrounds
- Building layered UI with depth planes using material blur
- Designing modal sheets and floating panels with translucent backgrounds

## Best Practices

- Use `.ultraThinMaterial` for topmost glass layers; `.regularMaterial` for deeper layers
- Add a 1pt white stroke at 0.2 opacity to define crisp glass edges
- Pair `MeshGradient` backgrounds with glass layers for a dynamic, liquid feel
- Use `ZStack` ordering to create clear depth planes: background → mid-glass → foreground

## Common Pitfalls

- Stacking too many material layers kills performance — limit to 2-3 glass planes
- Materials on opaque backgrounds look like plain gray — always use a vibrant background behind glass
- Forgetting dark mode testing — materials adapt automatically but your strokes and shadows may not
