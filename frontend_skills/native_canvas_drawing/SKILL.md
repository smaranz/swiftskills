---
name: Native Canvas Drawing
description: Rork-Max Quality elite iOS frontend skill for Native Canvas Drawing. Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.
---

# Native Canvas Drawing

Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct LineChart: View {
    let values: [Double]

    var body: some View {
        Canvas { context, size in
            guard values.count > 1, let maxVal = values.max(), maxVal > 0 else { return }
            let step = size.width / CGFloat(values.count - 1)

            // Draw grid lines
            for i in stride(from: 0.0, through: size.height, by: size.height / 4) {
                var gridLine = Path()
                gridLine.move(to: CGPoint(x: 0, y: i))
                gridLine.addLine(to: CGPoint(x: size.width, y: i))
                context.stroke(gridLine, with: .color(.gray.opacity(0.15)), lineWidth: 0.5)
            }

            // Build data path
            var path = Path()
            for (i, value) in values.enumerated() {
                let x = step * CGFloat(i)
                let y = size.height - (value / maxVal) * size.height * 0.9 - size.height * 0.05
                i == 0 ? path.move(to: CGPoint(x: x, y: y)) : path.addLine(to: CGPoint(x: x, y: y))
            }
            context.stroke(path, with: .color(.blue), style: StrokeStyle(lineWidth: 2.5, lineCap: .round, lineJoin: .round))

            // Fill gradient under the line
            var fill = path
            fill.addLine(to: CGPoint(x: size.width, y: size.height))
            fill.addLine(to: CGPoint(x: 0, y: size.height))
            fill.closeSubpath()
            context.fill(fill, with: .linearGradient(
                Gradient(colors: [.blue.opacity(0.3), .blue.opacity(0.0)]),
                startPoint: .zero, endPoint: CGPoint(x: 0, y: size.height)
            ))
        }
    }
}

// Usage: LineChart(values: [10, 25, 18, 42, 35, 50, 38])
```

## 💎 Elite Implementation Tips

- Use `Canvas` for charts and visualizations — it renders at 120Hz with Metal backing
- Draw grid lines first, data on top, gradient fill last for correct layering
- Use `StrokeStyle(lineCap: .round, lineJoin: .round)` for smooth chart lines
- Use `context.drawLayer` for group transforms and clipping within Canvas


## When to Use

- Drawing complex shapes, charts, or visualizations at 120Hz
- Rendering large numbers of graphic elements more efficiently than SwiftUI views
- Creating custom drawing tools, annotation layers, or game rendering

## Best Practices

- Use `Canvas` for any view with > 50 graphic elements — it flattens the hierarchy
- Draw paths using normalized coordinates to scale across screen sizes
- Leverage `context.drawLayer` for group transforms and clipping
- Use `context.resolveSymbol(id:)` to embed SwiftUI views inside Canvas draws

## Common Pitfalls

- Canvas doesn't respond to gestures on individual drawn elements — overlay hit-test views
- Forgetting that Canvas redraws entirely on state changes — cache expensive path calculations
- Using Canvas for simple layouts where `Path` or `Shape` would be more maintainable
