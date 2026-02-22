---
name: MACOS Menus, Cursors, and the Dock
description: Rork-Max Quality skill for MACOS Menus, Cursors, and the Dock on macos. Based on official Apple AppKit Documentation.
---

# MACOS Menus, Cursors, and the Dock

## 🚀 Rork-Max Quality Snippet

```swift
// Premium MACOS Menus, Cursors, and the Dock Implementation for macos
// Focus on platform-native excellence

import SwiftUI
#if os(macos)
// AppKit specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality MACOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the macos native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for macos: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Menus, Cursors, and the Dock

Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.

## Topics

### Menus

[`NSMenu`](/documentation/AppKit/NSMenu)

An object that manages an app’s menus.

[`NSMenuItem`](/documentation/AppKit/NSMenuItem)

A command item in an app menu.

[`NSMenuItemBadge`](/documentation/AppKit/NSMenuItemBadge)

A control that provides additional quantitative information specific to a menu item, such as the number of available updates.

[`NSMenuDelegate`](/documentation/AppKit/NSMenuDelegate)

The optional methods implemented by delegates of [`NSMenu`](/documentation/AppKit/NSMenu) objects to manage menu display and handle some events.

### Menu Validation

[`NSMenuItemValidation`](/documentation/AppKit/NSMenuItemValidation)

### Menu Bar Items

[`NSStatusBar`](/documentation/AppKit/NSStatusBar)

An object that manages a collection of status items displayed within the system-wide menu bar.

[`NSStatusItem`](/documentation/AppKit/NSStatusItem)

An individual element displayed in the system menu bar.

[`NSStatusBarButton`](/documentation/AppKit/NSStatusBarButton)

The appearance and behavior of an item in the systemwide menu bar.

### Cursors

[`NSCursor`](/documentation/AppKit/NSCursor)

A pointer (also called a cursor).

[`NSTrackingArea`](/documentation/AppKit/NSTrackingArea)

A region of a view that generates mouse-tracking and cursor-update events when the pointer is over that region.

### The Dock

[`NSDockTile`](/documentation/AppKit/NSDockTile)

The visual representation of your app’s miniaturized windows and app icon as they appear in the Dock.

[`NSDockTilePlugIn`](/documentation/AppKit/NSDockTilePlugIn)

A set of methods implemented by plug-ins that allow an app’s Dock tile to be customized while the app is not running.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
