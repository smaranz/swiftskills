---
name: Text input and output
description: Rork-Max Quality skill for Text input and output. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Text input and output


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Text input and output

Display formatted text and get text input from the user.

## Overview

To display read-only text, or read-only text paired with an image, use
the built-in [`Text`](/documentation/SwiftUI/Text) or [`Label`](/documentation/SwiftUI/Label) views, respectively. When you need to
collect text input from the user, use an appropriate text input view,
like [`TextField`](/documentation/SwiftUI/TextField) or [`TextEditor`](/documentation/SwiftUI/TextEditor).

![](images/com.apple.SwiftUI/text-input-and-output-hero@2x.png)

You add view modifiers to control the text’s font, selectability, alignment,
layout direction, and so on. These modifiers also affect other views that
display text, like the labels on controls, even if you don’t define an
explicit [`Text`](/documentation/SwiftUI/Text) view.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/typography>
in the Human Interface Guidelines.

## Topics

### Displaying text

[`Text`](/documentation/SwiftUI/Text)

A view that displays one or more lines of read-only text.

[`Label`](/documentation/SwiftUI/Label)

A standard label for user interface items, consisting of an icon with a
title.

[`labelStyle(_:)`](/documentation/SwiftUI/View/labelStyle(_:))

Sets the style for labels within this view.

### Getting text input

[Building rich SwiftUI text experiences](/documentation/SwiftUI/building-rich-swiftui-text-experiences)

Build an editor for formatted text using SwiftUI text editor views and attributed strings.

[`TextField`](/documentation/SwiftUI/TextField)

A control that displays an editable text interface.

[`textFieldStyle(_:)`](/documentation/SwiftUI/View/textFieldStyle(_:))

Sets the style for text fields within this view.

[`SecureField`](/documentation/SwiftUI/SecureField)

A control into which people securely enter private text.

[`TextEditor`](/documentation/SwiftUI/TextEditor)

A view that can display and edit long-form text.

### Selecting text

[`textSelection(_:)`](/documentation/SwiftUI/View/textSelection(_:))

Controls whether people can select text within this view.

[`TextSelectability`](/documentation/SwiftUI/TextSelectability)

A type that describes the ability to select text.

[`TextSelection`](/documentation/SwiftUI/TextSelection)

Represents a selection of text.

[`textSelectionAffinity(_:)`](/documentation/SwiftUI/View/textSelectionAffinity(_:))

Sets the direction of a selection or cursor relative to a text character.

[`textSelectionAffinity`](/documentation/SwiftUI/EnvironmentValues/textSelectionAffinity)

A representation of the direction or association of a selection or cursor
relative to a text character. This concept becomes much more prominent
when dealing with bidirectional text (text that contains both LTR and RTL
scripts, like English and Arabic combined).

[`TextSelectionAffinity`](/documentation/SwiftUI/TextSelectionAffinity)

A representation of the direction or association of a selection or cursor
relative to a text character. This concept becomes much more prominent
when dealing with bidirectional text (text that contains both LTR and RTL
scripts, like English and Arabic combined).

[`AttributedTextSelection`](/documentation/SwiftUI/AttributedTextSelection)

Represents a selection of attributed text.

### Setting a font

[Applying custom fonts to text](/documentation/SwiftUI/Applying-Custom-Fonts-to-Text)

Add and use a font in your app that scales with Dynamic Type.

[`font(_:)`](/documentation/SwiftUI/View/font(_:))

Sets the default font for text in this view.

[`fontDesign(_:)`](/documentation/SwiftUI/View/fontDesign(_:))

Sets the font design of the text in this view.

[`fontWeight(_:)`](/documentation/SwiftUI/View/fontWeight(_:))

Sets the font weight of the text in this view.

[`fontWidth(_:)`](/documentation/SwiftUI/View/fontWidth(_:))

Sets the font width of the text in this view.

[`font`](/documentation/SwiftUI/EnvironmentValues/font)

The default font of this environment.

[`Font`](/documentation/SwiftUI/Font)

An environment-dependent font.

### Adjusting text size

[`textScale(_:isEnabled:)`](/documentation/SwiftUI/View/textScale(_:isEnabled:))

Applies a text scale to text in the view.

[`dynamicTypeSize(_:)`](/documentation/SwiftUI/View/dynamicTypeSize(_:))

Sets the Dynamic Type size within the view to the given value.

[`dynamicTypeSize`](/documentation/SwiftUI/EnvironmentValues/dynamicTypeSize)

The current Dynamic Type size.

[`DynamicTypeSize`](/documentation/SwiftUI/DynamicTypeSize)

A Dynamic Type size, which specifies how large scalable content should be.

[`ScaledMetric`](/documentation/SwiftUI/ScaledMetric)

A dynamic property that scales a numeric value.

[`TextVariantPreference`](/documentation/SwiftUI/TextVariantPreference)

A protocol for controlling the size variant of text views.

[`FixedTextVariant`](/documentation/SwiftUI/FixedTextVariant)

