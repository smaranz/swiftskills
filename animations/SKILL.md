---
name: Animations
description: Apple SwiftUI Documentation for Animations.
---

# Animations

Create smooth visual updates in response to state changes.

## Overview

You tell SwiftUI how to draw your app’s user interface for different states,
and then rely on SwiftUI to make interface updates when the state changes.

![](images/com.apple.SwiftUI/animations-hero@2x.png)

To avoid abrupt visual transitions when the state changes, add animation in
one of the following ways:

- Animate all of the visual changes for a state change by changing
  the state inside a call to the ``doc://com.apple.SwiftUI/documentation/SwiftUI/withAnimation(_:_:)`` global function.
- Add animation to a particular view when a specific value changes by applying
  the ``doc://com.apple.SwiftUI/documentation/SwiftUI/View/animation(_:value:)`` view modifier to the view.
- Animate changes to a ``doc://com.apple.SwiftUI/documentation/SwiftUI/Binding`` by using the binding’s
  ``doc://com.apple.SwiftUI/documentation/SwiftUI/Binding/animation(_:)`` method.

SwiftUI animates the effects that many built-in view modifiers produce,
like those that set a scale or opacity value. You can animate other values
by making your custom views conform to the [`Animatable`](/documentation/SwiftUI/Animatable) protocol, and
telling SwiftUI about the value you want to animate.

When an animated state change results in adding or removing a view to or from
the view hierarchy, you can tell SwiftUI how to transition the view into or out
of place using built-in transitions that [`AnyTransition`](/documentation/SwiftUI/AnyTransition) defines, like
[`slide`](/documentation/SwiftUI/AnyTransition/slide) or [`scale`](/documentation/SwiftUI/AnyTransition/scale). You can also
create custom transitions.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/motion>
in the Human Interface Guidelines.

## Topics

### Adding state-based animation to an action

[`withAnimation(_:_:)`](/documentation/SwiftUI/withAnimation(_:_:))

Returns the result of recomputing the view’s body with the provided
animation.

[`withAnimation(_:completionCriteria:_:completion:)`](/documentation/SwiftUI/withAnimation(_:completionCriteria:_:completion:))

Returns the result of recomputing the view’s body with the provided
animation, and runs the completion when all animations are complete.

[`AnimationCompletionCriteria`](/documentation/SwiftUI/AnimationCompletionCriteria)

The criteria that determines when an animation is considered finished.

[`Animation`](/documentation/SwiftUI/Animation)

The way a view changes over time to create a smooth visual transition from
one state to another.

### Adding state-based animation to a view

[`animation(_:)`](/documentation/SwiftUI/View/animation(_:))

Applies the given animation to this view when this view changes.

[`animation(_:value:)`](/documentation/SwiftUI/View/animation(_:value:))

Applies the given animation to this view when the specified value
changes.

[`animation(_:body:)`](/documentation/SwiftUI/View/animation(_:body:))

Applies the given animation to all animatable values within the `body`
closure.

### Creating phase-based animation

[Controlling the timing and movements of your animations](/documentation/SwiftUI/Controlling-the-timing-and-movements-of-your-animations)

Build sophisticated animations that you control using phase and keyframe
animators.

[`phaseAnimator(_:content:animation:)`](/documentation/SwiftUI/View/phaseAnimator(_:content:animation:))

Animates effects that you apply to a view over a sequence of phases
that change continuously.

[`phaseAnimator(_:trigger:content:animation:)`](/documentation/SwiftUI/View/phaseAnimator(_:trigger:content:animation:))

Animates effects that you apply to a view over a sequence of phases
that change based on a trigger.

[`PhaseAnimator`](/documentation/SwiftUI/PhaseAnimator)

A container that animates its content by automatically cycling through
a collection of phases that you provide, each defining a discrete step
within an animation.

### Creating keyframe-based animation

[`keyframeAnimator(initialValue:repeating:content:keyframes:)`](/documentation/SwiftUI/View/keyframeAnimator(initialValue:repeating:content:keyframes:))

Loops the given keyframes continuously, updating
the view using the modifiers you apply in `body`.

[`keyframeAnimator(initialValue:trigger:content:keyframes:)`](/documentation/SwiftUI/View/keyframeAnimator(initialValue:trigger:content:keyframes:))

