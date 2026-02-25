---
name: Array
description: Rork-Max Quality skill for Array. Actionable Swift language patterns and best practices.
---

# Array

An ordered, random-access collection.
```
@frozen struct Array<Element>
```
Arrays are one of the most commonly used data types in an app. You use
arrays to organize your app’s data. Specifically, you use the `Array` type
to hold elements of a single type, the array’s `Element` type. An array
can store any kind of elements—from integers to strings to classes.
Swift makes it easy to create arrays in your code using an array literal:
simply surround a comma-separated list of values with square brackets.
Without any other information, Swift creates an array that includes the
specified values, automatically inferring the array’s `Element` type. For
example:
```
// An array of 'Int' elements
let oddNumbers = [1, 3, 5, 7, 9, 11, 13, 15]
// An array of 'String' elements
let streets = ["Albemarle", "Brandywine", "Chesapeake"]
```
You can create an empty array by specifying the `Element` type of your
array in the declaration. For example:
```
// Shortened forms are preferred
var emptyDoubles: [Double] = []
// The full type name is also allowed
var emptyFloats: Array<Float> = Array()
```
If you need an array that is preinitialized with a fixed number of default
values, use the `Array(repeating:count:)` initializer.
```
var digitCounts = Array(repeating: 0, count: 10)
print(digitCounts)
// Prints "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"
```
# Accessing Array Values
When you need to perform an operation on all of an array’s elements, use a
`for`-`in` loop to iterate through the array’s contents.
```
for street in streets {
print("I don't live on \(street).")
}
// Prints "I don't live on Albemarle."
// Prints "I don't live on Brandywine."
// Prints "I don't live on Chesapeake."
```
Use the `isEmpty` property to check quickly whether an array has any
elements, or use the `count` property to find the number of elements in
the array.
```
if oddNumbers.isEmpty {
print("I don't know any odd numbers.")
} else {
print("I know \(oddNumbers.count) odd numbers.")
}
// Prints "I know 8 odd numbers."
```
Use the `first` and `last` properties for safe access to the value of the
array’s first and last elements. If the array is empty, these properties
are `nil`.
```
if let firstElement = oddNumbers.first, let lastElement = oddNumbers.last {
print(firstElement, lastElement, separator: ", ")
}
// Prints "1, 15"
print(emptyDoubles.first, emptyDoubles.last, separator: ", ")
// Prints "nil, nil"
```
You can access individual array elements through a subscript. The first
element of a nonempty array is always at index zero. You can subscript an
array with any integer from zero up to, but not including, the count of
the array. Using a negative number or an index equal to or greater than
`count` triggers a runtime error. For example:
```
print(oddNumbers[0], oddNumbers[3], separator: ", ")
// Prints "1, 7"
print(emptyDoubles[0])
// Triggers runtime error: Index out of range
```
# Adding and Removing Elements
Suppose you need to store a list of the names of students that are signed
up for a class you’re teaching. During the registration period, you need
to add and remove names as students add and drop the class.
```
var students = ["Ben", "Ivy", "Jordell"]
```
To add single elements to the end of an array, use the `append(_:)` method.
Add multiple elements at the same time by passing another array or a
sequence of any kind to the `append(contentsOf:)` method.
```
students.append("Maxime")
students.append(contentsOf: ["Shakia", "William"])
// ["Ben", "Ivy", "Jordell", "Maxime", "Shakia", "William"]
```
You can add new elements in the middle of an array by using the
`insert(_:at:)` method for single elements and by using
`insert(contentsOf:at:)` to insert multiple elements from another
collection or array literal. The elements at that index and later indices
are shifted back to make room.
```
students.insert("Liam", at: 3)
// ["Ben", "Ivy", "Jordell", "Liam", "Maxime", "Shakia", "William"]
```
To remove elements from an array, use the `remove(at:)`,
`removeSubrange(_:)`, and `removeLast()` methods.
```
// Ben's family is moving to another state
students.remove(at: 0)
// ["Ivy", "Jordell", "Liam", "Maxime", "Shakia", "William"]
// William is signing up for a different class
students.removeLast()
// ["Ivy", "Jordell", "Liam", "Maxime", "Shakia"]
```
You can replace an existing element with a new value by assigning the new
value to the subscript.
```
if let i = students.firstIndex(of: "Maxime") {
students[i] = "Max"
}
// ["Ivy", "Jordell", "Liam", "Max", "Shakia"]
```

