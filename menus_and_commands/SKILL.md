---
name: Menus and commands
description: Rork-Max Quality skill for Menus and commands. Actionable patterns and best practices for SwiftUI development.
---

# Menus and commands

Provide space-efficient, context-dependent access to commands and controls.
Use a menu to provide people with easy access to common commands. You can add
items to a macOS or iPadOS app’s menu bar using the `commands(content:)` scene
modifier, or create context menus that people reveal near their current task
using the `contextMenu(menuItems:)` view modifier.
Create submenus by nesting `Menu` instances inside others. Use a `Divider`
view to create a separator between menu elements.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct MenuExample: View {
    @State private var sortOrder: SortOrder = .name

    var body: some View {
        List(items) { item in
            Text(item.name)
                .contextMenu {
                    Button("Copy", systemImage: "doc.on.doc") { }
                    Button("Share", systemImage: "square.and.arrow.up") { }
                    Divider()
                    Button("Delete", systemImage: "trash", role: .destructive) { }
                }
        }
        .toolbar {
            Menu("Sort", systemImage: "arrow.up.arrow.down") {
                Picker("Sort By", selection: $sortOrder) {
                    Text("Name").tag(SortOrder.name)
                    Text("Date").tag(SortOrder.date)
                }
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `.contextMenu` with `preview:` parameter for rich long-press previews
- Add `role: .destructive` to delete actions for automatic red styling
- Use `Menu` in toolbars for dropdown action lists; `Picker` inside for selection

## When to Use

- Displaying text with rich formatting, markdown, or attributed strings
- Rendering images from assets, SF Symbols, or async URLs
- Building interactive controls: buttons, toggles, pickers, sliders, steppers
- Creating menus, context menus, and keyboard shortcuts

## Best Practices

- Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography
- Prefer `AsyncImage` for remote images with placeholder and error states
- Use `Label` to pair text with icons — it adapts to context (list rows, menus, toolbars)
- Support Dynamic Type by using system text styles (`.title`, `.body`, `.caption`)

## Common Pitfalls

- Hard-coding font sizes instead of using Dynamic Type styles
- Loading large images synchronously on the main thread
- Forgetting to provide accessibility labels for image-only buttons

## Key APIs

### Building a menu bar

| API | Purpose |
|-----|---------|
| `Building and customizing the menu bar with SwiftUI` | Provide a seamless, cross-platform user experience by building a native menu bar for iPadOS and macOS. |

### Creating a menu

| API | Purpose |
|-----|---------|
| `Populating SwiftUI menus with adaptive controls` | Improve your app by populating menus with controls and organizing your content intuitively. |
| `Menu` | A control for presenting a menu of actions. |
| `menuStyle(_:)` | Sets the style for menus within this view. |

### Creating context menus

| API | Purpose |
|-----|---------|
| `contextMenu(menuItems:)` | Adds a context menu to a view. |
| `contextMenu(menuItems:preview:)` | Adds a context menu with a custom preview to a view. |
| `contextMenu(forSelectionType:menu:primaryAction:)` | Adds an item-based context menu to a view. |

### Defining commands

| API | Purpose |
|-----|---------|
| `commands(content:)` | Adds commands to the scene. |
| `commandsRemoved()` | Removes all commands defined by the modified scene. |
| `commandsReplaced(content:)` | Replaces all commands defined by the modified scene with the commands |
| `Commands` | Conforming types represent a group of related commands that can be exposed |
| `CommandMenu` | Command menus are stand-alone, top-level containers for controls that |
| `CommandGroup` | Groups of controls that you can add to existing command menus. |
| `CommandsBuilder` | Constructs command sets from multi-expression closures. Like `ViewBuilder`, |
| `CommandGroupPlacement` | The standard locations that you can place new command groups relative to. |

### Getting built-in command groups

| API | Purpose |
|-----|---------|
| `SidebarCommands` | A built-in set of commands for manipulating window sidebars. |
| `TextEditingCommands` | A built-in group of commands for searching, editing, and transforming |
| `TextFormattingCommands` | A built-in set of commands for transforming the styles applied to selections |
| `ToolbarCommands` | A built-in set of commands for manipulating window toolbars. |
| `ImportFromDevicesCommands` | A built-in set of commands that enables importing content from nearby |
| `InspectorCommands` | A built-in set of commands for manipulating inspectors. |
| `EmptyCommands` | An empty group of commands. |

### Showing a menu indicator

| API | Purpose |
|-----|---------|
| `menuIndicator(_:)` | Sets the menu indicator visibility for controls within this view. |
| `menuIndicatorVisibility` | The menu indicator visibility to apply to controls within a view. |

### Configuring menu dismissal

| API | Purpose |
|-----|---------|
| `menuActionDismissBehavior(_:)` | Tells a menu whether to dismiss after performing an action. |
| `MenuActionDismissBehavior` | The set of menu dismissal behavior options. |

### Setting a preferred order

| API | Purpose |
|-----|---------|
| `menuOrder(_:)` | Sets the preferred order of items for menus presented from this view. |
| `menuOrder` | The preferred order of items for menus presented from this view. |
| `MenuOrder` | The order in which a menu presents its content. |

### Deprecated types

| API | Purpose |
|-----|---------|
| `MenuButton` | A button that displays a menu containing a list of choices when pressed. |
| `PullDownButton` | — |
| `ContextMenu` | A container for views that you present as menu items in a context menu. |
