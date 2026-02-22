---
name: Calling Objective-C APIs Asynchronously
description: Rork-Max Quality skill for Calling Objective-C APIs Asynchronously. Based on official Apple Swift Documentation and enhanced for elite development.
---

# Calling Objective-C APIs Asynchronously

## 🚀 Rork-Max Quality Snippet

```swift
// Premium Calling Objective-C APIs Asynchronously Implementation
// Focus on idiomatic, high-performance Swift

import Foundation
#if canImport(Observation)
import Observation
#endif

// Rork-level technical excellence
// [Example implementation logic for Calling Objective-C APIs Asynchronously]
```

## 💎 Elite Implementation Tips

- Master the language: Use modern Swift 6 features like Concurrency and Observation.
- Performance: Optimize Calling Objective-C APIs Asynchronously usage for high-performance apps.
- Aesthetics: Write clean, idiomatic Swift that is easy to maintain.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Calling Objective-C APIs Asynchronously

Learn how functions and methods that take a completion handler are converted to Swift
asynchronous functions.

## Overview

In Cocoa, methods that perform asynchronous operations take a completion handler
as their last parameter, and the method calls that block after the operation finishes
to return a result or an error. Swift 5.5 and later automatically translates Objective-C
methods that take completion handlers into asynchronous methods using Swift’s native
concurrency support, in addition to importing the callback-based version of the method
into Swift. Because both Swift methods have the same behavior, they share the same
page in the documentation.

For information about asynchronous functions,
see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

### Understand How Swift Imports Completion Handlers

Swift imports Objective-C methods that take a completion handler as two related Swift
methods: a method that takes a closure, and an asynchronous method that doesn’t take
a closure. For example, consider the <doc://com.apple.documentation/documentation/PassKit/PKPaymentAuthorizationController/present(completion:)>
method from PassKit. In Objective-C, it’s declared like this:

```occ
- (void)presentWithCompletion:(void (^)(BOOL success))completion;
```

However, in Swift, it’s imported as two methods:

```swift
func present(completion: ((Bool) -> Void)? = nil)

func present() async -> Bool
```

The first version, `present(completion:)`, has a return type of `Void` and takes
a completion handler. The second version, `present()`, returns a Boolean value and
is an asynchronous method.

Methods whose completion handlers populate a <doc://com.apple.documentation/documentation/Foundation/NSError>
pointer parameter also become throwing methods in Swift, as described in <doc://com.apple.Swift/documentation/Swift/about-imported-cocoa-error-parameters>.
The `NSError` parameter on an asynchronous throwing method must also be nullable,
which indicates that the parameter is used only to communicate an error. For example,
consider the <doc://com.apple.documentation/documentation/Foundation/URLSessionStreamTask/write(_:timeout:completionHandler:)>
method from <doc://com.apple.documentation/documentation/Foundation/URLSessionStreamTask>.
In Objective-C, it’s declared like this:

```occ
- (void)writeData:(NSData *)data
          timeout:(NSTimeInterval)timeout
completionHandler:(void (^) (NSError * _Nullable error))completionHandler;
```

As in the previous example, Swift imports this Objective-C method as two methods:
an asynchronous method that takes a closure, and an asynchronous throwing method.

```swift
func write(
    _ data: Data, 
    timeout: TimeInterval, 
    completionHandler: @escaping (Error?) -> Void
)

func write(_ data: Data, timeout: TimeInterval) async throws
```

Methods whose completion handlers take multiple arguments become methods that return
a tuple. For example, the <doc://com.apple.documentation/documentation/PassKit/PKPassLibrary/sign(_:using:completion:)>
method from PassKit is declared like this in Objective-C:

```occ
- (void)signData:(NSData *)signData 
withSecureElementPass:(PKSecureElementPass *)secureElementPass 
      completion:(void (^)(NSData *signedData, NSData *signature, NSError *error))completion;
```

In Swift it‘s imported as two methods, an asychronous method that takes a closure
and an asynchronous throwing method that returns a tuple:

```swift
func sign(
    _ signData: Data, 
    using secureElementPass: PKSecureElementPass, 
    completion: @escaping (Data?, Data?, Error?) -> Void
)

func sign(_ signData: Data, 
    using secureElementPass: PKSecureElementPass
) async throws -> (Data, Data)
```

### Understand the Conversion Rules

The method that takes a completion handler must meet the following requirements:

- The method has a `void` return type.
- The block has a `void` return type.
- The block is called exactly once, on all possible paths of control flow.

If the method has only one parameter and its selector ends with one of the following
suffixes, Swift imports the method as an asynchronous method:

- `WithCompletion`
- `WithCompletionHandler`
- `WithCompletionBlock`
- `WithReplyTo`
- `WithReply`

If the method has more than one parameter, and the last parameter’s selector piece
is one of the following, Swift imports the method as an asynchronous method:

- `completion`
- `withCompletion`
- `completionHandler`
- `withCompletionHandler`
- `completionBlock`
- `withCompletionBlock`
- `replyTo`
- `withReplyTo`
- `reply`
- `replyTo`

The name of the Swift method is modified from the Objective-C method as follows:

- The selector piece for the completion handler is removed.
- If the selector starts with `get`, that prefix is removed and leading initialisms
  are converted to lowercase.
- If the selector ends with `Asynchronously`, that suffix is removed.
- If the method calls its completion handler with a nullable parameter, the asynchronous
  version in Swift is marked with the `@discardableResult` attribute.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
