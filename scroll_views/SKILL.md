---
name: Scroll views
description: Apple SwiftUI Documentation for Scroll views.
---

# Scroll views

Enable people to scroll to content that doesn’t fit in the current display.

## Overview

When the content of a view doesn’t fit in the display, you can wrap the view
in a [`ScrollView`](/documentation/SwiftUI/ScrollView) to enable people to scroll on one or more axes.
Configure the scroll view using view modifiers. For example, you can set the
visibility of the scroll indicators or the availability of scrolling in a given
dimension.

![](images/com.apple.SwiftUI/scroll-views-hero@2x.png)

You can put any view type in a scroll view, but you most often use a scroll
view for a layout container with too many elements to fit in the display.
For some container views that you put in a scroll view, like lazy stacks,
the container doesn’t load views until they are visible or almost visible.
For others, like regular stacks and grids, the container loads the
content all at once, regardless of the state of scrolling.

[Lists](/documentation/SwiftUI/Lists) and [Tables](/documentation/SwiftUI/Tables) implicitly include a scroll view, so you don’t
need to add scrolling to those container types. However, you can configure
their implicit scroll views with the same view modifiers that apply to
explicit scroll views.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/scroll-views>
in the Human Interface Guidelines.

## Topics

### Creating a scroll view

[`ScrollView`](/documentation/SwiftUI/ScrollView)

A scrollable view.

[`ScrollViewReader`](/documentation/SwiftUI/ScrollViewReader)

A view that provides programmatic scrolling, by working with a proxy
to scroll to known child views.

[`ScrollViewProxy`](/documentation/SwiftUI/ScrollViewProxy)

A proxy value that supports programmatic scrolling of the scrollable
views within a view hierarchy.

### Managing scroll position

[`scrollPosition(_:anchor:)`](/documentation/SwiftUI/View/scrollPosition(_:anchor:))

Associates a binding to a scroll position with a scroll view within this
view.

[`scrollPosition(id:anchor:)`](/documentation/SwiftUI/View/scrollPosition(id:anchor:))

Associates a binding to be updated when a scroll view within this
view scrolls.

[`defaultScrollAnchor(_:)`](/documentation/SwiftUI/View/defaultScrollAnchor(_:))

Associates an anchor to control which part of the scroll view’s
content should be rendered by default.

[`defaultScrollAnchor(_:for:)`](/documentation/SwiftUI/View/defaultScrollAnchor(_:for:))

Associates an anchor to control the position of a scroll view in a
particular circumstance.

[`ScrollAnchorRole`](/documentation/SwiftUI/ScrollAnchorRole)

A type defining the role of a scroll anchor.

[`ScrollPosition`](/documentation/SwiftUI/ScrollPosition)

A type that defines the semantic position of where a scroll view is
scrolled within its content.

### Defining scroll targets

[`scrollTargetBehavior(_:)`](/documentation/SwiftUI/View/scrollTargetBehavior(_:))

Sets the scroll behavior of views scrollable in the provided axes.

[`scrollTargetLayout(isEnabled:)`](/documentation/SwiftUI/View/scrollTargetLayout(isEnabled:))

Configures the outermost layout as a scroll target layout.

[`ScrollTarget`](/documentation/SwiftUI/ScrollTarget)

A type defining the target in which a scroll view should try and scroll to.

[`ScrollTargetBehavior`](/documentation/SwiftUI/ScrollTargetBehavior)

A type that defines the scroll behavior of a scrollable view.

[`ScrollTargetBehaviorContext`](/documentation/SwiftUI/ScrollTargetBehaviorContext)

The context in which a scroll target behavior updates its scroll target.

[`PagingScrollTargetBehavior`](/documentation/SwiftUI/PagingScrollTargetBehavior)

The scroll behavior that aligns scroll targets to container-based geometry.

[`ViewAlignedScrollTargetBehavior`](/documentation/SwiftUI/ViewAlignedScrollTargetBehavior)

