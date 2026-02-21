---
name: Drawing and graphics
description: Apple SwiftUI Documentation for Drawing and graphics.
---

# Drawing and graphics

Enhance your views with graphical effects and customized drawings.

## Overview

You create rich, dynamic user interfaces with the built-in views and
[Shapes](/documentation/SwiftUI/Shapes) that SwiftUI provides. To enhance any view, you can apply many
of the graphical effects typically associated with a graphics context,
like setting colors, adding masks, and creating composites.

![](images/com.apple.SwiftUI/drawing-and-graphics-hero@2x.png)

When you need the flexibility of immediate mode drawing in
a graphics context, use a [`Canvas`](/documentation/SwiftUI/Canvas) view. This can be particularly helpful
when you want to draw an extremely large number of dynamic shapes — for
example, to create particle effects.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/materials> and
<doc://com.apple.documentation/design/Human-Interface-Guidelines/color>
in the Human Interface Guidelines.

## Topics

### Immediate mode drawing

[Add rich graphics to your SwiftUI app](/documentation/SwiftUI/add-rich-graphics-to-your-swiftui-app)

Make your apps stand out by adding background materials, vibrancy, custom graphics, and animations.

[`Canvas`](/documentation/SwiftUI/Canvas)

A view type that supports immediate mode drawing.

[`GraphicsContext`](/documentation/SwiftUI/GraphicsContext)

An immediate mode drawing destination, and its current state.

### Setting a color

[`tint(_:)`](/documentation/SwiftUI/View/tint(_:))

Sets the tint color within this view.

[`Color`](/documentation/SwiftUI/Color)

A representation of a color that adapts to a given context.

### Styling content

[`border(_:width:)`](/documentation/SwiftUI/View/border(_:width:))

Adds a border to this view with the specified style and width.

[`foregroundStyle(_:)`](/documentation/SwiftUI/View/foregroundStyle(_:))

Sets a view’s foreground elements to use a given style.

[`foregroundStyle(_:_:)`](/documentation/SwiftUI/View/foregroundStyle(_:_:))

Sets the primary and secondary levels of the foreground
style in the child view.

[`foregroundStyle(_:_:_:)`](/documentation/SwiftUI/View/foregroundStyle(_:_:_:))

Sets the primary, secondary, and tertiary levels of
the foreground style.

[`backgroundStyle(_:)`](/documentation/SwiftUI/View/backgroundStyle(_:))

Sets the specified style to render backgrounds within the view.

[`backgroundStyle`](/documentation/SwiftUI/EnvironmentValues/backgroundStyle)

An optional style that overrides the default system background
style when set.

[`ShapeStyle`](/documentation/SwiftUI/ShapeStyle)

A color or pattern to use when rendering a shape.

[`AnyShapeStyle`](/documentation/SwiftUI/AnyShapeStyle)

A type-erased ShapeStyle value.

[`Gradient`](/documentation/SwiftUI/Gradient)

A color gradient represented as an array of color stops, each having a
parametric location value.

[`MeshGradient`](/documentation/SwiftUI/MeshGradient)

A two-dimensional gradient defined by a 2D grid of positioned
colors.

[`AnyGradient`](/documentation/SwiftUI/AnyGradient)

A color gradient.

[`ShadowStyle`](/documentation/SwiftUI/ShadowStyle)

A style to use when rendering shadows.

[`Glass`](/documentation/SwiftUI/Glass)

A structure that defines the configuration of the Liquid Glass material.

### Transforming colors

[`brightness(_:)`](/documentation/SwiftUI/View/brightness(_:))

Brightens this view by the specified amount.

[`contrast(_:)`](/documentation/SwiftUI/View/contrast(_:))

Sets the contrast and separation between similar colors in this view.

[`colorInvert()`](/documentation/SwiftUI/View/colorInvert())

Inverts the colors in this view.

[`colorMultiply(_:)`](/documentation/SwiftUI/View/colorMultiply(_:))

Adds a color multiplication effect to this view.

[`saturation(_:)`](/documentation/SwiftUI/View/saturation(_:))

Adjusts the color saturation of this view.

[`grayscale(_:)`](/documentation/SwiftUI/View/grayscale(_:))

Adds a grayscale effect to this view.

[`hueRotation(_:)`](/documentation/SwiftUI/View/hueRotation(_:))

Applies a hue rotation effect to this view.

[`luminanceToAlpha()`](/documentation/SwiftUI/View/luminanceToAlpha())

Adds a luminance to alpha effect to this view.

[`materialActiveAppearance(_:)`](/documentation/SwiftUI/View/materialActiveAppearance(_:))

Sets an explicit active appearance for materials in this view.

[`materialActiveAppearance`](/documentation/SwiftUI/EnvironmentValues/materialActiveAppearance)

The behavior materials should use for their active state, defaulting to
`automatic`.

