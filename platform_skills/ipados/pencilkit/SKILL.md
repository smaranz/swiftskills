---
name: IPADOS PencilKit
description: Apple PencilKit Documentation for IPADOS PencilKit on ipados.
---

# PencilKit

Capture touch and Apple Pencil input as a drawing, and display that content from your app.

## Overview

PencilKit makes it easy to incorporate hand-drawn content into your iPadOS or macOS apps. PencilKit provides a drawing environment for your iOS app that receives input from Apple Pencil or the user’s finger, and turns it into images you display in iPadOS, iOS, or macOS. The environment comes with tools for creating, erasing, and selecting lines.

You capture content in your iPad app using a [`PKCanvasView`](/documentation/PencilKit/PKCanvasView) object that you integrate into your existing view hierarchy. It supports the low-latency capture of touches originating from Apple Pencil or your finger. The canvas object sends final results as a [`PKDrawing`](/documentation/PencilKit/PKDrawing-swift.struct) object, whose contents you can save with your app’s content. You can also convert the drawn content into an image for display in iOS or macOS app.

For information about handling user interactions on Apple Pencil in your UIKit app, see <doc://com.apple.documentation/documentation/UIKit/apple-pencil-interactions>.

## Topics

### Canvas

[Drawing with PencilKit](/documentation/PencilKit/drawing-with-pencilkit)

Add expressive, low-latency drawing to your app using PencilKit.

[Customizing Scribble with Interactions](/documentation/PencilKit/customizing-scribble-with-interactions)

Enable writing on a non-text-input view by adding interactions.

[Inspecting, Modifying, and Constructing PencilKit Drawings](/documentation/PencilKit/inspecting-modifying-and-constructing-pencilkit-drawings)

Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings.

[`PKCanvasView`](/documentation/PencilKit/PKCanvasView)

A view that captures Apple Pencil input and displays the rendered results in an iOS app.

[`PKDrawing`](/documentation/PencilKit/PKDrawing-swift.struct)

A structure representing the drawing information captured by a canvas view.

[`PKStroke`](/documentation/PencilKit/PKStroke-swift.struct)

A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas.

[`PKStrokePath`](/documentation/PencilKit/PKStrokePath-swift.struct)

A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

[`PKStrokePoint`](/documentation/PencilKit/PKStrokePoint-swift.struct)

A structure that represents the properties of a specific point along a stroke’s path.

[`PKInk`](/documentation/PencilKit/PKInk-swift.struct)

A structure that represents an ink that specifies its type, color, and width.

### Canvas

[`PKCanvasView`](/documentation/PencilKit/PKCanvasView)

A view that captures Apple Pencil input and displays the rendered results in an iOS app.

[`PKDrawingReference`](/documentation/PencilKit/PKDrawingReference)

A data structure that contains the drawing information captured by a canvas view.

[`PKStrokeReference`](/documentation/PencilKit/PKStrokeReference)

A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.

[`PKStrokePathReference`](/documentation/PencilKit/PKStrokePathReference)

A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.

[`PKStrokePointReference`](/documentation/PencilKit/PKStrokePointReference)

A class that represents the properties of a specific point along a stroke’s path.

[`PKInkReference`](/documentation/PencilKit/PKInkReference)

Provides a description of the creation and rendering of marks on a canvas.

[`PKFloatRange`](/documentation/PencilKit/PKFloatRange)

A utility class that represents range components of a stroke.

### Tools

[Configuring the PencilKit tool picker](/documentation/PencilKit/configuring-the-pencilkit-tool-picker)

Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app.

[`PKToolPicker`](/documentation/PencilKit/PKToolPicker)

A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.

[`PKInkingTool`](/documentation/PencilKit/PKInkingTool-swift.struct)

A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

[`PKEraserTool`](/documentation/PencilKit/PKEraserTool-swift.struct)

A tool for erasing previously drawn content in a canvas view.

[`PKLassoTool`](/documentation/PencilKit/PKLassoTool-swift.struct)

A tool for selecting stroked lines and shapes in a canvas view.

[`PKTool`](/documentation/PencilKit/PKTool-swift.protocol)

An interface adopted by drawing and writing tools used by a canvas view.

### Tools

[`PKToolPicker`](/documentation/PencilKit/PKToolPicker)

A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from.

[`PKInkingToolReference`](/documentation/PencilKit/PKInkingToolReference)

An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view.

[`PKEraserToolReference`](/documentation/PencilKit/PKEraserToolReference)

A tool for erasing previously drawn content in a canvas view.

[`PKLassoToolReference`](/documentation/PencilKit/PKLassoToolReference)

A tool for selecting stroked lines and shapes in a canvas view.

[`PKTool`](/documentation/PencilKit/PKTool-c.class)

An abstract base class for tools used by a canvas view.

### Backward compatibility

[Supporting backward compatibility for ink types](/documentation/PencilKit/supporting-backward-compatibility-for-ink-types)

Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features.

[`PKContentVersion`](/documentation/PencilKit/PKContentVersion)

Constants that represent versions of PencilKit for backward compatibility.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
