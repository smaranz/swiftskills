---
name: Navigation
description: Apple SwiftUI Documentation for Navigation.
---

# Navigation

Enable people to move between different parts of your app’s view hierarchy
within a scene.

## Overview

Use navigation containers to provide structure to your app’s user interface,
enabling people to easily move among the parts of your app.

![](images/com.apple.SwiftUI/navigation-hero@2x.png)

For example, people can move forward and backward through a stack of views
using a [`NavigationStack`](/documentation/SwiftUI/NavigationStack), or choose which view to display from a tab bar
using a [`TabView`](/documentation/SwiftUI/TabView).

Configure navigation containers by adding view modifiers like
[`navigationSplitViewStyle(_:)`](/documentation/SwiftUI/View/navigationSplitViewStyle(_:)) to the container. Use other modifiers on
the views inside the container to affect the container’s behavior when showing
that view. For example, you can use [`navigationTitle(_:)`](/documentation/SwiftUI/View/navigationTitle(_:)) on a
view to provide a toolbar title to display when showing that view.

## Topics

### Essentials

[Understanding the navigation stack](/documentation/SwiftUI/Understanding-the-navigation-stack)

Learn about the navigation stack, links, and how to manage navigation types in your app’s structure.

### Presenting views in columns

[Bringing robust navigation structure to your SwiftUI app](/documentation/SwiftUI/Bringing-robust-navigation-structure-to-your-swiftui-app)

Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.

[Migrating to new navigation types](/documentation/SwiftUI/Migrating-to-New-Navigation-Types)

Improve navigation behavior in your app by replacing navigation views
with navigation stacks and navigation split views.

[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)

A view that presents views in two or three columns, where selections in
leading columns control presentations in subsequent columns.

[`navigationSplitViewStyle(_:)`](/documentation/SwiftUI/View/navigationSplitViewStyle(_:))

Sets the style for navigation split views within this view.

[`navigationSplitViewColumnWidth(_:)`](/documentation/SwiftUI/View/navigationSplitViewColumnWidth(_:))

Sets a fixed, preferred width for the column containing this view.

[`navigationSplitViewColumnWidth(min:ideal:max:)`](/documentation/SwiftUI/View/navigationSplitViewColumnWidth(min:ideal:max:))

Sets a flexible, preferred width for the column containing this view.

[`NavigationSplitViewVisibility`](/documentation/SwiftUI/NavigationSplitViewVisibility)

The visibility of the leading columns in a navigation split view.

[`NavigationLink`](/documentation/SwiftUI/NavigationLink)

A view that controls a navigation presentation.

### Stacking views in one column

[`NavigationStack`](/documentation/SwiftUI/NavigationStack)

A view that displays a root view and enables you to present additional
views over the root view.

[`NavigationPath`](/documentation/SwiftUI/NavigationPath)

A type-erased list of data representing the content of a navigation stack.

[`navigationDestination(for:destination:)`](/documentation/SwiftUI/View/navigationDestination(for:destination:))

Associates a destination view with a presented data type for use within
a navigation stack.

[`navigationDestination(isPresented:destination:)`](/documentation/SwiftUI/View/navigationDestination(isPresented:destination:))

Associates a destination view with a binding that can be used to push
the view onto a [`NavigationStack`](/documentation/SwiftUI/NavigationStack).

[`navigationDestination(item:destination:)`](/documentation/SwiftUI/View/navigationDestination(item:destination:))

Associates a destination view with a bound value for use within a
navigation stack or navigation split view

### Managing column collapse

[`NavigationSplitViewColumn`](/documentation/SwiftUI/NavigationSplitViewColumn)

A view that represents a column in a navigation split view.

### Setting titles for navigation content

[`navigationTitle(_:)`](/documentation/SwiftUI/View/navigationTitle(_:))

Configures the view’s title for purposes of navigation, using a string
binding.

[`navigationSubtitle(_:)`](/documentation/SwiftUI/View/navigationSubtitle(_:))

Configures the view’s subtitle for purposes of navigation.

[`navigationDocument(_:)`](/documentation/SwiftUI/View/navigationDocument(_:))

Configures the view’s document for purposes of navigation.

[`navigationDocument(_:preview:)`](/documentation/SwiftUI/View/navigationDocument(_:preview:))

Configures the view’s document for purposes of navigation.

### Configuring the navigation bar

[`navigationBarBackButtonHidden(_:)`](/documentation/SwiftUI/View/navigationBarBackButtonHidden(_:))

Hides the navigation bar back button for the view.

[`navigationBarTitleDisplayMode(_:)`](/documentation/SwiftUI/View/navigationBarTitleDisplayMode(_:))

Configures the title display mode for this view.

[`NavigationBarItem`](/documentation/SwiftUI/NavigationBarItem)

