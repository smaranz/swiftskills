---
name: Native Canvas Drawing
description: Rork-Max Quality elite iOS frontend skill for Native Canvas Drawing. Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.
---

# Native Canvas Drawing

Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.


## 🚀 Rork-Max Quality Snippet


```swift
Canvas { context, size in
    context.stroke(Path(ellipseIn: CGRect(origin: .zero, size: size)), with: .color(.blue), lineWidth: 2)
}
```


## 💎 Elite Implementation Tips

- Performance: Use Canvas for complex shapes that update at 120Hz.
- Resolution: Draw paths using normalized coordinates to scale perfectly.
- Filters: Leverage .blur and .colorMatrix in the Canvas context.


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
