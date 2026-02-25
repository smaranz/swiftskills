---
name: String
description: Rork-Max Quality skill for String. Actionable Swift language patterns and best practices.
---

# String

A Unicode string value that is a collection of characters.
```
@frozen struct String
```
A string is a series of characters, such as `"Swift"`, that forms a
collection. Strings in Swift are Unicode correct and locale insensitive,
and are designed to be efficient. The `String` type bridges with the
Objective-C class `NSString` and offers interoperability with C functions
that works with strings.
You can create new strings using string literals or string interpolations.
A *string literal* is a series of characters enclosed in quotes.
```
let greeting = "Welcome!"
```
*String interpolations* are string literals that evaluate any included
expressions and convert the results to string form. String interpolations
give you an easy way to build a string from multiple pieces. Wrap each
expression in a string interpolation in parentheses, prefixed by a
backslash.
```
let name = "Rosa"
let personalizedGreeting = "Welcome, \(name)!"
// personalizedGreeting == "Welcome, Rosa!"
let price = 2
let number = 3
let cookiePrice = "\(number) cookies: $\(price * number)."
// cookiePrice == "3 cookies: $6."
```
Combine strings using the concatenation operator (`+`).
```
let longerGreeting = greeting + " We're glad you're here!"
// longerGreeting == "Welcome! We're glad you're here!"
```
Multiline string literals are enclosed in three double quotation marks
(`"""`), with each delimiter on its own line. Indentation is stripped from
each line of a multiline string literal to match the indentation of the
closing delimiter.
```
let banner = """
__,
( o /) _/_
`. , , , , // /
(___)(_(_/_(_ //_ (__
/)
(/
"""
```
# Modifying and Comparing Strings
Strings always have value semantics. Modifying a copy of a string leaves
the original unaffected.
```
var otherGreeting = greeting
otherGreeting += " Have a nice time!"
// otherGreeting == "Welcome! Have a nice time!"
print(greeting)
// Prints "Welcome!"
```
Comparing strings for equality using the equal-to operator (`==`) or a
relational operator (like `<` or `>=`) is always performed using Unicode
canonical representation. As a result, different representations of a
string compare as being equal.
```
let cafe1 = "Cafe\u{301}"
let cafe2 = "Café"
print(cafe1 == cafe2)
// Prints "true"
```
The Unicode scalar value `"\u{301}"` modifies the preceding character to
include an accent, so `"e\u{301}"` has the same canonical representation
as the single Unicode scalar value `"é"`.
Basic string operations are not sensitive to locale settings, ensuring that
string comparisons and other operations always have a single, stable
result, allowing strings to be used as keys in `Dictionary` instances and
for other purposes.
# Accessing String Elements
A string is a collection of *extended grapheme clusters*, which approximate
human-readable characters. Many individual characters, such as “é”, “김”,
and “🇮🇳”, can be made up of multiple Unicode scalar values. These scalar
values are combined by Unicode’s boundary algorithms into extended
grapheme clusters, represented by the Swift `Character` type. Each element
of a string is represented by a `Character` instance.
For example, to retrieve the first word of a longer string, you can search
for a space and then create a substring from a prefix of the string up to
that point:
```
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
// firstName == "Marie"
```
The `firstName` constant is an instance of the `Substring` type—a type
that represents substrings of a string while sharing the original string’s
storage. Substrings present the same interface as strings.
```
print("\(name)'s first name has \(firstName.count) letters.")
// Prints "Marie Curie's first name has 5 letters."
```
# Accessing a String’s Unicode Representation
If you need to access the contents of a string as encoded in different
Unicode encodings, use one of the string’s `unicodeScalars`, `utf16`, or
`utf8` properties. Each property provides access to a view of the string
as a series of code units, each encoded in a different Unicode encoding.
To demonstrate the different views available for every string, the
following examples use this `String` instance:
```
let cafe = "Cafe\u{301} du 🌍"
print(cafe)
// Prints "Café du 🌍"
```
The `cafe` string is a collection of the nine characters that are visible
when the string is displayed.
```
print(cafe.count)
// Prints "9"
print(Array(cafe))
// Prints "["C", "a", "f", "é", " ", "d", "u", " ", "🌍"]"
```

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// String — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with String.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

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

### Creating a String

| API | Purpose |
|-----|---------|
| `init(decoding:)` | Creates a string by interpreting the file path’s content as UTF-8 on Unix |
| `init()` | Creates an empty string. |
| `init(_:)` | Creates a string containing the given character. |
| `init(_:)` | Creates a new string containing the characters in the given sequence. |
| `init(_:)` | Creates a new instance of a collection containing the elements of a |
| `init(_:)` | Creates a new string containing the characters in the given sequence. |
| `init(_:)` | Creates a new string from the given substring. |
| `init(repeating:count:)` | Creates a new string representing the given string repeated the specified |

### Inspecting a String

| API | Purpose |
|-----|---------|
| `isEmpty` | A Boolean value indicating whether a string has no characters. |
| `count` | The number of characters in a string. |

### Creating a String from Unicode Data

| API | Purpose |
|-----|---------|
| `init(_:)` | — |
| `init(data:encoding:)` | Returns a `String` initialized by converting given `data` into |
| `init(validatingUTF8:)` | Creates a new string by copying and validating the null-terminated UTF-8 |
| `init(validating:as:)` | Creates a new string by copying and validating the sequence of |
| `init(validating:as:)` | Creates a new string by copying and validating the sequence of |
| `init(utf8String:)` | Creates a string by copying the data from a given |
| `init(utf8String:)` | Creates a string by copying the data from a given |
| `init(utf16CodeUnits:count:)` | Creates a new string that contains the specified number of characters |

### Creating a String Using Formats

| API | Purpose |
|-----|---------|
| `init(format:_:)` | Returns a `String` object initialized by using a given |
| `init(format:arguments:)` | Returns a `String` object initialized by using a given |
| `init(format:locale:_:)` | Returns a `String` object initialized by using a given |
| `init(format:locale:arguments:)` | Returns a `String` object initialized by using a given |
| `localizedStringWithFormat(_:_:)` | Returns a string created by using a given format string as a |

### Creating a Localized String

| API | Purpose |
|-----|---------|
| `init(localized:table:bundle:locale:comment:)` | Creates a localized string from an interpolated string. |
| `init(localized:options:table:bundle:locale:comment:)` | Creates a localized string from an interpolated string, applying the specified options. |
| `String.LocalizationValue` | A reference to a localizable string, with optional string interpolation. |
| `String.LocalizationOptions` | Options to apply when initializing a localized string. |
| `init(localized:defaultValue:table:bundle:locale:comment:)` | Creates a localized string from an arbitrary static string key. |
| `init(localized:defaultValue:options:table:bundle:locale:comment:)` | Creates a localized string from an arbitrary static string key, applying the specified options. |
| `init(localized:)` | Creates a localized string from a localized string resource. |
| `init(localized:options:)` | Creates a localized string from a localized string resource, applying the specified options. |

### Converting Numeric Values

| API | Purpose |
|-----|---------|
| `init(_:radix:uppercase:)` | Creates a string representing the given value in base 10, or some other |

### Converting a C String

| API | Purpose |
|-----|---------|
| `init(bytes:encoding:)` | Creates a new string equivalent to the given bytes interpreted in the specified encoding. |
| `init(bytesNoCopy:length:encoding:freeWhenDone:)` | Creates a new string that contains the specified number of bytes from the |
| `init(validatingCString:)` | Creates a new string by copying and validating the null-terminated UTF-8 |
| `init(validatingCString:)` | Creates a new string by copying and validating the null-terminated UTF-8 |
| `init(cString:)` | Creates a new string by copying the null-terminated UTF-8 data referenced |
| `init(cString:)` | Creates a new string by copying the null-terminated UTF-8 data referenced |
| `init(cString:encoding:)` | Produces a string by copying the null-terminated bytes |
| `init(cString:encoding:)` | Produces a string by copying the null-terminated bytes |

### Converting Other Types to Strings

| API | Purpose |
|-----|---------|
| `init(_:)` | Creates an instance from the description of a given |
| `init(describing:)` | Creates a string representing the given value. |
| `init(describing:)` | Creates a string representing the given value. |
| `init(describing:)` | Creates a string representing the given value. |
| `init(describing:)` | Creates a string representing the given value. |
| `init(reflecting:)` | Creates a string with a detailed representation of the given value, |

### Creating a String from a File or URL

| API | Purpose |
|-----|---------|
| `init(contentsOf:)` | — |
| `init(contentsOf:encoding:)` | Produces a string created by reading data from a given URL interpreted using a given encoding. |
| `init(contentsOf:usedEncoding:)` | Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data. |
| `init(contentsOfFile:)` | — |
| `init(contentsOfFile:encoding:)` | Produces a string created by reading data from the file at a given path interpreted using a given encoding. |
| `init(contentsOfFile:usedEncoding:)` | Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file. |

### Writing to a File or URL

| API | Purpose |
|-----|---------|
| `write(_:)` | Appends the given string to this string. |
| `write(to:)` | Writes the string into the given output stream. |

### Appending Strings and Characters

| API | Purpose |
|-----|---------|
| `append(_:)` | Appends the given string to this string. |
| `append(_:)` | Appends the given character to the string. |
| `append(contentsOf:)` | — |
| `append(contentsOf:)` | — |
| `append(contentsOf:)` | Appends the characters in the given sequence to the string. |
| `append(contentsOf:)` | Adds the elements of a sequence or collection to the end of this |
| `reserveCapacity(_:)` | Reserves enough space in the string’s underlying storage to store the |
| `+(_:_:)` | — |

### Inserting Characters

| API | Purpose |
|-----|---------|
| `insert(_:at:)` | Inserts a new character at the specified position. |
| `insert(_:at:)` | Inserts a new element into the collection at the specified position. |
| `insert(contentsOf:at:)` | Inserts the elements of a sequence into the collection at the specified |
| `insert(contentsOf:at:)` | Inserts a collection of characters at the specified position. |

### Replacing Substrings

| API | Purpose |
|-----|---------|
| `replaceSubrange(_:with:)` | Replaces the text within the specified bounds with the given characters. |
| `replaceSubrange(_:with:)` | Replaces the specified subrange of elements with the given collection. |

### Removing Substrings

| API | Purpose |
|-----|---------|
| `remove(at:)` | Removes and returns the character at the specified position. |
| `remove(at:)` | Removes and returns the element at the specified position. |
| `removeAll(keepingCapacity:)` | Replaces this string with the empty string. |
| `removeAll(where:)` | Removes all the elements that satisfy the given predicate. |
| `removeFirst()` | Removes and returns the first element of the collection. |
| `removeFirst(_:)` | Removes the specified number of elements from the beginning of the |
| `removeLast()` | Removes and returns the last element of the collection. |
| `removeLast(_:)` | Removes the specified number of elements from the end of the |

### Changing Case

| API | Purpose |
|-----|---------|
| `lowercased()` | Returns a lowercase version of the string. |
| `uppercased()` | Returns an uppercase version of the string. |

### Comparing Strings Using Operators

| API | Purpose |
|-----|---------|
| `==(_:_:)` | Returns a Boolean value indicating whether two values are equal. |
| `==(_:_:)` | — |
| `!=(_:_:)` | Returns a Boolean value indicating whether two values are not equal. |
| `!=(_:_:)` | — |

### Comparing Characters

| API | Purpose |
|-----|---------|
| `elementsEqual(_:)` | Returns a Boolean value indicating whether this sequence and another |
| `elementsEqual(_:by:)` | Returns a Boolean value indicating whether this sequence and another |
| `starts(with:)` | Returns a Boolean value indicating whether the initial elements of the |
| `starts(with:by:)` | Returns a Boolean value indicating whether the initial elements of the |
| `lexicographicallyPrecedes(_:)` | Returns a Boolean value indicating whether the sequence precedes another |
| `lexicographicallyPrecedes(_:by:)` | Returns a Boolean value indicating whether the sequence precedes another |

### Creating and Applying Differences

| API | Purpose |
|-----|---------|
| `applying(_:)` | Applies the given difference to this collection. |
| `difference(from:)` | Returns the difference needed to produce this collection’s ordered |
| `difference(from:by:)` | Returns the difference needed to produce this collection’s ordered |

### Finding Substrings

| API | Purpose |
|-----|---------|
| `hasPrefix(_:)` | — |

### Finding Characters

| API | Purpose |
|-----|---------|
| `contains(_:)` | Returns a Boolean value indicating whether the sequence contains the |
| `allSatisfy(_:)` | Returns a Boolean value indicating whether every element of a sequence |
| `contains(where:)` | Returns a Boolean value indicating whether the sequence contains an |
| `first(where:)` | Returns the first element of the sequence that satisfies the given |
| `firstIndex(of:)` | Returns the first index where the specified value appears in the |
| `firstIndex(where:)` | Returns the first index in which an element of the collection satisfies |
| `last(where:)` | Returns the last element of the sequence that satisfies the given |
| `lastIndex(of:)` | Returns the last index where the specified value appears in the |

### Getting Substrings

| API | Purpose |
|-----|---------|
| `subscript(_:)` | Accesses a contiguous subrange of the collection’s elements. |
| `subscript(_:)` | Accesses the contiguous subrange of the collection’s elements specified |
| `subscript(_:)` | — |
| `prefix(_:)` | Returns a subsequence, up to the specified maximum length, containing |
| `prefix(through:)` | Returns a subsequence from the start of the collection through the |
| `prefix(upTo:)` | Returns a subsequence from the start of the collection up to, but not |
| `prefix(while:)` | Returns a subsequence containing the initial elements until `predicate` |
| `suffix(_:)` | Returns a subsequence, up to the given maximum length, containing the |

### Splitting a String

| API | Purpose |
|-----|---------|
| `split(separator:maxSplits:omittingEmptySubsequences:)` | Returns the longest possible subsequences of the collection, in order, |
| `split(maxSplits:omittingEmptySubsequences:whereSeparator:)` | Returns the longest possible subsequences of the collection, in order, |

### Getting Characters and Bytes

| API | Purpose |
|-----|---------|
| `subscript(_:)` | Accesses the character at the given position. |
| `first` | The first element of the collection. |
| `last` | The last element of the collection. |
| `randomElement()` | Returns a random element of the collection. |
| `randomElement(using:)` | Returns a random element of the collection, using the given generator as |

### Working with Encodings

| API | Purpose |
|-----|---------|
| `availableStringEncodings` | An array of the encodings that strings support in the application’s |
| `defaultCStringEncoding` | The C-string encoding assumed for any method accepting a C string as an |
| `localizedName(of:)` | Returns a human-readable string giving the name of the specified encoding. |
| `isContiguousUTF8` | Returns whether this string’s storage contains |
| `makeContiguousUTF8()` | If this string is not contiguous, make it so. If this mutates the string, |
| `withUTF8(_:)` | Runs `body` over the content of this string in contiguous memory. If this |

### Working with String Views

| API | Purpose |
|-----|---------|
| `unicodeScalars` | The string’s value represented as a collection of Unicode scalar values. |
| `init(_:)` | Creates a string corresponding to the given collection of Unicode |
| `init(_:)` | Creates a String having the given content. |
| `utf16` | A UTF-16 encoding of `self`. |
| `init(_:)` | Creates a string corresponding to the given sequence of UTF-16 code units. |
| `init(_:)` | Creates a String having the given content. |
| `utf8` | A UTF-8 encoding of `self`. |
| `init(_:)` | Creates a string corresponding to the given sequence of UTF-8 code units. |

### Transforming a String’s Characters

| API | Purpose |
|-----|---------|
| `compactMap(_:)` | Returns an array containing the non-`nil` results of calling the given |
| `flatMap(_:)` | Returns an array containing the concatenated results of calling the |
| `flatMap(_:)` | — |
| `reduce(_:_:)` | Returns the result of combining the elements of the sequence using the |
| `reduce(into:_:)` | Returns the result of combining the elements of the sequence using the |
| `lazy` | A sequence containing the same elements as this sequence, |

### Iterating over a String’s Characters

| API | Purpose |
|-----|---------|
| `forEach(_:)` | Calls the given closure on each element in the sequence in the same order |
| `enumerated()` | Returns a sequence of pairs (*n*, *x*), where *n* represents a |
| `makeIterator()` | Returns an iterator over the elements of the collection. |
| `underestimatedCount` | A value less than or equal to the number of elements in the collection. |

### Reordering a String’s Characters

| API | Purpose |
|-----|---------|
| `sorted()` | Returns the elements of the sequence, sorted. |
| `sorted(by:)` | Returns the elements of the sequence, sorted using the given predicate as |
| `reversed()` | Returns a view presenting the elements of the collection in reverse |
| `shuffled()` | Returns the elements of the sequence, shuffled. |
| `shuffled(using:)` | Returns the elements of the sequence, shuffled using the given generator |

### Getting C Strings

| API | Purpose |
|-----|---------|
| `utf8CString` | A contiguously stored null-terminated UTF-8 representation of the string. |
| `withCString(_:)` | Calls the given closure with a pointer to the contents of the string, |
| `withCString(encodedAs:_:)` | Calls the given closure with a pointer to the contents of the string, |

### Working with Paths

| API | Purpose |
|-----|---------|
| `init(_:)` | — |

### Manipulating Indices

| API | Purpose |
|-----|---------|
| `startIndex` | The position of the first character in a nonempty string. |
| `endIndex` | A string’s “past the end” position—that is, the position one greater |
| `index(after:)` | Returns the position immediately after the given index. |
| `formIndex(after:)` | Replaces the given index with its successor. |
| `index(before:)` | Returns the position immediately before the given index. |
| `formIndex(before:)` | Replaces the given index with its predecessor. |
| `index(_:offsetBy:)` | Returns an index that is the specified distance from the given index. |
| `index(_:offsetBy:limitedBy:)` | Returns an index that is the specified distance from the given index, |

### Creating a Range Expression

| API | Purpose |
|-----|---------|
| `...(_:_:)` | Returns a closed range that contains both of its bounds. |
| `...(_:)` | Returns a partial range up to, and including, its upper bound. |
| `...(_:)` | Returns a partial range extending upward from a lower bound. |

### Encoding and Decoding

| API | Purpose |
|-----|---------|
| `encode(to:)` | Encodes this value into the given encoder. |
| `init(from:)` | Creates a new instance by decoding from the given decoder. |

### Describing a String

| API | Purpose |
|-----|---------|
| `description` | The value of this string. |
| `debugDescription` | A representation of the string that is suitable for debugging. |
| `customMirror` | A mirror that reflects the `String` instance. |
| `hashValue` | The hash value. |
| `hash(into:)` | Hashes the essential components of this value by feeding them into the |

### Infrequently Used Functionality

| API | Purpose |
|-----|---------|
| `index(of:)` | Returns the first index where the specified value appears in the |
| `init(_:)` | — |
| `init(stringInterpolation:)` | Creates a new instance from an interpolated string literal. |
| `init(stringLiteral:)` | Creates an instance initialized to the given string value. |
| `init(unicodeScalarLiteral:)` | — |
| `init(extendedGraphemeClusterLiteral:)` | — |
| `customPlaygroundQuickLook` | A custom playground Quick Look for the `String` instance. |
| `withContiguousStorageIfAvailable(_:)` | Executes a closure on the sequence’s contiguous storage. |

### Related String Types

| API | Purpose |
|-----|---------|
| `Substring` | A slice of a string. |
| `StringProtocol` | A type that can represent a string as a collection of characters. |
| `String.Index` | A position of a character or code unit in a string. |
| `String.UnicodeScalarView` | A view of a string’s contents as a collection of Unicode scalar values. |
| `String.UTF16View` | A view of a string’s contents as a collection of UTF-16 code units. |
| `String.UTF8View` | A view of a string’s contents as a collection of UTF-8 code units. |
| `String.Iterator` | A type that provides the collection’s iteration interface and |
| `String.Encoding` | — |
