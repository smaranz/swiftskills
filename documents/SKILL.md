---
name: Documents
description: Rork-Max Quality skill for Documents. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Documents


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Documents

Enable people to open and manage documents.

## Overview

Create a user interface for opening and editing documents using the
[`DocumentGroup`](/documentation/SwiftUI/DocumentGroup) scene type.

![](images/com.apple.SwiftUI/documents-hero@2x.png)

You initialize the scene with a model that
describes the organization of the document’s data, and a view hierarchy that
SwiftUI uses to display the document’s contents to the user. You can use either
a value type model, which you typically store as a structure, that conforms to
the [`FileDocument`](/documentation/SwiftUI/FileDocument) protocol, or a reference type model you store in a class
instance that conforms to the [`ReferenceFileDocument`](/documentation/SwiftUI/ReferenceFileDocument) protocol. You can also
use SwiftData-backed documents using an initializer like [`init(editing:contentType:editor:prepareDocument:)`](/documentation/SwiftUI/DocumentGroup/init(editing:contentType:editor:prepareDocument:)).

SwiftUI supports standard behaviors that users expect from a document-based
app, appropriate for each platform, like multiwindow support, open and save
panels, drag and drop, and so on. For related design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/patterns>
in the Human Interface Guidelines.

## Topics

### Creating a document

[Building a document-based app with SwiftUI](/documentation/SwiftUI/Building-a-document-based-app-with-SwiftUI)

Create, save, and open documents in a multiplatform app.

[Building a document-based app using SwiftData](/documentation/SwiftUI/Building-a-document-based-app-using-SwiftData)

Code along with the WWDC presenter to transform an app with SwiftData.

[`DocumentGroup`](/documentation/SwiftUI/DocumentGroup)

A scene that enables support for opening, creating, and saving documents.

### Storing document data in a structure instance

[`FileDocument`](/documentation/SwiftUI/FileDocument)

A type that you use to serialize documents to and from file.

[`FileDocumentConfiguration`](/documentation/SwiftUI/FileDocumentConfiguration)

The properties of an open file document.

### Storing document data in a class instance

[`ReferenceFileDocument`](/documentation/SwiftUI/ReferenceFileDocument)

A type that you use to serialize reference type documents to and from file.

[`ReferenceFileDocumentConfiguration`](/documentation/SwiftUI/ReferenceFileDocumentConfiguration)

The properties of an open reference file document.

[`undoManager`](/documentation/SwiftUI/EnvironmentValues/undoManager)

The undo manager used to register a view’s undo operations.

### Accessing document configuration

[`documentConfiguration`](/documentation/SwiftUI/EnvironmentValues/documentConfiguration)

The configuration of a document in a [`DocumentGroup`](/documentation/SwiftUI/DocumentGroup).

[`DocumentConfiguration`](/documentation/SwiftUI/DocumentConfiguration)

### Reading and writing documents

[`FileDocumentReadConfiguration`](/documentation/SwiftUI/FileDocumentReadConfiguration)

The configuration for reading file contents.

[`FileDocumentWriteConfiguration`](/documentation/SwiftUI/FileDocumentWriteConfiguration)

The configuration for serializing file contents.

### Opening a document programmatically

[`newDocument`](/documentation/SwiftUI/EnvironmentValues/newDocument)

An action in the environment that presents a new document.

[`NewDocumentAction`](/documentation/SwiftUI/NewDocumentAction)

An action that presents a new document.

[`openDocument`](/documentation/SwiftUI/EnvironmentValues/openDocument)

An action in the environment that presents an existing document.

[`OpenDocumentAction`](/documentation/SwiftUI/OpenDocumentAction)

An action that presents an existing document.

### Configuring the document launch experience

[`DocumentGroupLaunchScene`](/documentation/SwiftUI/DocumentGroupLaunchScene)

A launch scene for document-based applications.

[`DocumentLaunchView`](/documentation/SwiftUI/DocumentLaunchView)

A view to present when launching document-related user experience.

[`DocumentLaunchGeometryProxy`](/documentation/SwiftUI/DocumentLaunchGeometryProxy)

A proxy for access to the frame of the scene and its title view.

[`DefaultDocumentGroupLaunchActions`](/documentation/SwiftUI/DefaultDocumentGroupLaunchActions)

The default actions for the document group launch scene and the document launch view.

[`NewDocumentButton`](/documentation/SwiftUI/NewDocumentButton)

A button that creates and opens new documents.

[`DocumentBaseBox`](/documentation/SwiftUI/DocumentBaseBox)

A Box that allows setting its Document base
not requiring the caller to know the exact types of the box and its base.

### Renaming a document

[`RenameButton`](/documentation/SwiftUI/RenameButton)

A button that triggers a standard rename action.

[`renameAction(_:)`](/documentation/SwiftUI/View/renameAction(_:))

Sets a closure to run for the rename action.

[`rename`](/documentation/SwiftUI/EnvironmentValues/rename)

An action that activates the standard rename interaction.

[`RenameAction`](/documentation/SwiftUI/RenameAction)

An action that activates a standard rename interaction.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
