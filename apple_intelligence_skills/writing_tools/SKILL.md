---
name: Apple Intelligence: UIWritingToolsCoordinator
description: Specialized skill for Apple Intelligence: UIWritingToolsCoordinator based on official Apple Developer Documentation.
---

# UIWritingToolsCoordinator

An object that manages interactions between Writing Tools and
your custom text view.

```
@MainActor class UIWritingToolsCoordinator
```

## Overview

Add a `UIWritingToolsCoordinator` object to a custom view when you
want to add Writing Tools support to that view. The coordinator manages
interactions between your view and the Writing Tools UI and back-end
capabilities. When creating a coordinator, you supply a delegate object
to respond to requests from the system and provide needed information.
Your delegate delivers your view’s text to Writing Tools, incorporates
suggested changes back into your text storage, and supports the animations
that Writing Tools creates to show the state of an operation.

Create the `UIWritingToolsCoordinator` object when setting up your UI, and
initialize it with a custom object that adopts the [`UIWritingToolsCoordinator.Delegate`](/documentation/UIKit/UIWritingToolsCoordinator/Delegate-swift.protocol)
protocol. Add the coordinator to your view using the [`addInteraction(_:)`](/documentation/UIKit/UIView/addInteraction(_:))
method. When a coordinator is present on a view, the system adds UI elements
to initiate Writing Tools operations.

When defining the delegate, choose an object from your app that has access
to your view and its text storage. You can adopt the [`UIWritingToolsCoordinator.Delegate`](/documentation/UIKit/UIWritingToolsCoordinator/Delegate-swift.protocol)
protocol in the view itself, or in another type that your view uses to
manage content. During the interactions with Writing Tools, the delegate
gets and sets the contents of the view’s text storage and supports Writing Tools behaviors.

> Note: You don’t need to create an `UIWritingToolsCoordinator`  object
> if you display text using a ``doc://com.apple.uikit/documentation/UIKit/UITextView``,
> <doc://com.apple.documentation/documentation/AppKit/NSTextView>,
> <doc://com.apple.documentation/documentation/SwiftUI/Text>,
> <doc://com.apple.documentation/documentation/SwiftUI/TextField>, or
> <doc://com.apple.documentation/documentation/SwiftUI/TextEditor> view.
> Those views already include the required support to handle Writing Tools
> interactions.

## Topics

### Creating a coordinator object

[`init(delegate:)`](/documentation/UIKit/UIWritingToolsCoordinator/init(delegate:))

Creates a writing tools coordinator and assigns the specified
delegate object to it.

### Checking the availability of Writing Tools

[`isWritingToolsAvailable`](/documentation/UIKit/UIWritingToolsCoordinator/isWritingToolsAvailable)

A Boolean value that indicates whether Writing Tools features are
currently available.

### Managing Writing Tools interactions

[`delegate`](/documentation/UIKit/UIWritingToolsCoordinator/delegate-swift.property)

The object that handles Writing Tools interactions for your view.

[`UIWritingToolsCoordinator.Delegate`](/documentation/UIKit/UIWritingToolsCoordinator/Delegate-swift.protocol)

An interface that you use to manage interactions between Writing Tools
and your custom text view.

### Getting the host views for effects

[`effectContainerView`](/documentation/UIKit/UIWritingToolsCoordinator/effectContainerView)

The view that Writing Tools uses to display visual effects during
the text-rewriting process.

[`decorationContainerView`](/documentation/UIKit/UIWritingToolsCoordinator/decorationContainerView)

The view that Writing Tools uses to display background decorations
such as proofreading marks.

### Configuring the experience

[`preferredBehavior`](/documentation/UIKit/UIWritingToolsCoordinator/preferredBehavior)

The level of Writing Tools support you want the system to provide
for your view.

[`behavior`](/documentation/UIKit/UIWritingToolsCoordinator/behavior)

The actual level of Writing Tools support the system provides for your view.

[`preferredResultOptions`](/documentation/UIKit/UIWritingToolsCoordinator/preferredResultOptions)

The type of content you allow Writing Tools to generate for your custom
text view.

[`resultOptions`](/documentation/UIKit/UIWritingToolsCoordinator/resultOptions)

The type of content the system generates for your custom text view.

### Reporting changes to Writing Tools

[`updateRange(_:with:reason:forContextWithIdentifier:)`](/documentation/UIKit/UIWritingToolsCoordinator/updateRange(_:with:reason:forContextWithIdentifier:))

Informs the coordinator about changes your app made to the text
in the specified context object.

[`updateForReflowedTextInContextWithIdentifier(_:)`](/documentation/UIKit/UIWritingToolsCoordinator/updateForReflowedTextInContextWithIdentifier(_:))

Informs the coordinator that a change occurred to the view or its text
that requires a layout update.

[`UIWritingToolsCoordinator.TextUpdateReason`](/documentation/UIKit/UIWritingToolsCoordinator/TextUpdateReason)

Constants that specify the reason you updated your view’s content
outside of the Writing Tools workflow.

### Managing the current state

[`stopWritingTools()`](/documentation/UIKit/UIWritingToolsCoordinator/stopWritingTools())

Stops the current Writing Tools operation and dismisses the system UI.

[`state`](/documentation/UIKit/UIWritingToolsCoordinator/state-swift.property)

The current level of Writing Tools activity in your view.

[`UIWritingToolsCoordinator.State`](/documentation/UIKit/UIWritingToolsCoordinator/State-swift.enum)

The states that indicate the current activity, if any, Writing Tools
is performing in your view.

### Getting the supporting types

[`UIWritingToolsCoordinator.ContextScope`](/documentation/UIKit/UIWritingToolsCoordinator/ContextScope)

Options that indicate how much of your content Writing Tools requested.

[`UIWritingToolsCoordinator.TextReplacementReason`](/documentation/UIKit/UIWritingToolsCoordinator/TextReplacementReason)

Options that indicate whether Writing Tools is animating changes to
your view’s text.

[`UIWritingToolsCoordinator.TextAnimation`](/documentation/UIKit/UIWritingToolsCoordinator/TextAnimation)

The types of animations that Writing Tools performs during an interactive
update of your view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
