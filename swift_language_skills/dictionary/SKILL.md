---
name: Dictionary
description: Apple Swift Documentation for Dictionary.
---

# Dictionary

A collection whose elements are key-value pairs.

```
@frozen struct Dictionary<Key, Value> where Key : Hashable
```

## Overview

A dictionary is a type of hash table, providing fast access to the entries
it contains. Each entry in the table is identified using its key, which is
a hashable type such as a string or number. You use that key to retrieve
the corresponding value, which can be any object. In other languages,
similar data types are known as hashes or associated arrays.

Create a new dictionary by using a dictionary literal. A dictionary literal
is a comma-separated list of key-value pairs, in which a colon separates
each key from its associated value, surrounded by square brackets. You can
assign a dictionary literal to a variable or constant or pass it to a
function that expects a dictionary.

Here’s how you would create a dictionary of HTTP response codes and their
related messages:

```
var responseMessages = [200: "OK",
                        403: "Access forbidden",
                        404: "File not found",
                        500: "Internal server error"]
```

The `responseMessages` variable is inferred to have type `[Int: String]`.
The `Key` type of the dictionary is `Int`, and the `Value` type of the
dictionary is `String`.

To create a dictionary with no key-value pairs, use an empty dictionary
literal (`[:]`).

```
var emptyDict: [String: String] = [:]
```

Any type that conforms to the `Hashable` protocol can be used as a
dictionary’s `Key` type, including all of Swift’s basic types. You can use
your own custom types as dictionary keys by making them conform to the
`Hashable` protocol.

# Getting and Setting Dictionary Values

The most common way to access values in a dictionary is to use a key as a
subscript. Subscripting with a key takes the following form:

```
print(responseMessages[200])
// Prints "Optional("OK")"
```

Subscripting a dictionary with a key returns an optional value, because a
dictionary might not hold a value for the key that you use in the
subscript.

The next example uses key-based subscripting of the `responseMessages`
dictionary with two keys that exist in the dictionary and one that does
not.

```
let httpResponseCodes = [200, 403, 301]
for code in httpResponseCodes {
    if let message = responseMessages[code] {
        print("Response \(code): \(message)")
    } else {
        print("Unknown response \(code)")
    }
}
// Prints "Response 200: OK"
// Prints "Response 403: Access forbidden"
// Prints "Unknown response 301"
```

You can also update, modify, or remove keys and values from a dictionary
using the key-based subscript. To add a new key-value pair, assign a value
to a key that isn’t yet a part of the dictionary.

```
responseMessages[301] = "Moved permanently"
print(responseMessages[301])
// Prints "Optional("Moved permanently")"
```

Update an existing value by assigning a new value to a key that already
exists in the dictionary. If you assign `nil` to an existing key, the key
and its associated value are removed. The following example updates the
value for the `404` code to be simply “Not found” and removes the
key-value pair for the `500` code entirely.

```
responseMessages[404] = "Not found"
responseMessages[500] = nil
print(responseMessages)
// Prints "[301: "Moved permanently", 200: "OK", 403: "Access forbidden", 404: "Not found"]"
```

In a mutable `Dictionary` instance, you can modify in place a value that
you’ve accessed through a keyed subscript. The code sample below declares a
dictionary called `interestingNumbers` with string keys and values that
are integer arrays, then sorts each array in-place in descending order.

```
var interestingNumbers = ["primes": [2, 3, 5, 7, 11, 13, 17],
                          "triangular": [1, 3, 6, 10, 15, 21, 28],
                          "hexagonal": [1, 6, 15, 28, 45, 66, 91]]
for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// Prints "[17, 13, 11, 7, 5, 3, 2]"
```

# Iterating Over the Contents of a Dictionary

Every dictionary is an unordered collection of key-value pairs. You can
iterate over a dictionary using a `for`-`in` loop, decomposing each
key-value pair into the elements of a tuple.

```
let imagePaths = ["star": "/glyphs/star.png",
                  "portrait": "/images/content/portrait.jpg",
                  "spacer": "/images/shared/spacer.gif"]

for (name, path) in imagePaths {
    print("The path to '\(name)' is '\(path)'.")
}
// Prints "The path to 'star' is '/glyphs/star.png'."
// Prints "The path to 'portrait' is '/images/content/portrait.jpg'."
// Prints "The path to 'spacer' is '/images/shared/spacer.gif'."
```

The order of key-value pairs in a dictionary is stable between mutations
but is otherwise unpredictable. If you need an ordered collection of
key-value pairs and don’t need the fast key lookup that `Dictionary`
provides, see the `KeyValuePairs` type for an alternative.

