---
name: IOS Menus and shortcuts
description: Rork-Max Quality skill for IOS Menus and shortcuts on ios. Based on official Apple UIKit Documentation.
---

# IOS Menus and shortcuts

## 🚀 Rork-Max Quality Snippet

```swift
// Premium IOS Menus and shortcuts Implementation for ios
// Focus on platform-native excellence

import SwiftUI
#if os(ios)
// UIKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality IOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the ios native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for ios: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Menus and shortcuts

Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.

## Topics

### Menu elements and keyboard shortcuts

[Adding menus and shortcuts to the menu bar and user interface](/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface)

Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.

[Adopting menus and UIActions in your user interface](/documentation/UIKit/adopting-menus-and-uiactions-in-your-user-interface)

Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.

[`UIMenuElement`](/documentation/UIKit/UIMenuElement)

An object representing a menu, action, or command.

[`UIAction`](/documentation/UIKit/UIAction)

A menu element that performs its action in a closure.

[`UICommand`](/documentation/UIKit/UICommand)

A menu element that performs its action in a selector.

[`UIKeyCommand`](/documentation/UIKit/UIKeyCommand)

An object that specifies a key press perform on a hardware keyboard and the resulting action.

[`UIDeferredMenuElement`](/documentation/UIKit/UIDeferredMenuElement)

A placeholder menu element that the system replaces with the result of the block’s completion handler.

[`UIDeferredMenuElement.Provider`](/documentation/UIKit/UIDeferredMenuElement/Provider)

[`UIMenuElement.Attributes`](/documentation/UIKit/UIMenuElement/Attributes)

Attributes that determine the style of the menu element.

[`UIMenuElement.State`](/documentation/UIKit/UIMenuElement/State)

Constants that indicate the state of an action- or command-based menu element.

[`UIMenuLeaf`](/documentation/UIKit/UIMenuLeaf)

An interface for an object that represents a menu element without child elements.

### Edit menus

[`UIEditMenuInteraction`](/documentation/UIKit/UIEditMenuInteraction)

An interaction that provides edit operations using a menu.

[`UIEditMenuInteractionDelegate`](/documentation/UIKit/UIEditMenuInteractionDelegate)

The methods for customizing the menu the interaction displays.

[`UIEditMenuConfiguration`](/documentation/UIKit/UIEditMenuConfiguration)

An object containing the configuration details for the menu your app presents in response to an edit menu interaction.

[`UIResponderStandardEditActions`](/documentation/UIKit/UIResponderStandardEditActions)

A set of standard methods that apps can adopt to support editing.

### App menus

[`UIMenu`](/documentation/UIKit/UIMenu)

A container for grouping related menu elements in an app menu or contextual menu.

[`UIMenuBuilder`](/documentation/UIKit/UIMenuBuilder)

An interface for adding and removing menus from a menu system.

[`UIMenuSystem`](/documentation/UIKit/UIMenuSystem)

An object representing a main or contextual menu system.

[`UIMainMenuSystem`](/documentation/UIKit/UIMainMenuSystem)

The main menu system.

### Contextual menus

[`UIContextMenuSystem`](/documentation/UIKit/UIContextMenuSystem)

The context menu system.

[`UIContextMenuInteraction`](/documentation/UIKit/UIContextMenuInteraction)

An interaction object that you use to display relevant actions for your content.

[`UIContextMenuInteractionDelegate`](/documentation/UIKit/UIContextMenuInteractionDelegate)

The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.

[`UITargetedPreview`](/documentation/UIKit/UITargetedPreview)

An object describing the view to use during preview-related animations.

[`UIPreviewTarget`](/documentation/UIKit/UIPreviewTarget)

An object that specifies the container view to use for animations.

[`UIPreviewParameters`](/documentation/UIKit/UIPreviewParameters)

Additional parameters to use when animating a preview interface.

### Find and replace

[`UIFindInteraction`](/documentation/UIKit/UIFindInteraction)

An interaction that provides text finding and replacing operations using a system find panel.

[`UIFindInteractionDelegate`](/documentation/UIKit/UIFindInteractionDelegate)

A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.

[`UIFindSession`](/documentation/UIKit/UIFindSession)

An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.

[`UITextSearchingFindSession`](/documentation/UIKit/UITextSearchingFindSession)

A find session object that wraps a searchable object implementing the text-searching protocol.

[`UITextSearching`](/documentation/UIKit/UITextSearching-53wjq)

The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.

[`UITextSearching`](/documentation/UIKit/UITextSearching-3wkjv)

The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.

[`UITextSearchOptions`](/documentation/UIKit/UITextSearchOptions)

An object containing the configurable options for a text search.

[`UITextSearchFoundTextStyle`](/documentation/UIKit/UITextSearchFoundTextStyle)

Constants that describe the style a find session uses to decorate the text.

[`UITextSearchOptions.WordMatchMethod`](/documentation/UIKit/UITextSearchOptions/WordMatchMethod-swift.enum)

Constants that describe the method to use when searching text for words that match a string.

[`UIFindSession.SearchResultDisplayStyle`](/documentation/UIKit/UIFindSession/SearchResultDisplayStyle-swift.enum)

Constants that describe the results summary the find panel UI includes.

### Home Screen quick actions

[Add Home Screen quick actions](/documentation/UIKit/add-home-screen-quick-actions)

Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.

[`UIApplicationShortcutItem`](/documentation/UIKit/UIApplicationShortcutItem)

An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.

[`UIApplicationShortcutIcon`](/documentation/UIKit/UIApplicationShortcutIcon)

An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.

[`UIMutableApplicationShortcutItem`](/documentation/UIKit/UIMutableApplicationShortcutItem)

A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
