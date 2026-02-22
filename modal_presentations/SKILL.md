---
name: Modal presentations
description: Rork-Max Quality skill for Modal presentations. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Modal presentations


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Modal presentations

Present content in a separate view that offers focused interaction.

## Overview

To draw attention to an important, narrowly scoped task, you display
a modal presentation, like an alert, popover, sheet, or confirmation
dialog.

![](images/com.apple.SwiftUI/modal-presentations-hero@2x.png)

In SwiftUI, you create a modal presentation using a view
modifier that defines how the presentation looks and the condition
under which SwiftUI presents it. SwiftUI detects when the condition
changes and makes the presentation for you. Because you provide a
[`Binding`](/documentation/SwiftUI/Binding) to the condition that initiates the presentation, SwiftUI
can reset the underlying value when the user dismisses the presentation.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/modality>
in the Human Interface Guidelines.

## Topics

### Configuring a dialog

[`DialogSeverity`](/documentation/SwiftUI/DialogSeverity)

The severity of an alert or confirmation dialog.

### Showing a sheet, cover, or popover

[`sheet(isPresented:onDismiss:content:)`](/documentation/SwiftUI/View/sheet(isPresented:onDismiss:content:))

Presents a sheet when a binding to a Boolean value that you
provide is true.

[`sheet(item:onDismiss:content:)`](/documentation/SwiftUI/View/sheet(item:onDismiss:content:))

Presents a sheet using the given item as a data source
for the sheet’s content.

[`fullScreenCover(isPresented:onDismiss:content:)`](/documentation/SwiftUI/View/fullScreenCover(isPresented:onDismiss:content:))

Presents a modal view that covers as much of the screen as
possible when binding to a Boolean value you provide is true.

[`fullScreenCover(item:onDismiss:content:)`](/documentation/SwiftUI/View/fullScreenCover(item:onDismiss:content:))

Presents a modal view that covers as much of the screen as
possible using the binding you provide as a data source for the
sheet’s content.

[`popover(item:attachmentAnchor:arrowEdge:content:)`](/documentation/SwiftUI/View/popover(item:attachmentAnchor:arrowEdge:content:))

Presents a popover using the given item as a data source for the
popover’s content.

[`popover(isPresented:attachmentAnchor:arrowEdge:content:)`](/documentation/SwiftUI/View/popover(isPresented:attachmentAnchor:arrowEdge:content:))

Presents a popover when a given condition is true.

[`PopoverAttachmentAnchor`](/documentation/SwiftUI/PopoverAttachmentAnchor)

An attachment anchor for a popover.

### Adapting a presentation size

[`presentationCompactAdaptation(horizontal:vertical:)`](/documentation/SwiftUI/View/presentationCompactAdaptation(horizontal:vertical:))

Specifies how to adapt a presentation to horizontally and vertically
compact size classes.

[`presentationCompactAdaptation(_:)`](/documentation/SwiftUI/View/presentationCompactAdaptation(_:))

Specifies how to adapt a presentation to compact size classes.

[`PresentationAdaptation`](/documentation/SwiftUI/PresentationAdaptation)

Strategies for adapting a presentation to a different size class.

[`presentationSizing(_:)`](/documentation/SwiftUI/View/presentationSizing(_:))

Sets the sizing of the containing presentation.

[`PresentationSizing`](/documentation/SwiftUI/PresentationSizing)

A type that defines the size of the presentation content and how the
presentation size adjusts to its content’s size changing.

[`PresentationSizingRoot`](/documentation/SwiftUI/PresentationSizingRoot)

A proxy to a view provided to the presentation with a
defined presentation size.

[`PresentationSizingContext`](/documentation/SwiftUI/PresentationSizingContext)

Contextual information about a presentation.

### Configuring a sheet’s height

[`presentationDetents(_:)`](/documentation/SwiftUI/View/presentationDetents(_:))

Sets the available detents for the enclosing sheet.

[`presentationDetents(_:selection:)`](/documentation/SwiftUI/View/presentationDetents(_:selection:))

Sets the available detents for the enclosing sheet, giving you
programmatic control of the currently selected detent.

[`presentationContentInteraction(_:)`](/documentation/SwiftUI/View/presentationContentInteraction(_:))

Configures the behavior of swipe gestures on a presentation.

[`presentationDragIndicator(_:)`](/documentation/SwiftUI/View/presentationDragIndicator(_:))

Sets the visibility of the drag indicator on top of a sheet.

[`PresentationDetent`](/documentation/SwiftUI/PresentationDetent)

A type that represents a height where a sheet naturally rests.

[`CustomPresentationDetent`](/documentation/SwiftUI/CustomPresentationDetent)

The definition of a custom detent with a calculated height.

[`PresentationContentInteraction`](/documentation/SwiftUI/PresentationContentInteraction)

A behavior that you can use to influence how a presentation responds to
swipe gestures.

### Styling a sheet and its background

[`presentationCornerRadius(_:)`](/documentation/SwiftUI/View/presentationCornerRadius(_:))

Requests that the presentation have a specific corner radius.

[`presentationBackground(_:)`](/documentation/SwiftUI/View/presentationBackground(_:))

