---
name: Apple Intelligence: UIWritingToolsCoordinator
description: Rork-Max Quality skill for Apple Intelligence: UIWritingToolsCoordinator. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: UIWritingToolsCoordinator

An object that manages interactions between Writing Tools and
your custom text view.
```
@MainActor class UIWritingToolsCoordinator
```
Add a `UIWritingToolsCoordinator` object to a custom view when you
want to add Writing Tools support to that view. The coordinator manages
interactions between your view and the Writing Tools UI and back-end
capabilities. When creating a coordinator, you supply a delegate object
to respond to requests from the system and provide needed information.
Your delegate delivers your view’s text to Writing Tools, incorporates
suggested changes back into your text storage, and supports the animations
that Writing Tools creates to show the state of an operation.
Create the `UIWritingToolsCoordinator` object when setting up your UI, and
initialize it with a custom object that adopts the `UIWritingToolsCoordinator.Delegate`
protocol. Add the coordinator to your view using the `addInteraction(_:)`
method. When a coordinator is present on a view, the system adds UI elements
to initiate Writing Tools operations.
When defining the delegate, choose an object from your app that has access
to your view and its text storage. You can adopt the `UIWritingToolsCoordinator.Delegate`
protocol in the view itself, or in another type that your view uses to
manage content. During the interactions with Writing Tools, the delegate
gets and sets the contents of the view’s text storage and supports Writing Tools behaviors.
> Note: You don’t need to create an `UIWritingToolsCoordinator` object
> if you display text using a `UITextView`,
> NSTextView,
> Text,
> TextField, or
> TextEditor view.
> Those views already include the required support to handle Writing Tools
> interactions.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

// Standard UITextView — Writing Tools work automatically, no extra code needed
let standardTextView = UITextView()

// Custom text view — add UIWritingToolsCoordinator for Writing Tools support
class CustomTextView: UIView {
    let coordinator: UIWritingToolsCoordinator

    init() {
        let delegate = WritingToolsHandler()
        coordinator = UIWritingToolsCoordinator(delegate: delegate)
        super.init(frame: .zero)
        addInteraction(coordinator)
    }

    required init?(coder: NSCoder) { fatalError() }
}

class WritingToolsHandler: NSObject, UIWritingToolsCoordinator.Delegate {
    func writingToolsCoordinator(_ coordinator: UIWritingToolsCoordinator,
                                  requestsTextIn range: NSRange,
                                  completion: @escaping (NSAttributedString) -> Void) {
        // Return the current text in the requested range
        let text = NSAttributedString(string: "Current text content")
        completion(text)
    }
}
```

## 💎 Elite Implementation Tips

- `UITextView`, `NSTextView`, `TextField`, and `TextEditor` get Writing Tools automatically — no code needed
- Only use `UIWritingToolsCoordinator` for fully custom text views that don't use system text input
- Implement the `Delegate` to provide text content, accept rewrites, and support proofreading animations
- Set `.preferredBehavior` to `.limited` if your view only supports plain text (no rich text rewrites)
- Writing Tools are available on iOS 18.1+, iPadOS 18.1+, and macOS 15.1+

## When to Use

- Integrating system writing tools (rewrite, proofread, summarize) into text views
- Enhancing text editing experiences with AI-powered writing assistance

## Best Practices

- Adopt `UIWritingToolsCoordinator` for custom text views
- Standard `UITextView` gets Writing Tools automatically — avoid disabling it

## Common Pitfalls

- Custom text views that don't adopt `UITextInteraction` won't get Writing Tools

## Key APIs

### Creating a coordinator object

| API | Purpose |
|-----|---------|
| `init(delegate:)` | Creates a writing tools coordinator and assigns the specified |

### Checking the availability of Writing Tools

| API | Purpose |
|-----|---------|
| `isWritingToolsAvailable` | A Boolean value that indicates whether Writing Tools features are |

### Managing Writing Tools interactions

| API | Purpose |
|-----|---------|
| `delegate` | The object that handles Writing Tools interactions for your view. |
| `UIWritingToolsCoordinator.Delegate` | An interface that you use to manage interactions between Writing Tools |

### Getting the host views for effects

| API | Purpose |
|-----|---------|
| `effectContainerView` | The view that Writing Tools uses to display visual effects during |
| `decorationContainerView` | The view that Writing Tools uses to display background decorations |

### Configuring the experience

| API | Purpose |
|-----|---------|
| `preferredBehavior` | The level of Writing Tools support you want the system to provide |
| `behavior` | The actual level of Writing Tools support the system provides for your view. |
| `preferredResultOptions` | The type of content you allow Writing Tools to generate for your custom |
| `resultOptions` | The type of content the system generates for your custom text view. |

### Reporting changes to Writing Tools

| API | Purpose |
|-----|---------|
| `updateRange(_:with:reason:forContextWithIdentifier:)` | Informs the coordinator about changes your app made to the text |
| `updateForReflowedTextInContextWithIdentifier(_:)` | Informs the coordinator that a change occurred to the view or its text |
| `UIWritingToolsCoordinator.TextUpdateReason` | Constants that specify the reason you updated your view’s content |

### Managing the current state

| API | Purpose |
|-----|---------|
| `stopWritingTools()` | Stops the current Writing Tools operation and dismisses the system UI. |
| `state` | The current level of Writing Tools activity in your view. |
| `UIWritingToolsCoordinator.State` | The states that indicate the current activity, if any, Writing Tools |

### Getting the supporting types

| API | Purpose |
|-----|---------|
| `UIWritingToolsCoordinator.ContextScope` | Options that indicate how much of your content Writing Tools requested. |
| `UIWritingToolsCoordinator.TextReplacementReason` | Options that indicate whether Writing Tools is animating changes to |
| `UIWritingToolsCoordinator.TextAnimation` | The types of animations that Writing Tools performs during an interactive |
