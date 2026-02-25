---
name: Contextual Haptic Menus
description: Rork-Max Quality elite iOS frontend skill for Contextual Haptic Menus. Polishing the UIContextMenuInteraction and preview feel for elite depth.
---

# Contextual Haptic Menus

Polishing the UIContextMenuInteraction and preview feel for elite depth.


## 🚀 Rork-Max Quality Snippet


```swift
Text("Press for Menu")
    .contextMenu {
        Button(role: .destructive) { } label: { Label("Delete", systemImage: "trash") }
    } preview: {
        PremiumPreviewView()
    }
```


## 💎 Elite Implementation Tips

- Previews: custom .contextMenu previews should use .ultraThinMaterial.
- Haptics: The system handles the press haptic—don't trigger a second one.
- Layout: Keep menu titles short to maintain the clean iOS aesthetic.


## When to Use

- Adding long-press context menus to list items, cards, or media
- Providing quick actions (share, delete, favorite) without navigation
- Showing rich previews of content before committing to navigation

## Best Practices

- Use custom `.contextMenu { } preview: { }` for rich previews with glass materials
- Keep menu item titles short — 1-3 words maintain the clean iOS aesthetic
- Use SF Symbols for every menu action icon
- The system handles press haptic — don't trigger a second one

## Common Pitfalls

- Too many menu items overwhelm users — limit to 5-7 actions maximum
- Heavy preview views cause the menu to appear slowly — keep previews lightweight
- Forgetting `role: .destructive` on delete actions — it provides the red color and grouping
