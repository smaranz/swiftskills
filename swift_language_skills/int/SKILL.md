---
name: Int
description: Apple Swift Documentation for Int.
---

# Int

A signed integer value type.

```
@frozen struct Int
```

## Overview

On 32-bit platforms, `Int` is the same size as `Int32`, and
on 64-bit platforms, `Int` is the same size as `Int64`.

## Topics

### Converting Integers

[`init(_:)`](/documentation/Swift/Int/init(_:)-4ekvl)

Creates a new instance from the given integer.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-b1dy)

[`init(clamping:)`](/documentation/Swift/Int/init(clamping:))

Creates a new instance with the representable value that’s closest to the
given integer.

[`init(truncatingIfNeeded:)`](/documentation/Swift/Int/init(truncatingIfNeeded:))

Creates a new instance from the bit pattern of the given instance by
sign-extending or truncating to fit this type.

[`init(bitPattern:)`](/documentation/Swift/Int/init(bitPattern:)-72037)

Creates a new instance with the same memory representation as the given
value.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-177ax)

[`init(truncating:)`](/documentation/Swift/Int/init(truncating:))

### Converting Floating-Point Values

[`init(_:)`](/documentation/Swift/Int/init(_:)-6gt9z)

[`init(_:)`](/documentation/Swift/Int/init(_:)-8vbwo)

Creates an integer from the given floating-point value, rounding toward
zero.

[`init(_:)`](/documentation/Swift/Int/init(_:)-2oscb)

Creates an integer from the given floating-point value, rounding toward
zero.

[`init(_:)`](/documentation/Swift/Int/init(_:)-3huv0)

Creates an integer from the given floating-point value, rounding toward
zero.

[`init(_:)`](/documentation/Swift/Int/init(_:)-66i0w)

Creates an integer from the given floating-point value, rounding toward
zero.

[`init(_:)`](/documentation/Swift/Int/init(_:)-5q6q5)

### Converting with No Loss of Precision

These initializers result in `nil` if the value passed can’t be represented without
any loss of precision.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-7yhn6)

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-77kq8)

Creates an integer from the given floating-point value, if it can be
represented exactly.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-7qdwf)

Creates an integer from the given floating-point value, if it can be
represented exactly.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-5xh2s)

Creates an integer from the given floating-point value, if it can be
represented exactly.

[`init(exactly:)`](/documentation/Swift/Int/init(exactly:)-5kot1)

Creates an integer from the given floating-point value, if it can be
represented exactly.

### Converting Strings

[`init(_:)`](/documentation/Swift/Int/init(_:)-2hmii)

Creates a new integer value from the given string.

[`init(_:radix:)`](/documentation/Swift/Int/init(_:radix:))

Creates a new integer value from the given string and radix.

### Creating a Random Integer

[`random(in:)`](/documentation/Swift/Int/random(in:)-9mjpw)

Returns a random value within the specified range.

[`random(in:using:)`](/documentation/Swift/Int/random(in:using:)-4lsb5)

Returns a random value within the specified range, using the given
generator as a source for randomness.

[`random(in:)`](/documentation/Swift/Int/random(in:)-8zzqh)

Returns a random value within the specified range.

[`random(in:using:)`](/documentation/Swift/Int/random(in:using:)-3dwv4)

Returns a random value within the specified range, using the given
generator as a source for randomness.

### Performing Calculations

  <doc://com.apple.Swift/documentation/Swift/integer-operators>

[`negate()`](/documentation/Swift/Int/negate())

Replaces this value with its additive inverse.

[`quotientAndRemainder(dividingBy:)`](/documentation/Swift/Int/quotientAndRemainder(dividingBy:))

Returns the quotient and remainder of this value divided by the given
value.

[`isMultiple(of:)`](/documentation/Swift/Int/isMultiple(of:))

Returns `true` if this value is a multiple of the given value, and `false`
otherwise.

### Performing Calculations with Overflow

These methods return the result of an operation, and a flag indicating whether the
operation overflowed the bounds of the type.

[`addingReportingOverflow(_:)`](/documentation/Swift/Int/addingReportingOverflow(_:))

Returns the sum of this value and the given value, along with a Boolean
value indicating whether overflow occurred in the operation.

[`subtractingReportingOverflow(_:)`](/documentation/Swift/Int/subtractingReportingOverflow(_:))

Returns the difference obtained by subtracting the given value from this
value, along with a Boolean value indicating whether overflow occurred in
the operation.

[`multipliedReportingOverflow(by:)`](/documentation/Swift/Int/multipliedReportingOverflow(by:))

Returns the product of this value and the given value, along with a
Boolean value indicating whether overflow occurred in the operation.

[`dividedReportingOverflow(by:)`](/documentation/Swift/Int/dividedReportingOverflow(by:))

Returns the quotient obtained by dividing this value by the given value,
along with a Boolean value indicating whether overflow occurred in the
operation.

[`remainderReportingOverflow(dividingBy:)`](/documentation/Swift/Int/remainderReportingOverflow(dividingBy:))

Returns the remainder after dividing this value by the given value, along
with a Boolean value indicating whether overflow occurred during division.

### Performing Double-Width Calculations

[`multipliedFullWidth(by:)`](/documentation/Swift/Int/multipliedFullWidth(by:))

Returns a tuple containing the high and low parts of the result of
multiplying this value by the given value.

[`dividingFullWidth(_:)`](/documentation/Swift/Int/dividingFullWidth(_:))

Returns a tuple containing the quotient and remainder of dividing the
given value by this value.

### Finding the Sign and Magnitude

[`magnitude`](/documentation/Swift/Int/magnitude-swift.property)

