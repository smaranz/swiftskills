---
name: Menus and commands
description: Rork-Max Quality skill for Menus and commands. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Menus and commands


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Menus and commands

Provide space-efficient, context-dependent access to commands and controls.

## Overview

Use a menu to provide people with easy access to common commands. You can add
items to a macOS or iPadOS app’s menu bar using the [`commands(content:)`](/documentation/SwiftUI/Scene/commands(content:)) scene
modifier, or create context menus that people reveal near their current task
using the [`contextMenu(menuItems:)`](/documentation/SwiftUI/View/contextMenu(menuItems:)) view modifier.

![](images/com.apple.SwiftUI/menus-and-commands-hero@2x.png)

Create submenus by nesting [`Menu`](/documentation/SwiftUI/Menu) instances inside others. Use a [`Divider`](/documentation/SwiftUI/Divider)
view to create a separator between menu elements.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/menus>
in the Human Interface Guidelines.

## Topics

### Building a menu bar

[Building and customizing the menu bar with SwiftUI](/documentation/SwiftUI/Building-and-customizing-the-menu-bar-with-SwiftUI)

Provide a seamless, cross-platform user experience by building a native menu bar for iPadOS and macOS.

### Creating a menu

[Populating SwiftUI menus with adaptive controls](/documentation/SwiftUI/Populating-SwiftUI-menus-with-adaptive-controls)

Improve your app by populating menus with controls and organizing your content intuitively.

[`Menu`](/documentation/SwiftUI/Menu)

A control for presenting a menu of actions.

[`menuStyle(_:)`](/documentation/SwiftUI/View/menuStyle(_:))

Sets the style for menus within this view.

### Creating context menus

[`contextMenu(menuItems:)`](/documentation/SwiftUI/View/contextMenu(menuItems:))

Adds a context menu to a view.

[`contextMenu(menuItems:preview:)`](/documentation/SwiftUI/View/contextMenu(menuItems:preview:))

Adds a context menu with a custom preview to a view.

[`contextMenu(forSelectionType:menu:primaryAction:)`](/documentation/SwiftUI/View/contextMenu(forSelectionType:menu:primaryAction:))

Adds an item-based context menu to a view.

### Defining commands

[`commands(content:)`](/documentation/SwiftUI/Scene/commands(content:))

Adds commands to the scene.

[`commandsRemoved()`](/documentation/SwiftUI/Scene/commandsRemoved())

Removes all commands defined by the modified scene.

[`commandsReplaced(content:)`](/documentation/SwiftUI/Scene/commandsReplaced(content:))

Replaces all commands defined by the modified scene with the commands
from the builder.

[`Commands`](/documentation/SwiftUI/Commands)

Conforming types represent a group of related commands that can be exposed
to the user via the main menu on macOS and key commands on iOS.

[`CommandMenu`](/documentation/SwiftUI/CommandMenu)

Command menus are stand-alone, top-level containers for controls that
perform related, app-specific commands.

[`CommandGroup`](/documentation/SwiftUI/CommandGroup)

Groups of controls that you can add to existing command menus.

[`CommandsBuilder`](/documentation/SwiftUI/CommandsBuilder)

Constructs command sets from multi-expression closures. Like `ViewBuilder`,
it supports up to ten expressions in the closure body.

[`CommandGroupPlacement`](/documentation/SwiftUI/CommandGroupPlacement)

The standard locations that you can place new command groups relative to.

### Getting built-in command groups

[`SidebarCommands`](/documentation/SwiftUI/SidebarCommands)

A built-in set of commands for manipulating window sidebars.

[`TextEditingCommands`](/documentation/SwiftUI/TextEditingCommands)

A built-in group of commands for searching, editing, and transforming
selections of text.

[`TextFormattingCommands`](/documentation/SwiftUI/TextFormattingCommands)

A built-in set of commands for transforming the styles applied to selections
of text.

[`ToolbarCommands`](/documentation/SwiftUI/ToolbarCommands)

A built-in set of commands for manipulating window toolbars.

[`ImportFromDevicesCommands`](/documentation/SwiftUI/ImportFromDevicesCommands)

A built-in set of commands that enables importing content from nearby
devices.

[`InspectorCommands`](/documentation/SwiftUI/InspectorCommands)

A built-in set of commands for manipulating inspectors.

[`EmptyCommands`](/documentation/SwiftUI/EmptyCommands)

An empty group of commands.

### Showing a menu indicator

[`menuIndicator(_:)`](/documentation/SwiftUI/View/menuIndicator(_:))

Sets the menu indicator visibility for controls within this view.

[`menuIndicatorVisibility`](/documentation/SwiftUI/EnvironmentValues/menuIndicatorVisibility)

The menu indicator visibility to apply to controls within a view.

### Configuring menu dismissal

[`menuActionDismissBehavior(_:)`](/documentation/SwiftUI/View/menuActionDismissBehavior(_:))

Tells a menu whether to dismiss after performing an action.

[`MenuActionDismissBehavior`](/documentation/SwiftUI/MenuActionDismissBehavior)

The set of menu dismissal behavior options.

### Setting a preferred order

[`menuOrder(_:)`](/documentation/SwiftUI/View/menuOrder(_:))

Sets the preferred order of items for menus presented from this view.

[`menuOrder`](/documentation/SwiftUI/EnvironmentValues/menuOrder)

The preferred order of items for menus presented from this view.

[`MenuOrder`](/documentation/SwiftUI/MenuOrder)

The order in which a menu presents its content.

### Deprecated types

[`MenuButton`](/documentation/SwiftUI/MenuButton)

A button that displays a menu containing a list of choices when pressed.

[`PullDownButton`](/documentation/SwiftUI/PullDownButton)

[`ContextMenu`](/documentation/SwiftUI/ContextMenu)

A container for views that you present as menu items in a context menu.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
