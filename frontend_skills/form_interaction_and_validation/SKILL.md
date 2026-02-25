---
name: Form Interaction & Validation
description: Rork-Max Quality elite iOS frontend skill for Form Interaction & Validation. Floating labels with fluid, bouncy feedback and focus-state brilliance.
---

# Form Interaction & Validation

Floating labels with fluid, bouncy feedback and focus-state brilliance.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct ValidatedForm: View {
    @State private var email = ""
    @State private var password = ""
    @State private var emailError: String?
    @State private var shake = false
    @FocusState private var field: Field?

    enum Field { case email, password }

    var body: some View {
        VStack(spacing: 16) {
            VStack(alignment: .leading, spacing: 4) {
                TextField("Email", text: $email)
                    .focused($field, equals: .email)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .submitLabel(.next)
                    .onSubmit { field = .password }
                    .padding(12)
                    .background(field == .email ? .ultraThinMaterial : .regularMaterial,
                                in: RoundedRectangle(cornerRadius: 12))
                    .offset(x: shake ? -6 : 0)

                if let error = emailError {
                    Text(error).font(.caption).foregroundStyle(.red)
                }
            }

            SecureField("Password", text: $password)
                .focused($field, equals: .password)
                .submitLabel(.done)
                .onSubmit { validate() }
                .padding(12)
                .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 12))

            Button("Sign In") { validate() }
                .buttonStyle(.borderedProminent)
                .disabled(email.isEmpty || password.isEmpty)
        }
        .padding()
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                Spacer()
                Button("Done") { field = nil }
            }
        }
    }

    func validate() {
        if !email.contains("@") {
            emailError = "Enter a valid email address"
            withAnimation(.spring(response: 0.1, dampingFraction: 0.2)) { shake = true }
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) { shake = false }
        } else {
            emailError = nil
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `@FocusState` enum + `.submitLabel(.next)` for keyboard-driven field navigation
- Show validation errors below the field with reserved space to avoid layout shift
- Shake invalid fields with a short, damped spring for visceral feedback
- Use `.ultraThinMaterial` behind the focused field to visually elevate it


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
