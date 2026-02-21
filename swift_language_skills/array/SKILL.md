---
name: Array
description: Apple Swift Documentation for Array.
---

# Array

An ordered, random-access collection.

```
@frozen struct Array<Element>
```

## Overview

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

## Growing the Size of an Array

Every array reserves a specific amount of memory to hold its contents. When
you add elements to an array and that array begins to exceed its reserved
capacity, the array allocates a larger region of memory and copies its
elements into the new storage. The new storage is a multiple of the old
storage’s size. This exponential growth strategy means that appending an
element happens in constant time, averaging the performance of many append
operations. Append operations that trigger reallocation have a performance
cost, but they occur less and less often as the array grows larger.

If you know approximately how many elements you will need to store, use the
`reserveCapacity(_:)` method before appending to the array to avoid
intermediate reallocations. Use the `capacity` and `count` properties to
determine how many more elements the array can store without allocating
larger storage.

For arrays of most `Element` types, this storage is a contiguous block of
memory. For arrays with an `Element` type that is a class or `@objc`
protocol type, this storage can be a contiguous block of memory or an
instance of `NSArray`. Because any arbitrary subclass of `NSArray` can
become an `Array`, there are no guarantees about representation or
efficiency in this case.

# Modifying Copies of Arrays

Each array has an independent value that includes the values of all of its
elements. For simple types such as integers and other structures, this
means that when you change a value in one array, the value of that element
does not change in any copies of the array. For example:

```
var numbers = [1, 2, 3, 4, 5]
var numbersCopy = numbers
numbers[0] = 100
print(numbers)
// Prints "[100, 2, 3, 4, 5]"
print(numbersCopy)
// Prints "[1, 2, 3, 4, 5]"
```

If the elements in an array are instances of a class, the semantics are the
same, though they might appear different at first. In this case, the
values stored in the array are references to objects that live outside the
array. If you change a reference to an object in one array, only that
array has a reference to the new object. However, if two arrays contain
references to the same object, you can observe changes to that object’s
properties from both arrays. For example:

```
// An integer type with reference semantics
class IntegerReference {
    var value = 10
}
var firstIntegers = [IntegerReference(), IntegerReference()]
var secondIntegers = firstIntegers

// Modifications to an instance are visible from either array
firstIntegers[0].value = 100
print(secondIntegers[0].value)
// Prints "100"

// Replacements, additions, and removals are still visible
// only in the modified array
firstIntegers[0] = IntegerReference()
print(firstIntegers[0].value)
// Prints "10"
print(secondIntegers[0].value)
// Prints "100"
```

Arrays, like all variable-size collections in the standard library, use
copy-on-write optimization. Multiple copies of an array share the same
storage until you modify one of the copies. When that happens, the array
being modified replaces its storage with a uniquely owned copy of itself,
which is then modified in place. Optimizations are sometimes applied that
can reduce the amount of copying.

This means that if an array is sharing storage with other copies, the first
mutating operation on that array incurs the cost of copying the array. An
array that is the sole owner of its storage can perform mutating
operations in place.

In the example below, a `numbers` array is created along with two copies
that share the same storage. When the original `numbers` array is
modified, it makes a unique copy of its storage before making the
modification. Further modifications to `numbers` are made in place, while
the two copies continue to share the original storage.

```
var numbers = [1, 2, 3, 4, 5]
var firstCopy = numbers
var secondCopy = numbers

// The storage for 'numbers' is copied here
numbers[0] = 100
numbers[1] = 200
numbers[2] = 300
// 'numbers' is [100, 200, 300, 4, 5]
// 'firstCopy' and 'secondCopy' are [1, 2, 3, 4, 5]
```

# Bridging Between Array and NSArray

When you need to access APIs that require data in an `NSArray` instance
instead of `Array`, use the type-cast operator (`as`) to bridge your
instance. For bridging to be possible, the `Element` type of your array
must be a class, an `@objc` protocol (a protocol imported from Objective-C
or marked with the `@objc` attribute), or a type that bridges to a
Foundation type.

The following example shows how you can bridge an `Array` instance to
`NSArray` to use the `write(to:atomically:)` method. In this example, the
`colors` array can be bridged to `NSArray` because the `colors` array’s
`String` elements bridge to `NSString`. The compiler prevents bridging the
`moreColors` array, on the other hand, because its `Element` type is
`Optional<String>`, which does *not* bridge to a Foundation type.

