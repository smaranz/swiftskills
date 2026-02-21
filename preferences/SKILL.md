---
name: Preferences
description: Apple SwiftUI Documentation for Preferences.
---

# Preferences

Indicate configuration preferences from views to their container views.

## Overview

Whereas you use the environment to configure the subviews of a view, you use
preferences to send configuration information from subviews toward their
container. However, unlike configuration information that flows down a view
hierarchy from one container to many subviews, a single container needs to
reconcile potentially conflicting preferences flowing up from its many subviews.

![](images/com.apple.SwiftUI/preferences-hero@2x.png)

When you use the [`PreferenceKey`](/documentation/SwiftUI/PreferenceKey) protocol to define a custom preference, you
indicate how to merge preferences from multiple subviews. You can then set a
value for the preference on a view using the [`preference(key:value:)`](/documentation/SwiftUI/View/preference(key:value:))
view modifier. Many built-in modifiers, like [`navigationTitle(_:)`](/documentation/SwiftUI/View/navigationTitle(_:)),
rely on preferences to send configuration information to their container.

## Topics

### Setting preferences

[`preference(key:value:)`](/documentation/SwiftUI/View/preference(key:value:))

Sets a value for the given preference.

[`transformPreference(_:_:)`](/documentation/SwiftUI/View/transformPreference(_:_:))

Applies a transformation to a preference value.

### Creating custom preferences

[`PreferenceKey`](/documentation/SwiftUI/PreferenceKey)

A named value produced by a view.

### Setting preferences based on geometry

[`anchorPreference(key:value:transform:)`](/documentation/SwiftUI/View/anchorPreference(key:value:transform:))

Sets a value for the specified preference key, the value is a
function of a geometry value tied to the current coordinate
space, allowing readers of the value to convert the geometry to
their local coordinates.

[`transformAnchorPreference(key:value:transform:)`](/documentation/SwiftUI/View/transformAnchorPreference(key:value:transform:))

Sets a value for the specified preference key, the value is a
function of the key’s current value and a geometry value tied
to the current coordinate space, allowing readers of the value
to convert the geometry to their local coordinates.

### Responding to changes in preferences

[`onPreferenceChange(_:perform:)`](/documentation/SwiftUI/View/onPreferenceChange(_:perform:))

Adds an action to perform when the specified preference key’s value
changes.

### Generating backgrounds and overlays from preferences

[`backgroundPreferenceValue(_:_:)`](/documentation/SwiftUI/View/backgroundPreferenceValue(_:_:))

Reads the specified preference value from the view, using it to
produce a second view that is applied as the background of the
original view.

[`backgroundPreferenceValue(_:alignment:_:)`](/documentation/SwiftUI/View/backgroundPreferenceValue(_:alignment:_:))

Reads the specified preference value from the view, using it to
produce a second view that is applied as the background of the
original view.

[`overlayPreferenceValue(_:_:)`](/documentation/SwiftUI/View/overlayPreferenceValue(_:_:))

Reads the specified preference value from the view, using it to
produce a second view that is applied as an overlay to the
original view.

[`overlayPreferenceValue(_:alignment:_:)`](/documentation/SwiftUI/View/overlayPreferenceValue(_:alignment:_:))

Reads the specified preference value from the view, using it to
produce a second view that is applied as an overlay to the
original view.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
