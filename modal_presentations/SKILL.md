---
name: Modal presentations
description: Rork-Max Quality skill for Modal presentations. Actionable patterns and best practices for SwiftUI development.
---

# Modal presentations

Present content in a separate view that offers focused interaction.
To draw attention to an important, narrowly scoped task, you display
a modal presentation, like an alert, popover, sheet, or confirmation
dialog.
In SwiftUI, you create a modal presentation using a view
modifier that defines how the presentation looks and the condition
under which SwiftUI presents it. SwiftUI detects when the condition
changes and makes the presentation for you. Because you provide a
`Binding` to the condition that initiates the presentation, SwiftUI
can reset the underlying value when the user dismisses the presentation.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Building hierarchical drill-down flows (settings, detail views)
- Implementing tab-based or sidebar navigation patterns
- Presenting modal sheets, popovers, alerts, or confirmation dialogs
- Creating deep-linkable navigation paths with `NavigationPath`

## Best Practices

- Use `NavigationStack` with a `path` binding for programmatic, deep-linkable navigation
- Prefer `NavigationSplitView` on iPad/Mac for sidebar + detail layouts
- Model navigation state explicitly so it can be saved, restored, and deep-linked
- Use `.sheet()`, `.fullScreenCover()`, and `.popover()` for modal presentations

## Common Pitfalls

- Using the deprecated `NavigationView` instead of `NavigationStack`/`NavigationSplitView`
- Nesting `NavigationStack` inside another `NavigationStack` causing double navigation bars
- Forgetting to make navigation destination types `Hashable` for `navigationDestination(for:)`

## Key APIs

### Configuring a dialog

| API | Purpose |
|-----|---------|
| `DialogSeverity` | The severity of an alert or confirmation dialog. |

### Showing a sheet, cover, or popover

| API | Purpose |
|-----|---------|
| `sheet(isPresented:onDismiss:content:)` | Presents a sheet when a binding to a Boolean value that you |
| `sheet(item:onDismiss:content:)` | Presents a sheet using the given item as a data source |
| `fullScreenCover(isPresented:onDismiss:content:)` | Presents a modal view that covers as much of the screen as |
| `fullScreenCover(item:onDismiss:content:)` | Presents a modal view that covers as much of the screen as |
| `popover(item:attachmentAnchor:arrowEdge:content:)` | Presents a popover using the given item as a data source for the |
| `popover(isPresented:attachmentAnchor:arrowEdge:content:)` | Presents a popover when a given condition is true. |
| `PopoverAttachmentAnchor` | An attachment anchor for a popover. |

### Adapting a presentation size

| API | Purpose |
|-----|---------|
| `presentationCompactAdaptation(horizontal:vertical:)` | Specifies how to adapt a presentation to horizontally and vertically |
| `presentationCompactAdaptation(_:)` | Specifies how to adapt a presentation to compact size classes. |
| `PresentationAdaptation` | Strategies for adapting a presentation to a different size class. |
| `presentationSizing(_:)` | Sets the sizing of the containing presentation. |
| `PresentationSizing` | A type that defines the size of the presentation content and how the |
| `PresentationSizingRoot` | A proxy to a view provided to the presentation with a |
| `PresentationSizingContext` | Contextual information about a presentation. |

### Configuring a sheet’s height

| API | Purpose |
|-----|---------|
| `presentationDetents(_:)` | Sets the available detents for the enclosing sheet. |
| `presentationDetents(_:selection:)` | Sets the available detents for the enclosing sheet, giving you |
| `presentationContentInteraction(_:)` | Configures the behavior of swipe gestures on a presentation. |
| `presentationDragIndicator(_:)` | Sets the visibility of the drag indicator on top of a sheet. |
| `PresentationDetent` | A type that represents a height where a sheet naturally rests. |
| `CustomPresentationDetent` | The definition of a custom detent with a calculated height. |
| `PresentationContentInteraction` | A behavior that you can use to influence how a presentation responds to |

### Styling a sheet and its background

| API | Purpose |
|-----|---------|
| `presentationCornerRadius(_:)` | Requests that the presentation have a specific corner radius. |
| `presentationBackground(_:)` | Sets the presentation background of the enclosing sheet using a shape |
| `presentationBackground(alignment:content:)` | Sets the presentation background of the enclosing sheet to a custom |
| `presentationBackgroundInteraction(_:)` | Controls whether people can interact with the view behind a |
| `PresentationBackgroundInteraction` | The kinds of interaction available to views behind a presentation. |

### Presenting an alert

| API | Purpose |
|-----|---------|
| `AlertScene` | A scene that renders itself as a standalone alert dialog. |
| `alert(_:isPresented:actions:)` | Presents an alert when a given condition is true, using a text view for |
| `alert(_:isPresented:presenting:actions:)` | Presents an alert using the given data to produce the alert’s content |
| `alert(isPresented:error:actions:)` | Presents an alert when an error is present. |
| `alert(_:isPresented:actions:message:)` | Presents an alert with a message when a given condition is true using |
| `alert(_:isPresented:presenting:actions:message:)` | Presents an alert with a message using the given data to produce the |
| `alert(isPresented:error:actions:message:)` | Presents an alert with a message when an error is present. |

