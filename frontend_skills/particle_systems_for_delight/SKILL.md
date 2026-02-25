---
name: Particle Systems for Delight
description: Rork-Max Quality elite iOS frontend skill for Particle Systems for Delight. Glitter, celebration, and feedback particles using high-performance emitters.
---

# Particle Systems for Delight

Glitter, celebration, and feedback particles using high-performance emitters.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct Particle: Identifiable {
    let id = UUID()
    var x: CGFloat
    var y: CGFloat
    var scale: CGFloat
    var opacity: Double
    var velocity: CGFloat
}

struct ConfettiView: View {
    @State private var particles: [Particle] = []
    let timer = Timer.publish(every: 1.0 / 60, on: .main, in: .common).autoconnect()

    var body: some View {
        Canvas { context, size in
            for particle in particles {
                let rect = CGRect(x: particle.x, y: particle.y, width: 6 * particle.scale, height: 6 * particle.scale)
                context.opacity = particle.opacity
                context.fill(
                    RoundedRectangle(cornerRadius: 1).path(in: rect),
                    with: .color([.red, .blue, .green, .yellow, .purple].randomElement()!)
                )
            }
        }
        .onReceive(timer) { _ in
            particles = particles.compactMap { p in
                var p = p
                p.y += p.velocity
                p.velocity += 0.15
                p.opacity -= 0.008
                return p.opacity > 0 ? p : nil
            }
        }
        .allowsHitTesting(false)
    }

    func burst(at point: CGPoint, count: Int = 40) {
        let new = (0..<count).map { _ in
            Particle(
                x: point.x + .random(in: -30...30),
                y: point.y + .random(in: -20...10),
                scale: .random(in: 0.6...1.4),
                opacity: 1.0,
                velocity: .random(in: -4...(-1))
            )
        }
        particles.append(contentsOf: new)
    }
}
```

## 💎 Elite Implementation Tips

- Use `Canvas` for software particles — it flattens rendering and handles 60fps easily
- Cap particles at 40–50; recycle by removing faded-out particles each frame
- Randomize size (±30%), velocity, and initial position for organic feel
- Apply gravity by incrementing velocity each frame (`velocity += 0.15`)


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