A configuration for a navigation bar that represents a view at the top of a
navigation stack.

### Configuring the sidebar

[`sidebarRowSize`](/documentation/SwiftUI/EnvironmentValues/sidebarRowSize)

The current size of sidebar rows.

[`SidebarRowSize`](/documentation/SwiftUI/SidebarRowSize)

The standard sizes of sidebar rows.

### Presenting views in tabs

[Enhancing your app’s content with tab navigation](/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation)

Keep your app content front and center while providing quick access to navigation using the tab bar.

[`TabView`](/documentation/SwiftUI/TabView)

A view that switches between multiple child views using interactive user
interface elements.

[`Tab`](/documentation/SwiftUI/Tab)

The content for a tab and the tab’s associated tab item in a tab view.

[`TabRole`](/documentation/SwiftUI/TabRole)

A value that defines the purpose of the tab.

[`TabSection`](/documentation/SwiftUI/TabSection)

A container that you can use to add hierarchy within a tab view.

[`tabViewStyle(_:)`](/documentation/SwiftUI/View/tabViewStyle(_:))

Sets the style for the tab view within the current environment.

### Configuring a tab bar

[`defaultAdaptableTabBarPlacement(_:)`](/documentation/SwiftUI/View/defaultAdaptableTabBarPlacement(_:))

Specifies the default placement for the tabs in a tab view using the
adaptable sidebar style.

[`tabViewSidebarHeader(content:)`](/documentation/SwiftUI/View/tabViewSidebarHeader(content:))

Adds a custom header to the sidebar of a tab view.

[`tabViewSidebarFooter(content:)`](/documentation/SwiftUI/View/tabViewSidebarFooter(content:))

Adds a custom footer to the sidebar of a tab view.

[`tabViewSidebarBottomBar(content:)`](/documentation/SwiftUI/View/tabViewSidebarBottomBar(content:))

Adds a custom bottom bar to the sidebar of a tab view.

[`AdaptableTabBarPlacement`](/documentation/SwiftUI/AdaptableTabBarPlacement)

A placement for tabs in a tab view using the adaptable sidebar style.

[`tabBarPlacement`](/documentation/SwiftUI/EnvironmentValues/tabBarPlacement)

The current placement of the tab bar.

[`TabBarPlacement`](/documentation/SwiftUI/TabBarPlacement)

A placement for tabs in a tab view.

[`isTabBarShowingSections`](/documentation/SwiftUI/EnvironmentValues/isTabBarShowingSections)

A Boolean value that determines whether a tab view shows the
expanded contents of a tab section.

[`TabBarMinimizeBehavior`](/documentation/SwiftUI/TabBarMinimizeBehavior)

[`TabViewBottomAccessoryPlacement`](/documentation/SwiftUI/TabViewBottomAccessoryPlacement)

A placement of the bottom accessory in a tab view. You can use this to
adjust the content of the accessory view based on the placement.

### Configuring a tab

[`sectionActions(content:)`](/documentation/SwiftUI/View/sectionActions(content:))

Adds custom actions to a section.

[`TabPlacement`](/documentation/SwiftUI/TabPlacement)

A place that a tab can appear.

[`TabContentBuilder`](/documentation/SwiftUI/TabContentBuilder)

A result builder that constructs tabs for a tab view that supports
programmatic selection. This builder requires that all tabs in the
tab view have the same selection type.

[`TabContent`](/documentation/SwiftUI/TabContent)

A type that provides content for programmatically selectable tabs in a
tab view.

[`AnyTabContent`](/documentation/SwiftUI/AnyTabContent)

Type erased tab content.

### Enabling tab customization

[`tabViewCustomization(_:)`](/documentation/SwiftUI/View/tabViewCustomization(_:))

Specifies the customizations to apply to the sidebar representation
of the tab view.

[`TabViewCustomization`](/documentation/SwiftUI/TabViewCustomization)

The customizations a person makes to an adaptable sidebar tab view.

[`TabCustomizationBehavior`](/documentation/SwiftUI/TabCustomizationBehavior)

The customization behavior of customizable tab view content.

### Displaying views in multiple panes

[`HSplitView`](/documentation/SwiftUI/HSplitView)

A layout container that arranges its children in a horizontal line and
allows the user to resize them using dividers placed between them.

[`VSplitView`](/documentation/SwiftUI/VSplitView)

A layout container that arranges its children in a vertical line and allows
the user to resize them using dividers placed between them.

### Deprecated Types

[`NavigationView`](/documentation/SwiftUI/NavigationView)

A view for presenting a stack of views that represents a visible path in a
navigation hierarchy.

[`tabItem(_:)`](/documentation/SwiftUI/View/tabItem(_:))

Sets the tab bar item associated with this view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