The magnitude of this value.

[`Int.Magnitude`](/documentation/Swift/Int/Magnitude-swift.typealias)

A type that can represent the absolute value of any possible value of
this type.

[`abs(_:)`](/documentation/Swift/abs(_:))

Returns the absolute value of the given number.

[`signum()`](/documentation/Swift/Int/signum())

Returns `-1` if this value is negative and `1` if it’s positive;
otherwise, `0`.

### Accessing Numeric Constants

[`zero`](/documentation/Swift/Int/zero)

The zero value.

[`min`](/documentation/Swift/Int/min)

The minimum representable integer in this type.

[`max`](/documentation/Swift/Int/max)

The maximum representable integer in this type.

[`isSigned`](/documentation/Swift/Int/isSigned)

A Boolean value indicating whether this type is a signed integer type.

### Working with Byte Order

[`byteSwapped`](/documentation/Swift/Int/byteSwapped)

A representation of this integer with the byte order swapped.

[`littleEndian`](/documentation/Swift/Int/littleEndian)

The little-endian representation of this integer.

[`bigEndian`](/documentation/Swift/Int/bigEndian)

The big-endian representation of this integer.

[`init(littleEndian:)`](/documentation/Swift/Int/init(littleEndian:))

Creates an integer from its little-endian representation, changing the
byte order if necessary.

[`init(bigEndian:)`](/documentation/Swift/Int/init(bigEndian:))

Creates an integer from its big-endian representation, changing the byte
order if necessary.

### Working with Binary Representation

[`bitWidth`](/documentation/Swift/Int/bitWidth)

The number of bits used for the underlying binary representation of
values of this type.

[`bitWidth`](/documentation/Swift/Int/bitWidth-swift.property)

The number of bits in the current binary representation of this value.

[`nonzeroBitCount`](/documentation/Swift/Int/nonzeroBitCount)

The number of bits equal to 1 in this value’s binary representation.

[`leadingZeroBitCount`](/documentation/Swift/Int/leadingZeroBitCount)

The number of leading zeros in this value’s binary representation.

[`trailingZeroBitCount`](/documentation/Swift/Int/trailingZeroBitCount)

The number of trailing zeros in this value’s binary representation.

[`words`](/documentation/Swift/Int/words-swift.property)

A collection containing the words of this value’s binary
representation, in order from the least significant to most significant.

[`Int.Words`](/documentation/Swift/Int/Words-swift.struct)

A type that represents the words of this integer.

### Working with Memory Addresses

These initializers create an integer with the bit pattern of the memory address of
a pointer or class instance.

[`init(bitPattern:)`](/documentation/Swift/Int/init(bitPattern:)-2i0qy)

Creates a new value with the bit pattern of the given pointer.

[`init(bitPattern:)`](/documentation/Swift/Int/init(bitPattern:)-2o9co)

Creates an integer that captures the full value of the given object
identifier.

[`init(bitPattern:)`](/documentation/Swift/Int/init(bitPattern:)-5qm7a)

Creates a new value with the bit pattern of the given pointer.

### Encoding and Decoding Values

[`encode(to:)`](/documentation/Swift/Int/encode(to:))

Encodes this value into the given encoder.

[`init(from:)`](/documentation/Swift/Int/init(from:))

Creates a new instance by decoding from the given decoder.

### Describing an Integer

[`description`](/documentation/Swift/Int/description)

A textual representation of this value.

[`hash(into:)`](/documentation/Swift/Int/hash(into:))

Hashes the essential components of this value by feeding them into the
given hasher.

[`customMirror`](/documentation/Swift/Int/customMirror)

A mirror that reflects the `Int` instance.

### Using an Integer as a Data Value

### Infrequently Used Functionality

[`init()`](/documentation/Swift/Int/init())

Creates a new value equal to zero.

[`init(integerLiteral:)`](/documentation/Swift/Int/init(integerLiteral:))

[`Int.IntegerLiteralType`](/documentation/Swift/Int/IntegerLiteralType)

A type that represents an integer literal.

[`distance(to:)`](/documentation/Swift/Int/distance(to:))

Returns the distance from this value to the given value, expressed as a
stride.

[`advanced(by:)`](/documentation/Swift/Int/advanced(by:))

Returns a value that is offset the specified distance from this value.

[`Int.Stride`](/documentation/Swift/Int/Stride)

A type that represents the distance between two values.

[`hashValue`](/documentation/Swift/Int/hashValue)

The hash value.

### Deprecated

[`customPlaygroundQuickLook`](/documentation/Swift/Int/customPlaygroundQuickLook)

A custom playground Quick Look for the `Int` instance.

[`init(_:)`](/documentation/Swift/Int/init(_:)-3mb3q)

### SIMD-Supporting Types

[`Int.SIMDMaskScalar`](/documentation/Swift/Int/SIMDMaskScalar)

[`Int.SIMD2Storage`](/documentation/Swift/Int/SIMD2Storage)

Storage for a vector of two integers.

[`Int.SIMD4Storage`](/documentation/Swift/Int/SIMD4Storage)

Storage for a vector of four integers.

[`Int.SIMD8Storage`](/documentation/Swift/Int/SIMD8Storage)

Storage for a vector of eight integers.

[`Int.SIMD16Storage`](/documentation/Swift/Int/SIMD16Storage)

Storage for a vector of 16 integers.

[`Int.SIMD32Storage`](/documentation/Swift/Int/SIMD32Storage)

Storage for a vector of 32 integers.

[`Int.SIMD64Storage`](/documentation/Swift/Int/SIMD64Storage)

Storage for a vector of 64 integers.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
