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

- Responsiveness: Always use .spring() instead of .easeInOut for interactive elements.\n- Naturalism: Match the response to the distance traveled—shorter distances need faster responses.\n- Interaction: Interruptible animations are key—ensure state updates don't snap back instantly.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
