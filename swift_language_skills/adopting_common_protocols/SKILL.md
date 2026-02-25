---
name: Adopting Common Protocols
description: Rork-Max Quality skill for Adopting Common Protocols. Actionable Swift language patterns and best practices.
---

# Adopting Common Protocols

Make your custom types easier to use by ensuring that they conform to Swift protocols.
When using custom types to model data in your programs, you may frequently need to
check whether two values are the same or different, or whether a particular value
is included in a list of values. This capability, as well as the ability to store
values in a set or use them as keys in a dictionary, are governed by two related
standard library protocols, `Equatable` and `Hashable`.
- You can compare instances of an *equatable* type by using the equal-to (`==`) and
not-equal-to (`!=`) operators.
- An instance of a *hashable* type can reduce its value mathematically to a single
integer, which is used internally by sets and dictionaries to make lookups consistently
fast.
Many standard library types are both equatable and hashable, including strings, integers,
floating-point values, Boolean values, and collections of equatable and hashable
types. The `==` comparison and the `contains(_:)` method call in the following example
depend on strings and integers being equatable:
```swift
if username == "Arturo" {
print("Hi, Arturo!")
}
let favoriteNumbers = [4, 7, 8, 9]
if favoriteNumbers.contains(todaysDate.day) {
print("It's a good day today!")
}
```
Conforming to the `Equatable` and `Hashable` protocols is straightforward and makes
it easier to use your own types in Swift. It’s a good idea for all your custom model
types to conform.

## 🚀 Rork-Max Quality Snippet

```swift
struct Song: Identifiable, Hashable, Codable, Comparable, CustomStringConvertible {
    let id: UUID
    let title: String
    let artist: String
    let durationSeconds: Int

    // Comparable — sort by title
    static func < (lhs: Song, rhs: Song) -> Bool {
        lhs.title.localizedCompare(rhs.title) == .orderedAscending
    }

    // CustomStringConvertible — debug-friendly display
    var description: String {
        "\(title) by \(artist) (\(durationSeconds)s)"
    }
}

// Usage in SwiftUI
// ForEach(songs.sorted()) { song in Text(song.title) }
```

## 💎 Elite Implementation Tips

- Implement `Identifiable` on all types used with `ForEach` and `List`
- Use `localizedCompare` in `Comparable` for correct alphabetical sorting across locales
- Conform to `Hashable` for types used in `Set`, `Dictionary`, or `NavigationPath`

## When to Use

- Designing app data models with structs, classes, and enums
- Choosing between value semantics (struct) and reference semantics (class)
- Implementing protocol conformances for custom types

## Best Practices

- Default to structs — use classes only when identity or inheritance is needed
- Implement `Equatable` and `Hashable` for types used in collections or SwiftUI
- Use enums with associated values for state machines and API responses

## Common Pitfalls

- Using classes when structs would be simpler and safer
- Forgetting that struct mutations create new copies — this matters for large data
- Not implementing `Hashable` on types used as `ForEach` identifiers


