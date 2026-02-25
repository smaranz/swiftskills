---
name: Text input and output
description: Rork-Max Quality skill for Text input and output. Actionable patterns and best practices for SwiftUI development.
---

# Text input and output

Display formatted text and get text input from the user.
To display read-only text, or read-only text paired with an image, use
the built-in `Text` or `Label` views, respectively. When you need to
collect text input from the user, use an appropriate text input view,
like `TextField` or `TextEditor`.
You add view modifiers to control the text’s font, selectability, alignment,
layout direction, and so on. These modifiers also affect other views that
display text, like the labels on controls, even if you don’t define an
explicit `Text` view.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct TextInputForm: View {
    @State private var name = ""
    @State private var bio = ""
    @FocusState private var focusedField: Field?

    enum Field { case name, bio }

    var body: some View {
        Form {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)
                .textContentType(.name)
                .submitLabel(.next)

            TextField("Bio", text: $bio, axis: .vertical)
                .focused($focusedField, equals: .bio)
                .lineLimit(3...6)

            Text("Preview: **\(name)**")
                .font(.body)
        }
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                Spacer()
                Button("Done") { focusedField = nil }
            }
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `TextField(_:text:axis:.vertical)` with `.lineLimit` for expandable multi-line input
- Set `.textContentType()` for autofill support (`.emailAddress`, `.password`, etc.)
- Add keyboard toolbar buttons with `ToolbarItemGroup(placement: .keyboard)`

## When to Use

- Displaying text with rich formatting, markdown, or attributed strings
- Rendering images from assets, SF Symbols, or async URLs
- Building interactive controls: buttons, toggles, pickers, sliders, steppers
- Creating menus, context menus, and keyboard shortcuts

## Best Practices

- Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography
- Prefer `AsyncImage` for remote images with placeholder and error states
- Use `Label` to pair text with icons — it adapts to context (list rows, menus, toolbars)
- Support Dynamic Type by using system text styles (`.title`, `.body`, `.caption`)

## Common Pitfalls

- Hard-coding font sizes instead of using Dynamic Type styles
- Loading large images synchronously on the main thread
- Forgetting to provide accessibility labels for image-only buttons

## Key APIs

### Displaying text

| API | Purpose |
|-----|---------|
| `Text` | A view that displays one or more lines of read-only text. |
| `Label` | A standard label for user interface items, consisting of an icon with a |
| `labelStyle(_:)` | Sets the style for labels within this view. |

### Getting text input

| API | Purpose |
|-----|---------|
| `Building rich SwiftUI text experiences` | Build an editor for formatted text using SwiftUI text editor views and attributed strings. |
| `TextField` | A control that displays an editable text interface. |
| `textFieldStyle(_:)` | Sets the style for text fields within this view. |
| `SecureField` | A control into which people securely enter private text. |
| `TextEditor` | A view that can display and edit long-form text. |

### Selecting text

| API | Purpose |
|-----|---------|
| `textSelection(_:)` | Controls whether people can select text within this view. |
| `TextSelectability` | A type that describes the ability to select text. |
| `TextSelection` | Represents a selection of text. |
| `textSelectionAffinity(_:)` | Sets the direction of a selection or cursor relative to a text character. |
| `textSelectionAffinity` | A representation of the direction or association of a selection or cursor |
| `TextSelectionAffinity` | A representation of the direction or association of a selection or cursor |
| `AttributedTextSelection` | Represents a selection of attributed text. |

### Setting a font

| API | Purpose |
|-----|---------|
| `Applying custom fonts to text` | Add and use a font in your app that scales with Dynamic Type. |
| `font(_:)` | Sets the default font for text in this view. |
| `fontDesign(_:)` | Sets the font design of the text in this view. |
| `fontWeight(_:)` | Sets the font weight of the text in this view. |
| `fontWidth(_:)` | Sets the font width of the text in this view. |
| `font` | The default font of this environment. |
| `Font` | An environment-dependent font. |

### Adjusting text size

| API | Purpose |
|-----|---------|
| `textScale(_:isEnabled:)` | Applies a text scale to text in the view. |
| `dynamicTypeSize(_:)` | Sets the Dynamic Type size within the view to the given value. |
| `dynamicTypeSize` | The current Dynamic Type size. |
| `DynamicTypeSize` | A Dynamic Type size, which specifies how large scalable content should be. |
| `ScaledMetric` | A dynamic property that scales a numeric value. |
| `TextVariantPreference` | A protocol for controlling the size variant of text views. |
| `FixedTextVariant` | The default text variant preference that chooses the largest available |
| `SizeDependentTextVariant` | The size dependent variant preference allows the text to take the available |

### Controlling text style

