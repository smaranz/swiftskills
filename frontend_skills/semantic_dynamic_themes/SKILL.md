---
name: Semantic Dynamic Themes
description: Rork-Max Quality elite iOS frontend skill for Semantic Dynamic Themes. Beyond Dark Mode—environmental-adaptive UI using system colors and vibrancies.
---

# Semantic Dynamic Themes

Beyond Dark Mode—environmental-adaptive UI using system colors and vibrancies.


## 🚀 Rork-Max Quality Snippet


```swift
struct AdaptiveTheme: ViewModifier {
    @Environment(\.colorScheme) var scheme
    var body(content: Content) -> some View {
        content.foregroundStyle(scheme == .dark ? .white : .black)
    }
}
```


## 💎 Elite Implementation Tips

- Tokens: Never use static 'Color.white'—always use semantic background/materials.
- Contrast: Dark mode backgrounds should be dark gray, not pure black.
- Vibrancy: Use .foregroundStyle(.tertiary) for hierarchy.


## When to Use

- Building apps that look correct in both light and dark modes without manual color sets
- Creating themed experiences (seasonal, branded) that still respect system appearance
- Designing for high-contrast and increased-contrast accessibility modes

## Best Practices

- Never use static `.white` or `.black` — use semantic colors (`.label`, `.background`, `.systemBackground`)
- Dark mode backgrounds should be dark gray (`.systemBackground`), not pure black
- Use `.foregroundStyle(.tertiary)` for visual hierarchy instead of custom opacity values
- Define custom colors in Asset Catalog with light/dark variants, not in code

## Common Pitfalls

- Testing only in one appearance mode — always verify both light and dark
- Hard-coded colors that break in dark mode or high-contrast mode
- Using `.opacity()` for de-emphasis instead of semantic `.secondary`/`.tertiary` styles
