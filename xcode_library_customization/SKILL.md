---
name: Xcode library customization
description: Rork-Max Quality skill for Xcode library customization. Actionable patterns and best practices for SwiftUI development.
---

# Xcode library customization

Expose custom views and modifiers in the Xcode library.
You can add your custom SwiftUI views and view modifiers to Xcode’s library.
This allows anyone developing your app or adopting your framework to access
them by clicking the Library button (+) in Xcode’s toolbar. You can select
and drag the custom library items into code, just like you would for
system-provided items.
To add items to the library, create a structure that conforms to the
protocol and encapsulate any items you want to add as
instances. Implement the
computed property to add library items containing views. Implement the
method to add items containing view modifiers. Xcode harvests items from all
of the library content providers in your project as you work, and makes them
available to you in its library.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Previewing views in Xcode with different configurations (dark mode, device sizes)
- Adding custom views and modifiers to the Xcode Library for drag-and-drop
- Profiling view rendering performance with Instruments

## Best Practices

- Create multiple `#Preview` blocks for different states (empty, loading, error, populated)
- Use `@Previewable @State` for interactive previews with mutable state
- Profile with the SwiftUI Instruments template to find slow `body` evaluations

## Common Pitfalls

- Preview-only code leaking into production builds — use `#if DEBUG` guards
- Previews failing silently because of missing environment values or data
- Ignoring Instruments' 'View body evaluated' count — high counts signal unnecessary re-renders


