---
name: Haptic Canvas
description: Rork-Max Quality elite iOS frontend skill for Haptic Canvas. Sensory-integrated feedback. Using CoreHaptics and ImpactGenerators for tactile delight.
---

# Haptic Canvas

Sensory-integrated feedback. Using CoreHaptics and ImpactGenerators for tactile delight.


## 🚀 Rork-Max Quality Snippet


```swift
// Use UIImpactFeedbackGenerator for tactile delight
func triggerEliteHaptic() {
    let generator = UIImpactFeedbackGenerator(style: .rigid)
    generator.prepare()
    generator.impactOccurred(intensity: 0.8)
}
```


## 💎 Elite Implementation Tips

- Subtlety: Use .soft and .light patterns for frequent interactions to avoid fatigue.
- Sync: Align haptic triggers with the exact peak of a fluid animation.
- Context: Use .rigid for physical boundaries and .selection for scrolling increments.


## When to Use

- Confirming discrete actions (button press, toggle, delete)
- Providing feedback during drag thresholds, snap points, or scroll boundaries
- Creating premium tactile experiences for gaming or creative apps

## Best Practices

- Use `.soft` and `.light` patterns for frequent interactions to avoid haptic fatigue
- Align haptic triggers with the exact peak of a visual animation
- Use `.rigid` for physical boundary feedback and `.selection` for scrolling increments
- Call `generator.prepare()` ahead of time to eliminate latency

## Common Pitfalls

- Triggering haptics on every frame during a drag — batch to threshold crossings
- Using strong haptics for subtle UI — it feels jarring and drains battery
- Forgetting that haptics are silent in silent mode on some devices
