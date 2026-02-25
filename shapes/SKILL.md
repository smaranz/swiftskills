---
name: Shapes
description: Rork-Max Quality skill for Shapes. Actionable patterns and best practices for SwiftUI development.
---

# Shapes

Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
Draw shapes like circles and rectangles, as well as custom paths that define
shapes of your own design. Apply styles that include environment-aware colors,
rich gradients, and material effects to the foreground, background, and outline
of your shapes.
If you need the efficiency or flexibility of immediate mode drawing
— for example, to create particle effects — use a `Canvas` view instead.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct StarShape: Shape {
    let points: Int
    let innerRatio: CGFloat

    func path(in rect: CGRect) -> Path {
        var path = Path()
        let center = CGPoint(x: rect.midX, y: rect.midY)
        let outerRadius = min(rect.width, rect.height) / 2
        let innerRadius = outerRadius * innerRatio

        for i in 0..<(points * 2) {
            let radius = i.isMultiple(of: 2) ? outerRadius : innerRadius
            let angle = Angle(degrees: Double(i) * 360.0 / Double(points * 2) - 90)
            let point = CGPoint(
                x: center.x + CGFloat(cos(angle.radians)) * radius,
                y: center.y + CGFloat(sin(angle.radians)) * radius
            )
            i == 0 ? path.move(to: point) : path.addLine(to: point)
        }
        path.closeSubpath()
        return path
    }
}

// Usage
StarShape(points: 5, innerRatio: 0.4)
    .fill(.yellow.gradient)
    .frame(width: 100, height: 100)
```

## 💎 Elite Implementation Tips

- Conform to `Shape` for reusable, animatable custom shapes
- Use `.fill()` with `ShapeStyle` (gradients, materials) for rich rendering
- Prefer `.continuous` corner style on `RoundedRectangle` for Apple's squircle aesthetic

## When to Use

- Creating custom shapes beyond the built-in Rectangle, Circle, Capsule
- Drawing complex graphics, charts, or data visualizations
- Applying gradients, blend modes, or visual effects to views
- Building performant 2D rendering with SwiftUI `Canvas`

## Best Practices

- Use `Canvas` for high-performance drawing that updates at 120Hz
- Prefer `Shape` protocol for reusable, animatable custom shapes
- Use `.fill()` with `ShapeStyle` (gradients, materials) instead of flat colors
- Leverage `.drawingGroup()` to flatten complex view hierarchies into Metal-backed layers

## Common Pitfalls

- Overusing `GeometryReader` for simple measurements — it can cause layout issues
- Creating `Path` objects inside `body` without caching — they're recalculated each render
- Forgetting to close paths when creating custom shapes

## Key APIs

### Creating rectangular shapes

| API | Purpose |
|-----|---------|
| `Rectangle` | A rectangular shape aligned inside the frame of the view containing it. |
| `RoundedRectangle` | A rectangular shape with rounded corners, aligned inside the frame of the |
| `RoundedCornerStyle` | Defines the shape of a rounded rectangle’s corners. |
| `RoundedRectangularShape` | A protocol of [`InsettableShape`](/documentation/SwiftUI/InsettableShape) that describes a rounded rectangular |
| `RoundedRectangularShapeCorners` | A type describing the corner styles of a [`RoundedRectangularShape`](/documentation/SwiftUI/RoundedRectangularShape). |
| `UnevenRoundedRectangle` | A rectangular shape with rounded corners with different values, aligned |
| `RectangleCornerRadii` | Describes the corner radius values of a rounded rectangle with |
| `RectangleCornerInsets` | The inset sizes for the corners of a rectangle. |

### Creating circular shapes

| API | Purpose |
|-----|---------|
| `Circle` | A circle centered on the frame of the view containing it. |
| `Ellipse` | An ellipse aligned inside the frame of the view containing it. |
| `Capsule` | A capsule shape aligned inside the frame of the view containing it. |

### Drawing custom shapes

| API | Purpose |
|-----|---------|
| `Path` | The outline of a 2D shape. |

### Defining shape behavior

| API | Purpose |
|-----|---------|
| `ShapeView` | A view that provides a shape that you can use for drawing operations. |
| `Shape` | A 2D shape that you can use when drawing a view. |
| `AnyShape` | A type-erased shape value. |
| `ShapeRole` | Ways of styling a shape. |
| `StrokeStyle` | The characteristics of a stroke that traces a path. |
| `StrokeShapeView` | A shape provider that strokes its shape. |
| `StrokeBorderShapeView` | A shape provider that strokes the border of its shape. |
| `FillStyle` | A style for rasterizing vector shapes. |

### Transforming a shape

| API | Purpose |
|-----|---------|
| `ScaledShape` | A shape with a scale transform applied to it. |
| `RotatedShape` | A shape with a rotation transform applied to it. |
| `OffsetShape` | A shape with a translation offset transform applied to it. |
| `TransformedShape` | A shape with an affine transform applied to it. |

### Setting a container shape

| API | Purpose |
|-----|---------|
| `containerShape(_:)` | Sets the container shape to use for any container relative shape or |
| `InsettableShape` | A shape type that is able to inset itself to produce another shape. |
| `ContainerRelativeShape` | A shape that is replaced by an inset version of the current |