## 🚀 Rork-Max Quality Snippet

```swift
var numbers = [3, 1, 4, 1, 5, 9, 2, 6]

// Functional operations
let evens = numbers.filter { $0.isMultiple(of: 2) }     // [4, 2, 6]
let doubled = numbers.map { $0 * 2 }                     // [6, 2, 8, ...]
let sum = numbers.reduce(0, +)                            // 31

// Safe access
let first = numbers.first                                // Optional(3)
let safeIndex = numbers.indices.contains(10) ? numbers[10] : nil

// Sorting
numbers.sort()                                            // In-place
let sorted = numbers.sorted(by: >)                        // Descending copy

// Collection operations
let unique = Array(Set(numbers))                          // Remove duplicates
let chunked = stride(from: 0, to: numbers.count, by: 3).map {
    Array(numbers[$0..<min($0 + 3, numbers.count)])
}
```

## 💎 Elite Implementation Tips

- Use `first`, `last`, and `indices.contains()` for safe access — avoid force-indexing
- Prefer `map`, `filter`, `reduce` over manual loops for cleaner, more readable code
- Use `sorted(by:)` for a new array, `.sort()` for in-place mutation

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

### Creating an Array

| API | Purpose |
|-----|---------|
| `init()` | Creates a new, empty array. |
| `init(_:)` | Creates a new instance of a collection containing the elements of a |
| `init(_:)` | Creates an array containing the elements of a sequence. |
| `init(repeating:count:)` | Creates a new array containing the specified number of a single, repeated |
| `init(unsafeUninitializedCapacity:initializingWith:)` | Creates an array with the specified capacity, and then calls the given |

### Inspecting an Array

| API | Purpose |
|-----|---------|
| `isEmpty` | A Boolean value indicating whether the collection is empty. |
| `count` | The number of elements in the array. |
| `capacity` | The total number of elements that the array can contain without |

### Accessing Elements

| API | Purpose |
|-----|---------|
| `subscript(_:)` | Accesses the element at the specified position. |
| `first` | The first element of the collection. |
| `last` | The last element of the collection. |
| `subscript(_:)` | Accesses a contiguous subrange of the array’s elements. |
| `subscript(_:)` | — |
| `subscript(_:)` | Accesses the contiguous subrange of the collection’s elements specified |
| `subscript(_:)` | — |
| `randomElement()` | Returns a random element of the collection. |

### Adding Elements

| API | Purpose |
|-----|---------|
| `append(_:)` | Adds a new element at the end of the array. |
| `insert(_:at:)` | Inserts a new element at the specified position. |
| `insert(contentsOf:at:)` | Inserts the elements of a sequence into the collection at the specified |
| `replaceSubrange(_:with:)` | Replaces a range of elements with the elements in the specified |
| `replaceSubrange(_:with:)` | Replaces the specified subrange of elements with the given collection. |
| `reserveCapacity(_:)` | Reserves enough space to store the specified number of elements. |

### Combining Arrays

| API | Purpose |
|-----|---------|
| `append(contentsOf:)` | Adds the elements of a sequence to the end of the array. |
| `append(contentsOf:)` | Adds the elements of a sequence or collection to the end of this |
| `+(_:_:)` | Creates a new collection by concatenating the elements of a sequence and a |
| `+(_:_:)` | Creates a new collection by concatenating the elements of a collection and |
| `+(_:_:)` | — |
| `+(_:_:)` | Creates a new collection by concatenating the elements of two collections. |
| `+=(_:_:)` | Appends the elements of a sequence to a range-replaceable collection. |

### Removing Elements