```
let colors = ["periwinkle", "rose", "moss"]
let moreColors: [String?] = ["ochre", "pine"]

let url = URL(fileURLWithPath: "names.plist")
(colors as NSArray).write(to: url, atomically: true)
// true

(moreColors as NSArray).write(to: url, atomically: true)
// error: cannot convert value of type '[String?]' to type 'NSArray'
```

Bridging from `Array` to `NSArray` takes O(1) time and O(1) space if the
array’s elements are already instances of a class or an `@objc` protocol;
otherwise, it takes O(*n*) time and space.

When the destination array’s element type is a class or an `@objc`
protocol, bridging from `NSArray` to `Array` first calls the `copy(with:)`
(`- copyWithZone:` in Objective-C) method on the array to get an immutable
copy and then performs additional Swift bookkeeping work that takes O(1)
time. For instances of `NSArray` that are already immutable, `copy(with:)`
usually returns the same array in O(1) time; otherwise, the copying
performance is unspecified. If `copy(with:)` returns the same array, the
instances of `NSArray` and `Array` share storage using the same
copy-on-write optimization that is used when two instances of `Array`
share storage.

When the destination array’s element type is a nonclass type that bridges
to a Foundation type, bridging from `NSArray` to `Array` performs a
bridging copy of the elements to contiguous storage in O(*n*) time. For
example, bridging from `NSArray` to `Array<Int>` performs such a copy. No
further bridging is required when accessing elements of the `Array`
instance.

> Note: The `ContiguousArray` and `ArraySlice` types are not bridged;
> instances of those types always have a contiguous block of memory as
> their storage.

## Topics

### Creating an Array

In addition to using an array literal, you can also create an array using these initializers.

[`init()`](/documentation/Swift/Array/init())

Creates a new, empty array.

[`init(_:)`](/documentation/Swift/Array/init(_:)-1ip9h)

Creates a new instance of a collection containing the elements of a
sequence.

[`init(_:)`](/documentation/Swift/Array/init(_:)-236cl)

Creates an array containing the elements of a sequence.

[`init(repeating:count:)`](/documentation/Swift/Array/init(repeating:count:))

Creates a new array containing the specified number of a single, repeated
value.

[`init(unsafeUninitializedCapacity:initializingWith:)`](/documentation/Swift/Array/init(unsafeUninitializedCapacity:initializingWith:))

Creates an array with the specified capacity, and then calls the given
closure with a buffer covering the array’s uninitialized memory.

### Inspecting an Array

[`isEmpty`](/documentation/Swift/Array/isEmpty)

A Boolean value indicating whether the collection is empty.

[`count`](/documentation/Swift/Array/count)

The number of elements in the array.

[`capacity`](/documentation/Swift/Array/capacity)

The total number of elements that the array can contain without
allocating new storage.

### Accessing Elements

[`subscript(_:)`](/documentation/Swift/Array/subscript(_:)-25iat)

Accesses the element at the specified position.

[`first`](/documentation/Swift/Array/first)

The first element of the collection.

[`last`](/documentation/Swift/Array/last)

The last element of the collection.

[`subscript(_:)`](/documentation/Swift/Array/subscript(_:)-53fvb)

Accesses a contiguous subrange of the array’s elements.

[`subscript(_:)`](/documentation/Swift/Array/subscript(_:)-3kwny)

[`subscript(_:)`](/documentation/Swift/Array/subscript(_:)-4h7rl)

Accesses the contiguous subrange of the collection’s elements specified
by a range expression.

[`subscript(_:)`](/documentation/Swift/Array/subscript(_:)-3pmfg)

[`randomElement()`](/documentation/Swift/Array/randomElement())

Returns a random element of the collection.

[`randomElement(using:)`](/documentation/Swift/Array/randomElement(using:))

Returns a random element of the collection, using the given generator as
a source for randomness.

### Adding Elements

[`append(_:)`](/documentation/Swift/Array/append(_:))

Adds a new element at the end of the array.

[`insert(_:at:)`](/documentation/Swift/Array/insert(_:at:))

Inserts a new element at the specified position.

[`insert(contentsOf:at:)`](/documentation/Swift/Array/insert(contentsOf:at:))

Inserts the elements of a sequence into the collection at the specified
position.

[`replaceSubrange(_:with:)`](/documentation/Swift/Array/replaceSubrange(_:with:))

Replaces a range of elements with the elements in the specified
collection.

[`replaceSubrange(_:with:)`](/documentation/Swift/Array/replaceSubrange(_:with:)-7293p)