You can search a dictionary’s contents for a particular value using the
`contains(where:)` or `firstIndex(where:)` methods supplied by default
implementation. The following example checks to see if `imagePaths` contains
any paths in the `"/glyphs"` directory:

```
let glyphIndex = imagePaths.firstIndex(where: { $0.value.hasPrefix("/glyphs") })
if let index = glyphIndex {
    print("The '\(imagePaths[index].key)' image is a glyph.")
} else {
    print("No glyphs found!")
}
// Prints "The 'star' image is a glyph."
```

Note that in this example, `imagePaths` is subscripted using a dictionary
index. Unlike the key-based subscript, the index-based subscript returns
the corresponding key-value pair as a non-optional tuple.

```
print(imagePaths[glyphIndex!])
// Prints "(key: "star", value: "/glyphs/star.png")"
```

A dictionary’s indices stay valid across additions to the dictionary as
long as the dictionary has enough capacity to store the added values
without allocating more buffer. When a dictionary outgrows its buffer,
existing indices may be invalidated without any notification.

When you know how many new values you’re adding to a dictionary, use the
`init(minimumCapacity:)` initializer to allocate the correct amount of
buffer.

# Bridging Between Dictionary and NSDictionary

You can bridge between `Dictionary` and `NSDictionary` using the `as`
operator. For bridging to be possible, the `Key` and `Value` types of a
dictionary must be classes, `@objc` protocols, or types that bridge to
Foundation types.

Bridging from `Dictionary` to `NSDictionary` always takes O(1) time and
space. When the dictionary’s `Key` and `Value` types are neither classes
nor `@objc` protocols, any required bridging of elements occurs at the
first access of each element. For this reason, the first operation that
uses the contents of the dictionary may take O(*n*).

Bridging from `NSDictionary` to `Dictionary` first calls the `copy(with:)`
method (`- copyWithZone:` in Objective-C) on the dictionary to get an
immutable copy and then performs additional Swift bookkeeping work that
takes O(1) time. For instances of `NSDictionary` that are already
immutable, `copy(with:)` usually returns the same dictionary in O(1) time;
otherwise, the copying performance is unspecified. The instances of
`NSDictionary` and `Dictionary` share buffer using the same copy-on-write
optimization that is used when two instances of `Dictionary` share
buffer.

## Topics

### Creating a Dictionary

In addition to using a dictionary literal, you can also create a dictionary using
these initializers.

[`init()`](/documentation/Swift/Dictionary/init())

Creates an empty dictionary.

[`init(minimumCapacity:)`](/documentation/Swift/Dictionary/init(minimumCapacity:))

Creates an empty dictionary with preallocated space for at least the
specified number of elements.

[`init(uniqueKeysWithValues:)`](/documentation/Swift/Dictionary/init(uniqueKeysWithValues:))

Creates a new dictionary from the key-value pairs in the given sequence.

[`init(_:uniquingKeysWith:)`](/documentation/Swift/Dictionary/init(_:uniquingKeysWith:))

Creates a new dictionary from the key-value pairs in the given sequence,
using a combining closure to determine the value for any duplicate keys.

[`init(grouping:by:)`](/documentation/Swift/Dictionary/init(grouping:by:))

Creates a new dictionary whose keys are the groupings returned by the
given closure and whose values are arrays of the elements that returned
each key.

### Inspecting a Dictionary

[`isEmpty`](/documentation/Swift/Dictionary/isEmpty)

A Boolean value that indicates whether the dictionary is empty.

[`count`](/documentation/Swift/Dictionary/count)

The number of key-value pairs in the dictionary.

[`capacity`](/documentation/Swift/Dictionary/capacity)

The total number of key-value pairs that the dictionary can contain without
allocating new storage.

### Accessing Keys and Values

[`subscript(_:)`](/documentation/Swift/Dictionary/subscript(_:)-8rfql)

Accesses the value associated with the given key for reading and writing.

[`subscript(_:default:)`](/documentation/Swift/Dictionary/subscript(_:default:))

Accesses the value with the given key, falling back to the given default
value if the key isn’t found.

[`index(forKey:)`](/documentation/Swift/Dictionary/index(forKey:))

Returns the index for the given key.

[`subscript(_:)`](/documentation/Swift/Dictionary/subscript(_:)-4bhoo)

Accesses the key-value pair at the specified position.

[`keys`](/documentation/Swift/Dictionary/keys-swift.property)

A collection containing just the keys of the dictionary.

