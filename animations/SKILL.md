---
name: Animations
description: Rork-Max Quality skill for Animations. Actionable patterns and best practices for SwiftUI development.
---

# Animations

Create smooth visual updates in response to state changes.
You tell SwiftUI how to draw your app’s user interface for different states,
and then rely on SwiftUI to make interface updates when the state changes.
To avoid abrupt visual transitions when the state changes, add animation in
one of the following ways:
- Animate all of the visual changes for a state change by changing
the state inside a call to the `withAnimation(_:_:)` global function.
- Add animation to a particular view when a specific value changes by applying
the `animation(_:value:)` view modifier to the view.
- Animate changes to a `Binding` by using the binding’s
`animation(_:)` method.
SwiftUI animates the effects that many built-in view modifiers produce,
like those that set a scale or opacity value. You can animate other values
by making your custom views conform to the `Animatable` protocol, and
telling SwiftUI about the value you want to animate.
When an animated state change results in adding or removing a view to or from
the view hierarchy, you can tell SwiftUI how to transition the view into or out
of place using built-in transitions that `AnyTransition` defines, like
`slide` or `scale`. You can also
create custom transitions.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet


```swift
import SwiftUI

struct RorkPremiumAnimation: View {
    @State private var isAnimating = false
    
    var body: some View {
        VStack(spacing: 30) {
            // Glassmorphic Card with Spring Animation
            RoundedRectangle(cornerRadius: 25)
                .fill(.ultraThinMaterial)
                .frame(width: 300, height: 200)
                .overlay {
                    Text("Rork Max Quality")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                }
                .scaleEffect(isAnimating ? 1.05 : 1.0)
                .rotation3DEffect(
                    .degrees(isAnimating ? 5 : 0),
                    axis: (x: 1.0, y: 1.0, z: 0.0)
                )
                .shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)
            
            Button {
                withAnimation(.spring(response: 0.5, dampingFraction: 0.6, blendDuration: 0)) {
                    isAnimating.toggle()
                }
            } label: {
                Text("Animate")
                    .font(.headline)
                    .foregroundStyle(.white)
                    .padding()
                    .frame(width: 200)
                    .background(.blue, in: Capsule())
            }
        }
    }
}
```


## 💎 Elite Implementation Tips

- Use `.spring(response:dampingFraction:)` for all physical movement to feel native and premium.
- Combine `scaleEffect` with `shadow` updates to create a sense of 'lifting' off the screen.
- Leverage `.ultraThinMaterial` for glassmorphic elements rather than solid colors.


## When to Use

- Providing visual feedback when state changes (toggle, expand, select)
- Creating smooth transitions when views appear, disappear, or move
- Building custom loading indicators, progress animations, or onboarding sequences
- Adding hero transitions between navigation destinations with matched geometry

## Best Practices

- Use `.spring(response:dampingFraction:)` for all interactive motion — it feels native
- Prefer `withAnimation` for explicit state-driven animations over implicit `.animation()`
- Use `PhaseAnimator` for multi-step sequential animations (iOS 17+)
- Test with Reduce Motion enabled — provide `UIAccessibility.isReduceMotionEnabled` fallbacks
- Keep durations under 0.4s for responsive UI; longer only for decorative animations

## Common Pitfalls

- Using `.animation(_:)` without a `value:` parameter — deprecated and causes unpredictable animations
- Animating too many properties simultaneously degrades performance
- Matched geometry effects break when the namespace isn't shared correctly across views
- Forgetting `.geometryGroup()` when child animations fight parent layout changes

## Key APIs

### Adding state-based animation to an action

| API | Purpose |
|-----|---------|
| `withAnimation(_:_:)` | Returns the result of recomputing the view’s body with the provided |
| `withAnimation(_:completionCriteria:_:completion:)` | Returns the result of recomputing the view’s body with the provided |
| `AnimationCompletionCriteria` | The criteria that determines when an animation is considered finished. |
| `Animation` | The way a view changes over time to create a smooth visual transition from |

### Adding state-based animation to a view

| API | Purpose |
|-----|---------|
| `animation(_:)` | Applies the given animation to this view when this view changes. |
| `animation(_:value:)` | Applies the given animation to this view when the specified value |
| `animation(_:body:)` | Applies the given animation to all animatable values within the `body` |

### Creating phase-based animation

