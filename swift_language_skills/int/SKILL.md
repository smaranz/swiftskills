---
name: Int
description: Rork-Max Quality skill for Int. Actionable Swift language patterns and best practices.
---

# Int

A signed integer value type.
```
@frozen struct Int
```
On 32-bit platforms, `Int` is the same size as `Int32`, and
on 64-bit platforms, `Int` is the same size as `Int64`.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Int — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Int.
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

### Converting Integers

| API | Purpose |
|-----|---------|
| `init(_:)` | Creates a new instance from the given integer. |
| `init(exactly:)` | — |
| `init(clamping:)` | Creates a new instance with the representable value that’s closest to the |
| `init(truncatingIfNeeded:)` | Creates a new instance from the bit pattern of the given instance by |
| `init(bitPattern:)` | Creates a new instance with the same memory representation as the given |
| `init(exactly:)` | — |

### Converting Floating-Point Values

| API | Purpose |
|-----|---------|
| `init(_:)` | — |
| `init(_:)` | Creates an integer from the given floating-point value, rounding toward |
| `init(_:)` | Creates an integer from the given floating-point value, rounding toward |
| `init(_:)` | Creates an integer from the given floating-point value, rounding toward |
| `init(_:)` | Creates an integer from the given floating-point value, rounding toward |

### Converting with No Loss of Precision

| API | Purpose |
|-----|---------|
| `init(exactly:)` | — |
| `init(exactly:)` | Creates an integer from the given floating-point value, if it can be |
| `init(exactly:)` | Creates an integer from the given floating-point value, if it can be |
| `init(exactly:)` | Creates an integer from the given floating-point value, if it can be |
| `init(exactly:)` | Creates an integer from the given floating-point value, if it can be |

### Converting Strings

| API | Purpose |
|-----|---------|
| `init(_:)` | Creates a new integer value from the given string. |
| `init(_:radix:)` | Creates a new integer value from the given string and radix. |

### Creating a Random Integer

| API | Purpose |
|-----|---------|
| `random(in:)` | Returns a random value within the specified range. |
| `random(in:using:)` | Returns a random value within the specified range, using the given |
| `random(in:)` | Returns a random value within the specified range. |
| `random(in:using:)` | Returns a random value within the specified range, using the given |

### Performing Calculations

| API | Purpose |
|-----|---------|
| `negate()` | Replaces this value with its additive inverse. |
| `quotientAndRemainder(dividingBy:)` | Returns the quotient and remainder of this value divided by the given |
| `isMultiple(of:)` | Returns `true` if this value is a multiple of the given value, and `false` |

### Performing Calculations with Overflow

| API | Purpose |
|-----|---------|
| `addingReportingOverflow(_:)` | Returns the sum of this value and the given value, along with a Boolean |
| `subtractingReportingOverflow(_:)` | Returns the difference obtained by subtracting the given value from this |
| `multipliedReportingOverflow(by:)` | Returns the product of this value and the given value, along with a |
| `dividedReportingOverflow(by:)` | Returns the quotient obtained by dividing this value by the given value, |
| `remainderReportingOverflow(dividingBy:)` | Returns the remainder after dividing this value by the given value, along |

### Performing Double-Width Calculations

| API | Purpose |
|-----|---------|
| `multipliedFullWidth(by:)` | Returns a tuple containing the high and low parts of the result of |
| `dividingFullWidth(_:)` | Returns a tuple containing the quotient and remainder of dividing the |

### Finding the Sign and Magnitude

| API | Purpose |
|-----|---------|
| `magnitude` | The magnitude of this value. |
| `Int.Magnitude` | A type that can represent the absolute value of any possible value of |
| `abs(_:)` | Returns the absolute value of the given number. |
| `signum()` | Returns `-1` if this value is negative and `1` if it’s positive; |

### Accessing Numeric Constants

| API | Purpose |
|-----|---------|
| `zero` | The zero value. |
| `min` | The minimum representable integer in this type. |
| `max` | The maximum representable integer in this type. |
| `isSigned` | A Boolean value indicating whether this type is a signed integer type. |

### Working with Byte Order

| API | Purpose |
|-----|---------|
| `byteSwapped` | A representation of this integer with the byte order swapped. |
| `littleEndian` | The little-endian representation of this integer. |
| `bigEndian` | The big-endian representation of this integer. |
| `init(littleEndian:)` | Creates an integer from its little-endian representation, changing the |
| `init(bigEndian:)` | Creates an integer from its big-endian representation, changing the byte |

### Working with Binary Representation

| API | Purpose |
|-----|---------|
| `bitWidth` | The number of bits used for the underlying binary representation of |
| `bitWidth` | The number of bits in the current binary representation of this value. |
| `nonzeroBitCount` | The number of bits equal to 1 in this value’s binary representation. |
| `leadingZeroBitCount` | The number of leading zeros in this value’s binary representation. |
| `trailingZeroBitCount` | The number of trailing zeros in this value’s binary representation. |
| `words` | A collection containing the words of this value’s binary |
| `Int.Words` | A type that represents the words of this integer. |

### Working with Memory Addresses

| API | Purpose |
|-----|---------|
| `init(bitPattern:)` | Creates a new value with the bit pattern of the given pointer. |
| `init(bitPattern:)` | Creates an integer that captures the full value of the given object |
| `init(bitPattern:)` | Creates a new value with the bit pattern of the given pointer. |

### Encoding and Decoding Values

| API | Purpose |
|-----|---------|
| `encode(to:)` | Encodes this value into the given encoder. |
| `init(from:)` | Creates a new instance by decoding from the given decoder. |

### Describing an Integer

| API | Purpose |
|-----|---------|
| `description` | A textual representation of this value. |
| `hash(into:)` | Hashes the essential components of this value by feeding them into the |
| `customMirror` | A mirror that reflects the `Int` instance. |

### Infrequently Used Functionality

| API | Purpose |
|-----|---------|
| `init()` | Creates a new value equal to zero. |
| `init(integerLiteral:)` | — |
| `Int.IntegerLiteralType` | A type that represents an integer literal. |
| `distance(to:)` | Returns the distance from this value to the given value, expressed as a |
| `advanced(by:)` | Returns a value that is offset the specified distance from this value. |
| `Int.Stride` | A type that represents the distance between two values. |
| `hashValue` | The hash value. |

### Deprecated

| API | Purpose |
|-----|---------|
| `customPlaygroundQuickLook` | A custom playground Quick Look for the `Int` instance. |

### SIMD-Supporting Types

| API | Purpose |
|-----|---------|
| `Int.SIMDMaskScalar` | — |
| `Int.SIMD2Storage` | Storage for a vector of two integers. |
| `Int.SIMD4Storage` | Storage for a vector of four integers. |
| `Int.SIMD8Storage` | Storage for a vector of eight integers. |
| `Int.SIMD16Storage` | Storage for a vector of 16 integers. |
| `Int.SIMD32Storage` | Storage for a vector of 32 integers. |
| `Int.SIMD64Storage` | Storage for a vector of 64 integers. |
