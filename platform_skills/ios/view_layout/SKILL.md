---
name: IOS View layout
description: Rork-Max Quality skill for IOS View layout. Platform-native patterns and best practices for ios development.
---

# IOS View layout

Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class RorkViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .systemBackground

        let label = UILabel()
        label.text = "View layout"
        label.font = .preferredFont(forTextStyle: .largeTitle)
        label.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(label)

        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }
}
```

## 💎 Elite Implementation Tips

- Follow the IOS Human Interface Guidelines for native feel.
- Use system-standard UIKit components before building custom ones.
- Support Dynamic Type and accessibility features from the start.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Building native iOS/iPadOS features using UIKit APIs
- Implementing UIKit-specific interactions not available in SwiftUI
- Working with view controllers, navigation controllers, and UIKit lifecycle

## Best Practices

- Use SwiftUI for new views and bridge UIKit only when necessary
- Adopt modern UIKit APIs: `UICollectionViewCompositionalLayout`, diffable data sources
- Handle all size classes and trait changes for iPhone and iPad adaptivity

## Common Pitfalls

- Mixing UIKit autolayout and SwiftUI layout can cause constraint conflicts
- Forgetting to test on iPad — multitasking changes your window size
- Not adopting the UIKit scene lifecycle for multi-window support

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `UIStackView` | A streamlined interface for laying out a collection of views in either a column or a row. |

### Constraints

| API | Purpose |
|-----|---------|
| `Positioning content within layout margins` | Position views so that they aren’t crowded by other content. |
| `Positioning content relative to the safe area` | Position views so that they aren’t obstructed by other content. |
| `NSLayoutConstraint` | The relationship between two user interface objects that must be satisfied by the constraint-based layout system. |
| `UILayoutSupport` | A set of methods that provide layout support and access to layout anchors. |
| `NSDictionaryOfVariableBindings` | Creates a dictionary wherein the keys are string representations of the corresponding values’ variable names. |

### Layout guides

| API | Purpose |
|-----|---------|
| `UILayoutGuide` | A rectangular area that can interact with Auto Layout. |
| `NSLayoutDimension` | A factory class for creating size-based layout constraint objects using a fluent API. |

### Anchors

| API | Purpose |
|-----|---------|
| `NSLayoutAnchor` | A factory class for creating layout constraint objects using a fluent API. |
| `NSLayoutXAxisAnchor` | A factory class for creating horizontal layout constraint objects using a fluent API. |
| `NSLayoutYAxisAnchor` | A factory class for creating vertical layout constraint objects using a fluent API. |

### Anchors

| API | Purpose |
|-----|---------|
| `NSLayoutAnchor` | A factory class for creating layout constraint objects using a fluent API. |
| `NSLayoutXAxisAnchor` | A factory class for creating horizontal layout constraint objects using a fluent API. |
| `NSLayoutYAxisAnchor` | A factory class for creating vertical layout constraint objects using a fluent API. |
| `NSLAYOUTANCHOR_H` | — |
