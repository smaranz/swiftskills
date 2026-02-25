---
name: WATCHOS Setting up a watchOS project
description: Rork-Max Quality skill for WATCHOS Setting up a watchOS project. Platform-native patterns and best practices for watchos development.
---

# WATCHOS Setting up a watchOS project

Create a new watchOS project or add a watch target to an existing iOS project.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

@main
struct WatchApp: App {
    var body: some Scene {
        WindowGroup {
            NavigationStack {
                List {
                    NavigationLink("Workouts") { WorkoutListView() }
                    NavigationLink("Settings") { SettingsView() }
                }
                .navigationTitle("My App")
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- watchOS apps use SwiftUI exclusively — no storyboards or WKInterfaceController needed
- Use `NavigationStack` with `List` for the standard watch navigation pattern
- Keep the app focused — one primary action per screen

## When to Use

- Building watchOS apps with glanceable, quick interactions
- Implementing complications, background refresh, and workout tracking
- Optimizing for the small screen and limited resources of Apple Watch

## Best Practices

- Keep interactions under 5 seconds — watchOS is for glances, not sessions
- Use `.digitalCrownRotation()` for scroll and value adjustment
- Schedule background refresh tasks for up-to-date complications

## Common Pitfalls

- Trying to replicate the iPhone UI on watch — design for the wrist
- Ignoring battery constraints — minimize animations and network requests
- Forgetting that watchOS apps have very limited background execution time