Replaces the specified subrange of elements with the given collection.

[`reserveCapacity(_:)`](/documentation/Swift/Array/reserveCapacity(_:))

Reserves enough space to store the specified number of elements.

### Combining Arrays

[`append(contentsOf:)`](/documentation/Swift/Array/append(contentsOf:))

Adds the elements of a sequence to the end of the array.

[`append(contentsOf:)`](/documentation/Swift/Array/append(contentsOf:)-9foli)

Adds the elements of a sequence or collection to the end of this
collection.

[`+(_:_:)`](/documentation/Swift/Array/+(_:_:)-6h58k)

Creates a new collection by concatenating the elements of a sequence and a
collection.

[`+(_:_:)`](/documentation/Swift/Array/+(_:_:)-n33n)

Creates a new collection by concatenating the elements of a collection and
a sequence.

[`+(_:_:)`](/documentation/Swift/Array/+(_:_:))

[`+(_:_:)`](/documentation/Swift/Array/+(_:_:)-9fm5l)

Creates a new collection by concatenating the elements of two collections.

[`+=(_:_:)`](/documentation/Swift/Array/+=(_:_:)-676ib)

Appends the elements of a sequence to a range-replaceable collection.

[`+=(_:_:)`](/documentation/Swift/Array/+=(_:_:))

### Removing Elements

[`remove(at:)`](/documentation/Swift/Array/remove(at:))

Removes and returns the element at the specified position.

[`removeFirst()`](/documentation/Swift/Array/removeFirst())

Removes and returns the first element of the collection.

[`removeFirst(_:)`](/documentation/Swift/Array/removeFirst(_:))

Removes the specified number of elements from the beginning of the
collection.

[`removeLast()`](/documentation/Swift/Array/removeLast())

Removes and returns the last element of the collection.

[`removeLast(_:)`](/documentation/Swift/Array/removeLast(_:))

Removes the specified number of elements from the end of the
collection.

[`removeSubrange(_:)`](/documentation/Swift/Array/removeSubrange(_:)-8may1)

Removes the elements in the specified subrange from the collection.

[`removeSubrange(_:)`](/documentation/Swift/Array/removeSubrange(_:)-9twou)

Removes the elements in the specified subrange from the collection.

[`removeAll(where:)`](/documentation/Swift/Array/removeAll(where:)-5k61r)

Removes all the elements that satisfy the given predicate.

[`removeAll(keepingCapacity:)`](/documentation/Swift/Array/removeAll(keepingCapacity:))

Removes all elements from the array.

[`popLast()`](/documentation/Swift/Array/popLast())

Removes and returns the last element of the collection.

### Finding Elements

[`contains(_:)`](/documentation/Swift/Array/contains(_:))

Returns a Boolean value indicating whether the sequence contains the
given element.

[`contains(where:)`](/documentation/Swift/Array/contains(where:))

Returns a Boolean value indicating whether the sequence contains an
element that satisfies the given predicate.

[`allSatisfy(_:)`](/documentation/Swift/Array/allSatisfy(_:))

Returns a Boolean value indicating whether every element of a sequence
satisfies a given predicate.

[`first(where:)`](/documentation/Swift/Array/first(where:))

Returns the first element of the sequence that satisfies the given
predicate.

[`firstIndex(of:)`](/documentation/Swift/Array/firstIndex(of:))

Returns the first index where the specified value appears in the
collection.

[`index(of:)`](/documentation/Swift/Array/index(of:))

Returns the first index where the specified value appears in the
collection.

[`firstIndex(where:)`](/documentation/Swift/Array/firstIndex(where:))

Returns the first index in which an element of the collection satisfies
the given predicate.

[`last(where:)`](/documentation/Swift/Array/last(where:))

Returns the last element of the sequence that satisfies the given
predicate.

[`lastIndex(of:)`](/documentation/Swift/Array/lastIndex(of:))

Returns the last index where the specified value appears in the
collection.

[`lastIndex(where:)`](/documentation/Swift/Array/lastIndex(where:))

Returns the index of the last element in the collection that matches the
given predicate.

[`min()`](/documentation/Swift/Array/min())

Returns the minimum element in the sequence.

[`min(by:)`](/documentation/Swift/Array/min(by:))

Returns the minimum element in the sequence, using the given predicate as
the comparison between elements.

[`max()`](/documentation/Swift/Array/max())

Returns the maximum element in the sequence.

