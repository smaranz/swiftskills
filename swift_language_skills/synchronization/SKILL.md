---
name: Synchronization
description: Apple Synchronization Documentation for Synchronization.
---

# Synchronization

Build synchronization constructs using low-level, primitive operations.

## Topics

### Atomic Values

[`Atomic`](/documentation/Synchronization/Atomic)

An atomic value.

[`AtomicLazyReference`](/documentation/Synchronization/AtomicLazyReference)

A lazily initializable atomic strong reference.

[`WordPair`](/documentation/Synchronization/WordPair)

A pair of two word sized `UInt`s.

[`AtomicRepresentable`](/documentation/Synchronization/AtomicRepresentable)

A type that supports atomic operations through a separate atomic storage
representation.

[`AtomicOptionalRepresentable`](/documentation/Synchronization/AtomicOptionalRepresentable)

An atomic value that also supports atomic operations when wrapped
in an `Optional`. Atomic optional representable types come with a standalone
atomic representation for their optional-wrapped variants.

### Memory Ordering Semantics

[`AtomicLoadOrdering`](/documentation/Synchronization/AtomicLoadOrdering)

Specifies the memory ordering semantics of an atomic load operation.

[`AtomicStoreOrdering`](/documentation/Synchronization/AtomicStoreOrdering)

Specifies the memory ordering semantics of an atomic store operation.

[`AtomicUpdateOrdering`](/documentation/Synchronization/AtomicUpdateOrdering)

Specifies the memory ordering semantics of an atomic read-modify-write
operation.

[`atomicMemoryFence(ordering:)`](/documentation/Synchronization/atomicMemoryFence(ordering:))

Establishes a memory ordering without associating it with a
particular atomic operation.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
