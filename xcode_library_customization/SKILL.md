---
name: Xcode library customization
description: Apple SwiftUI Documentation for Xcode library customization.
---

# Xcode library customization

Expose custom views and modifiers in the Xcode library.

## Overview

You can add your custom SwiftUI views and view modifiers to Xcode’s library.
This allows anyone developing your app or adopting your framework to access
them by clicking the Library button (+) in Xcode’s toolbar. You can select
and drag the custom library items into code, just like you would for
system-provided items.

![](images/com.apple.SwiftUI/xcode-library-customization-hero@2x.png)

To add items to the library, create a structure that conforms to the
<doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider>
protocol and encapsulate any items you want to add as
<doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryItem>
instances. Implement the
<doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider/views>
computed property to add library items containing views. Implement the
<doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider/modifiers(base:)>
method to add items containing view modifiers. Xcode harvests items from all
of the library content providers in your project as you work, and makes them
available to you in its library.

## Topics

### Creating library items

  <doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryContentProvider>

  <doc://com.apple.documentation/documentation/DeveloperToolsSupport/LibraryItem>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
