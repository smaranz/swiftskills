---
name: Physics-Driven Motion
description: Rork-Max Quality elite iOS frontend skill for Physics-Driven Motion. Spring systems, damping, and natural gestures. Moving beyond EaseInOut to physical realism.
---

# Physics-Driven Motion

Spring systems, damping, and natural gestures. Moving beyond EaseInOut to physical realism.


## 🚀 Rork-Max Quality Snippet


```swift
struct PhysicsMotionView: View {
    @State private var offset: CGSize = .zero
    
    var body: some View {
        Circle()
            .fill(.blue.gradient)
            .frame(width: 80, height: 80)
            .offset(offset)
            .gesture(
                DragGesture()
                    .onChanged { offset = $0.translation }
                    .onEnded { _ in
                        withAnimation(.spring(response: 0.4, dampingFraction: 0.5)) {
                            offset = .zero
                        }
                    }
            )
    }
}
```


## 💎 Elite Implementation Tips

- Responsiveness: Always use .spring() instead of .easeInOut for interactive elements.
- Naturalism: Match the response to the distance traveled—shorter distances need faster responses.
- Interaction: Interruptible animations are key—ensure state updates don't snap back instantly.


## When to Use

- Animating interactive drag, swipe, or bounce interactions
- Replacing ease-in/ease-out curves with natural spring physics
- Creating rubber-banding, snap-back, and throw-to-dismiss gestures

## Best Practices

- Always use `.spring(response:dampingFraction:)` instead of `.easeInOut` for interactive elements
- Match spring response to distance — shorter movements need faster response (0.2–0.3s)
- Use `dampingFraction` 0.5–0.7 for bouncy UI, 0.8–1.0 for settled, precise motion
- Make animations interruptible — never block gesture updates during spring animations

## Common Pitfalls

- Using `.linear` or `.easeInOut` for interactive elements — they feel robotic
- Overly bouncy springs (dampingFraction < 0.4) distract from content and annoy users
- Not testing with `UIAccessibility.isReduceMotionEnabled` — provide crossfade fallbacks
