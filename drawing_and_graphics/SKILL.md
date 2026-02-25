---
name: Drawing and graphics
description: Rork-Max Quality skill for Drawing and graphics. Actionable patterns and best practices for SwiftUI development.
---

# Drawing and graphics

Enhance your views with graphical effects and customized drawings.
You create rich, dynamic user interfaces with the built-in views and
Shapes that SwiftUI provides. To enhance any view, you can apply many
of the graphical effects typically associated with a graphics context,
like setting colors, adding masks, and creating composites.
When you need the flexibility of immediate mode drawing in
a graphics context, use a `Canvas` view. This can be particularly helpful
when you want to draw an extremely large number of dynamic shapes — for
example, to create particle effects.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct ChartView: View {
    let values: [Double]

    var body: some View {
        Canvas { context, size in
            let step = size.width / CGFloat(values.count - 1)
            let maxVal = values.max() ?? 1

            var path = Path()
            for (i, value) in values.enumerated() {
                let x = step * CGFloat(i)
                let y = size.height - (value / maxVal) * size.height
                i == 0 ? path.move(to: CGPoint(x: x, y: y))
                       : path.addLine(to: CGPoint(x: x, y: y))
            }
            context.stroke(path, with: .color(.blue), lineWidth: 2)

            // Gradient fill under the line
            var fillPath = path
            fillPath.addLine(to: CGPoint(x: size.width, y: size.height))
            fillPath.addLine(to: CGPoint(x: 0, y: size.height))
            fillPath.closeSubpath()
            context.fill(fillPath, with: .linearGradient(
                Gradient(colors: [.blue.opacity(0.3), .clear]),
                startPoint: .zero, endPoint: CGPoint(x: 0, y: size.height)
            ))
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `Canvas` for high-performance 2D drawing that renders at 120Hz
- Apply `.drawingGroup()` to flatten complex view hierarchies into Metal-backed layers
- Use `context.resolveSymbol(id:)` to embed SwiftUI views inside Canvas draws

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

### Immediate mode drawing

| API | Purpose |
|-----|---------|
| `Add rich graphics to your SwiftUI app` | Make your apps stand out by adding background materials, vibrancy, custom graphics, and animations. |
| `Canvas` | A view type that supports immediate mode drawing. |
| `GraphicsContext` | An immediate mode drawing destination, and its current state. |

### Setting a color

| API | Purpose |
|-----|---------|
| `tint(_:)` | Sets the tint color within this view. |
| `Color` | A representation of a color that adapts to a given context. |

### Styling content

| API | Purpose |
|-----|---------|
| `border(_:width:)` | Adds a border to this view with the specified style and width. |
| `foregroundStyle(_:)` | Sets a view’s foreground elements to use a given style. |
| `foregroundStyle(_:_:)` | Sets the primary and secondary levels of the foreground |
| `foregroundStyle(_:_:_:)` | Sets the primary, secondary, and tertiary levels of |
| `backgroundStyle(_:)` | Sets the specified style to render backgrounds within the view. |
| `backgroundStyle` | An optional style that overrides the default system background |
| `ShapeStyle` | A color or pattern to use when rendering a shape. |
| `AnyShapeStyle` | A type-erased ShapeStyle value. |

### Transforming colors

| API | Purpose |
|-----|---------|
| `brightness(_:)` | Brightens this view by the specified amount. |
| `contrast(_:)` | Sets the contrast and separation between similar colors in this view. |
| `colorInvert()` | Inverts the colors in this view. |
| `colorMultiply(_:)` | Adds a color multiplication effect to this view. |
| `saturation(_:)` | Adjusts the color saturation of this view. |
| `grayscale(_:)` | Adds a grayscale effect to this view. |
| `hueRotation(_:)` | Applies a hue rotation effect to this view. |
| `luminanceToAlpha()` | Adds a luminance to alpha effect to this view. |

### Scaling, rotating, or transforming a view

| API | Purpose |
|-----|---------|
| `scaledToFill()` | Scales this view to fill its parent. |
| `scaledToFit()` | Scales this view to fit its parent. |
| `scaleEffect(_:anchor:)` | Scales this view’s rendered output by the given amount in both the |
| `scaleEffect(_:anchor:)` | Scales this view’s rendered output by the given amount in both the |
| `scaleEffect(x:y:anchor:)` | Scales this view’s rendered output by the given horizontal and vertical |
| `scaleEffect(x:y:z:anchor:)` | Scales this view by the specified horizontal, vertical, and depth |
| `aspectRatio(_:contentMode:)` | Constrains this view’s dimensions to the specified aspect ratio. |
| `rotationEffect(_:anchor:)` | Rotates a view’s rendered output in two dimensions around the specified |

### Masking and clipping

| API | Purpose |
|-----|---------|
| `mask(alignment:_:)` | Masks this view using the alpha channel of the given view. |
| `clipped(antialiased:)` | Clips this view to its bounding rectangular frame. |
| `clipShape(_:style:)` | Sets a clipping shape for this view. |

### Applying blur and shadows

| API | Purpose |
|-----|---------|
| `blur(radius:opaque:)` | Applies a Gaussian blur to this view. |
| `shadow(color:radius:x:y:)` | Adds a shadow to this view. |
| `ColorMatrix` | A matrix to use in an RGBA color transformation. |

### Applying effects based on geometry

| API | Purpose |
|-----|---------|
| `visualEffect(_:)` | Applies effects to this view, while providing access to layout |
| `visualEffect3D(_:)` | Applies effects to this view, while providing access to layout |
| `VisualEffect` | Visual Effects change the visual appearance of a view without changing its |
| `EmptyVisualEffect` | The base visual effect that you apply additional effect to. |

### Compositing views

| API | Purpose |
|-----|---------|
| `blendMode(_:)` | Sets the blend mode for compositing this view with overlapping views. |
| `compositingGroup()` | Wraps this view in a compositing group. |
| `drawingGroup(opaque:colorMode:)` | Composites this view’s contents into an offscreen image before final |
| `BlendMode` | Modes for compositing a view with overlapping content. |
| `ColorRenderingMode` | The set of possible working color spaces for color-compositing operations. |
| `CompositorContent` | — |
| `CompositorContentBuilder` | A result builder for composing a collection of [`CompositorContent`](/documentation/SwiftUI/CompositorContent) |
| `AnyCompositorContent` | Type erased compositor content. |

### Measuring a view

| API | Purpose |
|-----|---------|
| `GeometryReader` | A container view that defines its content as a function of its own size and |
| `GeometryReader3D` | A container view that defines its content as a function of its own |
| `GeometryProxy` | A proxy for access to the size and coordinate space (for anchor resolution) |
| `GeometryProxy3D` | A proxy for access to the size and coordinate space of the container view. |
| `coordinateSpace(_:)` | Assigns a name to the view’s coordinate space, so other code can operate |
| `CoordinateSpace` | A resolved coordinate space created by the coordinate space protocol. |
| `CoordinateSpaceProtocol` | A frame of reference within the layout system. |
| `PhysicalMetric` | Provides access to a value in points that corresponds to the specified |

### Responding to a geometry change

| API | Purpose |
|-----|---------|
| `onGeometryChange(for:of:action:)` | Adds an action to be performed when a value, created from a |

### Accessing Metal shaders

| API | Purpose |
|-----|---------|
| `colorEffect(_:isEnabled:)` | Returns a new view that applies `shader` to `self` as a filter |
| `distortionEffect(_:maxSampleOffset:isEnabled:)` | Returns a new view that applies `shader` to `self` as a |
| `layerEffect(_:maxSampleOffset:isEnabled:)` | Returns a new view that applies `shader` to `self` as a filter |
| `Shader` | A reference to a function in a Metal shader library, along with its |
| `ShaderFunction` | A reference to a function in a Metal shader library. |
| `ShaderLibrary` | A Metal shader library. |

### Accessing geometric constructs

| API | Purpose |
|-----|---------|
| `Axis` | The horizontal or vertical dimension in a 2D coordinate system. |
| `Angle` | A geometric angle whose value you access in either radians or degrees. |
| `UnitPoint` | A normalized 2D point in a view’s coordinate space. |
| `UnitPoint3D` | A normalized 3D point in a view’s coordinate space. |
| `Anchor` | An opaque value derived from an anchor source and a particular view. |
| `DepthAlignmentID` | — |
| `Alignment3D` | An alignment in all three axes. |
| `GeometryProxyCoordinateSpace3D` | A representation of a `GeometryProxy3D` which can be used for |