[`MaterialActiveAppearance`](/documentation/SwiftUI/MaterialActiveAppearance)

The behavior for how materials appear active and inactive.

### Scaling, rotating, or transforming a view

[`scaledToFill()`](/documentation/SwiftUI/View/scaledToFill())

Scales this view to fill its parent.

[`scaledToFit()`](/documentation/SwiftUI/View/scaledToFit())

Scales this view to fit its parent.

[`scaleEffect(_:anchor:)`](/documentation/SwiftUI/View/scaleEffect(_:anchor:))

Scales this view’s rendered output by the given amount in both the
horizontal and vertical directions, relative to an anchor point.

[`scaleEffect(_:anchor:)`](/documentation/SwiftUI/View/scaleEffect(_:anchor:))

Scales this view’s rendered output by the given amount in both the
horizontal and vertical directions, relative to an anchor point.

[`scaleEffect(x:y:anchor:)`](/documentation/SwiftUI/View/scaleEffect(x:y:anchor:))

Scales this view’s rendered output by the given horizontal and vertical
amounts, relative to an anchor point.

[`scaleEffect(x:y:z:anchor:)`](/documentation/SwiftUI/View/scaleEffect(x:y:z:anchor:))

Scales this view by the specified horizontal, vertical, and depth
factors, relative to an anchor point.

[`aspectRatio(_:contentMode:)`](/documentation/SwiftUI/View/aspectRatio(_:contentMode:))

Constrains this view’s dimensions to the specified aspect ratio.

[`rotationEffect(_:anchor:)`](/documentation/SwiftUI/View/rotationEffect(_:anchor:))

Rotates a view’s rendered output in two dimensions around the specified
point.

[`rotation3DEffect(_:axis:anchor:anchorZ:perspective:)`](/documentation/SwiftUI/View/rotation3DEffect(_:axis:anchor:anchorZ:perspective:))

Renders a view’s content as if it’s rotated in three dimensions around
the specified axis.

[`perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)`](/documentation/SwiftUI/View/perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:))

Renders a view’s content as if it’s rotated in three dimensions around
the specified axis.

[`rotation3DEffect(_:anchor:)`](/documentation/SwiftUI/View/rotation3DEffect(_:anchor:))

Rotates the view’s content by the specified 3D rotation value.

[`rotation3DEffect(_:axis:anchor:)`](/documentation/SwiftUI/View/rotation3DEffect(_:axis:anchor:))

Rotates the view’s content by an angle about an axis that you specify
as a tuple of elements.

[`transformEffect(_:)`](/documentation/SwiftUI/View/transformEffect(_:))

Applies an affine transformation to this view’s rendered output.

[`transform3DEffect(_:)`](/documentation/SwiftUI/View/transform3DEffect(_:))

Applies a 3D transformation to this view’s rendered output.

[`projectionEffect(_:)`](/documentation/SwiftUI/View/projectionEffect(_:))

Applies a projection transformation to this view’s rendered output.

[`ProjectionTransform`](/documentation/SwiftUI/ProjectionTransform)

[`ContentMode`](/documentation/SwiftUI/ContentMode)

Constants that define how a view’s content fills the available space.

### Masking and clipping

[`mask(alignment:_:)`](/documentation/SwiftUI/View/mask(alignment:_:))

Masks this view using the alpha channel of the given view.

[`clipped(antialiased:)`](/documentation/SwiftUI/View/clipped(antialiased:))

Clips this view to its bounding rectangular frame.

[`clipShape(_:style:)`](/documentation/SwiftUI/View/clipShape(_:style:))

Sets a clipping shape for this view.

### Applying blur and shadows

[`blur(radius:opaque:)`](/documentation/SwiftUI/View/blur(radius:opaque:))

Applies a Gaussian blur to this view.

[`shadow(color:radius:x:y:)`](/documentation/SwiftUI/View/shadow(color:radius:x:y:))

Adds a shadow to this view.

[`ColorMatrix`](/documentation/SwiftUI/ColorMatrix)

A matrix to use in an RGBA color transformation.

### Applying effects based on geometry

[`visualEffect(_:)`](/documentation/SwiftUI/View/visualEffect(_:))

Applies effects to this view, while providing access to layout
information through a geometry proxy.

[`visualEffect3D(_:)`](/documentation/SwiftUI/View/visualEffect3D(_:))

Applies effects to this view, while providing access to layout
information through a 3D geometry proxy.

[`VisualEffect`](/documentation/SwiftUI/VisualEffect)

Visual Effects change the visual appearance of a view without changing its
ancestors or descendents.

[`EmptyVisualEffect`](/documentation/SwiftUI/EmptyVisualEffect)

The base visual effect that you apply additional effect to.

### Compositing views

[`blendMode(_:)`](/documentation/SwiftUI/View/blendMode(_:))

