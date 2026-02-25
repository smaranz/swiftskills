---
name: Double
description: Rork-Max Quality skill for Double. Actionable Swift language patterns and best practices.
---

# Double

A double-precision (64-bit), floating-point value type.
```
@frozen struct Double
```

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Double — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Double.
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
| `init(_:)` | Creates a new value, rounded to the closest possible representation. |
| `init(_:)` | Creates a new value, rounded to the closest possible representation. |

### Converting Strings

| API | Purpose |
|-----|---------|
| `init(_:)` | Creates a new instance from the given string. |

### Converting Floating-Point Values

| API | Purpose |
|-----|---------|
| `init(_:)` | Creates a new instance from the given value, rounded to the closest |
| `init(_:)` | Creates a new instance initialized to the given value. |
| `init(_:)` | Creates a new instance that approximates the given value. |
| `init(_:)` | Creates a new instance that approximates the given value. |
| `init(_:)` | Creates a new instance that approximates the given value. |
| `init(_:)` | — |
| `init(sign:exponent:significand:)` | Creates a new value from the given sign, exponent, and significand. |
| `init(signOf:magnitudeOf:)` | Creates a new floating-point value using the sign of one value and the |

### Converting with No Loss of Precision

| API | Purpose |
|-----|---------|
| `init(exactly:)` | Creates a new instance from the given value, if it can be represented |
| `init(exactly:)` | Creates a new value, if the given integer can be represented exactly. |
| `init(exactly:)` | Creates a new value, if the given integer can be represented exactly. |
| `init(exactly:)` | Creates a new instance initialized to the given value, if it can be |
| `init(exactly:)` | Creates a new instance initialized to the given value, if it can be |
| `init(exactly:)` | Creates a new instance initialized to the given value, if it can be |
| `init(exactly:)` | Creates a new instance initialized to the given value, if it can be |

### Creating a Random Value

| API | Purpose |
|-----|---------|
| `random(in:)` | Returns a random value within the specified range. |
| `random(in:using:)` | Returns a random value within the specified range, using the given |
| `random(in:)` | Returns a random value within the specified range. |
| `random(in:using:)` | Returns a random value within the specified range, using the given |

### Performing Calculations

| API | Purpose |
|-----|---------|
| `addingProduct(_:_:)` | Returns the result of adding the product of the two given values to this |
| `addProduct(_:_:)` | Adds the product of the two given values to this value in place, computed |
| `squareRoot()` | Returns the square root of the value, rounded to a representable value. |
| `formSquareRoot()` | Replaces this value with its square root, rounded to a representable |
| `remainder(dividingBy:)` | Returns the remainder of this value divided by the given value. |
| `formRemainder(dividingBy:)` | Replaces this value with the remainder of itself divided by the given |
| `truncatingRemainder(dividingBy:)` | Returns the remainder of this value divided by the given value using |
| `formTruncatingRemainder(dividingBy:)` | Replaces this value with the remainder of itself divided by the given |

### Rounding Values

| API | Purpose |
|-----|---------|
| `rounded()` | — |
| `rounded(_:)` | Returns this value rounded to an integral value using the specified |
| `round()` | — |
| `round(_:)` | Rounds the value to an integral value using the specified rounding rule. |

### Comparing Values

| API | Purpose |
|-----|---------|
| `isEqual(to:)` | Returns a Boolean value indicating whether this instance is equal to the |
| `isLess(than:)` | Returns a Boolean value indicating whether this instance is less than the |
| `isLessThanOrEqualTo(_:)` | Returns a Boolean value indicating whether this instance is less than or |
| `isTotallyOrdered(belowOrEqualTo:)` | Returns a Boolean value indicating whether this instance should precede |
| `minimum(_:_:)` | Returns the lesser of the two given values. |
| `minimumMagnitude(_:_:)` | Returns the value with lesser magnitude. |
| `maximum(_:_:)` | Returns the greater of the two given values. |
| `maximumMagnitude(_:_:)` | Returns the value with greater magnitude. |

### Finding the Sign and Magnitude

| API | Purpose |
|-----|---------|
| `magnitude` | The magnitude of this value. |
| `sign` | The sign of the floating-point value. |
| `Double.Magnitude` | A type that can represent the absolute value of any possible value of the |

### Querying a Double