The default text variant preference that chooses the largest available
variant.

[`SizeDependentTextVariant`](/documentation/SwiftUI/SizeDependentTextVariant)

The size dependent variant preference allows the text to take the available
space into account when choosing the variant to display.

### Controlling text style

[`bold(_:)`](/documentation/SwiftUI/View/bold(_:))

Applies a bold font weight to the text in this view.

[`italic(_:)`](/documentation/SwiftUI/View/italic(_:))

Applies italics to the text in this view.

[`underline(_:pattern:color:)`](/documentation/SwiftUI/View/underline(_:pattern:color:))

Applies an underline to the text in this view.

[`strikethrough(_:pattern:color:)`](/documentation/SwiftUI/View/strikethrough(_:pattern:color:))

Applies a strikethrough to the text in this view.

[`textCase(_:)`](/documentation/SwiftUI/View/textCase(_:))

Sets a transform for the case of the text contained in this view when
displayed.

[`textCase`](/documentation/SwiftUI/EnvironmentValues/textCase)

A stylistic override to transform the case of `Text` when displayed,
using the environment’s locale.

[`monospaced(_:)`](/documentation/SwiftUI/View/monospaced(_:))

Modifies the fonts of all child views to use the fixed-width variant of
the current font, if possible.

[`monospacedDigit()`](/documentation/SwiftUI/View/monospacedDigit())

Modifies the fonts of all child views to use fixed-width digits, if
possible, while leaving other characters proportionally spaced.

[`AttributedTextFormattingDefinition`](/documentation/SwiftUI/AttributedTextFormattingDefinition)

A protocol for defining how text can be styled in a view.

[`AttributedTextValueConstraint`](/documentation/SwiftUI/AttributedTextValueConstraint)

A protocol for defining a constraint on the value of a certain attribute.

[`AttributedTextFormatting`](/documentation/SwiftUI/AttributedTextFormatting)

A namespace for types related to attributed text formatting definitions.

### Managing text layout

[`truncationMode(_:)`](/documentation/SwiftUI/View/truncationMode(_:))

Sets the truncation mode for lines of text that are too long to fit in
the available space.

[`truncationMode`](/documentation/SwiftUI/EnvironmentValues/truncationMode)

A value that indicates how the layout truncates the last line of text to
fit into the available space.

[`allowsTightening(_:)`](/documentation/SwiftUI/View/allowsTightening(_:))

Sets whether text in this view can compress the space between characters
when necessary to fit text in a line.

[`allowsTightening`](/documentation/SwiftUI/EnvironmentValues/allowsTightening)

A Boolean value that indicates whether inter-character spacing should
tighten to fit the text into the available space.

[`minimumScaleFactor(_:)`](/documentation/SwiftUI/View/minimumScaleFactor(_:))

Sets the minimum amount that text in this view scales down to fit in the
available space.

[`minimumScaleFactor`](/documentation/SwiftUI/EnvironmentValues/minimumScaleFactor)

The minimum permissible proportion to shrink the font size to fit
the text into the available space.

[`baselineOffset(_:)`](/documentation/SwiftUI/View/baselineOffset(_:))

Sets the vertical offset for the text relative to its baseline
in this view.

[`kerning(_:)`](/documentation/SwiftUI/View/kerning(_:))

Sets the spacing, or kerning, between characters for the text in this view.

[`tracking(_:)`](/documentation/SwiftUI/View/tracking(_:))

Sets the tracking for the text in this view.

[`flipsForRightToLeftLayoutDirection(_:)`](/documentation/SwiftUI/View/flipsForRightToLeftLayoutDirection(_:))

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

[`TextAlignment`](/documentation/SwiftUI/TextAlignment)

An alignment position for text along the horizontal axis.

### Rendering text

[Creating visual effects with SwiftUI](/documentation/SwiftUI/Creating-visual-effects-with-SwiftUI)

Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.

[`TextAttribute`](/documentation/SwiftUI/TextAttribute)

A value that you can attach to text views and that text renderers can query.

[`textRenderer(_:)`](/documentation/SwiftUI/View/textRenderer(_:))

Returns a new view such that any text views within it will use
`renderer` to draw themselves.

[`TextRenderer`](/documentation/SwiftUI/TextRenderer)

A value that can replace the default text view rendering behavior.

[`TextProxy`](/documentation/SwiftUI/TextProxy)

A proxy for a text view that custom text renderers use.

### Limiting line count for multiline text

[`lineLimit(_:)`](/documentation/SwiftUI/View/lineLimit(_:))

Sets to a closed range the number of lines that text can occupy in
this view.

[`lineLimit(_:reservesSpace:)`](/documentation/SwiftUI/View/lineLimit(_:reservesSpace:))

Sets a limit for the number of lines text can occupy in this view.

[`lineLimit`](/documentation/SwiftUI/EnvironmentValues/lineLimit)

The maximum number of lines that text can occupy in a view.

### Formatting multiline text

[`lineSpacing(_:)`](/documentation/SwiftUI/View/lineSpacing(_:))