The scroll behavior that aligns scroll targets to view-based geometry.

[`AnyScrollTargetBehavior`](/documentation/SwiftUI/AnyScrollTargetBehavior)

A type-erased scroll target behavior.

[`ScrollTargetBehaviorProperties`](/documentation/SwiftUI/ScrollTargetBehaviorProperties)

Properties influencing the scroll view a scroll target behavior
applies to.

[`ScrollTargetBehaviorPropertiesContext`](/documentation/SwiftUI/ScrollTargetBehaviorPropertiesContext)

The context in which a scroll target behavior can decide its properties.

### Animating scroll transitions

[`scrollTransition(_:axis:transition:)`](/documentation/SwiftUI/View/scrollTransition(_:axis:transition:))

Applies the given transition, animating between the phases
of the transition as this view appears and disappears within the
visible region of the containing scroll view.

[`scrollTransition(topLeading:bottomTrailing:axis:transition:)`](/documentation/SwiftUI/View/scrollTransition(topLeading:bottomTrailing:axis:transition:))

Applies the given transition, animating between the phases
of the transition as this view appears and disappears within the
visible region of the containing scroll view.

[`ScrollTransitionPhase`](/documentation/SwiftUI/ScrollTransitionPhase)

The phases that a view transitions between when it scrolls among other views.

[`ScrollTransitionConfiguration`](/documentation/SwiftUI/ScrollTransitionConfiguration)

The configuration of a scroll transition that controls how a transition
is applied as a view is scrolled through the visible region of a containing
scroll view or other container.

### Responding to scroll view changes

[`onScrollGeometryChange(for:of:action:)`](/documentation/SwiftUI/View/onScrollGeometryChange(for:of:action:))

Adds an action to be performed when a value, created from a
scroll geometry, changes.

[`onScrollTargetVisibilityChange(idType:threshold:_:)`](/documentation/SwiftUI/View/onScrollTargetVisibilityChange(idType:threshold:_:))

Adds an action to be called with information about what views would
be considered visible.

[`onScrollVisibilityChange(threshold:_:)`](/documentation/SwiftUI/View/onScrollVisibilityChange(threshold:_:))

Adds an action to be called when the view crosses the threshold to be considered on/off screen.

[`onScrollPhaseChange(_:)`](/documentation/SwiftUI/View/onScrollPhaseChange(_:))

Adds an action to perform when the scroll phase of the first scroll
view in the hierarchy changes.

[`ScrollGeometry`](/documentation/SwiftUI/ScrollGeometry)

A type that defines the geometry of a scroll view.

[`ScrollPhase`](/documentation/SwiftUI/ScrollPhase)

A type that describes the state of a scroll gesture of a
scrollable view like a scroll view.

[`ScrollPhaseChangeContext`](/documentation/SwiftUI/ScrollPhaseChangeContext)

A type that provides you with more content when the phase of a scroll
view changes.

### Showing scroll indicators

[`scrollIndicatorsFlash(onAppear:)`](/documentation/SwiftUI/View/scrollIndicatorsFlash(onAppear:))

Flashes the scroll indicators of a scrollable view when it appears.

[`scrollIndicatorsFlash(trigger:)`](/documentation/SwiftUI/View/scrollIndicatorsFlash(trigger:))

Flashes the scroll indicators of scrollable views when a value changes.

[`scrollIndicators(_:axes:)`](/documentation/SwiftUI/View/scrollIndicators(_:axes:))

Sets the visibility of scroll indicators within this view.

[`horizontalScrollIndicatorVisibility`](/documentation/SwiftUI/EnvironmentValues/horizontalScrollIndicatorVisibility)

The visibility to apply to scroll indicators of any
horizontally scrollable content.

[`verticalScrollIndicatorVisibility`](/documentation/SwiftUI/EnvironmentValues/verticalScrollIndicatorVisibility)