| API | Purpose |
|-----|---------|
| `remove(at:)` | Removes and returns the element at the specified position. |
| `removeFirst()` | Removes and returns the first element of the collection. |
| `removeFirst(_:)` | Removes the specified number of elements from the beginning of the |
| `removeLast()` | Removes and returns the last element of the collection. |
| `removeLast(_:)` | Removes the specified number of elements from the end of the |
| `removeSubrange(_:)` | Removes the elements in the specified subrange from the collection. |
| `removeSubrange(_:)` | Removes the elements in the specified subrange from the collection. |
| `removeAll(where:)` | Removes all the elements that satisfy the given predicate. |

### Finding Elements

| API | Purpose |
|-----|---------|
| `contains(_:)` | Returns a Boolean value indicating whether the sequence contains the |
| `contains(where:)` | Returns a Boolean value indicating whether the sequence contains an |
| `allSatisfy(_:)` | Returns a Boolean value indicating whether every element of a sequence |
| `first(where:)` | Returns the first element of the sequence that satisfies the given |
| `firstIndex(of:)` | Returns the first index where the specified value appears in the |
| `index(of:)` | Returns the first index where the specified value appears in the |
| `firstIndex(where:)` | Returns the first index in which an element of the collection satisfies |
| `last(where:)` | Returns the last element of the sequence that satisfies the given |

### Selecting Elements

| API | Purpose |
|-----|---------|
| `prefix(_:)` | Returns a subsequence, up to the specified maximum length, containing |
| `prefix(through:)` | Returns a subsequence from the start of the collection through the |
| `prefix(upTo:)` | Returns a subsequence from the start of the collection up to, but not |
| `prefix(while:)` | Returns a subsequence containing the initial elements until `predicate` |
| `suffix(_:)` | Returns a subsequence, up to the given maximum length, containing the |
| `suffix(from:)` | Returns a subsequence from the specified position to the end of the |

### Excluding Elements

| API | Purpose |
|-----|---------|
| `dropFirst(_:)` | Returns a subsequence containing all but the given number of initial |
| `dropLast(_:)` | Returns a subsequence containing all but the specified number of final |
| `drop(while:)` | Returns a subsequence by skipping elements while `predicate` returns |

### Transforming an Array

| API | Purpose |
|-----|---------|
| `flatMap(_:)` | Returns an array containing the concatenated results of calling the |
| `flatMap(_:)` | — |
| `compactMap(_:)` | Returns an array containing the non-`nil` results of calling the given |
| `reduce(_:_:)` | Returns the result of combining the elements of the sequence using the |
| `reduce(into:_:)` | Returns the result of combining the elements of the sequence using the |
| `lazy` | A sequence containing the same elements as this sequence, |

### Iterating Over an Array’s Elements

| API | Purpose |
|-----|---------|
| `forEach(_:)` | Calls the given closure on each element in the sequence in the same order |
| `enumerated()` | Returns a sequence of pairs (*n*, *x*), where *n* represents a |
| `makeIterator()` | Returns an iterator over the elements of the collection. |
| `underestimatedCount` | A value less than or equal to the number of elements in the collection. |

### Reordering an Array’s Elements

| API | Purpose |
|-----|---------|
| `sort()` | Sorts the collection in place. |
| `sort(by:)` | Sorts the collection in place, using the given predicate as the |
| `sorted()` | Returns the elements of the sequence, sorted. |
| `sorted(by:)` | Returns the elements of the sequence, sorted using the given predicate as |
| `reverse()` | Reverses the elements of the collection in place. |
| `reversed()` | Returns a view presenting the elements of the collection in reverse |
| `shuffle()` | Shuffles the collection in place. |
| `shuffle(using:)` | Shuffles the collection in place, using the given generator as a source |

### Splitting and Joining Elements

| API | Purpose |
|-----|---------|
| `split(separator:maxSplits:omittingEmptySubsequences:)` | Returns the longest possible subsequences of the collection, in order, |
| `split(maxSplits:omittingEmptySubsequences:whereSeparator:)` | Returns the longest possible subsequences of the collection, in order, |
| `joined()` | Returns the elements of this sequence of sequences, concatenated. |
| `joined(separator:)` | Returns the concatenated elements of this sequence of sequences, |
| `joined(separator:)` | Returns a new string by concatenating the elements of the sequence, |
| `joined(separator:)` | Returns a new string by concatenating the elements of the sequence, |

