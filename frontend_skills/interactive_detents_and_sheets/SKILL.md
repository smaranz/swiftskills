---
name: Interactive Detents & Sheets
description: Rork-Max Quality elite iOS frontend skill for Interactive Detents & Sheets. High-end bottom sheet customization. Mastering presentationDetents and background interactions.
---

# Interactive Detents & Sheets

High-end bottom sheet customization. Mastering presentationDetents and background interactions.


## 🚀 Rork-Max Quality Snippet


```swift
Text("Content")
    .presentationDetents([.height(200), .medium, .large])
    .presentationBackgroundInteraction(.enabled(upThrough: .medium))
    .presentationCornerRadius(44)
```


## 💎 Elite Implementation Tips

- Detents: Use custom .height() detents for context-specific mini-players.
- Background: .enabled background interaction allows multi-tasking.
- Aesthetics: A large corner radius (32-44pt) makes sheets feel integrated.


## When to Use

- Building mini-player, map overlay, or drawer-style bottom sheets
- Allowing interaction with content behind a partially visible sheet
- Creating custom sheet heights for context-specific workflows

## Best Practices

- Use custom `.height()` detents for context-specific mini-players or drawers
- Enable `.presentationBackgroundInteraction(.enabled(upThrough: .medium))` for map-style UIs
- Set `.presentationCornerRadius(32–44)` for sheets that feel integrated with the app
- Combine detents: `[.height(200), .medium, .large]` for three-stop sheets

## Common Pitfalls

- Forgetting `.presentationDragIndicator(.visible)` — users need affordance to drag
- Background interaction enabled at `.large` detent — the sheet covers the content anyway
- Not testing with keyboard visible — sheets resize when the keyboard appears
