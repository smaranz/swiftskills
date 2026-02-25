---
name: IOS Menus and shortcuts
description: Rork-Max Quality skill for IOS Menus and shortcuts. Platform-native patterns and best practices for ios development.
---

# IOS Menus and shortcuts

Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class RorkViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "Menus and shortcuts"
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

### Menu elements and keyboard shortcuts

| API | Purpose |
|-----|---------|
| `Adding menus and shortcuts to the menu bar and user interface` | Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst. |
| `Adopting menus and UIActions in your user interface` | Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences. |
| `UIMenuElement` | An object representing a menu, action, or command. |
| `UIAction` | A menu element that performs its action in a closure. |
| `UICommand` | A menu element that performs its action in a selector. |
| `UIKeyCommand` | An object that specifies a key press perform on a hardware keyboard and the resulting action. |
| `UIDeferredMenuElement` | A placeholder menu element that the system replaces with the result of the block’s completion handler. |
| `UIDeferredMenuElement.Provider` | — |

### Edit menus

| API | Purpose |
|-----|---------|
| `UIEditMenuInteraction` | An interaction that provides edit operations using a menu. |
| `UIEditMenuInteractionDelegate` | The methods for customizing the menu the interaction displays. |
| `UIEditMenuConfiguration` | An object containing the configuration details for the menu your app presents in response to an edit menu interaction. |
| `UIResponderStandardEditActions` | A set of standard methods that apps can adopt to support editing. |

### App menus

| API | Purpose |
|-----|---------|
| `UIMenu` | A container for grouping related menu elements in an app menu or contextual menu. |
| `UIMenuBuilder` | An interface for adding and removing menus from a menu system. |
| `UIMenuSystem` | An object representing a main or contextual menu system. |
| `UIMainMenuSystem` | The main menu system. |

### Contextual menus

| API | Purpose |
|-----|---------|
| `UIContextMenuSystem` | The context menu system. |
| `UIContextMenuInteraction` | An interaction object that you use to display relevant actions for your content. |
| `UIContextMenuInteractionDelegate` | The methods for providing the set of actions to perform on your content, and for customizing the preview of that content. |
| `UITargetedPreview` | An object describing the view to use during preview-related animations. |
| `UIPreviewTarget` | An object that specifies the container view to use for animations. |
| `UIPreviewParameters` | Additional parameters to use when animating a preview interface. |

### Find and replace

| API | Purpose |
|-----|---------|
| `UIFindInteraction` | An interaction that provides text finding and replacing operations using a system find panel. |
| `UIFindInteractionDelegate` | A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes. |
| `UIFindSession` | An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates. |
| `UITextSearchingFindSession` | A find session object that wraps a searchable object implementing the text-searching protocol. |
| `UITextSearching` | The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results. |
| `UITextSearching` | The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results. |
| `UITextSearchOptions` | An object containing the configurable options for a text search. |
| `UITextSearchFoundTextStyle` | Constants that describe the style a find session uses to decorate the text. |

### Home Screen quick actions

| API | Purpose |
|-----|---------|
| `Add Home Screen quick actions` | Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions. |
| `UIApplicationShortcutItem` | An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app. |
| `UIApplicationShortcutIcon` | An image you can optionally associate with a Home Screen quick action to improve its appearance and usability. |
| `UIMutableApplicationShortcutItem` | A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app. |