| API | Purpose |
|-----|---------|
| `Controlling the timing and movements of your animations` | Build sophisticated animations that you control using phase and keyframe |
| `phaseAnimator(_:content:animation:)` | Animates effects that you apply to a view over a sequence of phases |
| `phaseAnimator(_:trigger:content:animation:)` | Animates effects that you apply to a view over a sequence of phases |
| `PhaseAnimator` | A container that animates its content by automatically cycling through |

### Creating keyframe-based animation

| API | Purpose |
|-----|---------|
| `keyframeAnimator(initialValue:repeating:content:keyframes:)` | Loops the given keyframes continuously, updating |
| `keyframeAnimator(initialValue:trigger:content:keyframes:)` | Plays the given keyframes when the given trigger value changes, updating |
| `KeyframeAnimator` | A container that animates its content with keyframes. |
| `Keyframes` | A type that defines changes to a value over time. |
| `KeyframeTimeline` | A description of how a value changes over time, modeled using keyframes. |
| `KeyframeTrack` | A sequence of keyframes animating a single property of a root type. |
| `KeyframeTrackContentBuilder` | The builder that creates keyframe track content from the keyframes |
| `KeyframesBuilder` | A builder that combines keyframe content values into a single value. |

### Creating custom animations

| API | Purpose |
|-----|---------|
| `CustomAnimation` | A type that defines how an animatable value changes over time. |
| `AnimationContext` | Contextual values that a custom animation can use to manage state and |
| `AnimationState` | A container that stores the state for a custom animation. |
| `AnimationStateKey` | A key for accessing animation state values. |
| `UnitCurve` | A  function defined by a two-dimensional curve that maps an input |
| `Spring` | A representation of a spring’s motion. |

### Making data animatable

| API | Purpose |
|-----|---------|
| `Animatable` | A type that describes how to animate a property of a view. |
| `AnimatableValues` | — |
| `AnimatablePair` | A pair of animatable values, which is itself animatable. |
| `VectorArithmetic` | A type that can serve as the animatable data of an animatable type. |
| `EmptyAnimatableData` | An empty type for animatable data. |

### Updating a view on a schedule

| API | Purpose |
|-----|---------|
| `TimelineView` | A view that updates according to a schedule that you provide. |
| `TimelineSchedule` | A type that provides a sequence of dates for use as a schedule. |
| `TimelineViewDefaultContext` | Information passed to a timeline view’s content callback. |

### Synchronizing geometries

| API | Purpose |
|-----|---------|
| `matchedGeometryEffect(id:in:properties:anchor:isSource:)` | Defines a group of views with synchronized geometry using an |
| `MatchedGeometryProperties` | A set of view properties that may be synchronized between views |
| `GeometryEffect` | An effect that changes the visual appearance of a view, largely without |
| `Namespace` | A dynamic property type that allows access to a namespace defined |
| `geometryGroup()` | Isolates the geometry (e.g. position and size) of the view |

### Defining transitions

| API | Purpose |
|-----|---------|
| `transition(_:)` | Associates a transition with the view. |
| `Transition` | A description of view changes to apply when a view is added to and removed |
| `TransitionProperties` | The properties a `Transition` can have. |
| `TransitionPhase` | An indication of which the current stage of a transition. |
| `AsymmetricTransition` | A composite `Transition` that uses a different transition for |
| `AnyTransition` | A type-erased transition. |
| `contentTransition(_:)` | Modifies the view to use a given transition as its method of animating |
| `contentTransition` | The current method of animating the contents of views. |

### Moving an animation to another view

| API | Purpose |
|-----|---------|
| `withTransaction(_:_:)` | Executes a closure with the specified transaction and returns the result. |
| `withTransaction(_:_:_:)` | Executes a closure with the specified transaction key path and value and |
| `transaction(_:)` | Applies the given transaction mutation function to all animations used |
| `transaction(value:_:)` | Applies the given transaction mutation function to all animations used |
| `transaction(_:body:)` | Applies the given transaction mutation function to all animations used |
| `Transaction` | The context of the current state-processing update. |
| `Entry()` | Creates an environment values, transaction, container values, |
| `TransactionKey` | A key for accessing values in a transaction. |

### Deprecated types

| API | Purpose |
|-----|---------|
| `AnimatableModifier` | A modifier that can create another modifier with animation. |
