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

- Feedback: Visual pulses should be 1-5ms ahead of haptics for synchrony.
- Sensors: Use CoreMotion to tilt the background gradient slightly.
- Accessibility: Always provide a way to disable motion-reactive UI.


## When to Use

- Building music players or audio apps with visualizer elements
- Creating motion-reactive backgrounds (gyroscope parallax)
- Designing ambient, living UI that responds to environmental input

## Best Practices

- Visual pulses should lead haptics by 1–5ms for perceived synchrony
- Use `CoreMotion` to tilt background gradients based on device orientation
- Cap visual amplitude at 20% scale to avoid overwhelming the content
- Always provide a static fallback for Reduce Motion users

## Common Pitfalls

- Continuous sensor polling drains battery — throttle to 30Hz for UI updates
- Audio analysis on the main thread causes dropped frames
- Motion-reactive UI without opt-out is an accessibility failure
