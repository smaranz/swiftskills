---
name: Navigation
description: Rork-Max Quality skill for Navigation. Actionable patterns and best practices for SwiftUI development.
---

# Navigation

Enable people to move between different parts of your app’s view hierarchy
within a scene.
Use navigation containers to provide structure to your app’s user interface,
enabling people to easily move among the parts of your app.
For example, people can move forward and backward through a stack of views
using a `NavigationStack`, or choose which view to display from a tab bar
using a `TabView`.
Configure navigation containers by adding view modifiers like
`navigationSplitViewStyle(_:)` to the container. Use other modifiers on
the views inside the container to affect the container’s behavior when showing
that view. For example, you can use `navigationTitle(_:)` on a
view to provide a toolbar title to display when showing that view.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct NavigationExample: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List(Recipe.all) { recipe in
                NavigationLink(value: recipe) {
                    Label(recipe.name, systemImage: "fork.knife")
                }
            }
            .navigationTitle("Recipes")
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `NavigationStack(path:)` with `NavigationPath` for programmatic, deep-linkable navigation
- Prefer `NavigationSplitView` on iPad/Mac for sidebar + detail column layouts
- Never nest a `NavigationStack` inside another — it creates double navigation bars


## When to Use

- Building hierarchical drill-down flows (settings, detail views)
- Implementing tab-based or sidebar navigation patterns
- Presenting modal sheets, popovers, alerts, or confirmation dialogs
- Creating deep-linkable navigation paths with `NavigationPath`

## Best Practices

- Use `NavigationStack` with a `path` binding for programmatic, deep-linkable navigation
- Prefer `NavigationSplitView` on iPad/Mac for sidebar + detail layouts
- Model navigation state explicitly so it can be saved, restored, and deep-linked
- Use `.sheet()`, `.fullScreenCover()`, and `.popover()` for modal presentations

## Common Pitfalls

- Using the deprecated `NavigationView` instead of `NavigationStack`/`NavigationSplitView`
- Nesting `NavigationStack` inside another `NavigationStack` causing double navigation bars
- Forgetting to make navigation destination types `Hashable` for `navigationDestination(for:)`

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Understanding the navigation stack` | Learn about the navigation stack, links, and how to manage navigation types in your app’s structure. |

### Presenting views in columns

| API | Purpose |
|-----|---------|
| `Bringing robust navigation structure to your SwiftUI app` | Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration. |
| `Migrating to new navigation types` | Improve navigation behavior in your app by replacing navigation views |
| `NavigationSplitView` | A view that presents views in two or three columns, where selections in |
| `navigationSplitViewStyle(_:)` | Sets the style for navigation split views within this view. |
| `navigationSplitViewColumnWidth(_:)` | Sets a fixed, preferred width for the column containing this view. |
| `navigationSplitViewColumnWidth(min:ideal:max:)` | Sets a flexible, preferred width for the column containing this view. |
| `NavigationSplitViewVisibility` | The visibility of the leading columns in a navigation split view. |
| `NavigationLink` | A view that controls a navigation presentation. |

### Stacking views in one column

| API | Purpose |
|-----|---------|
| `NavigationStack` | A view that displays a root view and enables you to present additional |
| `NavigationPath` | A type-erased list of data representing the content of a navigation stack. |
| `navigationDestination(for:destination:)` | Associates a destination view with a presented data type for use within |
| `navigationDestination(isPresented:destination:)` | Associates a destination view with a binding that can be used to push |
| `navigationDestination(item:destination:)` | Associates a destination view with a bound value for use within a |

### Managing column collapse

| API | Purpose |
|-----|---------|
| `NavigationSplitViewColumn` | A view that represents a column in a navigation split view. |

### Setting titles for navigation content

| API | Purpose |
|-----|---------|
| `navigationTitle(_:)` | Configures the view’s title for purposes of navigation, using a string |
| `navigationSubtitle(_:)` | Configures the view’s subtitle for purposes of navigation. |
| `navigationDocument(_:)` | Configures the view’s document for purposes of navigation. |
| `navigationDocument(_:preview:)` | Configures the view’s document for purposes of navigation. |

### Configuring the navigation bar

| API | Purpose |
|-----|---------|
| `navigationBarBackButtonHidden(_:)` | Hides the navigation bar back button for the view. |
| `navigationBarTitleDisplayMode(_:)` | Configures the title display mode for this view. |
| `NavigationBarItem` | A configuration for a navigation bar that represents a view at the top of a |

### Configuring the sidebar

| API | Purpose |
|-----|---------|
| `sidebarRowSize` | The current size of sidebar rows. |
| `SidebarRowSize` | The standard sizes of sidebar rows. |

### Presenting views in tabs

| API | Purpose |
|-----|---------|
| `Enhancing your app’s content with tab navigation` | Keep your app content front and center while providing quick access to navigation using the tab bar. |
| `TabView` | A view that switches between multiple child views using interactive user |
| `Tab` | The content for a tab and the tab’s associated tab item in a tab view. |
| `TabRole` | A value that defines the purpose of the tab. |
| `TabSection` | A container that you can use to add hierarchy within a tab view. |
| `tabViewStyle(_:)` | Sets the style for the tab view within the current environment. |

### Configuring a tab bar

| API | Purpose |
|-----|---------|
| `defaultAdaptableTabBarPlacement(_:)` | Specifies the default placement for the tabs in a tab view using the |
| `tabViewSidebarHeader(content:)` | Adds a custom header to the sidebar of a tab view. |
| `tabViewSidebarFooter(content:)` | Adds a custom footer to the sidebar of a tab view. |
| `tabViewSidebarBottomBar(content:)` | Adds a custom bottom bar to the sidebar of a tab view. |
| `AdaptableTabBarPlacement` | A placement for tabs in a tab view using the adaptable sidebar style. |
| `tabBarPlacement` | The current placement of the tab bar. |
| `TabBarPlacement` | A placement for tabs in a tab view. |
| `isTabBarShowingSections` | A Boolean value that determines whether a tab view shows the |

### Configuring a tab

| API | Purpose |
|-----|---------|
| `sectionActions(content:)` | Adds custom actions to a section. |
| `TabPlacement` | A place that a tab can appear. |
| `TabContentBuilder` | A result builder that constructs tabs for a tab view that supports |
| `TabContent` | A type that provides content for programmatically selectable tabs in a |
| `AnyTabContent` | Type erased tab content. |

### Enabling tab customization

| API | Purpose |
|-----|---------|
| `tabViewCustomization(_:)` | Specifies the customizations to apply to the sidebar representation |
| `TabViewCustomization` | The customizations a person makes to an adaptable sidebar tab view. |
| `TabCustomizationBehavior` | The customization behavior of customizable tab view content. |

### Displaying views in multiple panes

| API | Purpose |
|-----|---------|
| `HSplitView` | A layout container that arranges its children in a horizontal line and |
| `VSplitView` | A layout container that arranges its children in a vertical line and allows |

### Deprecated Types

| API | Purpose |
|-----|---------|
| `NavigationView` | A view for presenting a stack of views that represents a visible path in a |
| `tabItem(_:)` | Sets the tab bar item associated with this view. |
