---
name: Focus
description: Rork-Max Quality skill for Focus. Actionable patterns and best practices for SwiftUI development.
---

# Focus

Identify and control which visible object responds to user interaction.
Focus indicates which element in the display receives the next input.
Use view modifiers to indicate which views can receive focus, to detect
which view has focus, and to programmatically control focus state.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## When to Use

- Managing keyboard focus in forms and text input flows
- Implementing tab-order or focus-based navigation (tvOS, macOS)
- Highlighting the currently focused element for accessibility

## Best Practices

- Use `@FocusState` with an enum to manage focus across multiple fields
- Add Next/Done buttons to keyboard toolbars for field-to-field navigation
- Programmatically dismiss the keyboard by setting `@FocusState` to `nil`

## Common Pitfalls

- Forgetting to set `@FocusState` to `nil` when the user submits a form
- Not handling hardware keyboard tab navigation on iPad

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Focus Cookbook: Supporting and enhancing focus-driven interactions in your SwiftUI app` | Create custom focusable views with key-press handlers that accelerate keyboard input and support movement, and control focus programmatically. |

### Indicating that a view can receive focus

| API | Purpose |
|-----|---------|
| `focusable(_:)` | Specifies if the view is focusable. |
| `focusable(_:interactions:)` | Specifies if the view is focusable, and if so, what focus-driven |
| `FocusInteractions` | Values describe different focus interactions that a view can support. |

### Managing focus state

| API | Purpose |
|-----|---------|
| `focused(_:equals:)` | Modifies this view by binding its focus state to the given state value. |
| `focused(_:)` | Modifies this view by binding its focus state to the given Boolean state |
| `isFocused` | Returns whether the nearest focusable ancestor has focus. |
| `FocusState` | A property wrapper type that can read and write a value that SwiftUI updates |
| `FocusedValue` | A property wrapper for observing values from the focused view or one of its |
| `Entry()` | Creates an environment values, transaction, container values, |
| `FocusedValueKey` | A protocol for identifier types used when publishing and observing focused |
| `FocusedBinding` | A convenience property wrapper for observing and automatically unwrapping |

### Exposing value types to focused views

| API | Purpose |
|-----|---------|
| `focusedValue(_:)` | Sets the focused value for the given object type. |
| `focusedValue(_:_:)` | Modifies this view by injecting a value that you provide for use by |
| `focusedSceneValue(_:)` | Sets the focused value for the given object type at a scene-wide scope. |
| `focusedSceneValue(_:_:)` | Modifies this view by injecting a value that you provide for use by |
| `FocusedValues` | A collection of state exported by the focused scene or view and its ancestors. |

### Exposing reference types to focused views

| API | Purpose |
|-----|---------|
| `focusedObject(_:)` | Creates a new view that exposes the provided object to other views whose |
| `focusedSceneObject(_:)` | Creates a new view that exposes the provided object to other views whose |
| `FocusedObject` | A property wrapper type for an observable object supplied by the focused |

### Setting focus scope

| API | Purpose |
|-----|---------|
| `focusScope(_:)` | Creates a focus scope that SwiftUI uses to limit default focus |
| `focusSection()` | Indicates that the view’s frame and cohort of focusable descendants |

### Controlling default focus

| API | Purpose |
|-----|---------|
| `prefersDefaultFocus(_:in:)` | Indicates that the view should receive focus by default for a given |
| `defaultFocus(_:_:priority:)` | Defines a region of the window in which default focus is evaluated by |
| `DefaultFocusEvaluationPriority` | Prioritizations for default focus preferences when evaluating where |

### Resetting focus

| API | Purpose |
|-----|---------|
| `resetFocus` | An action that requests the focus system to reevaluate default focus. |
| `ResetFocusAction` | An environment value that provides the ability to reevaluate default |

### Configuring effects

| API | Purpose |
|-----|---------|
| `focusEffectDisabled(_:)` | Adds a condition that controls whether this view can display focus |
| `isFocusEffectEnabled` | A Boolean value that indicates whether the view associated with this |
