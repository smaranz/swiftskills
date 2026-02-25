---
name: WATCHOS Setting up a watchOS project
description: Rork-Max Quality skill for WATCHOS Setting up a watchOS project. Platform-native patterns and best practices for watchos development.
---

# WATCHOS Setting up a watchOS project

Create a new watchOS project or add a watch target to an existing iOS project.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct RorkWatchView: View {
    var body: some View {
        NavigationStack {
            List {
                Text("Setting up a watchOS project")
                    .font(.headline)
            }
            .navigationTitle("Rork")
        }
    }
}
```

## 💎 Elite Implementation Tips

- Follow the WATCHOS Human Interface Guidelines for native feel.
- Use system-standard WatchKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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


