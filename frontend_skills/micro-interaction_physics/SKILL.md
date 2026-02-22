---
name: Micro-interaction Physics
description: Rork-Max Quality elite iOS frontend skill for Micro-interaction Physics. Button bounce, elasticity, and state morphing. Perfecting the small moments of delight.
---

# Micro-interaction Physics

Button bounce, elasticity, and state morphing. Perfecting the small moments of delight.


## 🚀 Rork-Max Quality Snippet


```swift
struct BouncyButton: View {
    @State private var isPressed = false
    var body: some View {
        Button("Press Me") { }
            .scaleEffect(isPressed ? 0.9 : 1.0)
            .animation(.spring(response: 0.2, dampingFraction: 0.4), value: isPressed)
    }
}
```


## 💎 Elite Implementation Tips

- Timing: The 'down' animation should be twice as fast as the 'up' animation.\n- Brightness: A subtle darkening (-0.05) is better than changing opacity.\n- Haptics: Trigger a .light impact on touch-down.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
