---
name: Clipboard
description: Rork-Max Quality skill for Clipboard. Actionable patterns and best practices for SwiftUI development.
---

# Clipboard

Enable people to move or duplicate items by issuing Copy and Paste commands.
When people issue standard Copy and Cut commands, they expect to move
items to the system’s Clipboard, from which they can paste the items into
another place in the same app or into another app. Your app can participate
in this activity if you add view modifiers that indicate how to respond to
the standard commands.
In your copy and paste modifiers, provide or accept types that conform to the
protocol, or that inherit from the
When possible, prefer using transferable items.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct ClipboardExample: View {
    @State private var copiedText = ""

    var body: some View {
        VStack(spacing: 16) {
            Text("Tap to copy")
                .padding()
                .background(.blue, in: Capsule())
                .foregroundStyle(.white)
                .onTapGesture {
                    UIPasteboard.general.string = "Hello from Rork!"
                }

            PasteButton(payloadType: String.self) { strings in
                copiedText = strings.first ?? ""
            }

            if !copiedText.isEmpty {
                Text("Pasted: \(copiedText)")
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `PasteButton` for secure paste — it shows system UI confirming the paste action
- Adopt `Transferable` protocol for custom types to work with copy/paste and drag-and-drop
- Use `.copyable()` and `.pasteDestination()` modifiers for inline clipboard support


## When to Use

- Handling tap, long press, drag, magnification, or rotation gestures
- Implementing drag-and-drop between views or apps
- Reading clipboard content or providing copy/paste support
- Processing keyboard, pencil, or game controller input events

## Best Practices

- Use `.onTapGesture` for simple taps; `DragGesture` for custom interactive motion
- Combine `.gesture()` with `.simultaneously()` or `.sequenced()` for complex interactions
- Prefer `Transferable` protocol (iOS 16+) for modern drag-and-drop and sharing
- Always provide visual feedback during gesture recognition (scale, opacity, highlight)

## Common Pitfalls

- Gesture conflicts with `ScrollView` — use `.simultaneousGesture()` or `.highPriorityGesture()`
- Forgetting minimum distance on `DragGesture` when used inside scroll views
- Not testing gestures with VoiceOver — ensure all gesture-driven actions have accessible alternatives

## Key APIs

### Copying transferable items

| API | Purpose |
|-----|---------|
| `copyable(_:)` | Specifies a list of items to copy in response to the system’s Copy |
| `cuttable(for:action:)` | Specifies an action that moves items to the Clipboard in response to |
| `pasteDestination(for:action:validator:)` | Specifies an action that adds validated items to a view in response to |

### Copying items using item providers

| API | Purpose |
|-----|---------|
| `onCopyCommand(perform:)` | Adds an action to perform in response to the system’s Copy command. |
| `onCutCommand(perform:)` | Adds an action to perform in response to the system’s Cut command. |
| `onPasteCommand(of:perform:)` | Adds an action to perform in response to the system’s Paste command. |
| `onPasteCommand(of:validator:perform:)` | Adds an action to perform in response to the system’s Paste command with |
