---
name: IOS View controllers
description: Apple UIKit Documentation for IOS View controllers on ios.
---

# View controllers

Manage your interface using view controllers and facilitate navigation around your app’s content.

## Discussion

You use view controllers to manage your UIKit app’s interface. A view controller manages a single root view, which may itself contain any number of subviews. User interactions with that view hierarchy are handled by your view controller, which coordinates with other objects of your app as needed. Every app has at least one view controller whose content fills the main window. If your app has more content than can fit on-screen at once, use multiple view controllers to manage different parts of that content.

A *container view controller* embeds the content of other view controllers into its own root view. A container view controller may mix custom views with the contents of its contained view controllers to facilitate navigation or to create unique interfaces. For example, a [`UINavigationController`](/documentation/UIKit/UINavigationController) object manages a navigation bar and a stack of view controllers (only one of which is visible at a time), and provides an API to add and remove view controllers from the stack.

UIKit provides several standard view controllers for navigation and managing specific types of content. You define the view controllers containing your app’s custom content. You may also define custom container view controllers to implement new navigation schemes.

## Topics

### Essentials

[Managing content in your app’s windows](/documentation/UIKit/managing-content-in-your-app-s-windows)

Build your app’s user interface from view controllers, and change the currently visible view controller when you want to display new content.

[UIKit Catalog: Creating and customizing views and controls](/documentation/UIKit/uikit-catalog-creating-and-customizing-views-and-controls)

Customize your app’s user interface with views and controls.

### Content view controllers

[Displaying and managing views with a view controller](/documentation/UIKit/displaying-and-managing-views-with-a-view-controller)

Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.

[Showing and hiding view controllers](/documentation/UIKit/showing-and-hiding-view-controllers)

Display view controllers using different techniques, and pass data between them during transitions.

[`UIViewController`](/documentation/UIKit/UIViewController)

An object that manages a view hierarchy for your UIKit app.

[`UITableViewController`](/documentation/UIKit/UITableViewController)

A view controller that specializes in managing a table view.

[`UICollectionViewController`](/documentation/UIKit/UICollectionViewController)

A view controller that specializes in managing a collection view.

[`UIContentContainer`](/documentation/UIKit/UIContentContainer)

A set of methods for adapting the contents of your view controllers to size and trait changes.

### Container view controllers

[Creating a custom container view controller](/documentation/UIKit/creating-a-custom-container-view-controller)

Create a composite interface by combining content from one or more view controllers with other custom views.

[`UISplitViewController`](/documentation/UIKit/UISplitViewController)

A container view controller that implements a hierarchical interface.

[`UINavigationController`](/documentation/UIKit/UINavigationController)

A container view controller that defines a stack-based scheme for navigating hierarchical content.

[`UINavigationBar`](/documentation/UIKit/UINavigationBar)

Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.

[`UINavigationItem`](/documentation/UIKit/UINavigationItem)

The items that a navigation bar displays when the associated view controller is visible.

[`UITabBarController`](/documentation/UIKit/UITabBarController)

A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.

[`UITabBar`](/documentation/UIKit/UITabBar)

A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.

[`UITabBarItem`](/documentation/UIKit/UITabBarItem)

An object that describes an item in a tab bar.

[`UITab`](/documentation/UIKit/UITab)

An object that manages a tab in a tab bar.

[`UITabAccessory`](/documentation/UIKit/UITabAccessory)

[`UISearchTab`](/documentation/UIKit/UISearchTab)

A tab subclass that represents the system’s search tab.

[`UITabGroup`](/documentation/UIKit/UITabGroup)

An object that manages a collection of tab objects.

[`UIPageViewController`](/documentation/UIKit/UIPageViewController)

A container view controller that manages navigation between pages of content, where a subview controller manages each page.

### Presentation management

[Disabling the pull-down gesture for a sheet](/documentation/UIKit/disabling-the-pull-down-gesture-for-a-sheet)

Ensure a positive user experience when presenting a view controller as a sheet.

[`UIPresentationController`](/documentation/UIKit/UIPresentationController)

An object that manages the transition animations and the presentation of view controllers onscreen.

[`UISheetPresentationController`](/documentation/UIKit/UISheetPresentationController)

A presentation controller that manages the appearance and behavior of a sheet.

### Search interface

[`UISearchContainerViewController`](/documentation/UIKit/UISearchContainerViewController)

A view controller that manages the presentation of search results in your interface.

[`UISearchController`](/documentation/UIKit/UISearchController)

A view controller that manages the display of search results based on interactions with a search bar.

[`UISearchBar`](/documentation/UIKit/UISearchBar)

A specialized view for receiving search-related information from the user.

[`UISearchResultsUpdating`](/documentation/UIKit/UISearchResultsUpdating)

A set of methods that let you update search results based on information the user enters into the search bar.

[Displaying searchable content by using a search controller](/documentation/UIKit/displaying-searchable-content-by-using-a-search-controller)

Create a user interface with searchable content in a table view.

[Using suggested searches with a search controller](/documentation/UIKit/using-suggested-searches-with-a-search-controller)

Create a search interface with a table view of suggested searches.

### Images and video

[`UIImagePickerController`](/documentation/UIKit/UIImagePickerController)