Plays the given keyframes when the given trigger value changes, updating
the view using the modifiers you apply in `body`.

[`KeyframeAnimator`](/documentation/SwiftUI/KeyframeAnimator)

A container that animates its content with keyframes.

[`Keyframes`](/documentation/SwiftUI/Keyframes)

A type that defines changes to a value over time.

[`KeyframeTimeline`](/documentation/SwiftUI/KeyframeTimeline)

A description of how a value changes over time, modeled using keyframes.

[`KeyframeTrack`](/documentation/SwiftUI/KeyframeTrack)

A sequence of keyframes animating a single property of a root type.

[`KeyframeTrackContentBuilder`](/documentation/SwiftUI/KeyframeTrackContentBuilder)

The builder that creates keyframe track content from the keyframes
that you define within a closure.

[`KeyframesBuilder`](/documentation/SwiftUI/KeyframesBuilder)

A builder that combines keyframe content values into a single value.

[`KeyframeTrackContent`](/documentation/SwiftUI/KeyframeTrackContent)

A group of keyframes that define an interpolation curve of an animatable
value.

[`CubicKeyframe`](/documentation/SwiftUI/CubicKeyframe)

A keyframe that uses a cubic curve to smoothly interpolate between values.

[`LinearKeyframe`](/documentation/SwiftUI/LinearKeyframe)

A keyframe that uses simple linear interpolation.

[`MoveKeyframe`](/documentation/SwiftUI/MoveKeyframe)

A keyframe that immediately moves to the given value without interpolating.

[`SpringKeyframe`](/documentation/SwiftUI/SpringKeyframe)

A keyframe that uses a spring function to interpolate to the given value.

### Creating custom animations

[`CustomAnimation`](/documentation/SwiftUI/CustomAnimation)

A type that defines how an animatable value changes over time.

[`AnimationContext`](/documentation/SwiftUI/AnimationContext)

Contextual values that a custom animation can use to manage state and
access a view’s environment.

[`AnimationState`](/documentation/SwiftUI/AnimationState)

A container that stores the state for a custom animation.

[`AnimationStateKey`](/documentation/SwiftUI/AnimationStateKey)

A key for accessing animation state values.

[`UnitCurve`](/documentation/SwiftUI/UnitCurve)

A  function defined by a two-dimensional curve that maps an input
progress in the range [0,1] to an output progress that is also in the
range [0,1]. By changing the shape of the curve, the effective speed
of an animation or other interpolation can be changed.

[`Spring`](/documentation/SwiftUI/Spring)

A representation of a spring’s motion.

### Making data animatable

[`Animatable`](/documentation/SwiftUI/Animatable)

A type that describes how to animate a property of a view.

[`AnimatableValues`](/documentation/SwiftUI/AnimatableValues)

[`AnimatablePair`](/documentation/SwiftUI/AnimatablePair)

A pair of animatable values, which is itself animatable.

[`VectorArithmetic`](/documentation/SwiftUI/VectorArithmetic)

A type that can serve as the animatable data of an animatable type.

[`EmptyAnimatableData`](/documentation/SwiftUI/EmptyAnimatableData)

An empty type for animatable data.

### Updating a view on a schedule

  <doc://com.apple.documentation/documentation/watchOS-Apps/updating-watchos-apps-with-timelines>

[`TimelineView`](/documentation/SwiftUI/TimelineView)

A view that updates according to a schedule that you provide.

[`TimelineSchedule`](/documentation/SwiftUI/TimelineSchedule)

A type that provides a sequence of dates for use as a schedule.

[`TimelineViewDefaultContext`](/documentation/SwiftUI/TimelineViewDefaultContext)

Information passed to a timeline view’s content callback.

### Synchronizing geometries

[`matchedGeometryEffect(id:in:properties:anchor:isSource:)`](/documentation/SwiftUI/View/matchedGeometryEffect(id:in:properties:anchor:isSource:))

Defines a group of views with synchronized geometry using an
identifier and namespace that you provide.

[`MatchedGeometryProperties`](/documentation/SwiftUI/MatchedGeometryProperties)

A set of view properties that may be synchronized between views
using the `View.matchedGeometryEffect()` function.

[`GeometryEffect`](/documentation/SwiftUI/GeometryEffect)

