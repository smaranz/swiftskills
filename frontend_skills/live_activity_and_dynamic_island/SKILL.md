---
name: Live Activity & Dynamic Island
description: Rork-Max Quality elite iOS frontend skill for Live Activity & Dynamic Island. Designing for real-time presence. Mastering ActivityKit and Island regions.
---

# Live Activity & Dynamic Island

Designing for real-time presence. Mastering ActivityKit and Island regions.


## 🚀 Rork-Max Quality Snippet

```swift
import ActivityKit
import SwiftUI
import WidgetKit

struct DeliveryAttributes: ActivityAttributes {
    public struct ContentState: Codable, Hashable {
        var status: String
        var progress: Double
        var eta: Date
    }
    var orderNumber: String
}

struct DeliveryLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: DeliveryAttributes.self) { context in
            // Lock Screen presentation
            HStack {
                VStack(alignment: .leading) {
                    Text("Order #\(context.attributes.orderNumber)")
                        .font(.caption).foregroundStyle(.secondary)
                    Text(context.state.status).font(.headline)
                }
                Spacer()
                ProgressView(value: context.state.progress)
                    .frame(width: 60)
            }
            .padding()
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    Label(context.state.status, systemImage: "box.truck.fill")
                        .font(.caption)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    Text(context.state.eta, style: .timer)
                        .font(.caption.monospacedDigit())
                }
            } compactLeading: {
                Image(systemName: "box.truck.fill")
            } compactTrailing: {
                ProgressView(value: context.state.progress)
                    .frame(width: 24)
            } minimal: {
                Image(systemName: "box.truck.fill")
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `ActivityConfiguration` to define Lock Screen + Dynamic Island presentations together
- Keep compact regions minimal — icon + progress bar or icon + short value
- Use `.timer` text style for live countdowns that update automatically
- Only push updates when state changes significantly (>10% progress)


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
