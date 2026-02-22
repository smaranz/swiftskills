---
name: Immersive Audio-Visuals
description: Rork-Max Quality elite iOS frontend skill for Immersive Audio-Visuals. UI that reacts to sound and motion sensors. Creating living, reactive interfaces.
---

# Immersive Audio-Visuals

UI that reacts to sound and motion sensors. Creating living, reactive interfaces.


## 🚀 Rork-Max Quality Snippet


```swift
struct AudioReactiveView: View {
    @State private var amplitude: CGFloat = 0.5
    var body: some View {
        Circle()
            .scaleEffect(1.0 + amplitude * 0.2)
            .foregroundStyle(.blue.gradient)
    }
}
```


## 💎 Elite Implementation Tips

- Feedback: Visual pulses should be 1-5ms ahead of haptics for synchrony.\n- Sensors: Use CoreMotion to tilt the background gradient slightly.\n- Accessibility: Always provide a way to disable motion-reactive UI.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