[`values`](/documentation/Swift/Dictionary/values-swift.property)

A collection containing just the values of the dictionary.

[`first`](/documentation/Swift/Dictionary/first)

The first element of the collection.

[`randomElement()`](/documentation/Swift/Dictionary/randomElement())

Returns a random element of the collection.

[`randomElement(using:)`](/documentation/Swift/Dictionary/randomElement(using:))

Returns a random element of the collection, using the given generator as
a source for randomness.

### Adding Keys and Values

[`updateValue(_:forKey:)`](/documentation/Swift/Dictionary/updateValue(_:forKey:))

Updates the value stored in the dictionary for the given key, or adds a
new key-value pair if the key does not exist.

[`merge(_:uniquingKeysWith:)`](/documentation/Swift/Dictionary/merge(_:uniquingKeysWith:)-m2ub)

Merges the given dictionary into this dictionary, using a combining
closure to determine the value for any duplicate keys.

[`merge(_:uniquingKeysWith:)`](/documentation/Swift/Dictionary/merge(_:uniquingKeysWith:)-7smbb)

Merges the key-value pairs in the given sequence into the dictionary,
using a combining closure to determine the value for any duplicate keys.

[`merging(_:uniquingKeysWith:)`](/documentation/Swift/Dictionary/merging(_:uniquingKeysWith:)-3vtfs)

Creates a dictionary by merging the given dictionary into this
dictionary, using a combining closure to determine the value for
duplicate keys.

[`merging(_:uniquingKeysWith:)`](/documentation/Swift/Dictionary/merging(_:uniquingKeysWith:)-9bik6)

Creates a dictionary by merging key-value pairs in a sequence into the
dictionary, using a combining closure to determine the value for
duplicate keys.

[`reserveCapacity(_:)`](/documentation/Swift/Dictionary/reserveCapacity(_:))

Reserves enough space to store the specified number of key-value pairs.

### Removing Keys and Values

[`filter(_:)`](/documentation/Swift/Dictionary/filter(_:))

Returns a new dictionary containing the key-value pairs of the dictionary
that satisfy the given predicate.

[`removeValue(forKey:)`](/documentation/Swift/Dictionary/removeValue(forKey:))

Removes the given key and its associated value from the dictionary.

[`remove(at:)`](/documentation/Swift/Dictionary/remove(at:))

Removes and returns the key-value pair at the specified index.

[`removeAll(keepingCapacity:)`](/documentation/Swift/Dictionary/removeAll(keepingCapacity:))

Removes all key-value pairs from the dictionary.

### Comparing Dictionaries

[`==(_:_:)`](/documentation/Swift/Dictionary/==(_:_:))

Returns a Boolean value indicating whether two values are equal.

[`!=(_:_:)`](/documentation/Swift/Dictionary/!=(_:_:))

Returns a Boolean value indicating whether two values are not equal.

### Iterating over Keys and Values

[`forEach(_:)`](/documentation/Swift/Dictionary/forEach(_:))

Calls the given closure on each element in the sequence in the same order
as a `for`-`in` loop.

[`enumerated()`](/documentation/Swift/Dictionary/enumerated())

Returns a sequence of pairs (*n*, *x*), where *n* represents a
consecutive integer starting at zero and *x* represents an element of
the sequence.

[`lazy`](/documentation/Swift/Dictionary/lazy)

A sequence containing the same elements as this sequence,
but on which some operations, such as `map` and `filter`, are
implemented lazily.

[`makeIterator()`](/documentation/Swift/Dictionary/makeIterator())

Returns an iterator over the dictionary’s key-value pairs.

[`underestimatedCount`](/documentation/Swift/Dictionary/underestimatedCount)

A value less than or equal to the number of elements in the collection.

### Finding Elements

[`contains(where:)`](/documentation/Swift/Dictionary/contains(where:))

Returns a Boolean value indicating whether the sequence contains an
element that satisfies the given predicate.

[`allSatisfy(_:)`](/documentation/Swift/Dictionary/allSatisfy(_:))

Returns a Boolean value indicating whether every element of a sequence
satisfies a given predicate.

[`first(where:)`](/documentation/Swift/Dictionary/first(where:))

Returns the first element of the sequence that satisfies the given
predicate.

[`firstIndex(where:)`](/documentation/Swift/Dictionary/firstIndex(where:))

Returns the first index in which an element of the collection satisfies
the given predicate.

[`min(by:)`](/documentation/Swift/Dictionary/min(by:))

Returns the minimum element in the sequence, using the given predicate as
the comparison between elements.