An effect that changes the visual appearance of a view, largely without
changing its ancestors or descendants.

[`Namespace`](/documentation/SwiftUI/Namespace)

A dynamic property type that allows access to a namespace defined
by the persistent identity of the object containing the property
(e.g. a view).

[`geometryGroup()`](/documentation/SwiftUI/View/geometryGroup())

Isolates the geometry (e.g. position and size) of the view
from its parent view.

### Defining transitions

[`transition(_:)`](/documentation/SwiftUI/View/transition(_:))

Associates a transition with the view.

[`Transition`](/documentation/SwiftUI/Transition)

A description of view changes to apply when a view is added to and removed
from the view hierarchy.

[`TransitionProperties`](/documentation/SwiftUI/TransitionProperties)

The properties a `Transition` can have.

[`TransitionPhase`](/documentation/SwiftUI/TransitionPhase)

An indication of which the current stage of a transition.

[`AsymmetricTransition`](/documentation/SwiftUI/AsymmetricTransition)

A composite `Transition` that uses a different transition for
insertion versus removal.

[`AnyTransition`](/documentation/SwiftUI/AnyTransition)

A type-erased transition.

[`contentTransition(_:)`](/documentation/SwiftUI/View/contentTransition(_:))

Modifies the view to use a given transition as its method of animating
changes to the contents of its views.

[`contentTransition`](/documentation/SwiftUI/EnvironmentValues/contentTransition)

The current method of animating the contents of views.

[`contentTransitionAddsDrawingGroup`](/documentation/SwiftUI/EnvironmentValues/contentTransitionAddsDrawingGroup)

A Boolean value that controls whether views that render content
transitions use GPU-accelerated rendering.

[`ContentTransition`](/documentation/SwiftUI/ContentTransition)

A kind of transition that applies to the content within a single view,
rather than to the insertion or removal of a view.

[`PlaceholderContentView`](/documentation/SwiftUI/PlaceholderContentView)

A placeholder used to construct an inline modifier, transition, or other
helper type.

[`navigationTransition(_:)`](/documentation/SwiftUI/View/navigationTransition(_:))

Sets the navigation transition style for this view.

[`NavigationTransition`](/documentation/SwiftUI/NavigationTransition)

A type that defines the transition to use when navigating to a view.

[`matchedTransitionSource(id:in:)`](/documentation/SwiftUI/View/matchedTransitionSource(id:in:))

Identifies this view as the source of a navigation transition, such
as a zoom transition.

[`matchedTransitionSource(id:in:configuration:)`](/documentation/SwiftUI/View/matchedTransitionSource(id:in:configuration:))

Identifies this view as the source of a navigation transition, such
as a zoom transition.

[`MatchedTransitionSourceConfiguration`](/documentation/SwiftUI/MatchedTransitionSourceConfiguration)

A configuration that defines the appearance of a matched transition
source.

[`EmptyMatchedTransitionSourceConfiguration`](/documentation/SwiftUI/EmptyMatchedTransitionSourceConfiguration)

An unstyled matched transition source configuration.

### Moving an animation to another view

[`withTransaction(_:_:)`](/documentation/SwiftUI/withTransaction(_:_:))

Executes a closure with the specified transaction and returns the result.

[`withTransaction(_:_:_:)`](/documentation/SwiftUI/withTransaction(_:_:_:))

Executes a closure with the specified transaction key path and value and
returns the result.

[`transaction(_:)`](/documentation/SwiftUI/View/transaction(_:))

Applies the given transaction mutation function to all animations used
within the view.

[`transaction(value:_:)`](/documentation/SwiftUI/View/transaction(value:_:))

Applies the given transaction mutation function to all animations used
within the view.

[`transaction(_:body:)`](/documentation/SwiftUI/View/transaction(_:body:))

Applies the given transaction mutation function to all animations used
within the `body` closure.

[`Transaction`](/documentation/SwiftUI/Transaction)

The context of the current state-processing update.

[`Entry()`](/documentation/SwiftUI/Entry())

Creates an environment values, transaction, container values,
or focused values entry.

[`TransactionKey`](/documentation/SwiftUI/TransactionKey)

A key for accessing values in a transaction.

### Deprecated types

[`AnimatableModifier`](/documentation/SwiftUI/AnimatableModifier)

A modifier that can create another modifier with animation.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
