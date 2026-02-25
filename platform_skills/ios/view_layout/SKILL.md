---
name: IOS View layout
description: Rork-Max Quality skill for IOS View layout. Platform-native patterns and best practices for ios development.
---

# IOS View layout

Use stack views to lay out the views of your interface automatically. Use Auto Layout when you require precise placement of your views.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class AdaptiveLayoutController: UIViewController {
    private let contentView = UIView()

    override func viewDidLoad() {
        super.viewDidLoad()
        contentView.translatesAutoresizingMaskIntoConstraints = false
        contentView.backgroundColor = .secondarySystemBackground
        contentView.layer.cornerRadius = 16
        view.addSubview(contentView)

        NSLayoutConstraint.activate([
            contentView.leadingAnchor.constraint(equalTo: view.layoutMarginsGuide.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: view.layoutMarginsGuide.trailingAnchor),
            contentView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16),
            contentView.heightAnchor.constraint(greaterThanOrEqualToConstant: 100),
        ])
    }

    override func traitCollectionDidChange(_ previous: UITraitCollection?) {
        super.traitCollectionDidChange(previous)
        if traitCollection.horizontalSizeClass == .compact {
            // Adjust for narrow layout
        }
    }
}
```

## 💎 Elite Implementation Tips

- Always use `safeAreaLayoutGuide` and `layoutMarginsGuide` instead of hard-coded insets
- Use `UITraitCollection` to adapt layouts for size classes, Dynamic Type, and appearance
- Prefer `UICollectionViewCompositionalLayout` over manual Auto Layout for complex lists

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