| API | Purpose |
|-----|---------|
| `bold(_:)` | Applies a bold font weight to the text in this view. |
| `italic(_:)` | Applies italics to the text in this view. |
| `underline(_:pattern:color:)` | Applies an underline to the text in this view. |
| `strikethrough(_:pattern:color:)` | Applies a strikethrough to the text in this view. |
| `textCase(_:)` | Sets a transform for the case of the text contained in this view when |
| `textCase` | A stylistic override to transform the case of `Text` when displayed, |
| `monospaced(_:)` | Modifies the fonts of all child views to use the fixed-width variant of |
| `monospacedDigit()` | Modifies the fonts of all child views to use fixed-width digits, if |

### Managing text layout

| API | Purpose |
|-----|---------|
| `truncationMode(_:)` | Sets the truncation mode for lines of text that are too long to fit in |
| `truncationMode` | A value that indicates how the layout truncates the last line of text to |
| `allowsTightening(_:)` | Sets whether text in this view can compress the space between characters |
| `allowsTightening` | A Boolean value that indicates whether inter-character spacing should |
| `minimumScaleFactor(_:)` | Sets the minimum amount that text in this view scales down to fit in the |
| `minimumScaleFactor` | The minimum permissible proportion to shrink the font size to fit |
| `baselineOffset(_:)` | Sets the vertical offset for the text relative to its baseline |
| `kerning(_:)` | Sets the spacing, or kerning, between characters for the text in this view. |

### Rendering text

| API | Purpose |
|-----|---------|
| `Creating visual effects with SwiftUI` | Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer. |
| `TextAttribute` | A value that you can attach to text views and that text renderers can query. |
| `textRenderer(_:)` | Returns a new view such that any text views within it will use |
| `TextRenderer` | A value that can replace the default text view rendering behavior. |
| `TextProxy` | A proxy for a text view that custom text renderers use. |

### Limiting line count for multiline text

| API | Purpose |
|-----|---------|
| `lineLimit(_:)` | Sets to a closed range the number of lines that text can occupy in |
| `lineLimit(_:reservesSpace:)` | Sets a limit for the number of lines text can occupy in this view. |
| `lineLimit` | The maximum number of lines that text can occupy in a view. |

### Formatting multiline text

| API | Purpose |
|-----|---------|
| `lineSpacing(_:)` | Sets the amount of space between lines of text in this view. |
| `lineSpacing` | The distance in points between the bottom of one line fragment and the |
| `multilineTextAlignment(_:)` | Sets the alignment of a text view that contains multiple lines of text. |
| `multilineTextAlignment` | An environment value that indicates how a text view aligns its lines |

### Formatting date and time

| API | Purpose |
|-----|---------|
| `SystemFormatStyle` | A namespace for format styles that implement designs used across Apple’s |
| `TimeDataSource` | A source of time related data. |

### Managing text entry

| API | Purpose |
|-----|---------|
| `autocorrectionDisabled(_:)` | Sets whether to disable autocorrection for this view. |
| `autocorrectionDisabled` | A Boolean value that determines whether the view hierarchy has |
| `keyboardType(_:)` | Sets the keyboard type for this view. |
| `scrollDismissesKeyboard(_:)` | Configures the behavior in which scrollable content interacts with |
| `textContentType(_:)` | Sets the text content type for this view, which the system uses to |
| `textInputAutocapitalization(_:)` | Sets how often the shift key in the keyboard is automatically enabled. |
| `TextInputAutocapitalization` | The kind of autocapitalization behavior applied during text input. |
| `textInputCompletion(_:)` | Associates a fully formed string with the value of this view when used |

### Dictating text

| API | Purpose |
|-----|---------|
| `searchDictationBehavior(_:)` | Configures the dictation behavior for any search fields configured |
| `TextInputDictationActivation` | — |

### Configuring the Writing Tools behavior

| API | Purpose |
|-----|---------|
| `writingToolsBehavior(_:)` | Specifies the Writing Tools behavior for text and text input in the |
| `WritingToolsBehavior` | The Writing Tools editing experience for text and text input. |

### Specifying text equivalents

| API | Purpose |
|-----|---------|
| `typeSelectEquivalent(_:)` | Sets an explicit type select equivalent text in a collection, such as |

### Localizing text

| API | Purpose |
|-----|---------|
| `Preparing views for localization` | Specify hints and add strings to localize your SwiftUI views. |
| `LocalizedStringKey` | The key used to look up an entry in a strings file or strings dictionary |
| `locale` | The current locale that views should use. |
| `typesettingLanguage(_:isEnabled:)` | Specifies the language for typesetting. |
| `TypesettingLanguage` | Defines how typesetting language is determined for text. |

### Deprecated types

| API | Purpose |
|-----|---------|
| `ContentSizeCategory` | The sizes that you can specify for content. |
