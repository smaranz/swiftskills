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

- Grain: A subtle noise shader (0.05 intensity) adds a premium tactile feel.
- Performance: Shaders are GPU-accelerated—use them for full-screen background effects.
- Dynamics: Pass the current timestamp to shaders for organic transitions.


## When to Use

- Adding organic noise, grain, or shimmer to backgrounds
- Creating custom blur, distortion, or glow effects beyond built-in modifiers
- Building real-time animated effects (water ripple, heat haze, light leak)

## Best Practices

- Keep shader intensity subtle (0.03–0.08 noise) for premium tactile texture
- Shaders are GPU-accelerated — use them for full-screen backgrounds without fear
- Pass `Date.now.timeIntervalSince1970` as a float uniform for organic motion
- Use `.visualEffect { content, proxy in }` for per-view shader application (iOS 17+)

## Common Pitfalls

- Over-processing — heavy shaders on every view cause GPU throttling on older devices
- Not providing a fallback for pre-iOS 17 devices where ShaderLibrary is unavailable
- Testing only in Simulator — Metal shaders behave differently on real hardware
