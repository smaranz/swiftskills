---
name: Accessible descriptions
description: Apple SwiftUI Documentation for Accessible descriptions.
---

# Accessible descriptions

Describe interface elements to help people understand what they represent.

## Overview

SwiftUI can often infer some information about your user interface elements,
but you can use accessibility modifiers to provide even more information for
users that need it.

![](images/com.apple.SwiftUI/accessible-descriptions-hero@2x.png)

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/accessibility#Content-descriptions>
in the Accessibility section of the Human Interface Guidelines.

## Topics

### Applying labels

[`accessibilityLabel(_:)`](/documentation/SwiftUI/View/accessibilityLabel(_:))

Adds a label to the view that describes its contents.

[`accessibilityLabel(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityLabel(_:isEnabled:))

Adds a label to the view that describes its contents.

[`accessibilityLabel(content:)`](/documentation/SwiftUI/View/accessibilityLabel(content:))

Adds a label to the view that describes its contents.

[`accessibilityInputLabels(_:)`](/documentation/SwiftUI/View/accessibilityInputLabels(_:))

Sets alternate input labels with which users identify a view.

[`accessibilityInputLabels(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityInputLabels(_:isEnabled:))

Sets alternate input labels with which users identify a view.

[`accessibilityLabeledPair(role:id:in:)`](/documentation/SwiftUI/View/accessibilityLabeledPair(role:id:in:))

Pairs an accessibility element representing a label with the element
for the matching content.

[`AccessibilityLabeledPairRole`](/documentation/SwiftUI/AccessibilityLabeledPairRole)

The role of an accessibility element in a label / content pair.

### Describing values

[`accessibilityValue(_:)`](/documentation/SwiftUI/View/accessibilityValue(_:))

Adds a textual description of the value that the view contains.

[`accessibilityValue(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityValue(_:isEnabled:))

Adds a textual description of the value that the view contains.

### Describing content

[`accessibilityTextContentType(_:)`](/documentation/SwiftUI/View/accessibilityTextContentType(_:))

Sets an accessibility text content type.

[`accessibilityHeading(_:)`](/documentation/SwiftUI/View/accessibilityHeading(_:))

Sets the accessibility level of this heading.

[`AccessibilityHeadingLevel`](/documentation/SwiftUI/AccessibilityHeadingLevel)

The hierarchy of a heading in relation to other headings.

[`AccessibilityTextContentType`](/documentation/SwiftUI/AccessibilityTextContentType)

Textual context that assistive technologies can use to improve the
presentation of spoken text.

### Describing charts

[`accessibilityChartDescriptor(_:)`](/documentation/SwiftUI/View/accessibilityChartDescriptor(_:))

Adds a descriptor to a View that represents a chart to make
the chart’s contents accessible to all users.

[`AXChartDescriptorRepresentable`](/documentation/SwiftUI/AXChartDescriptorRepresentable)

A type to generate an `AXChartDescriptor` object that you use to provide
information about a chart and its data for an accessible experience
in VoiceOver or other assistive technologies.

### Adding custom descriptions

[`accessibilityCustomContent(_:_:importance:)`](/documentation/SwiftUI/View/accessibilityCustomContent(_:_:importance:))

Add additional accessibility information to the view.

[`AccessibilityCustomContentKey`](/documentation/SwiftUI/AccessibilityCustomContentKey)

Key used to specify the identifier and label associated with
an entry of additional accessibility information.

### Assigning traits to content

[`accessibilityAddTraits(_:)`](/documentation/SwiftUI/View/accessibilityAddTraits(_:))

Adds the given traits to the view.

[`accessibilityRemoveTraits(_:)`](/documentation/SwiftUI/View/accessibilityRemoveTraits(_:))

Removes the given traits from this view.

[`AccessibilityTraits`](/documentation/SwiftUI/AccessibilityTraits)

A set of accessibility traits that describe how an element behaves.

### Offering hints

[`accessibilityHint(_:)`](/documentation/SwiftUI/View/accessibilityHint(_:))

Communicates to the user what happens after performing the view’s
action.

[`accessibilityHint(_:isEnabled:)`](/documentation/SwiftUI/View/accessibilityHint(_:isEnabled:))

Communicates to the user what happens after performing the view’s
action.

### Configuring VoiceOver

[`speechAdjustedPitch(_:)`](/documentation/SwiftUI/View/speechAdjustedPitch(_:))

Raises or lowers the pitch of spoken text.

[`speechAlwaysIncludesPunctuation(_:)`](/documentation/SwiftUI/View/speechAlwaysIncludesPunctuation(_:))

Sets whether VoiceOver should always speak all punctuation in the text
view.

[`speechAnnouncementsQueued(_:)`](/documentation/SwiftUI/View/speechAnnouncementsQueued(_:))

Controls whether to queue pending announcements behind existing speech
rather than interrupting speech in progress.

[`speechSpellsOutCharacters(_:)`](/documentation/SwiftUI/View/speechSpellsOutCharacters(_:))

Sets whether VoiceOver should speak the contents of the text view
character by character.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
