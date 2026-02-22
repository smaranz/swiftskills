---
name: Fluid Navigation Transitions
description: Rork-Max Quality elite iOS frontend skill for Fluid Navigation Transitions. Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.
---

# Fluid Navigation Transitions

Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.


## 🚀 Rork-Max Quality Snippet


```swift
struct HeroTransition: View {
    @Namespace var namespace
    @State private var isExpanded = false
    
    var body: some View {
        if !isExpanded {
            RoundedRectangle(cornerRadius: 20)
                .matchedGeometryEffect(id: "card", in: namespace)
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        } else {
            Rectangle()
                .matchedGeometryEffect(id: "card", in: namespace)
                .ignoresSafeArea()
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        }
    }
}
```


## 💎 Elite Implementation Tips

- Consistency: Ensure the namespace is passed down if moving between views.\n- Smoothing: Use .geometryGroup() to resolve layout conflicts.\n- Depth: Scale the background view slightly (0.95) when the hero card expands.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
