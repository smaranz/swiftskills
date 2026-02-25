---
name: Scroll views
description: Rork-Max Quality skill for Scroll views. Actionable patterns and best practices for SwiftUI development.
---

# Scroll views

Enable people to scroll to content that doesn’t fit in the current display.
When the content of a view doesn’t fit in the display, you can wrap the view
in a `ScrollView` to enable people to scroll on one or more axes.
Configure the scroll view using view modifiers. For example, you can set the
visibility of the scroll indicators or the availability of scrolling in a given
dimension.
You can put any view type in a scroll view, but you most often use a scroll
view for a layout container with too many elements to fit in the display.
For some container views that you put in a scroll view, like lazy stacks,
the container doesn’t load views until they are visible or almost visible.
For others, like regular stacks and grids, the container loads the
content all at once, regardless of the state of scrolling.
Lists and Tables implicitly include a scroll view, so you don’t
need to add scrolling to those container types. However, you can configure
their implicit scroll views with the same view modifiers that apply to
explicit scroll views.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct HorizontalGallery: View {
    let items: [GalleryItem]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 16) {
                ForEach(items) { item in
                    VStack {
                        RoundedRectangle(cornerRadius: 16)
                            .fill(item.color.gradient)
                            .frame(width: 280, height: 180)
                        Text(item.title).font(.caption)
                    }
                    .scrollTransition { content, phase in
                        content
                            .opacity(phase.isIdentity ? 1 : 0.5)
                            .scaleEffect(phase.isIdentity ? 1 : 0.9)
                    }
                }
            }
            .scrollTargetLayout()
        }
        .scrollTargetBehavior(.viewAligned)
        .contentMargins(.horizontal, 20)
    }
}
```

## 💎 Elite Implementation Tips

- Use `.scrollTargetBehavior(.viewAligned)` with `.scrollTargetLayout()` for snap-to-item scrolling
- Apply `.scrollTransition` for per-item opacity/scale effects as items enter/exit
- Use `LazyVStack`/`LazyHStack` inside `ScrollView` — they only render visible items


## When to Use

- Arranging views in stacks, grids, or custom layout containers
- Building responsive layouts that adapt to different screen sizes
- Creating scrollable lists, tables, or collection-style interfaces
- Implementing custom layout algorithms with the `Layout` protocol

## Best Practices

- Use `LazyVStack`/`LazyHStack` inside `ScrollView` for large data sets
- Prefer `Grid` (iOS 16+) over nested stacks for tabular 2D layouts
- Use `ViewThatFits` to automatically choose between layout variants
- Apply `.frame(maxWidth: .infinity)` for full-width sections rather than hard-coding widths

## Common Pitfalls

- Putting `LazyVStack` without a `ScrollView` — it won't scroll
- Using `List` when you want custom styling — `LazyVStack` gives more control
- Nesting `ScrollView`s in the same axis causes confusing scroll behavior
- Forgetting `.listRowInsets(EdgeInsets())` when you want edge-to-edge list content

## Key APIs

### Creating a scroll view

| API | Purpose |
|-----|---------|
| `ScrollView` | A scrollable view. |
| `ScrollViewReader` | A view that provides programmatic scrolling, by working with a proxy |
| `ScrollViewProxy` | A proxy value that supports programmatic scrolling of the scrollable |

### Managing scroll position

| API | Purpose |
|-----|---------|
| `scrollPosition(_:anchor:)` | Associates a binding to a scroll position with a scroll view within this |
| `scrollPosition(id:anchor:)` | Associates a binding to be updated when a scroll view within this |
| `defaultScrollAnchor(_:)` | Associates an anchor to control which part of the scroll view’s |
| `defaultScrollAnchor(_:for:)` | Associates an anchor to control the position of a scroll view in a |
| `ScrollAnchorRole` | A type defining the role of a scroll anchor. |
| `ScrollPosition` | A type that defines the semantic position of where a scroll view is |

### Defining scroll targets

| API | Purpose |
|-----|---------|
| `scrollTargetBehavior(_:)` | Sets the scroll behavior of views scrollable in the provided axes. |
| `scrollTargetLayout(isEnabled:)` | Configures the outermost layout as a scroll target layout. |
| `ScrollTarget` | A type defining the target in which a scroll view should try and scroll to. |
| `ScrollTargetBehavior` | A type that defines the scroll behavior of a scrollable view. |
| `ScrollTargetBehaviorContext` | The context in which a scroll target behavior updates its scroll target. |
| `PagingScrollTargetBehavior` | The scroll behavior that aligns scroll targets to container-based geometry. |
| `ViewAlignedScrollTargetBehavior` | The scroll behavior that aligns scroll targets to view-based geometry. |
| `AnyScrollTargetBehavior` | A type-erased scroll target behavior. |

### Animating scroll transitions

| API | Purpose |
|-----|---------|
| `scrollTransition(_:axis:transition:)` | Applies the given transition, animating between the phases |
| `scrollTransition(topLeading:bottomTrailing:axis:transition:)` | Applies the given transition, animating between the phases |
| `ScrollTransitionPhase` | The phases that a view transitions between when it scrolls among other views. |
| `ScrollTransitionConfiguration` | The configuration of a scroll transition that controls how a transition |

### Responding to scroll view changes

| API | Purpose |
|-----|---------|
| `onScrollGeometryChange(for:of:action:)` | Adds an action to be performed when a value, created from a |
| `onScrollTargetVisibilityChange(idType:threshold:_:)` | Adds an action to be called with information about what views would |
| `onScrollVisibilityChange(threshold:_:)` | Adds an action to be called when the view crosses the threshold to be considered on/off screen. |
| `onScrollPhaseChange(_:)` | Adds an action to perform when the scroll phase of the first scroll |
| `ScrollGeometry` | A type that defines the geometry of a scroll view. |
| `ScrollPhase` | A type that describes the state of a scroll gesture of a |
| `ScrollPhaseChangeContext` | A type that provides you with more content when the phase of a scroll |

### Showing scroll indicators

| API | Purpose |
|-----|---------|
| `scrollIndicatorsFlash(onAppear:)` | Flashes the scroll indicators of a scrollable view when it appears. |
| `scrollIndicatorsFlash(trigger:)` | Flashes the scroll indicators of scrollable views when a value changes. |
| `scrollIndicators(_:axes:)` | Sets the visibility of scroll indicators within this view. |
| `horizontalScrollIndicatorVisibility` | The visibility to apply to scroll indicators of any |
| `verticalScrollIndicatorVisibility` | The visiblity to apply to scroll indicators of any |
| `ScrollIndicatorVisibility` | The visibility of scroll indicators of a UI element. |

### Managing content visibility

| API | Purpose |
|-----|---------|
| `scrollContentBackground(_:)` | Specifies the visibility of the background for scrollable views within |
| `scrollClipDisabled(_:)` | Sets whether a scroll view clips its content to its bounds. |
| `ScrollContentOffsetAdjustmentBehavior` | A type that defines the different kinds of content offset adjusting |

### Disabling scrolling

| API | Purpose |
|-----|---------|
| `scrollDisabled(_:)` | Disables or enables scrolling in scrollable views. |
| `isScrollEnabled` | A Boolean value that indicates whether any scroll views associated |

### Configuring scroll bounce behavior

| API | Purpose |
|-----|---------|
| `scrollBounceBehavior(_:axes:)` | Configures the bounce behavior of scrollable views along the specified |
| `horizontalScrollBounceBehavior` | The scroll bounce mode for the horizontal axis of scrollable views. |
| `verticalScrollBounceBehavior` | The scroll bounce mode for the vertical axis of scrollable views. |
| `ScrollBounceBehavior` | The ways that a scrollable view can bounce when it reaches the end of its |

### Configuring scroll edge effects

| API | Purpose |
|-----|---------|
| `scrollEdgeEffectStyle(_:for:)` | Configures the scroll edge effect style for scroll views within this |
| `scrollEdgeEffectHidden(_:for:)` | Hides any scroll edge effects for scroll views within this |
| `ScrollEdgeEffectStyle` | A structure that defines the style of pocket a scroll view will have. |
| `safeAreaBar(edge:alignment:spacing:content:)` | Shows the specified content as a custom bar beside the modified view. |

### Interacting with a software keyboard

| API | Purpose |
|-----|---------|
| `scrollDismissesKeyboard(_:)` | Configures the behavior in which scrollable content interacts with |
| `scrollDismissesKeyboardMode` | The way that scrollable content interacts with the software keyboard. |
| `ScrollDismissesKeyboardMode` | The ways that scrollable content can interact with the software keyboard. |

### Managing scrolling for different inputs

| API | Purpose |
|-----|---------|
| `scrollInputBehavior(_:for:)` | Enables or disables scrolling in scrollable views when using particular |
| `ScrollInputKind` | Inputs used to scroll views. |
| `ScrollInputBehavior` | A type that defines whether input should scroll a view. |