A view controller that manages the system interfaces for taking pictures, recording movies, and choosing items from the user’s media library.

[`UIVideoEditorController`](/documentation/UIKit/UIVideoEditorController)

A view controller that manages the system interface for trimming video frames and encoding a previously recorded movie.

### Documents and directories

[Customizing a document-based app’s launch experience](/documentation/UIKit/customizing-a-document-based-app-s-launch-experience)

Add unique elements to your app’s document launch scene.

[Adding a document browser to your app](/documentation/UIKit/adding-a-document-browser-to-your-app)

Give people access to their local or remote documents from within your app.

[Providing access to directories](/documentation/UIKit/providing-access-to-directories)

Use a document picker to access the content of a directory outside your app’s container.

[Building an app with a document browser](/documentation/UIKit/building-an-app-with-a-document-browser)

Provide access to on-device and cloud files by adding a document browser to your app.

[Building a document browser app for custom file formats](/documentation/UIKit/building-a-document-browser-app-for-custom-file-formats)

Implement a custom document file format to manage user interactions with files on different cloud storage providers.

[`UIDocumentViewController`](/documentation/UIKit/UIDocumentViewController)

A view controller that manages and presents a document stored locally or in the cloud.

[`UIDocumentBrowserViewController`](/documentation/UIKit/UIDocumentBrowserViewController)

A view controller for browsing and performing actions on documents that you store locally and in the cloud.

[`UIDocumentPickerViewController`](/documentation/UIKit/UIDocumentPickerViewController)

A view controller that provides access to documents or destinations outside your app’s sandbox.

[`UIDocumentInteractionController`](/documentation/UIKit/UIDocumentInteractionController)

A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.

### iCloud Sharing

[`UICloudSharingController`](/documentation/UIKit/UICloudSharingController)

A view controller that presents standard screens for adding and removing people from a CloudKit share record.

### Activities interface

[Collaborating and sharing copies of your data](/documentation/UIKit/collaborating-and-sharing-copies-of-your-data)

Share data and collaborate with people from your app.

[`UIActivityViewController`](/documentation/UIKit/UIActivityViewController)

A view controller that you use to offer standard services from your app.

[`UIActivityItemProvider`](/documentation/UIKit/UIActivityItemProvider)

A proxy for data that passes to an activity view controller.

[`UIActivityItemSource`](/documentation/UIKit/UIActivityItemSource)

A set of methods that an activity view controller uses to retrieve the data items to act on.

[`UIActivity`](/documentation/UIKit/UIActivity)

An abstract class that you subclass to implement app-specific services.

[`UIActivityItemsConfigurationProviding`](/documentation/UIKit/UIActivityItemsConfigurationProviding)

An interface that provides a source for shareable content to fulfill user requests to share current content.

### Font picker

[`UIFontPickerViewController`](/documentation/UIKit/UIFontPickerViewController)

A view controller that manages the interface for selecting a font that the system provides or the user installs.

[`UIFontPickerViewControllerDelegate`](/documentation/UIKit/UIFontPickerViewControllerDelegate)

A set of optional methods for receiving messages about the user’s interaction with the font picker.

[`UIFontPickerViewController.Configuration`](/documentation/UIKit/UIFontPickerViewController/Configuration-swift.class)

The filters and display settings a font picker view controller uses to set up a font picker.

### Color picker

[`UIColorPickerViewController`](/documentation/UIKit/UIColorPickerViewController)

A view controller that manages the interface for selecting a color.

[`UIColorPickerViewControllerDelegate`](/documentation/UIKit/UIColorPickerViewControllerDelegate)

The delegate protocol to inform about changes in color selection.

### Word lookup

[`UIReferenceLibraryViewController`](/documentation/UIKit/UIReferenceLibraryViewController)

A view controller that displays a standard interface for looking up the definition of a word or term.

### Text formatting

[`UITextFormattingViewController`](/documentation/UIKit/UITextFormattingViewController)

A view controller that manages the interface for common text formatting options.

### Printer picker

[`UIPrinterPickerController`](/documentation/UIKit/UIPrinterPickerController)

A view controller that displays the standard interface for selecting a printer.

### Interface orientation

[`isPortrait`](/documentation/UIKit/UIInterfaceOrientation/isPortrait)

A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.

[`isLandscape`](/documentation/UIKit/UIInterfaceOrientation/isLandscape)

A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.

### Interface restoration

[Restoring your app’s state](/documentation/UIKit/restoring-your-app-s-state)

Provide continuity for the user by preserving current activities.

  <doc://com.apple.documentation/documentation/SwiftUI/restoring-your-app-s-state-with-swiftui>

[Preserving your app’s UI across launches](/documentation/UIKit/preserving-your-app-s-ui-across-launches)

Return your app to its previous state after the system terminates it.

[`UIViewControllerRestoration`](/documentation/UIKit/UIViewControllerRestoration)

The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.

[`UIObjectRestoration`](/documentation/UIKit/UIObjectRestoration)

The interface that restoration classes use to restore preserved objects.

[`UIStateRestoring`](/documentation/UIKit/UIStateRestoring)

Methods for adding objects to your state restoration archives.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
