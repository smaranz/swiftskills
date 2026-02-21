---
name: Double
description: Apple Swift Documentation for Double.
---

# Double

A double-precision (64-bit), floating-point value type.

```
@frozen struct Double
```

## Topics

### Converting Integers

[`init(_:)`](/documentation/Swift/Double/init(_:)-5blrp)

Creates a new value, rounded to the closest possible representation.

[`init(_:)`](/documentation/Swift/Double/init(_:)-84ohu)

Creates a new value, rounded to the closest possible representation.

### Converting Strings

[`init(_:)`](/documentation/Swift/Double/init(_:)-5wmm8)

Creates a new instance from the given string.

[`init(_:)`](/documentation/Swift/Double/init(_:)-15kej)

### Converting Floating-Point Values

[`init(_:)`](/documentation/Swift/Double/init(_:)-1488d)

Creates a new instance from the given value, rounded to the closest
possible representation.

[`init(_:)`](/documentation/Swift/Double/init(_:)-o1k9)

Creates a new instance initialized to the given value.

[`init(_:)`](/documentation/Swift/Double/init(_:)-5h7qh)

Creates a new instance that approximates the given value.

[`init(_:)`](/documentation/Swift/Double/init(_:)-aeox)

Creates a new instance that approximates the given value.

[`init(_:)`](/documentation/Swift/Double/init(_:)-9z7ob)

Creates a new instance that approximates the given value.

[`init(_:)`](/documentation/Swift/Double/init(_:)-7ag2w)

[`init(sign:exponent:significand:)`](/documentation/Swift/Double/init(sign:exponent:significand:))

Creates a new value from the given sign, exponent, and significand.

[`init(signOf:magnitudeOf:)`](/documentation/Swift/Double/init(signOf:magnitudeOf:))

Creates a new floating-point value using the sign of one value and the
magnitude of another.

[`init(_:)`](/documentation/Swift/Double/init(_:)-1oh9r)

Creates a new value, rounded to the closest possible representation.

[`init(truncating:)`](/documentation/Swift/Double/init(truncating:))

### Converting with No Loss of Precision

These initializers result in `nil` if the value passed can’t be represented without
any loss of precision.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-8esra)

Creates a new instance from the given value, if it can be represented
exactly.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-1h1oc)

Creates a new value, if the given integer can be represented exactly.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-2uexo)

Creates a new value, if the given integer can be represented exactly.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-2l6p1)

Creates a new instance initialized to the given value, if it can be
represented without rounding.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-7cl0t)

Creates a new instance initialized to the given value, if it can be
represented without rounding.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-50ofc)

Creates a new instance initialized to the given value, if it can be
represented without rounding.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-63925)

Creates a new instance initialized to the given value, if it can be
represented without rounding.

[`init(exactly:)`](/documentation/Swift/Double/init(exactly:)-8e00y)

### Creating a Random Value

[`random(in:)`](/documentation/Swift/Double/random(in:)-6idef)

Returns a random value within the specified range.

[`random(in:using:)`](/documentation/Swift/Double/random(in:using:)-1m6gd)

Returns a random value within the specified range, using the given
generator as a source for randomness.

[`random(in:)`](/documentation/Swift/Double/random(in:)-5o5ha)

Returns a random value within the specified range.

[`random(in:using:)`](/documentation/Swift/Double/random(in:using:)-613hz)

Returns a random value within the specified range, using the given
generator as a source for randomness.

### Performing Calculations

  <doc://com.apple.Swift/documentation/Swift/floating-point-operators-for-double>

[`addingProduct(_:_:)`](/documentation/Swift/Double/addingProduct(_:_:))

Returns the result of adding the product of the two given values to this
value, computed without intermediate rounding.

[`addProduct(_:_:)`](/documentation/Swift/Double/addProduct(_:_:))

Adds the product of the two given values to this value in place, computed
without intermediate rounding.

[`squareRoot()`](/documentation/Swift/Double/squareRoot())

Returns the square root of the value, rounded to a representable value.

[`formSquareRoot()`](/documentation/Swift/Double/formSquareRoot())

Replaces this value with its square root, rounded to a representable
value.

[`remainder(dividingBy:)`](/documentation/Swift/Double/remainder(dividingBy:))

Returns the remainder of this value divided by the given value.

[`formRemainder(dividingBy:)`](/documentation/Swift/Double/formRemainder(dividingBy:))

Replaces this value with the remainder of itself divided by the given
value.

[`truncatingRemainder(dividingBy:)`](/documentation/Swift/Double/truncatingRemainder(dividingBy:))

Returns the remainder of this value divided by the given value using
truncating division.

[`formTruncatingRemainder(dividingBy:)`](/documentation/Swift/Double/formTruncatingRemainder(dividingBy:))

Replaces this value with the remainder of itself divided by the given
value using truncating division.

[`negate()`](/documentation/Swift/Double/negate())

Replaces this value with its additive inverse.

### Rounding Values

[`rounded()`](/documentation/Swift/Double/rounded())

