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

- Previews: custom .contextMenu previews should use .ultraThinMaterial.\n- Haptics: The system handles the press haptic—don't trigger a second one.\n- Layout: Keep menu titles short to maintain the clean iOS aesthetic.


## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
