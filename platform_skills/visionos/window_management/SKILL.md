---
name: VISIONOS Positioning and sizing windows
description: Rork-Max Quality skill for VISIONOS Positioning and sizing windows on visionos. Based on official Apple visionOS Documentation.
---

# VISIONOS Positioning and sizing windows

## 🚀 Rork-Max Quality Snippet

```swift
// Premium VISIONOS Positioning and sizing windows Implementation for visionos
// Focus on platform-native excellence

import SwiftUI
#if os(visionos)
// visionOS specific imports
#endif

struct RorkPlatformView: View {
    var body: some View {
        Text("Rork Quality VISIONOS Experience")
            .font(.system(.title, design: .rounded))
            .padding()
            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
    }
}
```

## 💎 Elite Implementation Tips

- Master the visionos native feel: Use system-standard components correctly before customizing.
- Ensure optimal performance for visionos: Handle lifecycle events efficiently.
- Aesthetics: Keep designs clean and aligned with the platform's HIG.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Positioning and sizing windows

Influence the initial geometry of windows that your app presents.

## Overview

visionOS and macOS enable people to move and resize windows. In some cases,
your app can use scene modifiers to influence a window’s initial geometry
on these platforms, as well as to specify the strategy that the system employs
to place minimum and maximum size limitations on a window. This kind of
configuration affects both windows and volumes, which are windows with the
<doc://com.apple.documentation/documentation/SwiftUI/WindowStyle/volumetric>
window style.

Your ability to configure window size and position is subject to the
following constraints:

- The system might be unable to fulfill your request. For example, if you
  specify a default size that’s outside the range of the window’s resizability,
  the system clamps the affected dimension to keep it in range.
- Although you can change the window’s content, you can’t directly manipulate
  window position or size after the window appears. This ensures that people
  have full control over their workspace.
- During state restoration, the system restores windows to their previous
  position and size.

> Note: Windows in iPadOS occupy the full screen, or share the screen with
> another window in Slide Over or Split View. You can’t programmatically
> affect window geometry on that platform.

### Specify initial window position

**macOS:**

In macOS, the first time your app opens a window from a particular scene
declaration, the system places the window at the center of the screen by
default.
For scene types that support multiple simultaneous windows, the
system offsets each additional window by a small amount to avoid fully
obscuring existing windows.

You can override the default placement of the first window in macOS by applying
the <doc://com.apple.documentation/documentation/SwiftUI/Scene/defaultPosition(_:)>
scene modifier to indicate where to place the window relative to the screen
bounds. For example, you can request that the system place a new window in the
bottom trailing corner of the screen.

```
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultPosition(.bottomTrailing)
    }
}
```

The system aligns the point in the window that corresponds to the specified
<doc://com.apple.documentation/documentation/SwiftUI/UnitPoint> with the point in the screen that corresponds to the
same unit point. You can use a built-in unit point, like
<doc://com.apple.documentation/documentation/SwiftUI/UnitPoint/bottomTrailing> in the above example, or define a custom
one.