Sets the blend mode for compositing this view with overlapping views.

[`compositingGroup()`](/documentation/SwiftUI/View/compositingGroup())

Wraps this view in a compositing group.

[`drawingGroup(opaque:colorMode:)`](/documentation/SwiftUI/View/drawingGroup(opaque:colorMode:))

Composites this view’s contents into an offscreen image before final
display.

[`BlendMode`](/documentation/SwiftUI/BlendMode)

Modes for compositing a view with overlapping content.

[`ColorRenderingMode`](/documentation/SwiftUI/ColorRenderingMode)

The set of possible working color spaces for color-compositing operations.

[`CompositorContent`](/documentation/SwiftUI/CompositorContent)

[`CompositorContentBuilder`](/documentation/SwiftUI/CompositorContentBuilder)

A result builder for composing a collection of [`CompositorContent`](/documentation/SwiftUI/CompositorContent)
elements.

[`AnyCompositorContent`](/documentation/SwiftUI/AnyCompositorContent)

Type erased compositor content.

### Measuring a view

[`GeometryReader`](/documentation/SwiftUI/GeometryReader)

A container view that defines its content as a function of its own size and
coordinate space.

[`GeometryReader3D`](/documentation/SwiftUI/GeometryReader3D)

A container view that defines its content as a function of its own
size and coordinate space.

[`GeometryProxy`](/documentation/SwiftUI/GeometryProxy)

A proxy for access to the size and coordinate space (for anchor resolution)
of the container view.

[`GeometryProxy3D`](/documentation/SwiftUI/GeometryProxy3D)

A proxy for access to the size and coordinate space of the container view.

[`coordinateSpace(_:)`](/documentation/SwiftUI/View/coordinateSpace(_:))

Assigns a name to the view’s coordinate space, so other code can operate
on dimensions like points and sizes relative to the named space.

[`CoordinateSpace`](/documentation/SwiftUI/CoordinateSpace)

A resolved coordinate space created by the coordinate space protocol.

[`CoordinateSpaceProtocol`](/documentation/SwiftUI/CoordinateSpaceProtocol)

A frame of reference within the layout system.

[`PhysicalMetric`](/documentation/SwiftUI/PhysicalMetric)

Provides access to a value in points that corresponds to the specified
physical measurement.

[`PhysicalMetricsConverter`](/documentation/SwiftUI/PhysicalMetricsConverter)

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

### Responding to a geometry change

[`onGeometryChange(for:of:action:)`](/documentation/SwiftUI/View/onGeometryChange(for:of:action:))

Adds an action to be performed when a value, created from a
geometry proxy, changes.

### Accessing Metal shaders

[`colorEffect(_:isEnabled:)`](/documentation/SwiftUI/View/colorEffect(_:isEnabled:))

Returns a new view that applies `shader` to `self` as a filter
effect on the color of each pixel.

[`distortionEffect(_:maxSampleOffset:isEnabled:)`](/documentation/SwiftUI/View/distortionEffect(_:maxSampleOffset:isEnabled:))

Returns a new view that applies `shader` to `self` as a
geometric distortion effect on the location of each pixel.

[`layerEffect(_:maxSampleOffset:isEnabled:)`](/documentation/SwiftUI/View/layerEffect(_:maxSampleOffset:isEnabled:))

Returns a new view that applies `shader` to `self` as a filter
on the raster layer created from `self`.

[`Shader`](/documentation/SwiftUI/Shader)

A reference to a function in a Metal shader library, along with its
bound uniform argument values.

[`ShaderFunction`](/documentation/SwiftUI/ShaderFunction)

A reference to a function in a Metal shader library.

[`ShaderLibrary`](/documentation/SwiftUI/ShaderLibrary)

A Metal shader library.

### Accessing geometric constructs

[`Axis`](/documentation/SwiftUI/Axis)

The horizontal or vertical dimension in a 2D coordinate system.

[`Angle`](/documentation/SwiftUI/Angle)

A geometric angle whose value you access in either radians or degrees.

[`UnitPoint`](/documentation/SwiftUI/UnitPoint)

A normalized 2D point in a view’s coordinate space.

[`UnitPoint3D`](/documentation/SwiftUI/UnitPoint3D)

A normalized 3D point in a view’s coordinate space.

[`Anchor`](/documentation/SwiftUI/Anchor)

An opaque value derived from an anchor source and a particular view.

[`DepthAlignmentID`](/documentation/SwiftUI/DepthAlignmentID)

[`Alignment3D`](/documentation/SwiftUI/Alignment3D)

An alignment in all three axes.

[`GeometryProxyCoordinateSpace3D`](/documentation/SwiftUI/GeometryProxyCoordinateSpace3D)

A representation of a `GeometryProxy3D` which can be used for
`CoordinateSpace3D` based conversions.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
