---
name: WATCHOS Life cycles
description: Rork-Max Quality skill for WATCHOS Life cycles. Platform-native patterns and best practices for watchos development.
---

# WATCHOS Life cycles

Receive and respond to life-cycle notifications.

## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct SessionTracker: View {
    @Environment(\.isLuminanceReduced) private var isAlwaysOn
    @State private var elapsedTime: TimeInterval = 0

    var body: some View {
        TimelineView(.periodic(from: .now, by: isAlwaysOn ? 60 : 1)) { _ in
            Text(Duration.seconds(elapsedTime), format: .time(pattern: .minuteSecond))
                .font(.system(.title, design: .rounded, weight: .bold))
        }
    }
}
```

## 💎 Elite Implementation Tips

- Check `isLuminanceReduced` for Always On Display — reduce update frequency and dim the UI
- Use `TimelineView` for live-updating displays (timers, countdowns, sports scores)
- Extended runtime sessions keep the app active during workouts and navigation

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

## Key APIs

### Responding to life cycle events

| API | Purpose |
|-----|---------|
| `Handling Common State Transitions` | Detect and respond to common state transitions. |
| `Working with the watchOS app life cycle` | Learn how the watchOS app life cycle operates and responds to life cycle notification methods. |
| `Handling User Activity` | Detect and respond to user activity information from Handoff or a complication. |
| `Taking advantage of frontmost app state` | Understand the frontmost app state, and the features it provides to your app. |