[`max(by:)`](/documentation/Swift/Array/max(by:))

Returns the maximum element in the sequence, using the given predicate
as the comparison between elements.

### Selecting Elements

[`prefix(_:)`](/documentation/Swift/Array/prefix(_:))

Returns a subsequence, up to the specified maximum length, containing
the initial elements of the collection.

[`prefix(through:)`](/documentation/Swift/Array/prefix(through:))

Returns a subsequence from the start of the collection through the
specified position.

[`prefix(upTo:)`](/documentation/Swift/Array/prefix(upTo:))

Returns a subsequence from the start of the collection up to, but not
including, the specified position.

[`prefix(while:)`](/documentation/Swift/Array/prefix(while:))

Returns a subsequence containing the initial elements until `predicate`
returns `false` and skipping the remaining elements.

[`suffix(_:)`](/documentation/Swift/Array/suffix(_:))

Returns a subsequence, up to the given maximum length, containing the
final elements of the collection.

[`suffix(from:)`](/documentation/Swift/Array/suffix(from:))

Returns a subsequence from the specified position to the end of the
collection.

### Excluding Elements

[`dropFirst(_:)`](/documentation/Swift/Array/dropFirst(_:))

Returns a subsequence containing all but the given number of initial
elements.

[`dropLast(_:)`](/documentation/Swift/Array/dropLast(_:))

Returns a subsequence containing all but the specified number of final
elements.

[`drop(while:)`](/documentation/Swift/Array/drop(while:))

Returns a subsequence by skipping elements while `predicate` returns
`true` and returning the remaining elements.

### Transforming an Array

[`flatMap(_:)`](/documentation/Swift/Array/flatMap(_:)-i3mr)

Returns an array containing the concatenated results of calling the
given transformation with each element of this sequence.

[`flatMap(_:)`](/documentation/Swift/Array/flatMap(_:)-6chu8)

[`compactMap(_:)`](/documentation/Swift/Array/compactMap(_:))

Returns an array containing the non-`nil` results of calling the given
transformation with each element of this sequence.

[`reduce(_:_:)`](/documentation/Swift/Array/reduce(_:_:))

Returns the result of combining the elements of the sequence using the
given closure.

[`reduce(into:_:)`](/documentation/Swift/Array/reduce(into:_:))

Returns the result of combining the elements of the sequence using the
given closure.

[`lazy`](/documentation/Swift/Array/lazy)

A sequence containing the same elements as this sequence,
but on which some operations, such as `map` and `filter`, are
implemented lazily.

### Iterating Over an Array’s Elements

[`forEach(_:)`](/documentation/Swift/Array/forEach(_:))

Calls the given closure on each element in the sequence in the same order
as a `for`-`in` loop.

[`enumerated()`](/documentation/Swift/Array/enumerated())

Returns a sequence of pairs (*n*, *x*), where *n* represents a
consecutive integer starting at zero and *x* represents an element of
the sequence.

[`makeIterator()`](/documentation/Swift/Array/makeIterator())

Returns an iterator over the elements of the collection.

[`underestimatedCount`](/documentation/Swift/Array/underestimatedCount)

A value less than or equal to the number of elements in the collection.

### Reordering an Array’s Elements

[`sort()`](/documentation/Swift/Array/sort())

Sorts the collection in place.

[`sort(by:)`](/documentation/Swift/Array/sort(by:))

Sorts the collection in place, using the given predicate as the
comparison between elements.

[`sorted()`](/documentation/Swift/Array/sorted())

Returns the elements of the sequence, sorted.

[`sorted(by:)`](/documentation/Swift/Array/sorted(by:))

Returns the elements of the sequence, sorted using the given predicate as
the comparison between elements.

[`reverse()`](/documentation/Swift/Array/reverse())

Reverses the elements of the collection in place.

[`reversed()`](/documentation/Swift/Array/reversed())

Returns a view presenting the elements of the collection in reverse
order.

[`shuffle()`](/documentation/Swift/Array/shuffle())

Shuffles the collection in place.

[`shuffle(using:)`](/documentation/Swift/Array/shuffle(using:))

Shuffles the collection in place, using the given generator as a source
for randomness.

[`shuffled()`](/documentation/Swift/Array/shuffled())

Returns the elements of the sequence, shuffled.

[`shuffled(using:)`](/documentation/Swift/Array/shuffled(using:))

Returns the elements of the sequence, shuffled using the given generator
as a source for randomness.

[`partition(by:)`](/documentation/Swift/Array/partition(by:)-90po8)

