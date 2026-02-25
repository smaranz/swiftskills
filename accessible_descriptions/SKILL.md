---
name: Accessible descriptions
description: Rork-Max Quality skill for Accessible descriptions. Actionable patterns and best practices for SwiftUI development.
---

# Accessible descriptions

Describe interface elements to help people understand what they represent.
SwiftUI can often infer some information about your user interface elements,
but you can use accessibility modifiers to provide even more information for
users that need it.
For design guidance, see
in the Accessibility section of the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct DescriptiveChart: View {
    let data: [DataPoint]

    var body: some View {
        ChartView(data: data)
            .accessibilityLabel("Sales chart")
            .accessibilityValue("Trending upward, highest point in March at $42,000")
            .accessibilityHint("Double-tap for detailed breakdown")
            .accessibilityChartDescriptor(SalesChartDescriptor(data: data))
    }
}
```

## 💎 Elite Implementation Tips

- Use `.accessibilityLabel()` for what the element IS, `.accessibilityValue()` for its current STATE
- Add `.accessibilityHint()` to describe what happens on interaction
- Use `.accessibilityChartDescriptor()` for audio graph support in charts


## When to Use

- Ensuring VoiceOver users can navigate and interact with all app features
- Supporting Dynamic Type, Reduce Motion, and high-contrast modes
- Providing accessible labels, hints, and traits for custom controls
- Implementing accessible drag-and-drop or custom gesture alternatives

## Best Practices

- Add `.accessibilityLabel()` to every image, icon, and custom control
- Use `.accessibilityAddTraits(.isButton)` for interactive non-button elements
- Group related elements with `.accessibilityElement(children: .combine)`
- Test with VoiceOver enabled — it reveals issues no other tool catches
- Support Dynamic Type by never hard-coding font sizes

## Common Pitfalls

- Decorative images without `.accessibilityHidden(true)` clutter VoiceOver
- Custom gestures with no accessible action alternative lock out VoiceOver users
- Using color alone to convey information (red = error) without text/shape cues

## Key APIs

### Applying labels

| API | Purpose |
|-----|---------|
| `accessibilityLabel(_:)` | Adds a label to the view that describes its contents. |
| `accessibilityLabel(_:isEnabled:)` | Adds a label to the view that describes its contents. |
| `accessibilityLabel(content:)` | Adds a label to the view that describes its contents. |
| `accessibilityInputLabels(_:)` | Sets alternate input labels with which users identify a view. |
| `accessibilityInputLabels(_:isEnabled:)` | Sets alternate input labels with which users identify a view. |
| `accessibilityLabeledPair(role:id:in:)` | Pairs an accessibility element representing a label with the element |
| `AccessibilityLabeledPairRole` | The role of an accessibility element in a label / content pair. |

### Describing values

| API | Purpose |
|-----|---------|
| `accessibilityValue(_:)` | Adds a textual description of the value that the view contains. |
| `accessibilityValue(_:isEnabled:)` | Adds a textual description of the value that the view contains. |

### Describing content

| API | Purpose |
|-----|---------|
| `accessibilityTextContentType(_:)` | Sets an accessibility text content type. |
| `accessibilityHeading(_:)` | Sets the accessibility level of this heading. |
| `AccessibilityHeadingLevel` | The hierarchy of a heading in relation to other headings. |
| `AccessibilityTextContentType` | Textual context that assistive technologies can use to improve the |

### Describing charts

| API | Purpose |
|-----|---------|
| `accessibilityChartDescriptor(_:)` | Adds a descriptor to a View that represents a chart to make |
| `AXChartDescriptorRepresentable` | A type to generate an `AXChartDescriptor` object that you use to provide |

### Adding custom descriptions

| API | Purpose |
|-----|---------|
| `accessibilityCustomContent(_:_:importance:)` | Add additional accessibility information to the view. |
| `AccessibilityCustomContentKey` | Key used to specify the identifier and label associated with |

### Assigning traits to content

| API | Purpose |
|-----|---------|
| `accessibilityAddTraits(_:)` | Adds the given traits to the view. |
| `accessibilityRemoveTraits(_:)` | Removes the given traits from this view. |
| `AccessibilityTraits` | A set of accessibility traits that describe how an element behaves. |

### Offering hints

| API | Purpose |
|-----|---------|
| `accessibilityHint(_:)` | Communicates to the user what happens after performing the view’s |
| `accessibilityHint(_:isEnabled:)` | Communicates to the user what happens after performing the view’s |

### Configuring VoiceOver

| API | Purpose |
|-----|---------|
| `speechAdjustedPitch(_:)` | Raises or lowers the pitch of spoken text. |
| `speechAlwaysIncludesPunctuation(_:)` | Sets whether VoiceOver should always speak all punctuation in the text |
| `speechAnnouncementsQueued(_:)` | Controls whether to queue pending announcements behind existing speech |
| `speechSpellsOutCharacters(_:)` | Sets whether VoiceOver should speak the contents of the text view |
