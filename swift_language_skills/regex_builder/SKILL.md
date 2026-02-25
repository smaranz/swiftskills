---
name: RegexBuilder
description: Rork-Max Quality skill for RegexBuilder. Actionable Swift language patterns and best practices.
---

# RegexBuilder

Use an expressive domain-specific language to build regular expressions,
for operations like searching and replacing in text.
Regular expressions, also known as regexes,
are a powerful tool for matching patterns in text.
Swift supports several ways to create a regular expression,
including from a string, as a literal, and using this DSL.
For example:
```swift
let word = OneOrMore(.word)
let emailPattern = Regex {
Capture {
ZeroOrMore {
word
"."
}
word
}
"@"
Capture {
word
OneOrMore {
"."
word
}
}
}
let text = "My email is my.name@example.com."
if let match = text.firstMatch(of: emailPattern) {
let (wholeMatch, name, domain) = match.output
// wholeMatch is "my.name@example.com"
// name is "my.name"
// domain is "example.com"
}
```

## 🚀 Rork-Max Quality Snippet

```swift
import RegexBuilder

// Type-safe regex with RegexBuilder (Swift 5.7+)
let dateRegex = Regex {
    Capture { OneOrMore(.digit) }          // Year
    "-"
    Capture { Repeat(.digit, count: 2) }   // Month
    "-"
    Capture { Repeat(.digit, count: 2) }   // Day
}

let input = "Event on 2025-06-15 at venue"
if let match = input.firstMatch(of: dateRegex) {
    let year = match.1   // "2025"
    let month = match.2  // "06"
    let day = match.3    // "15"
}

// With strong typing
let priceRegex = Regex {
    "$"
    Capture { .localizedDouble(locale: Locale(identifier: "en_US")) }
}
```

## 💎 Elite Implementation Tips

- Use `RegexBuilder` for complex patterns — it's type-safe and readable
- Use `Capture { }` for extracting matched groups with proper types
- Combine with `.localizedDouble()` and `.localizedInteger()` for locale-aware parsing

## When to Use

- Working with fundamental types: strings, numbers, collections
- Choosing between value types (structs/enums) and reference types (classes)
- Implementing protocols like `Codable`, `Hashable`, `Equatable`, `Comparable`

## Best Practices

- Use `Int` unless you have a specific reason for sized integers
- Prefer `[Element]` array literal syntax over `Array<Element>`
- Use `guard let` for early exits and `if let` for optional binding
- Leverage `Codable` for JSON parsing instead of manual dictionary access

## Common Pitfalls

- Floating-point equality checks — use `isApproximatelyEqual(to:)` or tolerances
- Force-unwrapping optionals (`!`) without safety checks
- String index arithmetic — Swift strings are not random-access, use `String.Index`

## Key APIs

### Components

| API | Purpose |
|-----|---------|
| `CharacterClass` | A class of characters that match in a regex. |
| `Anchor` | A regex component that matches a specific condition at a particular position |
| `Lookahead` | A regex component that allows a match to continue only if its contents |
| `NegativeLookahead` | A regex component that allows a match to continue only if its contents |
| `ChoiceOf` | A regex component that chooses exactly one of its constituent regex |

### Quantifiers

| API | Purpose |
|-----|---------|
| `One` | A regex component that matches exactly one occurrence of its underlying |
| `Optionally` | A regex component that matches zero or one occurrences of its underlying |
| `ZeroOrMore` | A regex component that matches zero or more occurrences of its underlying |
| `OneOrMore` | A regex component that matches one or more occurrences of its underlying |
| `Repeat` | A regex component that matches a selectable number of occurrences of its |
| `Local` | A regex component that represents an atomic group. |

### Captures

| API | Purpose |
|-----|---------|
| `Capture` | A regex component that saves the matched substring, or a transformed result, |
| `TryCapture` | A regex component that attempts to transform a matched substring, saving |
| `Reference` | A reference to a captured portion of a regular expression. |

### Builders

| API | Purpose |
|-----|---------|
| `RegexComponentBuilder` | A custom parameter attribute that constructs regular expressions from |
| `AlternationBuilder` | A custom parameter attribute that constructs regular expression alternations |