Sets the presentation background of the enclosing sheet using a shape
style.

[`presentationBackground(alignment:content:)`](/documentation/SwiftUI/View/presentationBackground(alignment:content:))

Sets the presentation background of the enclosing sheet to a custom
view.

[`presentationBackgroundInteraction(_:)`](/documentation/SwiftUI/View/presentationBackgroundInteraction(_:))

Controls whether people can interact with the view behind a
presentation.

[`PresentationBackgroundInteraction`](/documentation/SwiftUI/PresentationBackgroundInteraction)

The kinds of interaction available to views behind a presentation.

### Presenting an alert

[`AlertScene`](/documentation/SwiftUI/AlertScene)

A scene that renders itself as a standalone alert dialog.

[`alert(_:isPresented:actions:)`](/documentation/SwiftUI/View/alert(_:isPresented:actions:))

Presents an alert when a given condition is true, using a text view for
the title.

[`alert(_:isPresented:presenting:actions:)`](/documentation/SwiftUI/View/alert(_:isPresented:presenting:actions:))

Presents an alert using the given data to produce the alert’s content
and a text view as a title.

[`alert(isPresented:error:actions:)`](/documentation/SwiftUI/View/alert(isPresented:error:actions:))

Presents an alert when an error is present.

[`alert(_:isPresented:actions:message:)`](/documentation/SwiftUI/View/alert(_:isPresented:actions:message:))

Presents an alert with a message when a given condition is true using
a text view as a title.

[`alert(_:isPresented:presenting:actions:message:)`](/documentation/SwiftUI/View/alert(_:isPresented:presenting:actions:message:))

Presents an alert with a message using the given data to produce the
alert’s content and a text view for a title.

[`alert(isPresented:error:actions:message:)`](/documentation/SwiftUI/View/alert(isPresented:error:actions:message:))

Presents an alert with a message when an error is present.

### Getting confirmation for an action

[`confirmationDialog(_:isPresented:titleVisibility:actions:)`](/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:actions:))

Presents a confirmation dialog when a given condition is true, using a
text view for the title.

[`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)`](/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:presenting:actions:))

Presents a confirmation dialog using data to produce the dialog’s
content and a text view for the title.

[`dismissalConfirmationDialog(_:shouldPresent:actions:)`](/documentation/SwiftUI/View/dismissalConfirmationDialog(_:shouldPresent:actions:))

Presents a confirmation dialog when a dismiss action has been triggered.

### Showing a confirmation dialog with a message

[`confirmationDialog(_:isPresented:titleVisibility:actions:message:)`](/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:actions:message:))

Presents a confirmation dialog with a message when a given condition is
true, using a text view for the title.

[`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`](/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:))

Presents a confirmation dialog with a message using data to produce the
dialog’s content and a text view for the message.

[`dismissalConfirmationDialog(_:shouldPresent:actions:message:)`](/documentation/SwiftUI/View/dismissalConfirmationDialog(_:shouldPresent:actions:message:))

Presents a confirmation dialog when a dismiss action has been triggered.

### Configuring a dialog

[`dialogIcon(_:)`](/documentation/SwiftUI/View/dialogIcon(_:))

Configures the icon used by dialogs within this view.

[`dialogIcon(_:)`](/documentation/SwiftUI/Scene/dialogIcon(_:))

Configures the icon used by alerts.

[`dialogSeverity(_:)`](/documentation/SwiftUI/View/dialogSeverity(_:))

[`dialogSeverity(_:)`](/documentation/SwiftUI/Scene/dialogSeverity(_:))

Sets the severity for alerts.

[`dialogSuppressionToggle(isSuppressed:)`](/documentation/SwiftUI/View/dialogSuppressionToggle(isSuppressed:))

Enables user suppression of dialogs and alerts presented within `self`,
with a default suppression message on macOS. Unused on other platforms.

[`dialogSuppressionToggle(isSuppressed:)`](/documentation/SwiftUI/Scene/dialogSuppressionToggle(isSuppressed:))

Enables user suppression of an alert with a custom suppression
message.

[`dialogSuppressionToggle(_:isSuppressed:)`](/documentation/SwiftUI/View/dialogSuppressionToggle(_:isSuppressed:))

Enables user suppression of dialogs and alerts presented within `self`,
with a custom suppression message on macOS. Unused on other platforms.

[`dialogSuppressionToggle(_:isSuppressed:)`](/documentation/SwiftUI/Scene/dialogSuppressionToggle(_:isSuppressed:))

Enables user suppression of an alert with a custom suppression
message.

### Exporting to file

[`fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)`](/documentation/SwiftUI/View/fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:))

Presents a system interface for exporting a document that’s stored in
a value type, like a structure, to a file on disk.

[`fileExporter(isPresented:documents:contentType:onCompletion:)`](/documentation/SwiftUI/View/fileExporter(isPresented:documents:contentType:onCompletion:))

Presents a system interface for exporting a collection of value type
documents to files on disk.

[`fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:))

Presents a system interface for allowing the user to export a
`FileDocument` to a file on disk.

[`fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:))

