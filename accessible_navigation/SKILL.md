---
name: Accessible navigation
description: Apple SwiftUI Documentation for Accessible navigation.
---

# Accessible navigation

Enable users to navigate to specific user interface elements using rotors.

## Overview

An accessibility rotor is a shortcut that enables users
to quickly navigate to specific elements of the user interface,
and, optionally, to specific ranges of text within those elements.

![](images/com.apple.SwiftUI/accessible-navigation-hero@2x.png)

The system automatically provides rotors for many navigable elements,
but you can supply additional rotors for specific purposes, or
replace system rotors when they don’t automatically pick
up off-screen elements, like those far down in a [`LazyVStack`](/documentation/SwiftUI/LazyVStack) or a [`List`](/documentation/SwiftUI/List).

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/accessibility#Navigation>
in the Accessibility section of the Human Interface Guidelines.

## Topics

### Working with rotors

[`accessibilityRotor(_:entries:)`](/documentation/SwiftUI/View/accessibilityRotor(_:entries:))

Create an Accessibility Rotor with the specified user-visible label,
and entries generated from the content closure.

[`accessibilityRotor(_:entries:entryID:entryLabel:)`](/documentation/SwiftUI/View/accessibilityRotor(_:entries:entryID:entryLabel:))

Create an Accessibility Rotor with the specified user-visible label
and entries.

[`accessibilityRotor(_:entries:entryLabel:)`](/documentation/SwiftUI/View/accessibilityRotor(_:entries:entryLabel:))

Create an Accessibility Rotor with the specified user-visible label
and entries.

[`accessibilityRotor(_:textRanges:)`](/documentation/SwiftUI/View/accessibilityRotor(_:textRanges:))

Create an Accessibility Rotor with the specified user-visible label
and entries for each of the specified ranges. The Rotor will be attached
to the current Accessibility element, and each entry will go the
specified range of that element.

### Creating rotors

[`AccessibilityRotorContent`](/documentation/SwiftUI/AccessibilityRotorContent)

Content within an accessibility rotor.

[`AccessibilityRotorContentBuilder`](/documentation/SwiftUI/AccessibilityRotorContentBuilder)

Result builder you use to generate rotor entry content.

[`AccessibilityRotorEntry`](/documentation/SwiftUI/AccessibilityRotorEntry)

A struct representing an entry in an Accessibility Rotor.

### Replacing system rotors

[`AccessibilitySystemRotor`](/documentation/SwiftUI/AccessibilitySystemRotor)

Designates a Rotor that replaces one of the automatic, system-provided
Rotors with a developer-provided Rotor.

### Configuring rotors

[`accessibilityRotorEntry(id:in:)`](/documentation/SwiftUI/View/accessibilityRotorEntry(id:in:))

Defines an explicit identifier tying an Accessibility element for this
view to an entry in an Accessibility Rotor.

[`accessibilityLinkedGroup(id:in:)`](/documentation/SwiftUI/View/accessibilityLinkedGroup(id:in:))

Links multiple accessibility elements so that the user can quickly
navigate from one element to another, even when the elements are not near
each other in the accessibility hierarchy.

[`accessibilitySortPriority(_:)`](/documentation/SwiftUI/View/accessibilitySortPriority(_:))

Sets the sort priority order for this view’s accessibility element,
relative to other elements at the same level.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
