---
name: Toolbars
description: Rork-Max Quality skill for Toolbars. Actionable patterns and best practices for SwiftUI development.
---

# Toolbars

Provide immediate access to frequently used commands and controls.
The system might present toolbars above or below your app’s content,
depending on the platform and the context.
Add items to a toolbar by applying the `toolbar(content:)`
view modifier to a view in your app. You can also configure the toolbar
using view modifiers. For example, you can set the visibility of a toolbar
with the `toolbar(_:for:)` modifier.
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

### Populating a toolbar

| API | Purpose |
|-----|---------|
| `toolbar(content:)` | Populates the toolbar or navigation bar with the specified items. |
| `ToolbarItem` | A model that represents an item which can be placed in the toolbar |
| `ToolbarItemGroup` | A model that represents a group of `ToolbarItem`s which can be placed in |
| `ToolbarItemPlacement` | A structure that defines the placement of a toolbar item. |
| `ToolbarContent` | Conforming types represent items that can be placed in various locations |
| `ToolbarContentBuilder` | Constructs a toolbar item set from multi-expression closures. |
| `ToolbarSpacer` | A standard space item in toolbars. |
| `DefaultToolbarItem` | A toolbar item that represents a system component. |

### Populating a customizable toolbar

| API | Purpose |
|-----|---------|
| `toolbar(id:content:)` | Populates the toolbar or navigation bar with the specified items, |
| `CustomizableToolbarContent` | Conforming types represent items that can be placed in various locations |
| `ToolbarCustomizationBehavior` | The customization behavior of customizable toolbar content. |
| `ToolbarCustomizationOptions` | Options that influence the default customization behavior of |
| `SearchToolbarBehavior` | The behavior of a search field in a toolbar. |

### Removing default items

| API | Purpose |
|-----|---------|
| `toolbar(removing:)` | Remove a toolbar item present by default |
| `ToolbarDefaultItemKind` | A kind of toolbar item a `View` adds by default. |

### Setting toolbar visibility

| API | Purpose |
|-----|---------|
| `toolbar(_:for:)` | Specifies the visibility of a bar managed by SwiftUI. |
| `toolbarVisibility(_:for:)` | Specifies the visibility of a bar managed by SwiftUI. |
| `toolbarBackgroundVisibility(_:for:)` | Specifies the preferred visibility of backgrounds on a bar managed by |
| `ToolbarPlacement` | The placement of a toolbar. |

### Specifying the role of toolbar content

| API | Purpose |
|-----|---------|
| `toolbarRole(_:)` | Configures the semantic role for the content populating the toolbar. |
| `ToolbarRole` | The purpose of content that populates the toolbar. |

### Styling a toolbar

| API | Purpose |
|-----|---------|
| `toolbarBackground(_:for:)` | Specifies the preferred shape style of the background of a bar managed |
| `toolbarColorScheme(_:for:)` | Specifies the preferred color scheme of a bar managed by SwiftUI. |
| `toolbarForegroundStyle(_:for:)` | Specifies the preferred foreground style of bars managed by SwiftUI. |
| `windowToolbarStyle(_:)` | Sets the style for the toolbar defined within this scene. |
| `WindowToolbarStyle` | A specification for the appearance and behavior of a window’s toolbar. |
| `toolbarLabelStyle` | The label style to apply to controls within a toolbar. |
| `ToolbarLabelStyle` | The label style of a toolbar. |
| `SpacerSizing` | A type which defines how spacers should size themselves. |

### Configuring the toolbar title display mode

| API | Purpose |
|-----|---------|
| `toolbarTitleDisplayMode(_:)` | Configures the toolbar title display mode for this view. |
| `ToolbarTitleDisplayMode` | A type that defines the behavior of title of a toolbar. |

### Setting the toolbar title menu

| API | Purpose |
|-----|---------|
| `toolbarTitleMenu(content:)` | Configure the title menu of a toolbar. |
| `ToolbarTitleMenu` | The title menu of a toolbar. |

### Creating an ornament

| API | Purpose |
|-----|---------|
| `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` | Presents an ornament. |
| `OrnamentAttachmentAnchor` | An attachment anchor for an ornament. |