[`rounded(_:)`](/documentation/Swift/Double/rounded(_:))

Returns this value rounded to an integral value using the specified
rounding rule.

[`round()`](/documentation/Swift/Double/round())

[`round(_:)`](/documentation/Swift/Double/round(_:))

Rounds the value to an integral value using the specified rounding rule.

### Comparing Values

  <doc://com.apple.Swift/documentation/Swift/floating-point-operators-for-double>

[`isEqual(to:)`](/documentation/Swift/Double/isEqual(to:))

Returns a Boolean value indicating whether this instance is equal to the
given value.

[`isLess(than:)`](/documentation/Swift/Double/isLess(than:))

Returns a Boolean value indicating whether this instance is less than the
given value.

[`isLessThanOrEqualTo(_:)`](/documentation/Swift/Double/isLessThanOrEqualTo(_:))

Returns a Boolean value indicating whether this instance is less than or
equal to the given value.

[`isTotallyOrdered(belowOrEqualTo:)`](/documentation/Swift/Double/isTotallyOrdered(belowOrEqualTo:))

Returns a Boolean value indicating whether this instance should precede
or tie positions with the given value in an ascending sort.

[`minimum(_:_:)`](/documentation/Swift/Double/minimum(_:_:))

Returns the lesser of the two given values.

[`minimumMagnitude(_:_:)`](/documentation/Swift/Double/minimumMagnitude(_:_:))

Returns the value with lesser magnitude.

[`maximum(_:_:)`](/documentation/Swift/Double/maximum(_:_:))

Returns the greater of the two given values.

[`maximumMagnitude(_:_:)`](/documentation/Swift/Double/maximumMagnitude(_:_:))

Returns the value with greater magnitude.

### Finding the Sign and Magnitude

[`magnitude`](/documentation/Swift/Double/magnitude-swift.property)

The magnitude of this value.

[`sign`](/documentation/Swift/Double/sign)

The sign of the floating-point value.

[`Double.Magnitude`](/documentation/Swift/Double/Magnitude-swift.typealias)

A type that can represent the absolute value of any possible value of the
conforming type.

### Querying a Double

[`ulp`](/documentation/Swift/Double/ulp)

The unit in the last place of this value.

[`significand`](/documentation/Swift/Double/significand)

The significand of the floating-point value.

[`exponent`](/documentation/Swift/Double/exponent-swift.property)

The exponent of the floating-point value.

[`nextUp`](/documentation/Swift/Double/nextUp)

The least representable value that compares greater than this value.

[`nextDown`](/documentation/Swift/Double/nextDown)

The greatest representable value that compares less than this value.

[`binade`](/documentation/Swift/Double/binade)

The floating-point value with the same sign and exponent as this value,
but with a significand of 1.0.

### Accessing Numeric Constants

[`pi`](/documentation/Swift/Double/pi)

The mathematical constant pi (π), approximately equal to 3.14159.

[`infinity`](/documentation/Swift/Double/infinity)

Positive infinity.

[`greatestFiniteMagnitude`](/documentation/Swift/Double/greatestFiniteMagnitude)

The greatest finite number representable by this type.

[`nan`](/documentation/Swift/Double/nan)

A quiet NaN (“not a number”).

[`signalingNaN`](/documentation/Swift/Double/signalingNaN)

A signaling NaN (“not a number”).

[`ulpOfOne`](/documentation/Swift/Double/ulpOfOne)

The unit in the last place of 1.0.

[`leastNonzeroMagnitude`](/documentation/Swift/Double/leastNonzeroMagnitude)

The least positive number.

[`leastNormalMagnitude`](/documentation/Swift/Double/leastNormalMagnitude)

The least positive normal number.

[`zero`](/documentation/Swift/Double/zero)

The zero value.

### Working with Binary Representation

[`bitPattern`](/documentation/Swift/Double/bitPattern)

The bit pattern of the value’s encoding.

[`significandBitPattern`](/documentation/Swift/Double/significandBitPattern)

The raw encoding of the value’s significand field.

[`significandWidth`](/documentation/Swift/Double/significandWidth)

The number of bits required to represent the value’s significand.

[`exponentBitPattern`](/documentation/Swift/Double/exponentBitPattern)

The raw encoding of the value’s exponent field.

[`significandBitCount`](/documentation/Swift/Double/significandBitCount)

The available number of fractional significand bits.

[`exponentBitCount`](/documentation/Swift/Double/exponentBitCount)

The number of bits used to represent the type’s exponent.

[`radix`](/documentation/Swift/Double/radix)

The radix, or base of exponentiation, for a floating-point type.

[`init(bitPattern:)`](/documentation/Swift/Double/init(bitPattern:))

Creates a new value with the given bit pattern.

[`init(sign:exponentBitPattern:significandBitPattern:)`](/documentation/Swift/Double/init(sign:exponentBitPattern:significandBitPattern:))

Creates a new instance from the specified sign and bit patterns.

[`init(nan:signaling:)`](/documentation/Swift/Double/init(nan:signaling:))