Sets the amount of space between lines of text in this view.

[`lineSpacing`](/documentation/SwiftUI/EnvironmentValues/lineSpacing)

The distance in points between the bottom of one line fragment and the
top of the next.

[`multilineTextAlignment(_:)`](/documentation/SwiftUI/View/multilineTextAlignment(_:))

Sets the alignment of a text view that contains multiple lines of text.

[`multilineTextAlignment`](/documentation/SwiftUI/EnvironmentValues/multilineTextAlignment)

An environment value that indicates how a text view aligns its lines
when the content wraps or contains newlines.

### Formatting date and time

[`SystemFormatStyle`](/documentation/SwiftUI/SystemFormatStyle)

A namespace for format styles that implement designs used across Apple’s
platformes.

[`TimeDataSource`](/documentation/SwiftUI/TimeDataSource)

A source of time related data.

### Managing text entry

[`autocorrectionDisabled(_:)`](/documentation/SwiftUI/View/autocorrectionDisabled(_:))

Sets whether to disable autocorrection for this view.

[`autocorrectionDisabled`](/documentation/SwiftUI/EnvironmentValues/autocorrectionDisabled)

A Boolean value that determines whether the view hierarchy has
auto-correction enabled.

[`keyboardType(_:)`](/documentation/SwiftUI/View/keyboardType(_:))

Sets the keyboard type for this view.

[`scrollDismissesKeyboard(_:)`](/documentation/SwiftUI/View/scrollDismissesKeyboard(_:))

Configures the behavior in which scrollable content interacts with
the software keyboard.

[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType(_:))

Sets the text content type for this view, which the system uses to
offer suggestions while the user enters text on macOS.

[`textInputAutocapitalization(_:)`](/documentation/SwiftUI/View/textInputAutocapitalization(_:))

Sets how often the shift key in the keyboard is automatically enabled.

[`TextInputAutocapitalization`](/documentation/SwiftUI/TextInputAutocapitalization)

The kind of autocapitalization behavior applied during text input.

[`textInputCompletion(_:)`](/documentation/SwiftUI/View/textInputCompletion(_:))

Associates a fully formed string with the value of this view when used
as a text input suggestion

[`textInputSuggestions(_:)`](/documentation/SwiftUI/View/textInputSuggestions(_:))

Configures the text input suggestions for this view.

[`textInputSuggestions(_:content:)`](/documentation/SwiftUI/View/textInputSuggestions(_:content:))

Configures the text input suggestions for this view.

[`textInputSuggestions(_:id:content:)`](/documentation/SwiftUI/View/textInputSuggestions(_:id:content:))

Configures the text input suggestions for this view.

[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType(_:)-4dqqb)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType(_:)-6fic1)

Sets the text content type for this view, which the system uses to
offer suggestions while the user enters text on macOS.

[`textContentType(_:)`](/documentation/SwiftUI/View/textContentType(_:)-ufdv)

Sets the text content type for this view, which the system uses to
offer suggestions while the user enters text on an iOS or tvOS device.

[`TextInputFormattingControlPlacement`](/documentation/SwiftUI/TextInputFormattingControlPlacement)

A structure defining the system text formatting controls
available on each platform.

### Dictating text

[`searchDictationBehavior(_:)`](/documentation/SwiftUI/View/searchDictationBehavior(_:))

Configures the dictation behavior for any search fields configured
by the searchable modifier.

[`TextInputDictationActivation`](/documentation/SwiftUI/TextInputDictationActivation)

[`TextInputDictationBehavior`](/documentation/SwiftUI/TextInputDictationBehavior)

### Configuring the Writing Tools behavior

[`writingToolsBehavior(_:)`](/documentation/SwiftUI/View/writingToolsBehavior(_:))

Specifies the Writing Tools behavior for text and text input in the
environment.

[`WritingToolsBehavior`](/documentation/SwiftUI/WritingToolsBehavior)

The Writing Tools editing experience for text and text input.

### Specifying text equivalents

[`typeSelectEquivalent(_:)`](/documentation/SwiftUI/View/typeSelectEquivalent(_:))

Sets an explicit type select equivalent text in a collection, such as
a list or table.

### Localizing text

[Preparing views for localization](/documentation/SwiftUI/Preparing-views-for-localization)

Specify hints and add strings to localize your SwiftUI views.

[`LocalizedStringKey`](/documentation/SwiftUI/LocalizedStringKey)

The key used to look up an entry in a strings file or strings dictionary
file.

[`locale`](/documentation/SwiftUI/EnvironmentValues/locale)

The current locale that views should use.

[`typesettingLanguage(_:isEnabled:)`](/documentation/SwiftUI/View/typesettingLanguage(_:isEnabled:))

Specifies the language for typesetting.

[`TypesettingLanguage`](/documentation/SwiftUI/TypesettingLanguage)

Defines how typesetting language is determined for text.

### Deprecated types

[`ContentSizeCategory`](/documentation/SwiftUI/ContentSizeCategory)

The sizes that you can specify for content.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
