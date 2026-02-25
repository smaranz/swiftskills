---
name: View fundamentals
description: Rork-Max Quality skill for View fundamentals. Actionable patterns and best practices for SwiftUI development.
---

# View fundamentals

Define the visual elements of your app using a hierarchy of views.
Views are the building blocks that you use to declare your app’s user interface.
Each view contains a description of what to display for a given state.
Every bit of your app that’s visible to the user derives from the description
in a view, and any type that conforms to the `View` protocol can act as a
view in your app.
Compose a custom view by combining built-in views that SwiftUI provides with
other custom views that you create in your view’s `body`
computed property. Configure views using the view modifiers that SwiftUI
provides, or by defining your own view modifiers using the
`ViewModifier` protocol and the `modifier(_:)` method.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct RorkCardView: View {
    let title: String
    let subtitle: String

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.headline)
            Text(subtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16, style: .continuous))
        .shadow(color: .black.opacity(0.08), radius: 12, y: 6)
    }
}
```

## 💎 Elite Implementation Tips

- Extract reusable views into separate structs to keep `body` under ~30 lines
- Use `@ViewBuilder` for conditional content in custom container views
- Prefer composition (small views combined) over massive single-view bodies

## When to Use

- Creating reusable UI components with customizable appearance
- Applying consistent styling across an app using view modifiers
- Configuring view behavior like disabled state, tint, and redaction
- Building design-system components (buttons, cards, badges) with custom styles

## Best Practices

- Extract reusable view modifiers instead of duplicating modifier chains
- Use `ViewModifier` protocol for complex, reusable modifier bundles
- Prefer `.foregroundStyle()` over `.foregroundColor()` for hierarchical tinting
- Apply `.compositingGroup()` before opacity to treat a view subtree as one layer

## Common Pitfalls

- Modifier order matters — `.padding().background()` differs from `.background().padding()`
- Creating views that are too large — break them into smaller extracted views
- Using `AnyView` for type erasure when `@ViewBuilder` or generics work better

## Key APIs

### Creating a view

| API | Purpose |
|-----|---------|
| `Declaring a custom view` | Define views and assemble them into a view hierarchy. |
| `View` | A type that represents part of your app’s user interface and provides |
| `ViewBuilder` | A custom parameter attribute that constructs views from closures. |

### Modifying a view

| API | Purpose |
|-----|---------|
| `Configuring views` | Adjust the characteristics of a view by applying view modifiers. |
| `Reducing view modifier maintenance` | Bundle view modifiers that you regularly reuse into a custom view modifier. |
| `modifier(_:)` | Applies a modifier to a view and returns a new view. |
| `ViewModifier` | A modifier that you apply to a view or another view modifier, producing a |
| `EmptyModifier` | An empty, or identity, modifier, used during development to switch |
| `ModifiedContent` | A value with a modifier applied to it. |
| `EnvironmentalModifier` | A modifier that must resolve to a concrete modifier in an environment before |
| `ManipulableModifier` | — |

### Responding to view life cycle updates

| API | Purpose |
|-----|---------|
| `onAppear(perform:)` | Adds an action to perform before this view appears. |
| `onDisappear(perform:)` | Adds an action to perform after this view disappears. |

### Managing the view hierarchy

| API | Purpose |
|-----|---------|
| `id(_:)` | Binds a view’s identity to the given proxy value. |
| `tag(_:includeOptional:)` | Sets the unique tag value of this view. |
| `equatable()` | Prevents the view from updating its child view when its new value is the |

### Supporting view types

| API | Purpose |
|-----|---------|
| `AnyView` | A type-erased view. |
| `EmptyView` | A view that doesn’t contain any content. |
| `EquatableView` | A view type that compares itself against its previous value and prevents its |
| `SubscriptionView` | A view that subscribes to a publisher with an action. |
| `TupleView` | A View created from a swift tuple of View values. |
