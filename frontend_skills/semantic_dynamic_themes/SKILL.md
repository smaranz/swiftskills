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

- Tokens: Never use static 'Color.white'—always use semantic background/materials.\n- Contrast: Dark mode backgrounds should be dark gray, not pure black.\n- Vibrancy: Use .foregroundStyle(.tertiary) for hierarchy.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
