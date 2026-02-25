---
name: IOS Views and controls
description: Rork-Max Quality skill for IOS Views and controls. Platform-native patterns and best practices for ios development.
---

# IOS Views and controls

Present your content onscreen and define the interactions allowed with that content.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class ProfileViewController: UIViewController {
    private let avatarView = UIImageView()
    private let nameLabel = UILabel()
    private let actionButton = UIButton(configuration: .filled())

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground

        avatarView.image = UIImage(systemName: "person.circle.fill")
        avatarView.tintColor = .systemBlue
        avatarView.contentMode = .scaleAspectFit

        nameLabel.text = "Rork User"
        nameLabel.font = .preferredFont(forTextStyle: .title2)

        actionButton.configuration?.title = "Edit Profile"
        actionButton.addAction(UIAction { _ in self.editProfile() }, for: .touchUpInside)

        let stack = UIStackView(arrangedSubviews: [avatarView, nameLabel, actionButton])
        stack.axis = .vertical
        stack.spacing = 16
        stack.alignment = .center
        stack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stack)

        NSLayoutConstraint.activate([
            stack.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            stack.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            avatarView.widthAnchor.constraint(equalToConstant: 80),
            avatarView.heightAnchor.constraint(equalToConstant: 80),
        ])
    }

    func editProfile() { }
}
```

## 💎 Elite Implementation Tips

- Use `UIButton.Configuration` (iOS 15+) instead of manual button styling
- Use `UIAction`-based targets instead of `#selector` for cleaner action handling
- Build layouts with `UIStackView` + Auto Layout for maintainable hierarchies

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

### View fundamentals

| API | Purpose |
|-----|---------|
| `UIView` | An object that manages the content for a rectangular area on the screen. |
| `UIKit Catalog: Creating and customizing views and controls` | Customize your app’s user interface with views and controls. |

### Container views

| API | Purpose |
|-----|---------|
| `Collection views` | Display nested views using a configurable and highly customizable layout. |
| `Table views` | Display data in a single column of customizable rows. |
| `UIStackView` | A streamlined interface for laying out a collection of views in either a column or a row. |
| `UIScrollView` | A view that allows the scrolling and zooming of its contained views. |

### Content views

| API | Purpose |
|-----|---------|
| `UIActivityIndicatorView` | A view that shows that a task is in progress. |
| `UICalendarView` | A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates. |
| `UIContentUnavailableView` | A view that indicates there’s no content to display. |
| `UIImageView` | A view that displays a single image or a sequence of animated images in your interface. |
| `UIPickerView` | A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values. |
| `UIProgressView` | A view that depicts the progress of a task over time. |

### Controls

| API | Purpose |
|-----|---------|
| `Responding to control-based events using target-action` | Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern. |
| `UIControl` | The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions. |
| `UIButton` | A control that executes your custom code in response to user interactions. |
| `UIColorWell` | A control that displays a color picker. |
| `UIDatePicker` | A control for inputting date and time values. |
| `UIPageControl` | A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity. |
| `UISegmentedControl` | A horizontal control that consists of multiple segments, each segment functioning as a discrete button. |
| `UISlider` | A control for selecting a single value from a continuous range of values. |

### Text views

| API | Purpose |
|-----|---------|
| `UILabel` | A view that displays one or more lines of informational text. |
| `UITextField` | An object that displays an editable text area in your interface. |
| `UITextView` | A scrollable, multiline text region. |
| `Drag and drop customization` | Extend the standard drag and drop support for text views to include custom types of content. |

### Search field

| API | Purpose |
|-----|---------|
| `UISearchTextField` | A view for displaying and editing text and search tokens. |
| `UISearchToken` | Search criteria in a search text field, represented by text and an optional icon. |
| `UISearchTextFieldDelegate` | The interface for the delegate of a search field. |

### Visual effects

| API | Purpose |
|-----|---------|
| `UIVisualEffect` | An initializer for visual effect views and blur and vibrancy effect objects. |
| `UIVisualEffectView` | An object that implements some complex visual effects. |
| `UIVibrancyEffect` | An object that amplifies and adjusts the color of the content layered behind a visual effect view. |
| `UIBlurEffect` | An object that applies a blurring effect to the content layered behind a visual effect view. |

### Bars

| API | Purpose |
|-----|---------|
| `UIBarItem` | An abstract superclass for items that you can add to a bar that appears at the bottom of the screen. |
| `UIBarButtonItem` | A specialized button for placement on a toolbar, navigation bar, or shortcuts bar. |
| `UIBarButtonItemGroup` | A group of one or more bar button items for placement on a navigation bar or shortcuts bar. |
| `UINavigationBar` | Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller. |
| `UISearchBar` | A specialized view for receiving search-related information from the user. |
| `UIToolbar` | A control that displays one or more buttons along an edge of your interface. |
| `UITabBar` | A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app. |
| `UITabBarItem` | An object that describes an item in a tab bar. |

### Content viewer

| API | Purpose |
|-----|---------|
| `UILargeContentViewerInteraction` | An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate. |
| `UILargeContentViewerInteractionDelegate` | An object that customizes the behavior of the large content viewer interactions. |
| `UILargeContentViewerItem` | Methods that provide details about how to display your custom content in the large content viewer. |

### Private Click Measurement (PCM)

| API | Purpose |
|-----|---------|
| `UIEventAttributionView` | An overlay view that verifies user interaction for Web AdAttributionKit. |
| `UIEventAttribution` | An object that contains event attribution information for Web AdAttributionKit. |

### SwiftUI

| API | Purpose |
|-----|---------|
| `Using SwiftUI with UIKit` | Learn how to incorporate SwiftUI views into a UIKit app. |

### Related types

| API | Purpose |
|-----|---------|
| `UIOffset` | A structure that specifies an amount to offset a position. |
| `UIAxis` | A structure that specifies the layout axes. |
| `UIEdgeInsets` | The inset distances for views. |
| `NSDirectionalEdgeInsets` | The inset distances for views, taking the user interface layout direction into account. |
| `NSDirectionalRectEdge` | Constants that specify an edge or a set of edges, taking the user interface layout direction into account. |
| `NSRectAlignment` | Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction. |
| `UIKit macros` | Macros that UIKit defines. |