Reorders the elements of the collection such that all the elements
that match the given predicate are after all the elements that don’t
match.

[`swapAt(_:_:)`](/documentation/Swift/Array/swapAt(_:_:))

Exchanges the values at the specified indices of the collection.

### Splitting and Joining Elements

[`split(separator:maxSplits:omittingEmptySubsequences:)`](/documentation/Swift/Array/split(separator:maxSplits:omittingEmptySubsequences:)-3dgmv)

Returns the longest possible subsequences of the collection, in order,
around elements equal to the given element.

[`split(maxSplits:omittingEmptySubsequences:whereSeparator:)`](/documentation/Swift/Array/split(maxSplits:omittingEmptySubsequences:whereSeparator:))

Returns the longest possible subsequences of the collection, in order,
that don’t contain elements satisfying the given predicate.

[`joined()`](/documentation/Swift/Array/joined())

Returns the elements of this sequence of sequences, concatenated.

[`joined(separator:)`](/documentation/Swift/Array/joined(separator:)-7uber)

Returns the concatenated elements of this sequence of sequences,
inserting the given separator between each element.

[`joined(separator:)`](/documentation/Swift/Array/joined(separator:)-5do1g)

Returns a new string by concatenating the elements of the sequence,
adding the given separator between each element.

[`joined(separator:)`](/documentation/Swift/Array/joined(separator:)-1ckod)

Returns a new string by concatenating the elements of the sequence,
adding the given separator between each element.

### Creating and Applying Differences

[`applying(_:)`](/documentation/Swift/Array/applying(_:))

Applies the given difference to this collection.

[`difference(from:)`](/documentation/Swift/Array/difference(from:))

Returns the difference needed to produce this collection’s ordered
elements from the given collection.

[`difference(from:by:)`](/documentation/Swift/Array/difference(from:by:))

Returns the difference needed to produce this collection’s ordered
elements from the given collection, using the given predicate as an
equivalence test.

### Comparing Arrays

[`==(_:_:)`](/documentation/Swift/Array/==(_:_:))

Returns a Boolean value indicating whether two arrays contain the same
elements in the same order.

[`!=(_:_:)`](/documentation/Swift/Array/!=(_:_:))

Returns a Boolean value indicating whether two values are not equal.

[`elementsEqual(_:)`](/documentation/Swift/Array/elementsEqual(_:))

Returns a Boolean value indicating whether this sequence and another
sequence contain the same elements in the same order.

[`elementsEqual(_:by:)`](/documentation/Swift/Array/elementsEqual(_:by:))

Returns a Boolean value indicating whether this sequence and another
sequence contain equivalent elements in the same order, using the given
predicate as the equivalence test.

[`starts(with:)`](/documentation/Swift/Array/starts(with:))

Returns a Boolean value indicating whether the initial elements of the
sequence are the same as the elements in another sequence.

[`starts(with:by:)`](/documentation/Swift/Array/starts(with:by:))

Returns a Boolean value indicating whether the initial elements of the
sequence are equivalent to the elements in another sequence, using
the given predicate as the equivalence test.

[`lexicographicallyPrecedes(_:)`](/documentation/Swift/Array/lexicographicallyPrecedes(_:))

Returns a Boolean value indicating whether the sequence precedes another
sequence in a lexicographical (dictionary) ordering, using the
less-than operator (`<`) to compare elements.

[`lexicographicallyPrecedes(_:by:)`](/documentation/Swift/Array/lexicographicallyPrecedes(_:by:))

Returns a Boolean value indicating whether the sequence precedes another
sequence in a lexicographical (dictionary) ordering, using the given
predicate to compare elements.

### Manipulating Indices

[`startIndex`](/documentation/Swift/Array/startIndex)

The position of the first element in a nonempty array.

[`endIndex`](/documentation/Swift/Array/endIndex)

The array’s “past the end” position—that is, the position one greater
than the last valid subscript argument.

[`index(after:)`](/documentation/Swift/Array/index(after:))

Returns the position immediately after the given index.

[`formIndex(after:)`](/documentation/Swift/Array/formIndex(after:))

Replaces the given index with its successor.

[`index(before:)`](/documentation/Swift/Array/index(before:))

Returns the position immediately before the given index.

[`formIndex(before:)`](/documentation/Swift/Array/formIndex(before:))

Replaces the given index with its predecessor.

[`index(_:offsetBy:)`](/documentation/Swift/Array/index(_:offsetBy:))

