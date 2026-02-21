---
name: Clipboard
description: Apple SwiftUI Documentation for Clipboard.
---

# Clipboard

Enable people to move or duplicate items by issuing Copy and Paste commands.

## Overview

When people issue standard Copy and Cut commands, they expect to move
items to the system’s Clipboard, from which they can paste the items into
another place in the same app or into another app. Your app can participate
in this activity if you add view modifiers that indicate how to respond to
the standard commands.

![](images/com.apple.SwiftUI/clipboard-hero@2x.png)

In your copy and paste modifiers, provide or accept types that conform to the
<doc://com.apple.documentation/documentation/CoreTransferable/Transferable>
protocol, or that inherit from the
<doc://com.apple.documentation/documentation/Foundation/NSItemProvider> class.
When possible, prefer using transferable items.

## Topics

### Copying transferable items

[`copyable(_:)`](/documentation/SwiftUI/View/copyable(_:))

Specifies a list of items to copy in response to the system’s Copy
command.

[`cuttable(for:action:)`](/documentation/SwiftUI/View/cuttable(for:action:))

Specifies an action that moves items to the Clipboard in response to
the system’s Cut command.

[`pasteDestination(for:action:validator:)`](/documentation/SwiftUI/View/pasteDestination(for:action:validator:))

Specifies an action that adds validated items to a view in response to
the system’s Paste command.

### Copying items using item providers

[`onCopyCommand(perform:)`](/documentation/SwiftUI/View/onCopyCommand(perform:))

Adds an action to perform in response to the system’s Copy command.

[`onCutCommand(perform:)`](/documentation/SwiftUI/View/onCutCommand(perform:))

Adds an action to perform in response to the system’s Cut command.

[`onPasteCommand(of:perform:)`](/documentation/SwiftUI/View/onPasteCommand(of:perform:))

Adds an action to perform in response to the system’s Paste command.

[`onPasteCommand(of:validator:perform:)`](/documentation/SwiftUI/View/onPasteCommand(of:validator:perform:))

Adds an action to perform in response to the system’s Paste command with
items that you validate.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
