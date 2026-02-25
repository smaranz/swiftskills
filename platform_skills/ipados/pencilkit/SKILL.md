---
name: IPADOS PencilKit
description: Rork-Max Quality skill for IPADOS PencilKit. Platform-native patterns and best practices for ipados development.
---

# IPADOS PencilKit

Capture touch and Apple Pencil input as a drawing, and display that content from your app.
PencilKit makes it easy to incorporate hand-drawn content into your iPadOS or macOS apps. PencilKit provides a drawing environment for your iOS app that receives input from Apple Pencil or the user’s finger, and turns it into images you display in iPadOS, iOS, or macOS. The environment comes with tools for creating, erasing, and selecting lines.
You capture content in your iPad app using a `PKCanvasView` object that you integrate into your existing view hierarchy. It supports the low-latency capture of touches originating from Apple Pencil or your finger. The canvas object sends final results as a `PKDrawing` object, whose contents you can save with your app’s content. You can also convert the drawn content into an image for display in iOS or macOS app.
For information about handling user interactions on Apple Pencil in your UIKit app, see apple-pencil-interactions.

## 🚀 Rork-Max Quality Snippet

```swift
import PencilKit
import UIKit

class DrawingViewController: UIViewController, PKCanvasViewDelegate {
    let canvasView = PKCanvasView()
    let toolPicker = PKToolPicker()

    override func viewDidLoad() {
        super.viewDidLoad()
        canvasView.delegate = self
        canvasView.drawingPolicy = .anyInput
        canvasView.tool = PKInkingTool(.pen, color: .systemBlue, width: 5)
        canvasView.frame = view.bounds
        canvasView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(canvasView)

        toolPicker.setVisible(true, forFirstResponder: canvasView)
        toolPicker.addObserver(canvasView)
        canvasView.becomeFirstResponder()
    }

    func canvasViewDrawingDidChange(_ canvasView: PKCanvasView) {
        // Auto-save or process drawing
        let drawing = canvasView.drawing
        let image = drawing.image(from: drawing.bounds, scale: UIScreen.main.scale)
    }
}
```

## 💎 Elite Implementation Tips

- Use `PKToolPicker` to present the system drawing tool palette
- Set `.drawingPolicy = .anyInput` for finger + pencil, `.pencilOnly` for pencil-exclusive
- Extract raster images with `drawing.image(from:scale:)` for export/sharing

## When to Use

- Implementing iPad-specific features like Apple Pencil, Stage Manager, or drag-and-drop
- Building productivity interfaces with multi-column navigation

## Best Practices

- Support Apple Pencil with `PKCanvasView` for drawing and handwriting
- Design for keyboard and trackpad in addition to touch
- Use `NavigationSplitView` for two- or three-column layouts

## Common Pitfalls

- Testing only in portrait — iPad apps must handle all orientations and multitasking sizes
- Not supporting external keyboard shortcuts — iPad power users expect them

## Key APIs

### Canvas

| API | Purpose |
|-----|---------|
| `Drawing with PencilKit` | Add expressive, low-latency drawing to your app using PencilKit. |
| `Customizing Scribble with Interactions` | Enable writing on a non-text-input view by adding interactions. |
| `Inspecting, Modifying, and Constructing PencilKit Drawings` | Score users’ ability to match PencilKit drawings generated from text, by accessing the strokes and points inside PencilKit drawings. |
| `PKCanvasView` | A view that captures Apple Pencil input and displays the rendered results in an iOS app. |
| `PKDrawing` | A structure representing the drawing information captured by a canvas view. |
| `PKStroke` | A structure that represents the paths, boundaries, and other properties of a stroke drawn on a canvas. |
| `PKStrokePath` | A structure that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path. |
| `PKStrokePoint` | A structure that represents the properties of a specific point along a stroke’s path. |

### Canvas

| API | Purpose |
|-----|---------|
| `PKCanvasView` | A view that captures Apple Pencil input and displays the rendered results in an iOS app. |
| `PKDrawingReference` | A data structure that contains the drawing information captured by a canvas view. |
| `PKStrokeReference` | A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas. |
| `PKStrokePathReference` | A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path. |
| `PKStrokePointReference` | A class that represents the properties of a specific point along a stroke’s path. |
| `PKInkReference` | Provides a description of the creation and rendering of marks on a canvas. |
| `PKFloatRange` | A utility class that represents range components of a stroke. |

### Tools

| API | Purpose |
|-----|---------|
| `Configuring the PencilKit tool picker` | Incorporate a custom PencilKit tool picker with a variety of system and custom tools into a drawing app. |
| `PKToolPicker` | A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from. |
| `PKInkingTool` | A structure that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view. |
| `PKEraserTool` | A tool for erasing previously drawn content in a canvas view. |
| `PKLassoTool` | A tool for selecting stroked lines and shapes in a canvas view. |
| `PKTool` | An interface adopted by drawing and writing tools used by a canvas view. |

### Tools

| API | Purpose |
|-----|---------|
| `PKToolPicker` | A tool palette that displays a selection of drawing tools and colors for tools that a person can choose from. |
| `PKInkingToolReference` | An object that defines the drawing characteristics (width, color, pen style) to use when drawing lines on a canvas view. |
| `PKEraserToolReference` | A tool for erasing previously drawn content in a canvas view. |
| `PKLassoToolReference` | A tool for selecting stroked lines and shapes in a canvas view. |
| `PKTool` | An abstract base class for tools used by a canvas view. |

### Backward compatibility

| API | Purpose |
|-----|---------|
| `Supporting backward compatibility for ink types` | Leverage the latest PencilKit features while providing a good user experience in earlier versions of the OS that don’t support those features. |
| `PKContentVersion` | Constants that represent versions of PencilKit for backward compatibility. |
