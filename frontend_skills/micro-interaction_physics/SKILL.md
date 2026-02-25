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

- Timing: The 'down' animation should be twice as fast as the 'up' animation.
- Brightness: A subtle darkening (-0.05) is better than changing opacity.
- Haptics: Trigger a .light impact on touch-down.


## When to Use

- Adding tactile press feedback to buttons and interactive elements
- Morphing icons or shapes between states (play → pause, plus → X)
- Creating subtle spring responses on toggles, checkboxes, and selection changes

## Best Practices

- Scale down to 0.92–0.95 on press; spring back with dampingFraction 0.4
- The 'down' animation should be 2x faster than the 'up' animation
- Use brightness adjustment (-0.05) on press instead of opacity changes
- Trigger `.light` haptic on touch-down for confirming engagement

## Common Pitfalls

- Over-animating every element — micro-interactions should be barely noticed, not distracting
- Missing the press-cancel path — if a drag leaves the button, reset without spring
- Scale effects on buttons inside scroll views can conflict with scroll gesture detection