The visiblity to apply to scroll indicators of any
vertically scrollable content.

[`ScrollIndicatorVisibility`](/documentation/SwiftUI/ScrollIndicatorVisibility)

The visibility of scroll indicators of a UI element.

### Managing content visibility

[`scrollContentBackground(_:)`](/documentation/SwiftUI/View/scrollContentBackground(_:))

Specifies the visibility of the background for scrollable views within
this view.

[`scrollClipDisabled(_:)`](/documentation/SwiftUI/View/scrollClipDisabled(_:))

Sets whether a scroll view clips its content to its bounds.

[`ScrollContentOffsetAdjustmentBehavior`](/documentation/SwiftUI/ScrollContentOffsetAdjustmentBehavior)

A type that defines the different kinds of content offset adjusting
behaviors a scroll view can have.

### Disabling scrolling

[`scrollDisabled(_:)`](/documentation/SwiftUI/View/scrollDisabled(_:))

Disables or enables scrolling in scrollable views.

[`isScrollEnabled`](/documentation/SwiftUI/EnvironmentValues/isScrollEnabled)

A Boolean value that indicates whether any scroll views associated
with this environment allow scrolling to occur.

### Configuring scroll bounce behavior

[`scrollBounceBehavior(_:axes:)`](/documentation/SwiftUI/View/scrollBounceBehavior(_:axes:))

Configures the bounce behavior of scrollable views along the specified
axis.

[`horizontalScrollBounceBehavior`](/documentation/SwiftUI/EnvironmentValues/horizontalScrollBounceBehavior)

The scroll bounce mode for the horizontal axis of scrollable views.

[`verticalScrollBounceBehavior`](/documentation/SwiftUI/EnvironmentValues/verticalScrollBounceBehavior)

The scroll bounce mode for the vertical axis of scrollable views.

[`ScrollBounceBehavior`](/documentation/SwiftUI/ScrollBounceBehavior)

The ways that a scrollable view can bounce when it reaches the end of its
content.

### Configuring scroll edge effects

[`scrollEdgeEffectStyle(_:for:)`](/documentation/SwiftUI/View/scrollEdgeEffectStyle(_:for:))

Configures the scroll edge effect style for scroll views within this
hierarchy.

[`scrollEdgeEffectHidden(_:for:)`](/documentation/SwiftUI/View/scrollEdgeEffectHidden(_:for:))

Hides any scroll edge effects for scroll views within this
hierarchy.

[`ScrollEdgeEffectStyle`](/documentation/SwiftUI/ScrollEdgeEffectStyle)

A structure that defines the style of pocket a scroll view will have.

[`safeAreaBar(edge:alignment:spacing:content:)`](/documentation/SwiftUI/View/safeAreaBar(edge:alignment:spacing:content:))

Shows the specified content as a custom bar beside the modified view.

### Interacting with a software keyboard

[`scrollDismissesKeyboard(_:)`](/documentation/SwiftUI/View/scrollDismissesKeyboard(_:))

Configures the behavior in which scrollable content interacts with
the software keyboard.

[`scrollDismissesKeyboardMode`](/documentation/SwiftUI/EnvironmentValues/scrollDismissesKeyboardMode)

The way that scrollable content interacts with the software keyboard.

[`ScrollDismissesKeyboardMode`](/documentation/SwiftUI/ScrollDismissesKeyboardMode)

The ways that scrollable content can interact with the software keyboard.

### Managing scrolling for different inputs

[`scrollInputBehavior(_:for:)`](/documentation/SwiftUI/View/scrollInputBehavior(_:for:))

Enables or disables scrolling in scrollable views when using particular
inputs.

[`ScrollInputKind`](/documentation/SwiftUI/ScrollInputKind)

Inputs used to scroll views.

[`ScrollInputBehavior`](/documentation/SwiftUI/ScrollInputBehavior)

A type that defines whether input should scroll a view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