Presents a system dialog for allowing the user to export a
collection of documents that conform to `FileDocument`
to files on disk.

[`fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:))

Presents a system interface allowing the user to export
a `Transferable` item to file on disk.

[`fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:))

Presents a system interface allowing the user to export
a collection of items to files on disk.

[`fileExporterFilenameLabel(_:)`](/documentation/SwiftUI/View/fileExporterFilenameLabel(_:))

On macOS, configures the `fileExporter`
with a label for the file name field.

### Importing from file

[`fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)`](/documentation/SwiftUI/View/fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:))

Presents a system interface for allowing the user to import multiple
files.

[`fileImporter(isPresented:allowedContentTypes:onCompletion:)`](/documentation/SwiftUI/View/fileImporter(isPresented:allowedContentTypes:onCompletion:))

Presents a system interface for allowing the user to import an existing
file.

[`fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:))

Presents a system dialog for allowing the user to import multiple
files.

### Moving a file

[`fileMover(isPresented:file:onCompletion:)`](/documentation/SwiftUI/View/fileMover(isPresented:file:onCompletion:))

Presents a system interface for allowing the user to move an existing
file to a new location.

[`fileMover(isPresented:files:onCompletion:)`](/documentation/SwiftUI/View/fileMover(isPresented:files:onCompletion:))

Presents a system interface for allowing the user to move a collection
of existing files to a new location.

[`fileMover(isPresented:file:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileMover(isPresented:file:onCompletion:onCancellation:))

Presents a system dialog for allowing the user to move
an existing file to a new location.

[`fileMover(isPresented:files:onCompletion:onCancellation:)`](/documentation/SwiftUI/View/fileMover(isPresented:files:onCompletion:onCancellation:))

Presents a system dialog for allowing the user to move
a collection of existing files to a new location.

### Configuring a file dialog

[`fileDialogBrowserOptions(_:)`](/documentation/SwiftUI/View/fileDialogBrowserOptions(_:))

On macOS, configures the `fileExporter`, `fileImporter`,
or `fileMover` to provide a refined URL search experience: include or exclude
hidden files, allow searching by tag, etc.

[`fileDialogConfirmationLabel(_:)`](/documentation/SwiftUI/View/fileDialogConfirmationLabel(_:))

On macOS, configures the `fileExporter`, `fileImporter`,
or `fileMover` with a custom confirmation button label.

[`fileDialogCustomizationID(_:)`](/documentation/SwiftUI/View/fileDialogCustomizationID(_:))

On macOS, configures the `fileExporter`, `fileImporter`,
or `fileMover` to persist and restore the file dialog configuration.

[`fileDialogDefaultDirectory(_:)`](/documentation/SwiftUI/View/fileDialogDefaultDirectory(_:))

Configures the `fileExporter`, `fileImporter`, or `fileMover` to
open with the specified default directory.

[`fileDialogImportsUnresolvedAliases(_:)`](/documentation/SwiftUI/View/fileDialogImportsUnresolvedAliases(_:))

On macOS, configures the `fileExporter`, `fileImporter`,
or `fileMover` behavior when a user chooses an alias.

[`fileDialogMessage(_:)`](/documentation/SwiftUI/View/fileDialogMessage(_:))

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover`
with a custom text that is presented to the user,
similar to a title.

[`fileDialogURLEnabled(_:)`](/documentation/SwiftUI/View/fileDialogURLEnabled(_:))

On macOS, configures the `fileImporter`
or `fileMover` to conditionally disable presented URLs.

[`FileDialogBrowserOptions`](/documentation/SwiftUI/FileDialogBrowserOptions)

The way that file dialogs present the file system.

### Presenting an inspector

[`inspector(isPresented:content:)`](/documentation/SwiftUI/View/inspector(isPresented:content:))

Inserts an inspector at the applied position in the view hierarchy.

[`inspectorColumnWidth(_:)`](/documentation/SwiftUI/View/inspectorColumnWidth(_:))

Sets a fixed, preferred width for the inspector containing this view
when presented as a trailing column.

[`inspectorColumnWidth(min:ideal:max:)`](/documentation/SwiftUI/View/inspectorColumnWidth(min:ideal:max:))

Sets a flexible, preferred width for the inspector in a trailing-column
presentation.

### Dismissing a presentation

[`isPresented`](/documentation/SwiftUI/EnvironmentValues/isPresented)

A Boolean value that indicates whether the view associated with this
environment is currently presented.

[`dismiss`](/documentation/SwiftUI/EnvironmentValues/dismiss)

An action that dismisses the current presentation.

[`DismissAction`](/documentation/SwiftUI/DismissAction)

An action that dismisses a presentation.

[`interactiveDismissDisabled(_:)`](/documentation/SwiftUI/View/interactiveDismissDisabled(_:))

Conditionally prevents interactive dismissal of presentations like
popovers, sheets, and inspectors.

### Deprecated modal presentations

[`Alert`](/documentation/SwiftUI/Alert)

A representation of an alert presentation.

[`ActionSheet`](/documentation/SwiftUI/ActionSheet)

A representation of an action sheet presentation.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
