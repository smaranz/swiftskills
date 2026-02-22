---
name: Custom Metal Shaders
description: Rork-Max Quality elite iOS frontend skill for Custom Metal Shaders. Pixel-perfect visual effects. Using iOS 17+ colorEffect and distortionEffect for premium VFX.
---

# Custom Metal Shaders

Pixel-perfect visual effects. Using iOS 17+ colorEffect and distortionEffect for premium VFX.


## 🚀 Rork-Max Quality Snippet


```swift
// SwiftUI + Metal Shaders (iOS 17+)
struct ShaderDelightView: View {
    var body: some View {
        Rectangle()
            .fill(.blue)
            .visualEffect { content, proxy in
                content.colorEffect(
                    ShaderLibrary.default.noise(
                        .float(Date.now.timeIntervalSince1970)
                    )
                )
            }
    }
}
```


## 💎 Elite Implementation Tips

- Grain: A subtle noise shader (0.05 intensity) adds a premium tactile feel.\n- Performance: Shaders are GPU-accelerated—use them for full-screen background effects.\n- Dynamics: Pass the current timestamp to shaders for organic transitions.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
