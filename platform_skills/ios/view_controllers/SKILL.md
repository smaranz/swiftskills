---
name: IOS View controllers
description: Rork-Max Quality skill for IOS View controllers. Platform-native patterns and best practices for ios development.
---

# IOS View controllers

Manage your interface using view controllers and facilitate navigation around your app’s content.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class RorkViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "View controllers"
        label.font = .preferredFont(forTextStyle: .largeTitle)
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }
}
```

## 💎 Elite Implementation Tips

- Follow the IOS Human Interface Guidelines for native feel.
- Use system-standard UIKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building native iOS/iPadOS features using UIKit APIs
- Implementing UIKit-specific interactions not available in SwiftUI
- Working with view controllers, navigation controllers, and UIKit lifecycle

## Best Practices

- Use SwiftUI for new views and bridge UIKit only when necessary
- Adopt modern UIKit APIs: `UICollectionViewCompositionalLayout`, diffable data sources
- Handle all size classes and trait changes for iPhone and iPad adaptivity

## Common Pitfalls

- Mixing UIKit autolayout and SwiftUI layout can cause constraint conflicts
- Forgetting to test on iPad — multitasking changes your window size
- Not adopting the UIKit scene lifecycle for multi-window support

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Managing content in your app’s windows` | Build your app’s user interface from view controllers, and change the currently visible view controller when you want to display new content. |
| `UIKit Catalog: Creating and customizing views and controls` | Customize your app’s user interface with views and controls. |

### Content view controllers

| API | Purpose |
|-----|---------|
| `Displaying and managing views with a view controller` | Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data. |
| `Showing and hiding view controllers` | Display view controllers using different techniques, and pass data between them during transitions. |
| `UIViewController` | An object that manages a view hierarchy for your UIKit app. |
| `UITableViewController` | A view controller that specializes in managing a table view. |
| `UICollectionViewController` | A view controller that specializes in managing a collection view. |
| `UIContentContainer` | A set of methods for adapting the contents of your view controllers to size and trait changes. |

### Container view controllers

| API | Purpose |
|-----|---------|
| `Creating a custom container view controller` | Create a composite interface by combining content from one or more view controllers with other custom views. |
| `UISplitViewController` | A container view controller that implements a hierarchical interface. |
| `UINavigationController` | A container view controller that defines a stack-based scheme for navigating hierarchical content. |
| `UINavigationBar` | Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller. |
| `UINavigationItem` | The items that a navigation bar displays when the associated view controller is visible. |
| `UITabBarController` | A container view controller that manages a multiselection interface, where the selection determines which child view controller to display. |
| `UITabBar` | A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app. |
| `UITabBarItem` | An object that describes an item in a tab bar. |

### Presentation management

| API | Purpose |
|-----|---------|
| `Disabling the pull-down gesture for a sheet` | Ensure a positive user experience when presenting a view controller as a sheet. |
| `UIPresentationController` | An object that manages the transition animations and the presentation of view controllers onscreen. |
| `UISheetPresentationController` | A presentation controller that manages the appearance and behavior of a sheet. |

### Search interface

| API | Purpose |
|-----|---------|
| `UISearchContainerViewController` | A view controller that manages the presentation of search results in your interface. |
| `UISearchController` | A view controller that manages the display of search results based on interactions with a search bar. |
| `UISearchBar` | A specialized view for receiving search-related information from the user. |
| `UISearchResultsUpdating` | A set of methods that let you update search results based on information the user enters into the search bar. |
| `Displaying searchable content by using a search controller` | Create a user interface with searchable content in a table view. |
| `Using suggested searches with a search controller` | Create a search interface with a table view of suggested searches. |

### Images and video

| API | Purpose |
|-----|---------|
| `UIImagePickerController` | A view controller that manages the system interfaces for taking pictures, recording movies, and choosing items from the user’s media library. |
| `UIVideoEditorController` | A view controller that manages the system interface for trimming video frames and encoding a previously recorded movie. |

### Documents and directories

| API | Purpose |
|-----|---------|
| `Customizing a document-based app’s launch experience` | Add unique elements to your app’s document launch scene. |
| `Adding a document browser to your app` | Give people access to their local or remote documents from within your app. |
| `Providing access to directories` | Use a document picker to access the content of a directory outside your app’s container. |
| `Building an app with a document browser` | Provide access to on-device and cloud files by adding a document browser to your app. |
| `Building a document browser app for custom file formats` | Implement a custom document file format to manage user interactions with files on different cloud storage providers. |
| `UIDocumentViewController` | A view controller that manages and presents a document stored locally or in the cloud. |
| `UIDocumentBrowserViewController` | A view controller for browsing and performing actions on documents that you store locally and in the cloud. |
| `UIDocumentPickerViewController` | A view controller that provides access to documents or destinations outside your app’s sandbox. |

### iCloud Sharing

| API | Purpose |
|-----|---------|
| `UICloudSharingController` | A view controller that presents standard screens for adding and removing people from a CloudKit share record. |

### Activities interface

| API | Purpose |
|-----|---------|
| `Collaborating and sharing copies of your data` | Share data and collaborate with people from your app. |
| `UIActivityViewController` | A view controller that you use to offer standard services from your app. |
| `UIActivityItemProvider` | A proxy for data that passes to an activity view controller. |
| `UIActivityItemSource` | A set of methods that an activity view controller uses to retrieve the data items to act on. |
| `UIActivity` | An abstract class that you subclass to implement app-specific services. |
| `UIActivityItemsConfigurationProviding` | An interface that provides a source for shareable content to fulfill user requests to share current content. |

### Font picker

| API | Purpose |
|-----|---------|
| `UIFontPickerViewController` | A view controller that manages the interface for selecting a font that the system provides or the user installs. |
| `UIFontPickerViewControllerDelegate` | A set of optional methods for receiving messages about the user’s interaction with the font picker. |
| `UIFontPickerViewController.Configuration` | The filters and display settings a font picker view controller uses to set up a font picker. |

### Color picker

| API | Purpose |
|-----|---------|
| `UIColorPickerViewController` | A view controller that manages the interface for selecting a color. |
| `UIColorPickerViewControllerDelegate` | The delegate protocol to inform about changes in color selection. |

### Word lookup

| API | Purpose |
|-----|---------|
| `UIReferenceLibraryViewController` | A view controller that displays a standard interface for looking up the definition of a word or term. |

### Text formatting

| API | Purpose |
|-----|---------|
| `UITextFormattingViewController` | A view controller that manages the interface for common text formatting options. |

### Printer picker

| API | Purpose |
|-----|---------|
| `UIPrinterPickerController` | A view controller that displays the standard interface for selecting a printer. |

### Interface orientation

| API | Purpose |
|-----|---------|
| `isPortrait` | A Boolean value that indicates whether the user interface is currently presented in a portrait orientation. |
| `isLandscape` | A Boolean value that indicates whether the user interface is currently presented in a landscape orientation. |

### Interface restoration

| API | Purpose |
|-----|---------|
| `Restoring your app’s state` | Provide continuity for the user by preserving current activities. |
| `Preserving your app’s UI across launches` | Return your app to its previous state after the system terminates it. |
| `UIViewControllerRestoration` | The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration. |
| `UIObjectRestoration` | The interface that restoration classes use to restore preserved objects. |
| `UIStateRestoring` | Methods for adding objects to your state restoration archives. |