Creates a NaN (“not a number”) value with the specified payload.

[`Double.Exponent`](/documentation/Swift/Double/Exponent-swift.typealias)

A type that can represent any written exponent.

[`Double.RawSignificand`](/documentation/Swift/Double/RawSignificand)

A type that represents the encoded significand of a value.

[`Double.RawExponent`](/documentation/Swift/Double/RawExponent)

A type that represents the encoded exponent of a value.

### Querying a Double’s State

[`isZero`](/documentation/Swift/Double/isZero)

A Boolean value indicating whether the instance is equal to zero.

[`isFinite`](/documentation/Swift/Double/isFinite)

A Boolean value indicating whether this instance is finite.

[`isInfinite`](/documentation/Swift/Double/isInfinite)

A Boolean value indicating whether the instance is infinite.

[`isNaN`](/documentation/Swift/Double/isNaN)

A Boolean value indicating whether the instance is NaN (“not a number”).

[`isSignalingNaN`](/documentation/Swift/Double/isSignalingNaN)

A Boolean value indicating whether the instance is a signaling NaN.

[`isNormal`](/documentation/Swift/Double/isNormal)

A Boolean value indicating whether this instance is normal.

[`isSubnormal`](/documentation/Swift/Double/isSubnormal)

A Boolean value indicating whether the instance is subnormal.

[`isCanonical`](/documentation/Swift/Double/isCanonical)

A Boolean value indicating whether the instance’s representation is in
its canonical form.

[`floatingPointClass`](/documentation/Swift/Double/floatingPointClass)

The classification of this value.

### Encoding and Decoding Values

[`encode(to:)`](/documentation/Swift/Double/encode(to:))

Encodes this value into the given encoder.

[`init(from:)`](/documentation/Swift/Double/init(from:))

Creates a new instance by decoding from the given decoder.

### Creating a Range

[`...(_:_:)`](/documentation/Swift/Double/...(_:_:))

Returns a closed range that contains both of its bounds.

### Describing a Double

[`description`](/documentation/Swift/Double/description)

A textual representation of the value.

[`debugDescription`](/documentation/Swift/Double/debugDescription)

A textual representation of the value, suitable for debugging.

[`customMirror`](/documentation/Swift/Double/customMirror)

A mirror that reflects the `Double` instance.

[`hash(into:)`](/documentation/Swift/Double/hash(into:))

Hashes the essential components of this value by feeding them into the
given hasher.

### Using a Double as a Data Value

### Infrequently Used Functionality

[`init()`](/documentation/Swift/Double/init())

[`init(floatLiteral:)`](/documentation/Swift/Double/init(floatLiteral:))

Creates an instance initialized to the specified floating-point value.

[`init(integerLiteral:)`](/documentation/Swift/Double/init(integerLiteral:))

Creates an instance initialized to the specified integer value.

[`init(integerLiteral:)`](/documentation/Swift/Double/init(integerLiteral:)-6hc7j)

[`Double.FloatLiteralType`](/documentation/Swift/Double/FloatLiteralType)

A type that represents a floating-point literal.

[`Double.IntegerLiteralType`](/documentation/Swift/Double/IntegerLiteralType)

A type that represents an integer literal.

[`advanced(by:)`](/documentation/Swift/Double/advanced(by:))

Returns a value that is offset the specified distance from this value.

[`distance(to:)`](/documentation/Swift/Double/distance(to:))

Returns the distance from this value to the given value, expressed as a
stride.

[`Double.Stride`](/documentation/Swift/Double/Stride)

A type that represents the distance between two values.

[`write(to:)`](/documentation/Swift/Double/write(to:))

Writes a textual representation of this instance into the given output
stream.

[`hashValue`](/documentation/Swift/Double/hashValue)

The hash value.

### SIMD-Supporting Types

[`Double.SIMDMaskScalar`](/documentation/Swift/Double/SIMDMaskScalar)

[`Double.SIMD2Storage`](/documentation/Swift/Double/SIMD2Storage)

Storage for a vector of two floating-point values.

[`Double.SIMD4Storage`](/documentation/Swift/Double/SIMD4Storage)

Storage for a vector of four floating-point values.

[`Double.SIMD8Storage`](/documentation/Swift/Double/SIMD8Storage)

Storage for a vector of eight floating-point values.

[`Double.SIMD16Storage`](/documentation/Swift/Double/SIMD16Storage)

Storage for a vector of 16 floating-point values.

[`Double.SIMD32Storage`](/documentation/Swift/Double/SIMD32Storage)

Storage for a vector of 32 floating-point values.

[`Double.SIMD64Storage`](/documentation/Swift/Double/SIMD64Storage)

Storage for a vector of 64 floating-point values.

### Deprecated

[`customPlaygroundQuickLook`](/documentation/Swift/Double/customPlaygroundQuickLook)

A custom playground Quick Look for the `Double` instance.

[`init(_:)`](/documentation/Swift/Double/init(_:)-8kme5)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
