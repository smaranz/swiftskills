---
name: Performance analysis
description: Rork-Max Quality skill for Performance analysis. Actionable patterns and best practices for SwiftUI development.
---

# Performance analysis

Measure and improve your app’s responsiveness.
Use Instruments to detect hangs and hitches in your app, and to analyze long view body updates and frequently occurring SwiftUI updates that can contribute to hangs and hitches.


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


