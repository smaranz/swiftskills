---
name: Toolbars
description: Rork-Max Quality skill for Toolbars. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Toolbars


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Toolbars

Provide immediate access to frequently used commands and controls.

## Overview

The system might present toolbars above or below your app’s content,
depending on the platform and the context.

![](images/com.apple.SwiftUI/toolbars-hero@2x.png)

Add items to a toolbar by applying the [`toolbar(content:)`](/documentation/SwiftUI/View/toolbar(content:))
view modifier to a view in your app. You can also configure the toolbar
using view modifiers. For example, you can set the visibility of a toolbar
with the [`toolbar(_:for:)`](/documentation/SwiftUI/View/toolbar(_:for:)) modifier.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/toolbars>
in the Human Interface Guidelines.

## Topics

### Populating a toolbar

[`toolbar(content:)`](/documentation/SwiftUI/View/toolbar(content:))

Populates the toolbar or navigation bar with the specified items.

[`ToolbarItem`](/documentation/SwiftUI/ToolbarItem)

A model that represents an item which can be placed in the toolbar
or navigation bar.

[`ToolbarItemGroup`](/documentation/SwiftUI/ToolbarItemGroup)

A model that represents a group of `ToolbarItem`s which can be placed in
the toolbar or navigation bar.

[`ToolbarItemPlacement`](/documentation/SwiftUI/ToolbarItemPlacement)

A structure that defines the placement of a toolbar item.

[`ToolbarContent`](/documentation/SwiftUI/ToolbarContent)

Conforming types represent items that can be placed in various locations
in a toolbar.

[`ToolbarContentBuilder`](/documentation/SwiftUI/ToolbarContentBuilder)

Constructs a toolbar item set from multi-expression closures.

[`ToolbarSpacer`](/documentation/SwiftUI/ToolbarSpacer)

A standard space item in toolbars.

[`DefaultToolbarItem`](/documentation/SwiftUI/DefaultToolbarItem)

A toolbar item that represents a system component.

### Populating a customizable toolbar

[`toolbar(id:content:)`](/documentation/SwiftUI/View/toolbar(id:content:))

Populates the toolbar or navigation bar with the specified items,
allowing for user customization.

[`CustomizableToolbarContent`](/documentation/SwiftUI/CustomizableToolbarContent)

Conforming types represent items that can be placed in various locations
in a customizable toolbar.

[`ToolbarCustomizationBehavior`](/documentation/SwiftUI/ToolbarCustomizationBehavior)

The customization behavior of customizable toolbar content.

[`ToolbarCustomizationOptions`](/documentation/SwiftUI/ToolbarCustomizationOptions)

Options that influence the default customization behavior of
customizable toolbar content.

[`SearchToolbarBehavior`](/documentation/SwiftUI/SearchToolbarBehavior)

The behavior of a search field in a toolbar.

### Removing default items

[`toolbar(removing:)`](/documentation/SwiftUI/View/toolbar(removing:))

Remove a toolbar item present by default

[`ToolbarDefaultItemKind`](/documentation/SwiftUI/ToolbarDefaultItemKind)

A kind of toolbar item a `View` adds by default.

### Setting toolbar visibility

[`toolbar(_:for:)`](/documentation/SwiftUI/View/toolbar(_:for:))

Specifies the visibility of a bar managed by SwiftUI.

[`toolbarVisibility(_:for:)`](/documentation/SwiftUI/View/toolbarVisibility(_:for:))

Specifies the visibility of a bar managed by SwiftUI.

[`toolbarBackgroundVisibility(_:for:)`](/documentation/SwiftUI/View/toolbarBackgroundVisibility(_:for:))

Specifies the preferred visibility of backgrounds on a bar managed by
SwiftUI.

[`ToolbarPlacement`](/documentation/SwiftUI/ToolbarPlacement)

The placement of a toolbar.

[`ContentToolbarPlacement`](/documentation/SwiftUI/ContentToolbarPlacement)

### Specifying the role of toolbar content

[`toolbarRole(_:)`](/documentation/SwiftUI/View/toolbarRole(_:))

Configures the semantic role for the content populating the toolbar.

[`ToolbarRole`](/documentation/SwiftUI/ToolbarRole)

The purpose of content that populates the toolbar.

### Styling a toolbar

[`toolbarBackground(_:for:)`](/documentation/SwiftUI/View/toolbarBackground(_:for:))

Specifies the preferred shape style of the background of a bar managed
by SwiftUI.

[`toolbarColorScheme(_:for:)`](/documentation/SwiftUI/View/toolbarColorScheme(_:for:))

Specifies the preferred color scheme of a bar managed by SwiftUI.

[`toolbarForegroundStyle(_:for:)`](/documentation/SwiftUI/View/toolbarForegroundStyle(_:for:))

Specifies the preferred foreground style of bars managed by SwiftUI.

[`windowToolbarStyle(_:)`](/documentation/SwiftUI/Scene/windowToolbarStyle(_:))

Sets the style for the toolbar defined within this scene.

[`WindowToolbarStyle`](/documentation/SwiftUI/WindowToolbarStyle)

A specification for the appearance and behavior of a window’s toolbar.

[`toolbarLabelStyle`](/documentation/SwiftUI/EnvironmentValues/toolbarLabelStyle)

The label style to apply to controls within a toolbar.

[`ToolbarLabelStyle`](/documentation/SwiftUI/ToolbarLabelStyle)

The label style of a toolbar.

[`SpacerSizing`](/documentation/SwiftUI/SpacerSizing)

A type which defines how spacers should size themselves.

### Configuring the toolbar title display mode

[`toolbarTitleDisplayMode(_:)`](/documentation/SwiftUI/View/toolbarTitleDisplayMode(_:))

Configures the toolbar title display mode for this view.

[`ToolbarTitleDisplayMode`](/documentation/SwiftUI/ToolbarTitleDisplayMode)

A type that defines the behavior of title of a toolbar.

### Setting the toolbar title menu

[`toolbarTitleMenu(content:)`](/documentation/SwiftUI/View/toolbarTitleMenu(content:))

Configure the title menu of a toolbar.

[`ToolbarTitleMenu`](/documentation/SwiftUI/ToolbarTitleMenu)

The title menu of a toolbar.

### Creating an ornament

[`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:))

Presents an ornament.

[`OrnamentAttachmentAnchor`](/documentation/SwiftUI/OrnamentAttachmentAnchor)

An attachment anchor for an ornament.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
