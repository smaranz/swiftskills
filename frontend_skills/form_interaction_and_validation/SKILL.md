---
name: Form Interaction & Validation
description: Rork-Max Quality elite iOS frontend skill for Form Interaction & Validation. Floating labels with fluid, bouncy feedback and focus-state brilliance.
---

# Form Interaction & Validation

Floating labels with fluid, bouncy feedback and focus-state brilliance.


## 🚀 Rork-Max Quality Snippet


```swift
TextField("Label", text: $text)
    .focused($isFocused)
    .animation(.spring(response: 0.3), value: isFocused)
```


## 💎 Elite Implementation Tips

- Feedback: Shake the text field on invalid input using offsets.
- Focus: Use .ultraThinMaterial behind focused fields to highlight them.
- Keyboard: Add 'Done' or 'Next' button to the keyboard toolbar.


## When to Use

- Building sign-up, login, or data-entry forms with validation
- Creating professional text input experiences with focus management
- Implementing inline validation with real-time error feedback

## Best Practices

- Use `@FocusState` with an enum to manage focus across fields
- Shake the text field on invalid input using offset animation
- Add `.ultraThinMaterial` behind focused fields to highlight active input
- Add 'Done' or 'Next' toolbar buttons to the keyboard for field navigation

## Common Pitfalls

- Validating on every keystroke — debounce to 300ms or validate on focus loss
- Not handling keyboard toolbar for field-to-field navigation
- Error messages that push layout around — reserve space or use overlay
