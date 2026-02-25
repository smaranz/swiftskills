---
name: Interactive Detents & Sheets
description: Rork-Max Quality elite iOS frontend skill for Interactive Detents & Sheets. High-end bottom sheet customization. Mastering presentationDetents and background interactions.
---

# Interactive Detents & Sheets

High-end bottom sheet customization. Mastering presentationDetents and background interactions.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct MiniPlayerSheet: View {
    @State private var showSheet = false

    var body: some View {
        Button("Show Player") { showSheet = true }
            .sheet(isPresented: $showSheet) {
                VStack(spacing: 16) {
                    Capsule()
                        .fill(.secondary.opacity(0.4))
                        .frame(width: 36, height: 5)
                        .padding(.top, 8)

                    HStack(spacing: 16) {
                        RoundedRectangle(cornerRadius: 8)
                            .fill(.blue.gradient)
                            .frame(width: 48, height: 48)
                        VStack(alignment: .leading) {
                            Text("Now Playing").font(.headline)
                            Text("Artist Name").font(.caption).foregroundStyle(.secondary)
                        }
                        Spacer()
                        Button(action: {}) {
                            Image(systemName: "play.fill").font(.title2)
                        }
                    }
                    .padding(.horizontal)
                }
                .presentationDetents([.height(120), .medium, .large])
                .presentationBackgroundInteraction(.enabled(upThrough: .medium))
                .presentationCornerRadius(32)
                .presentationDragIndicator(.hidden)
                .interactiveDismissDisabled()
            }
    }
}
```

## 💎 Elite Implementation Tips

- Combine `.height()`, `.medium`, `.large` detents for three-stop drawer behavior
- Use `.presentationBackgroundInteraction(.enabled(upThrough:))` for map-style UIs
- Hide the system drag indicator and add a custom capsule grabber for full design control
- Set `.presentationCornerRadius(32–44)` for sheets that feel integrated with the app


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