| API | Purpose |
|-----|---------|
| `ulp` | The unit in the last place of this value. |
| `significand` | The significand of the floating-point value. |
| `exponent` | The exponent of the floating-point value. |
| `nextUp` | The least representable value that compares greater than this value. |
| `nextDown` | The greatest representable value that compares less than this value. |
| `binade` | The floating-point value with the same sign and exponent as this value, |

### Accessing Numeric Constants

| API | Purpose |
|-----|---------|
| `pi` | The mathematical constant pi (π), approximately equal to 3.14159. |
| `infinity` | Positive infinity. |
| `greatestFiniteMagnitude` | The greatest finite number representable by this type. |
| `nan` | A quiet NaN (“not a number”). |
| `signalingNaN` | A signaling NaN (“not a number”). |
| `ulpOfOne` | The unit in the last place of 1.0. |
| `leastNonzeroMagnitude` | The least positive number. |
| `leastNormalMagnitude` | The least positive normal number. |

### Working with Binary Representation

| API | Purpose |
|-----|---------|
| `bitPattern` | The bit pattern of the value’s encoding. |
| `significandBitPattern` | The raw encoding of the value’s significand field. |
| `significandWidth` | The number of bits required to represent the value’s significand. |
| `exponentBitPattern` | The raw encoding of the value’s exponent field. |
| `significandBitCount` | The available number of fractional significand bits. |
| `exponentBitCount` | The number of bits used to represent the type’s exponent. |
| `radix` | The radix, or base of exponentiation, for a floating-point type. |
| `init(bitPattern:)` | Creates a new value with the given bit pattern. |

### Querying a Double’s State

| API | Purpose |
|-----|---------|
| `isZero` | A Boolean value indicating whether the instance is equal to zero. |
| `isFinite` | A Boolean value indicating whether this instance is finite. |
| `isInfinite` | A Boolean value indicating whether the instance is infinite. |
| `isNaN` | A Boolean value indicating whether the instance is NaN (“not a number”). |
| `isSignalingNaN` | A Boolean value indicating whether the instance is a signaling NaN. |
| `isNormal` | A Boolean value indicating whether this instance is normal. |
| `isSubnormal` | A Boolean value indicating whether the instance is subnormal. |
| `isCanonical` | A Boolean value indicating whether the instance’s representation is in |

### Encoding and Decoding Values

| API | Purpose |
|-----|---------|
| `encode(to:)` | Encodes this value into the given encoder. |
| `init(from:)` | Creates a new instance by decoding from the given decoder. |

### Creating a Range

| API | Purpose |
|-----|---------|
| `...(_:_:)` | Returns a closed range that contains both of its bounds. |

### Describing a Double

| API | Purpose |
|-----|---------|
| `description` | A textual representation of the value. |
| `debugDescription` | A textual representation of the value, suitable for debugging. |
| `customMirror` | A mirror that reflects the `Double` instance. |
| `hash(into:)` | Hashes the essential components of this value by feeding them into the |

### Infrequently Used Functionality

| API | Purpose |
|-----|---------|
| `init()` | — |
| `init(floatLiteral:)` | Creates an instance initialized to the specified floating-point value. |
| `init(integerLiteral:)` | Creates an instance initialized to the specified integer value. |
| `init(integerLiteral:)` | — |
| `Double.FloatLiteralType` | A type that represents a floating-point literal. |
| `Double.IntegerLiteralType` | A type that represents an integer literal. |
| `advanced(by:)` | Returns a value that is offset the specified distance from this value. |
| `distance(to:)` | Returns the distance from this value to the given value, expressed as a |

### SIMD-Supporting Types

| API | Purpose |
|-----|---------|
| `Double.SIMDMaskScalar` | — |
| `Double.SIMD2Storage` | Storage for a vector of two floating-point values. |
| `Double.SIMD4Storage` | Storage for a vector of four floating-point values. |
| `Double.SIMD8Storage` | Storage for a vector of eight floating-point values. |
| `Double.SIMD16Storage` | Storage for a vector of 16 floating-point values. |
| `Double.SIMD32Storage` | Storage for a vector of 32 floating-point values. |
| `Double.SIMD64Storage` | Storage for a vector of 64 floating-point values. |

### Deprecated

| API | Purpose |
|-----|---------|
| `customPlaygroundQuickLook` | A custom playground Quick Look for the `Double` instance. |
| `init(_:)` | — |
