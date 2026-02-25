---
name: Documents
description: Rork-Max Quality skill for Documents. Actionable patterns and best practices for SwiftUI development.
---

# Documents

Enable people to open and manage documents.
Create a user interface for opening and editing documents using the
`DocumentGroup` scene type.
You initialize the scene with a model that
describes the organization of the document’s data, and a view hierarchy that
SwiftUI uses to display the document’s contents to the user. You can use either
a value type model, which you typically store as a structure, that conforms to
the `FileDocument` protocol, or a reference type model you store in a class
instance that conforms to the `ReferenceFileDocument` protocol. You can also
use SwiftData-backed documents using an initializer like `init(editing:contentType:editor:prepareDocument:)`.
SwiftUI supports standard behaviors that users expect from a document-based
app, appropriate for each platform, like multiwindow support, open and save
panels, drag and drop, and so on. For related design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import UniformTypeIdentifiers

struct TextDocument: FileDocument {
    static var readableContentTypes: [UTType] { [.plainText] }
    var text: String

    init(text: String = "") { self.text = text }

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents else {
            throw CocoaError(.fileReadCorruptFile)
        }
        text = String(data: data, encoding: .utf8) ?? ""
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        FileWrapper(regularFileWithContents: text.data(using: .utf8)!)
    }
}

@main
struct EditorApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditor(text: file.$document.text)
                .padding()
        }
    }
}
```

## 💎 Elite Implementation Tips

- Conform to `FileDocument` for value-type documents, `ReferenceFileDocument` for class-based
- Use `DocumentGroup` to get automatic open/save/rename for free
- Declare `readableContentTypes` with `UTType` for proper file association


## When to Use

- Defining the entry point and top-level structure of a SwiftUI app
- Managing multiple windows, scenes, or document-based workflows
- Configuring app-wide lifecycle events and state restoration
- Building multi-platform apps that adapt their structure per platform

## Best Practices

- Keep `@main` App structs thin — delegate complex logic to dedicated model objects
- Use `@Environment(\.scenePhase)` to react to foreground/background transitions
- Prefer `WindowGroup` for document-based apps and `Window` for utility panels
- Store app-level state in an `@Observable` singleton injected via `.environment()`

## Common Pitfalls

- Putting heavy initialization in the App `init()` delays launch
- Forgetting that each `WindowGroup` can spawn multiple instances on macOS/iPadOS
- Using `@StateObject` in the App struct when `@State` with `@Observable` is simpler in Swift 6

## Key APIs

### Creating a document

| API | Purpose |
|-----|---------|
| `Building a document-based app with SwiftUI` | Create, save, and open documents in a multiplatform app. |
| `Building a document-based app using SwiftData` | Code along with the WWDC presenter to transform an app with SwiftData. |
| `DocumentGroup` | A scene that enables support for opening, creating, and saving documents. |

### Storing document data in a structure instance

| API | Purpose |
|-----|---------|
| `FileDocument` | A type that you use to serialize documents to and from file. |
| `FileDocumentConfiguration` | The properties of an open file document. |

### Storing document data in a class instance

| API | Purpose |
|-----|---------|
| `ReferenceFileDocument` | A type that you use to serialize reference type documents to and from file. |
| `ReferenceFileDocumentConfiguration` | The properties of an open reference file document. |
| `undoManager` | The undo manager used to register a view’s undo operations. |

### Accessing document configuration

| API | Purpose |
|-----|---------|
| `documentConfiguration` | The configuration of a document in a [`DocumentGroup`](/documentation/SwiftUI/DocumentGroup). |

### Reading and writing documents

| API | Purpose |
|-----|---------|
| `FileDocumentReadConfiguration` | The configuration for reading file contents. |
| `FileDocumentWriteConfiguration` | The configuration for serializing file contents. |

### Opening a document programmatically

| API | Purpose |
|-----|---------|
| `newDocument` | An action in the environment that presents a new document. |
| `NewDocumentAction` | An action that presents a new document. |
| `openDocument` | An action in the environment that presents an existing document. |
| `OpenDocumentAction` | An action that presents an existing document. |

### Configuring the document launch experience

| API | Purpose |
|-----|---------|
| `DocumentGroupLaunchScene` | A launch scene for document-based applications. |
| `DocumentLaunchView` | A view to present when launching document-related user experience. |
| `DocumentLaunchGeometryProxy` | A proxy for access to the frame of the scene and its title view. |
| `DefaultDocumentGroupLaunchActions` | The default actions for the document group launch scene and the document launch view. |
| `NewDocumentButton` | A button that creates and opens new documents. |
| `DocumentBaseBox` | A Box that allows setting its Document base |

### Renaming a document

| API | Purpose |
|-----|---------|
| `RenameButton` | A button that triggers a standard rename action. |
| `renameAction(_:)` | Sets a closure to run for the rename action. |
| `rename` | An action that activates the standard rename interaction. |
| `RenameAction` | An action that activates a standard rename interaction. |
