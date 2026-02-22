---
name: Spatial Design
description: Rork-Max Quality elite iOS frontend skill for Spatial Design. Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.
---

# Spatial Design

Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.


## 🚀 Rork-Max Quality Snippet


#if os(visionOS)
Text("Spatial UI")
    .glassBackgroundEffect()
#else
Text("Spatial Style on iOS")
    .background(.ultraThinMaterial, in: Capsule())
#endif


## 💎 Elite Implementation Tips

- Z-Axis: Use .offset(z:) and .rotation3DEffect to mimic spatial depth.\n- Interaction: Implement 'hover effects' via touch-down feedback on iOS.\n- Lighting: Simulate a global light source by consistent shadow X/Y offsets.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
