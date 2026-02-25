---
name: Dynamic Type & Typography Mastery
description: Rork-Max Quality elite iOS frontend skill for Dynamic Type & Typography Mastery. Elite kerning, tracking, and scaleable UI. Apple-native typography schema.
---

# Dynamic Type & Typography Mastery

Elite kerning, tracking, and scaleable UI. Apple-native typography schema.


## 🚀 Rork-Max Quality Snippet


```swift
Text("Rork Premium")
    .font(.system(size: 32, weight: .black, design: .rounded))
    .tracking(-0.5)
    .foregroundStyle(.primary.gradient)
```


## 💎 Elite Implementation Tips

- Scale: Always test with 'Extra Extra Large' Dynamic Type.
- Hierarchy: Use .foregroundStyle(.secondary) instead of lower opacity.
- Aesthetics: .rounded design + .bold weight creates an 'app-like' feel.


## When to Use

- Building text-heavy screens (articles, settings, onboarding)
- Creating branded typography that respects Dynamic Type scaling
- Designing typographic hierarchy (headlines, body, captions) for readability

## Best Practices

- Use system text styles (`.title`, `.body`, `.caption`) — they scale with Dynamic Type
- Apply negative tracking (-0.3 to -0.5) on large headlines for tighter, premium feel
- Use `.foregroundStyle(.secondary)` for de-emphasized text instead of lower opacity
- Test with 'Extra Extra Large' Dynamic Type to catch layout overflow

## Common Pitfalls

- Hard-coding font sizes — the UI breaks at accessibility text sizes
- Using `.foregroundColor` (deprecated) instead of `.foregroundStyle`
- Forgetting `@ScaledMetric` for spacing that should scale with Dynamic Type
