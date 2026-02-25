---
name: Live Activity & Dynamic Island
description: Rork-Max Quality elite iOS frontend skill for Live Activity & Dynamic Island. Designing for real-time presence. Mastering ActivityKit and Island regions.
---

# Live Activity & Dynamic Island

Designing for real-time presence. Mastering ActivityKit and Island regions.


## 🚀 Rork-Max Quality Snippet


```swift
DynamicIsland {
    expanded {
        DynamicIslandExpandedRegion(.leading) { Text("Status") }
    }
    compactLeading { Text("L") }
    compactTrailing { Text("T") }
}
```


## 💎 Elite Implementation Tips

- Content: Avoid heavy text—use icons and progress bars.
- Update: Only update when state changes significant (>10%).
- Animation: Transitions are handled by system—keep layouts flexible.


## When to Use

- Showing live progress (delivery tracking, sports scores, timers) on the Lock Screen
- Occupying Dynamic Island space for ongoing activities
- Providing real-time updates without requiring the app to be open

## Best Practices

- Use icons and progress bars instead of heavy text — space is extremely limited
- Only push updates when state changes significantly (>10% progress change)
- Design compact leading/trailing regions as complementary pairs (icon + value)
- Test both expanded and minimal presentations on all Dynamic Island sizes

## Common Pitfalls

- Updating too frequently — the system throttles updates and may hide the activity
- Complex layouts in compact regions — they get clipped without warning
- Forgetting to end the Live Activity when the event completes