[`max(by:)`](/documentation/Swift/Dictionary/max(by:))

Returns the maximum element in the sequence, using the given predicate
as the comparison between elements.

### Transforming a Dictionary

[`mapValues(_:)`](/documentation/Swift/Dictionary/mapValues(_:))

Returns a new dictionary containing the keys of this dictionary with the
values transformed by the given closure.

[`reduce(_:_:)`](/documentation/Swift/Dictionary/reduce(_:_:))

Returns the result of combining the elements of the sequence using the
given closure.

[`reduce(into:_:)`](/documentation/Swift/Dictionary/reduce(into:_:))

Returns the result of combining the elements of the sequence using the
given closure.

[`compactMap(_:)`](/documentation/Swift/Dictionary/compactMap(_:))

Returns an array containing the non-`nil` results of calling the given
transformation with each element of this sequence.

[`compactMapValues(_:)`](/documentation/Swift/Dictionary/compactMapValues(_:))

Returns a new dictionary containing only the key-value pairs that have
non-`nil` values as the result of transformation by the given closure.

[`flatMap(_:)`](/documentation/Swift/Dictionary/flatMap(_:)-i3ly)

Returns an array containing the concatenated results of calling the
given transformation with each element of this sequence.

[`flatMap(_:)`](/documentation/Swift/Dictionary/flatMap(_:)-6chv9)

[`sorted(by:)`](/documentation/Swift/Dictionary/sorted(by:))

Returns the elements of the sequence, sorted using the given predicate as
the comparison between elements.

[`shuffled()`](/documentation/Swift/Dictionary/shuffled())

Returns the elements of the sequence, shuffled.

[`shuffled(using:)`](/documentation/Swift/Dictionary/shuffled(using:))

Returns the elements of the sequence, shuffled using the given generator
as a source for randomness.

### Performing Collection Operations

  <doc://com.apple.Swift/documentation/Swift/order-dependent-operations-on-dictionary>

### Encoding and Decoding

[`encode(to:)`](/documentation/Swift/Dictionary/encode(to:))

Encodes the contents of this dictionary into the given encoder.

[`init(from:)`](/documentation/Swift/Dictionary/init(from:)-6e6js)

Creates a new dictionary by decoding from the given decoder.

### Describing a Dictionary

[`description`](/documentation/Swift/Dictionary/description)

A string that represents the contents of the dictionary.

[`debugDescription`](/documentation/Swift/Dictionary/debugDescription)

A string that represents the contents of the dictionary, suitable for
debugging.

[`customMirror`](/documentation/Swift/Dictionary/customMirror)

A mirror that reflects the dictionary.

[`hash(into:)`](/documentation/Swift/Dictionary/hash(into:))

Hashes the essential components of this value by feeding them into the
given hasher.

### Using a Dictionary as a Data Value

[`init(from:)`](/documentation/Swift/Dictionary/init(from:)-5zhfu)

### Reference Types

Use bridged reference types when you need reference semantics or Foundation-specific
behavior.

  <doc://com.apple.documentation/documentation/Foundation/NSDictionary>

  <doc://com.apple.documentation/documentation/Foundation/NSMutableDictionary>

### Supporting Types

[`Dictionary.Keys`](/documentation/Swift/Dictionary/Keys-swift.struct)

A view of a dictionary’s keys.

[`Dictionary.Values`](/documentation/Swift/Dictionary/Values-swift.struct)

A view of a dictionary’s values.

[`Dictionary.Index`](/documentation/Swift/Dictionary/Index)

The position of a key-value pair in a dictionary.

[`Dictionary.Indices`](/documentation/Swift/Dictionary/Indices)

A type that represents the indices that are valid for subscripting the
collection, in ascending order.

[`Dictionary.Iterator`](/documentation/Swift/Dictionary/Iterator)

An iterator over the members of a `Dictionary<Key, Value>`.

### Converting Between Dictionaries and Create ML Types

### Creating a Dictionary from an Attribute Container

[`init(_:including:)`](/documentation/Swift/Dictionary/init(_:including:)-7afz2)

[`init(_:including:)`](/documentation/Swift/Dictionary/init(_:including:)-8ls7v)

[`init(_:)`](/documentation/Swift/Dictionary/init(_:))

### Infrequently Used Functionality

[`init(dictionaryLiteral:)`](/documentation/Swift/Dictionary/init(dictionaryLiteral:))

Creates a dictionary initialized with a dictionary literal.

[`hashValue`](/documentation/Swift/Dictionary/hashValue)

The hash value.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
