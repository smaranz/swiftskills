---
name: Particle Systems for Delight
description: Rork-Max Quality elite iOS frontend skill for Particle Systems for Delight. Glitter, celebration, and feedback particles using high-performance emitters.
---

# Particle Systems for Delight

Glitter, celebration, and feedback particles using high-performance emitters.


## 🚀 Rork-Max Quality Snippet


```swift
Canvas { context, size in
    // Render particles
    context.fill(Path(CGRect(x: 50, y: 50, width: 4, height: 4)), with: .color(.yellow))
}
```


## 💎 Elite Implementation Tips

- Optimization: Limit to 50 particles max for high-end feel.
- Variance: Randomize size, velocity, and rotation slightly.
- Gravity: Apply a gentle downward acceleration (y += 0.1).


## When to Use

- Celebrating completion events (purchase, achievement, level up)
- Adding ambient effects (snow, confetti, sparkle) to themed screens
- Providing visual feedback for destructive or impactful actions

## Best Practices

- Limit to 30–50 particles max for performance and visual clarity
- Randomize size (±30%), velocity (±20%), and rotation for organic feel
- Apply gentle gravity (y acceleration ≈ 0.1 per frame) for realistic falloff
- Use `Canvas` for software particles or `CAEmitterLayer` for hardware-accelerated ones

## Common Pitfalls

- Unbounded particle count — always cap maximum and recycle particles
- Running particle effects continuously — use them for moments, not backgrounds
- Forgetting Reduce Motion — disable particle animations when accessibility setting is on
