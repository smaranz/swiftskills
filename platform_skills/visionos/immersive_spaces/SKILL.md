---
name: VISIONOS Creating fully immersive experiences in your app
description: Rork-Max Quality skill for VISIONOS Creating fully immersive experiences in your app on visionos. Based on official Apple visionOS Documentation.
---

# VISIONOS Creating fully immersive experiences in your app

## 🚀 Rork-Max Quality Snippet

```swift
// Premium VISIONOS Creating fully immersive experiences in your app Implementation for visionos
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

# Creating fully immersive experiences in your app

Build fully immersive experiences by combining spaces with
content you create using RealityKit or Metal.

## Overview

A fully immersive experience replaces everything the person sees with
custom content you create. You might use this type of experience to:

- Offer a temporary transitional experience
- Create a distraction-free space for your content
- Implement a virtual reality (VR) game
- Present a virtual world to explore

With a fully immersive experience, you’re responsible for everything
that appears onscreen. The system hides passthrough video and displays
the content you provide, showing the person’s hands only when they
come into view. To achieve the best performance, use RealityKit or
Metal to create and animate your content.

![A window titled Destination Video floats in a room above a gray couch. There is a tall lamp next to the window. The window contains three featured columns showing videos to select. The first column is titled A Beach and has a picture of a boat on the ocean. The second column is titled Prehistoric Planet Clip has a picture of the head of a Tyrannosaurus rex. The third column is titled By the Lake and shows a closeup turtles sitting on a log that’s on the water. The user selects By the Lake and the window’s content changes to show information about that video, and the room changes to an immersive background of a lake with a shoreline just behind it. The window moves to the right as the person turns their head to view the immersive background.](videos/com.apple.visionOS/fully-immersive-example.mp4)

Typically, you combine a fully immersive experience with other types
of experiences and provide transitions between them. When you display
a window first and then offer controls to enter your immersive
experience, you give people time to prepare for the transition. It also
gives them the option to skip the experience if they prefer to use
your app’s windows instead.

![A window titled The Solar System floats in a room next to a gray couch. The right side of the window contains a picture of the sun and earth. The left side contains a paragraph describing how the earth orbits the sun. There’s a button beneath the text titled View Outer Space. The user selects the button, then the window fades into a completely immersive view of outer space and the earth spinning. As the person moves their head from left to right, the Moon and the Sun come into view.](videos/com.apple.visionOS/fully-immersive-transition.mp4)

### Prepare someone for your app’s transitions

Give people control over when they enter or exit fully immersive
experiences, and provide clear transitions to and from those experiences.
Clear visual transitions make it easier to adjust to such a large change.
Sudden transitions might be disorienting, unpleasant, or make the person
think something went wrong.

At launch time, display windows or other content that allows the person
to see their surroundings. Add controls to that content to initiate the
transition to the fully immersive experience, and provide a clear
indication of what the controls do. Inside your experience, provide
clear controls and instructions on how to exit the experience.

> Warning: When you start a fully immersive experience, visionOS defines
> a system boundary that extends approximately 1.5 meters from the initial position
> of the person’s head. If their head moves outside of that zone, the
> system automatically stops the immersive experience and turns on the
> external video again. This feature is an assistant to help prevent
> someone from colliding with objects.

For guidelines on how to design fully immersive experiences, see
[Human Interface Guidelines](doc://com.apple.documentation/design/human-interface-guidelines).

### Open an immersive space

To create a fully immersive experience, open an <doc://com.apple.documentation/documentation/SwiftUI/ImmersiveSpace>
and set its style to <doc://com.apple.documentation/documentation/SwiftUI/ImmersionStyle/full>.
An immersive space is a type of SwiftUI scene that lets you place
content anywhere in the person’s surroundings. Applying the
<doc://com.apple.documentation/documentation/SwiftUI/ImmersionStyle/full>
style to the scene tells the system to hide passthrough video and
display only your app’s content.

Declare spaces in the <doc://com.apple.documentation/documentation/SwiftUI/App/body-swift.property>
property of your app object, or anywhere you manage SwiftUI scenes. The
following example shows an app with a main window and a fully immersive
space. At launch time, the app displays the window.

```
@main
struct MyImmersiveApp: App {
    @State private var currentStyle: ImmersionStyle = .full

    var body: some Scene {
        WindowGroup() {
            ContentView()
        }

        // Display a fully immersive space.
        ImmersiveSpace(id: "solarSystem") {
            SolarSystemView()
        }.immersionStyle(selection: $currentStyle, in: .full)
    }
}
```

To display an <doc://com.apple.documentation/documentation/SwiftUI/ImmersiveSpace>,
open it using the <doc://com.apple.documentation/documentation/SwiftUI/EnvironmentValues/openImmersiveSpace>
action, which you obtain from the SwiftUI environment. This action runs
asynchronously and uses the provided information to find and initialize
your scene. The following example shows a button that opens the space with
the `solarSystem` identifier:

```
Button("Show Solar System") {
    Task {
        let result = await openImmersiveSpace(id: "solarSystem")
        if case .error = result {
            print("An error occurred")
        }
    }
}
```

An app can display only one space at a time, and it’s an error for you to try to
open a space while another space is visible. To dismiss an open space, use the
<doc://com.apple.documentation/documentation/SwiftUI/EnvironmentValues/dismissImmersiveSpace>
action.

For more information about displaying spaces, see the
<doc://com.apple.documentation/documentation/SwiftUI/ImmersiveSpace> type.

### Draw your content using RealityKit

RealityKit works well when your content consists of primitive shapes or
existing content in USD files. Organize the contents of your scene using
RealityKit entities, and animate that content using components and systems.
Use Reality Composer Pro to assemble your content visually, and to attach
dynamic shaders, animations, audio, and other behaviors to your content.
Display the contents of your RealityKit scene in a
<doc://com.apple.documentation/documentation/RealityKit/RealityView>
in your scene.

To load a Reality Composer Pro scene at runtime, fetch the URL of your
Reality Composer Pro package file, and load the root entity of your scene.
The following example shows how to create the entity for a package located
in the app’s bundle:

```
import MyRealityBundle

let url = MyRealityBundle.bundle.url(forResource:
         "MyRealityBundle", withExtension: "reality")
let scene = try await Entity(contentsOf: url)
```

For more information about how to display content in a
<doc://com.apple.documentation/documentation/RealityKit/RealityView> and
manage interactions with your content, see [Adding 3D content to your app](/documentation/visionOS/adding-3d-content-to-your-app).

### Draw your content using Metal

Another option for creating fully immersive scenes is to draw everything
yourself using Metal. When using Metal to draw your content, use the
Compositor Services framework to place that content onscreen. Compositor
Services provides the code you need to set up your Metal rendering engine
and start drawing.

For details on how to render content using Metal and Compositor Services,
and manage interactions with your content, see
<doc://com.apple.documentation/documentation/CompositorServices/drawing-fully-immersive-content-using-metal>.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