### Getting confirmation for an action

| API | Purpose |
|-----|---------|
| `confirmationDialog(_:isPresented:titleVisibility:actions:)` | Presents a confirmation dialog when a given condition is true, using a |
| `confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)` | Presents a confirmation dialog using data to produce the dialog’s |
| `dismissalConfirmationDialog(_:shouldPresent:actions:)` | Presents a confirmation dialog when a dismiss action has been triggered. |

### Showing a confirmation dialog with a message

| API | Purpose |
|-----|---------|
| `confirmationDialog(_:isPresented:titleVisibility:actions:message:)` | Presents a confirmation dialog with a message when a given condition is |
| `confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)` | Presents a confirmation dialog with a message using data to produce the |
| `dismissalConfirmationDialog(_:shouldPresent:actions:message:)` | Presents a confirmation dialog when a dismiss action has been triggered. |

### Configuring a dialog

| API | Purpose |
|-----|---------|
| `dialogIcon(_:)` | Configures the icon used by dialogs within this view. |
| `dialogIcon(_:)` | Configures the icon used by alerts. |
| `dialogSeverity(_:)` | — |
| `dialogSeverity(_:)` | Sets the severity for alerts. |
| `dialogSuppressionToggle(isSuppressed:)` | Enables user suppression of dialogs and alerts presented within `self`, |
| `dialogSuppressionToggle(isSuppressed:)` | Enables user suppression of an alert with a custom suppression |
| `dialogSuppressionToggle(_:isSuppressed:)` | Enables user suppression of dialogs and alerts presented within `self`, |
| `dialogSuppressionToggle(_:isSuppressed:)` | Enables user suppression of an alert with a custom suppression |

### Exporting to file

| API | Purpose |
|-----|---------|
| `fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)` | Presents a system interface for exporting a document that’s stored in |
| `fileExporter(isPresented:documents:contentType:onCompletion:)` | Presents a system interface for exporting a collection of value type |
| `fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)` | Presents a system interface for allowing the user to export a |
| `fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)` | Presents a system dialog for allowing the user to export a |
| `fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)` | Presents a system interface allowing the user to export |
| `fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)` | Presents a system interface allowing the user to export |
| `fileExporterFilenameLabel(_:)` | On macOS, configures the `fileExporter` |

### Importing from file

| API | Purpose |
|-----|---------|
| `fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)` | Presents a system interface for allowing the user to import multiple |
| `fileImporter(isPresented:allowedContentTypes:onCompletion:)` | Presents a system interface for allowing the user to import an existing |
| `fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)` | Presents a system dialog for allowing the user to import multiple |

### Moving a file

| API | Purpose |
|-----|---------|
| `fileMover(isPresented:file:onCompletion:)` | Presents a system interface for allowing the user to move an existing |
| `fileMover(isPresented:files:onCompletion:)` | Presents a system interface for allowing the user to move a collection |
| `fileMover(isPresented:file:onCompletion:onCancellation:)` | Presents a system dialog for allowing the user to move |
| `fileMover(isPresented:files:onCompletion:onCancellation:)` | Presents a system dialog for allowing the user to move |

### Configuring a file dialog

| API | Purpose |
|-----|---------|
| `fileDialogBrowserOptions(_:)` | On macOS, configures the `fileExporter`, `fileImporter`, |
| `fileDialogConfirmationLabel(_:)` | On macOS, configures the `fileExporter`, `fileImporter`, |
| `fileDialogCustomizationID(_:)` | On macOS, configures the `fileExporter`, `fileImporter`, |
| `fileDialogDefaultDirectory(_:)` | Configures the `fileExporter`, `fileImporter`, or `fileMover` to |
| `fileDialogImportsUnresolvedAliases(_:)` | On macOS, configures the `fileExporter`, `fileImporter`, |
| `fileDialogMessage(_:)` | On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` |
| `fileDialogURLEnabled(_:)` | On macOS, configures the `fileImporter` |
| `FileDialogBrowserOptions` | The way that file dialogs present the file system. |

### Presenting an inspector

| API | Purpose |
|-----|---------|
| `inspector(isPresented:content:)` | Inserts an inspector at the applied position in the view hierarchy. |
| `inspectorColumnWidth(_:)` | Sets a fixed, preferred width for the inspector containing this view |
| `inspectorColumnWidth(min:ideal:max:)` | Sets a flexible, preferred width for the inspector in a trailing-column |

### Dismissing a presentation

| API | Purpose |
|-----|---------|
| `isPresented` | A Boolean value that indicates whether the view associated with this |
| `dismiss` | An action that dismisses the current presentation. |
| `DismissAction` | An action that dismisses a presentation. |
| `interactiveDismissDisabled(_:)` | Conditionally prevents interactive dismissal of presentations like |

### Deprecated modal presentations

| API | Purpose |
|-----|---------|
| `Alert` | A representation of an alert presentation. |
| `ActionSheet` | A representation of an action sheet presentation. |
