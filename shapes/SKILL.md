---
name: Shapes
description: Apple SwiftUI Documentation for Shapes.
---

# Shapes

Trace and fill built-in and custom shapes with a color, gradient, or other pattern.

## Overview

Draw shapes like circles and rectangles, as well as custom paths that define
shapes of your own design. Apply styles that include environment-aware colors,
rich gradients, and material effects to the foreground, background, and outline
of your shapes.

![](images/com.apple.SwiftUI/shapes-hero@2x.png)

If you need the efficiency or flexibility of immediate mode drawing
— for example, to create particle effects — use a [`Canvas`](/documentation/SwiftUI/Canvas) view instead.

## Topics

### Creating rectangular shapes

[`Rectangle`](/documentation/SwiftUI/Rectangle)

A rectangular shape aligned inside the frame of the view containing it.

[`RoundedRectangle`](/documentation/SwiftUI/RoundedRectangle)

A rectangular shape with rounded corners, aligned inside the frame of the
view containing it.

[`RoundedCornerStyle`](/documentation/SwiftUI/RoundedCornerStyle)

Defines the shape of a rounded rectangle’s corners.

[`RoundedRectangularShape`](/documentation/SwiftUI/RoundedRectangularShape)

A protocol of [`InsettableShape`](/documentation/SwiftUI/InsettableShape) that describes a rounded rectangular
shape.

[`RoundedRectangularShapeCorners`](/documentation/SwiftUI/RoundedRectangularShapeCorners)

A type describing the corner styles of a [`RoundedRectangularShape`](/documentation/SwiftUI/RoundedRectangularShape).

[`UnevenRoundedRectangle`](/documentation/SwiftUI/UnevenRoundedRectangle)

A rectangular shape with rounded corners with different values, aligned
inside the frame of the view containing it.

[`RectangleCornerRadii`](/documentation/SwiftUI/RectangleCornerRadii)

Describes the corner radius values of a rounded rectangle with
uneven corners.

[`RectangleCornerInsets`](/documentation/SwiftUI/RectangleCornerInsets)

The inset sizes for the corners of a rectangle.

[`ConcentricRectangle`](/documentation/SwiftUI/ConcentricRectangle)

A shape that is replaced by a concentric version of the current container
shape. If the container shape is a rectangle derived shape with four
corners, this shape could choose to respect corners individually.

### Creating circular shapes

[`Circle`](/documentation/SwiftUI/Circle)

A circle centered on the frame of the view containing it.

[`Ellipse`](/documentation/SwiftUI/Ellipse)

An ellipse aligned inside the frame of the view containing it.

[`Capsule`](/documentation/SwiftUI/Capsule)

A capsule shape aligned inside the frame of the view containing it.

### Drawing custom shapes

[`Path`](/documentation/SwiftUI/Path)

The outline of a 2D shape.

### Defining shape behavior

[`ShapeView`](/documentation/SwiftUI/ShapeView)

A view that provides a shape that you can use for drawing operations.

[`Shape`](/documentation/SwiftUI/Shape)

A 2D shape that you can use when drawing a view.

[`AnyShape`](/documentation/SwiftUI/AnyShape)

A type-erased shape value.

[`ShapeRole`](/documentation/SwiftUI/ShapeRole)

Ways of styling a shape.

[`StrokeStyle`](/documentation/SwiftUI/StrokeStyle)

The characteristics of a stroke that traces a path.

[`StrokeShapeView`](/documentation/SwiftUI/StrokeShapeView)

A shape provider that strokes its shape.

[`StrokeBorderShapeView`](/documentation/SwiftUI/StrokeBorderShapeView)

A shape provider that strokes the border of its shape.

[`FillStyle`](/documentation/SwiftUI/FillStyle)

A style for rasterizing vector shapes.

[`FillShapeView`](/documentation/SwiftUI/FillShapeView)

A shape provider that fills its shape.

### Transforming a shape

[`ScaledShape`](/documentation/SwiftUI/ScaledShape)

A shape with a scale transform applied to it.

[`RotatedShape`](/documentation/SwiftUI/RotatedShape)

A shape with a rotation transform applied to it.

[`OffsetShape`](/documentation/SwiftUI/OffsetShape)

A shape with a translation offset transform applied to it.

[`TransformedShape`](/documentation/SwiftUI/TransformedShape)

A shape with an affine transform applied to it.

### Setting a container shape

[`containerShape(_:)`](/documentation/SwiftUI/View/containerShape(_:))

Sets the container shape to use for any container relative shape or
concentric rectangle within this view.

[`InsettableShape`](/documentation/SwiftUI/InsettableShape)

A shape type that is able to inset itself to produce another shape.

[`ContainerRelativeShape`](/documentation/SwiftUI/ContainerRelativeShape)

A shape that is replaced by an inset version of the current
container shape. If no container shape was defined, is replaced by
a rectangle.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
