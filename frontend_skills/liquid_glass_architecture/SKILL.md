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

- Hierarchy: Use varying material thicknesses (.ultraThin vs .regular) to create depth planes.\n- Stroke: A 1pt white stroke at 0.2 opacity is the secret to crisp 'glass' edges.\n- Visual: MeshGradients provide the 'liquid' feel behind glass layers.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