### Creating and Applying Differences

| API | Purpose |
|-----|---------|
| `applying(_:)` | Applies the given difference to this collection. |
| `difference(from:)` | Returns the difference needed to produce this collection’s ordered |
| `difference(from:by:)` | Returns the difference needed to produce this collection’s ordered |

### Comparing Arrays

| API | Purpose |
|-----|---------|
| `==(_:_:)` | Returns a Boolean value indicating whether two arrays contain the same |
| `!=(_:_:)` | Returns a Boolean value indicating whether two values are not equal. |
| `elementsEqual(_:)` | Returns a Boolean value indicating whether this sequence and another |
| `elementsEqual(_:by:)` | Returns a Boolean value indicating whether this sequence and another |
| `starts(with:)` | Returns a Boolean value indicating whether the initial elements of the |
| `starts(with:by:)` | Returns a Boolean value indicating whether the initial elements of the |
| `lexicographicallyPrecedes(_:)` | Returns a Boolean value indicating whether the sequence precedes another |
| `lexicographicallyPrecedes(_:by:)` | Returns a Boolean value indicating whether the sequence precedes another |

### Manipulating Indices

| API | Purpose |
|-----|---------|
| `startIndex` | The position of the first element in a nonempty array. |
| `endIndex` | The array’s “past the end” position—that is, the position one greater |
| `index(after:)` | Returns the position immediately after the given index. |
| `formIndex(after:)` | Replaces the given index with its successor. |
| `index(before:)` | Returns the position immediately before the given index. |
| `formIndex(before:)` | Replaces the given index with its predecessor. |
| `index(_:offsetBy:)` | Returns an index that is the specified distance from the given index. |
| `formIndex(_:offsetBy:)` | Offsets the given index by the specified distance. |

### Accessing Underlying Storage

| API | Purpose |
|-----|---------|
| `withUnsafeBufferPointer(_:)` | Calls a closure with a pointer to the array’s contiguous storage. |
| `withUnsafeMutableBufferPointer(_:)` | Calls the given closure with a pointer to the array’s mutable contiguous |
| `withUnsafeBytes(_:)` | Calls the given closure with a pointer to the underlying bytes of the |
| `withUnsafeMutableBytes(_:)` | Calls the given closure with a pointer to the underlying bytes of the |
| `withContiguousStorageIfAvailable(_:)` | Executes a closure on the sequence’s contiguous storage. |
| `withContiguousMutableStorageIfAvailable(_:)` | Executes a closure on the collection’s contiguous storage. |

### Encoding and Decoding

| API | Purpose |
|-----|---------|
| `encode(to:)` | Encodes the elements of this array into the given encoder in an unkeyed |
| `init(from:)` | Creates a new array by decoding from the given decoder. |

### Describing an Array

| API | Purpose |
|-----|---------|
| `description` | A textual representation of the array and its elements. |
| `debugDescription` | A textual representation of the array and its elements, suitable for |
| `customMirror` | A mirror that reflects the array. |
| `hash(into:)` | Hashes the essential components of this value by feeding them into the |

### Converting Between Arrays and Create ML Types

| API | Purpose |
|-----|---------|
| `init(_:)` | Constructs an Array with the elements of a DataColumn. |
| `init(_:)` | Constructs an Array with the elements of an MLUntypedColumn. |

### Related Array Types

| API | Purpose |
|-----|---------|
| `ContiguousArray` | A contiguously stored array. |
| `ArraySlice` | A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance. |

### Supporting Types

| API | Purpose |
|-----|---------|
| `Array.Index` | The index type for arrays, `Int`. |
| `Array.Indices` | The type that represents the indices that are valid for subscripting an |
| `Array.Iterator` | The type that allows iteration over an array’s elements. |
| `Array.ArrayLiteralElement` | The type of the elements of an array literal. |
| `Array.SubSequence` | A collection representing a contiguous subrange of this collection’s |

### Infrequently Used Functionality

| API | Purpose |
|-----|---------|
| `init(arrayLiteral:)` | Creates an array from the given array literal. |
| `hashValue` | The hash value. |