You can also use <doc://com.apple.documentation/documentation/SwiftUI/Scene/defaultWindowPlacement(_:)> to place windows.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        // ...
        
        Window("Status", id: "status") {
            StatusView()
        }
        .windowResizability(.contentSize)
        .defaultWindowPlacement { content, context in
            let displayBounds = context.defaultDisplay.visibleRect
            let size = content.sizeThatFits(.unspecified)
            let verticalOffset = 140
            
            // The system places the window 140 points from the bottom of the screen.
            let position = CGPoint(
                x: displayBounds.midX - (size.width / 2),
                y: displayBounds.maxY - size.height - verticalOffset)
            return WindowPlacement(position: position, size: size)
        }
    }
}
```

**visionOS:**

In visionOS, the system places new windows automatically depending on the situation:
        
        - When someone first launches an app from the Home View, the system places the app’s window where they’re looking.
        - When a running app opens a new window, the system places the new window in front of one of the app’s existing windows, offsetting each additional window by a small amount to avoid fully obscuring existing windows.

You can override the default placement of the window by applying
the
<doc://com.apple.documentation/documentation/SwiftUI/Scene/defaultWindowPlacement(_:)>
scene modifier to indicate where to place the window.
For example, you can request that the system place a new window on the trailing edge of the existing window.

```
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup(id: "content") {
            ContentView()
        }
        WindowGroup(id: "trailingWindow") {
           TrailingWindowView()
        }
        .defaultWindowPlacement { content, context in
           guard let contentWindow = context.windows.first(where: { $0.id == "content" }) else { return WindowPlacement(nil) 
           }
           return WindowPlacement(.trailing(contentWindow))
       }
    }
}
```

Use one of the
<doc://com.apple.documentation/documentation/SwiftUI/WindowPlacement/Position> enumerations to choose the position of the window.

### Specify initial window size

You can indicate a default initial size for a new
window that the system creates from a
<doc://com.apple.documentation/documentation/SwiftUI/Scene> declaration by applying
one of the default size scene modifiers, like <doc://com.apple.documentation/documentation/SwiftUI/Scene/defaultSize(width:height:)>.
For example, you can request that new windows that a <doc://com.apple.documentation/documentation/SwiftUI/WindowGroup>
generates occupy 600 points in the x-dimension and 400 points in the
y-dimension.

```
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(CGSize(width: 600, height: 400))
    }
}
```

The system might clamp the actual size of the window, depending on both the
window’s content and resizability settings.

### Specify window resizability

Both macOS and visionOS provide interface controls that enable people to resize
windows within certain limits. For example, people can use the control that
appears when they look at the corner of a visionOS window to resize a window
on that platform.

![A video showing someone resizing an app's window using the control that appears in the lower-right corner.](videos/com.apple.visionOS/resizing-window.mp4)

You can specify how the system limits window resizability.
The default resizability for all scenes is
<doc://com.apple.documentation/documentation/SwiftUI/WindowResizability/automatic>.
With that strategy,
<doc://com.apple.documentation/documentation/SwiftUI/Settings>
windows use the
<doc://com.apple.documentation/documentation/SwiftUI/WindowResizability/contentSize>
strategy, where both the minimum and maximum window size match the respective
minimum and maximum sizes of the content that the window contains.
Other scene types use
<doc://com.apple.documentation/documentation/SwiftUI/WindowResizability/contentMinSize>
by default, which retains the minimum size restriction, but doesn’t limit the
maximium size.

You can specify one of these resizability strategies explicitly by adding the
<doc://com.apple.documentation/documentation/SwiftUI/Scene/windowResizability(_:)>
scene modifier to a scene. For example, people can resize windows from the
following window group to between 100 and 400 points in both dimensions because
the frame modifier imposes those bounds on the content view:

```
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 100, maxWidth: 400,
                    minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentSize)
    }
}
```

You can take this even further and enforce a specific size for a window with
content that has a fixed size.

### Specify a volume size

When you create a volume, which is a window with the
<doc://com.apple.documentation/documentation/SwiftUI/WindowStyle/volumetric>
style, you can specify the volume’s size using one of the three-dimensional
default size modifiers, like
<doc://com.apple.documentation/documentation/SwiftUI/Scene/defaultSize(width:height:depth:in:)>.
The following code creates a volume that’s one meter on a side:

```
WindowGroup(id: "globe") {
    Globe()
}
.windowStyle(.volumetric)
.defaultSize(width: 1, height: 1, depth: 1, in: .meters)
```

Although you can specify a volume’s size in points, it’s typically better
to use physical units, like the above code, which specifies a size in meters.
This is because the system renders a volume with fixed scaling rather than
dynamic scaling, unlike a regular window, which means the volume appears more
like a physical object than a user interface. For information about the
different kinds of scaling, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/spatial-layout>.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