Returns an index that is the specified distance from the given index.

[`formIndex(_:offsetBy:)`](/documentation/Swift/Array/formIndex(_:offsetBy:))

Offsets the given index by the specified distance.

[`index(_:offsetBy:limitedBy:)`](/documentation/Swift/Array/index(_:offsetBy:limitedBy:))

Returns an index that is the specified distance from the given index,
unless that distance is beyond a given limiting index.

[`formIndex(_:offsetBy:limitedBy:)`](/documentation/Swift/Array/formIndex(_:offsetBy:limitedBy:))

Offsets the given index by the specified distance, or so that it equals
the given limiting index.

[`distance(from:to:)`](/documentation/Swift/Array/distance(from:to:))

Returns the distance between two indices.

### Accessing Underlying Storage

[`withUnsafeBufferPointer(_:)`](/documentation/Swift/Array/withUnsafeBufferPointer(_:))

Calls a closure with a pointer to the array’s contiguous storage.

[`withUnsafeMutableBufferPointer(_:)`](/documentation/Swift/Array/withUnsafeMutableBufferPointer(_:))

Calls the given closure with a pointer to the array’s mutable contiguous
storage.

[`withUnsafeBytes(_:)`](/documentation/Swift/Array/withUnsafeBytes(_:))

Calls the given closure with a pointer to the underlying bytes of the
array’s contiguous storage.

[`withUnsafeMutableBytes(_:)`](/documentation/Swift/Array/withUnsafeMutableBytes(_:))

Calls the given closure with a pointer to the underlying bytes of the
array’s mutable contiguous storage.

[`withContiguousStorageIfAvailable(_:)`](/documentation/Swift/Array/withContiguousStorageIfAvailable(_:))

Executes a closure on the sequence’s contiguous storage.

[`withContiguousMutableStorageIfAvailable(_:)`](/documentation/Swift/Array/withContiguousMutableStorageIfAvailable(_:))

Executes a closure on the collection’s contiguous storage.

### Encoding and Decoding

[`encode(to:)`](/documentation/Swift/Array/encode(to:))

Encodes the elements of this array into the given encoder in an unkeyed
container.

[`init(from:)`](/documentation/Swift/Array/init(from:))

Creates a new array by decoding from the given decoder.

### Describing an Array

[`description`](/documentation/Swift/Array/description)

A textual representation of the array and its elements.

[`debugDescription`](/documentation/Swift/Array/debugDescription)

A textual representation of the array and its elements, suitable for
debugging.

[`customMirror`](/documentation/Swift/Array/customMirror)

A mirror that reflects the array.

[`hash(into:)`](/documentation/Swift/Array/hash(into:))

Hashes the essential components of this value by feeding them into the
given hasher.

### Converting Between Arrays and Create ML Types

[`init(_:)`](/documentation/Swift/Array/init(_:)-2ln1a)

Constructs an Array with the elements of a DataColumn.

[`init(_:)`](/documentation/Swift/Array/init(_:)-86ka8)

Constructs an Array with the elements of an MLUntypedColumn.

### Related Array Types

[`ContiguousArray`](/documentation/Swift/ContiguousArray)

A contiguously stored array.

[`ArraySlice`](/documentation/Swift/ArraySlice)

A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance.

### Reference Types

Use bridged reference types when you need reference semantics or Foundation-specific
behavior.

  <doc://com.apple.documentation/documentation/Foundation/NSArray>

  <doc://com.apple.documentation/documentation/Foundation/NSMutableArray>

### Supporting Types

[`Array.Index`](/documentation/Swift/Array/Index)

The index type for arrays, `Int`.

[`Array.Indices`](/documentation/Swift/Array/Indices)

The type that represents the indices that are valid for subscripting an
array, in ascending order.

[`Array.Iterator`](/documentation/Swift/Array/Iterator)

The type that allows iteration over an array’s elements.

[`Array.ArrayLiteralElement`](/documentation/Swift/Array/ArrayLiteralElement)

The type of the elements of an array literal.

[`Array.SubSequence`](/documentation/Swift/Array/SubSequence)

A collection representing a contiguous subrange of this collection’s
elements. The subsequence shares indices with the original collection.

### Infrequently Used Functionality

[`init(arrayLiteral:)`](/documentation/Swift/Array/init(arrayLiteral:))

Creates an array from the given array literal.

[`hashValue`](/documentation/Swift/Array/hashValue)

The hash value.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
