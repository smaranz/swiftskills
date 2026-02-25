---
name: Calling Objective-C APIs Asynchronously
description: Rork-Max Quality skill for Calling Objective-C APIs Asynchronously. Actionable Swift language patterns and best practices.
---

# Calling Objective-C APIs Asynchronously

Learn how functions and methods that take a completion handler are converted to Swift
asynchronous functions.
In Cocoa, methods that perform asynchronous operations take a completion handler
as their last parameter, and the method calls that block after the operation finishes
to return a result or an error. Swift 5.5 and later automatically translates Objective-C
methods that take completion handlers into asynchronous methods using Swift’s native
concurrency support, in addition to importing the callback-based version of the method
into Swift. Because both Swift methods have the same behavior, they share the same
page in the documentation.
For information about asynchronous functions,
see Concurrency in The Swift Programming Language.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// ObjC completion handler API automatically gets an async overload:
// ObjC: - (void)fetchDataWithCompletion:(void (^)(NSData *, NSError *))completion;
// Swift: func fetchData() async throws -> Data

// Using the async version
func loadProfile() async throws -> UserProfile {
    let url = URL(string: "https://api.example.com/profile")!
    let (data, response) = try await URLSession.shared.data(from: url)

    guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
        throw NetworkError.badResponse
    }

    return try JSONDecoder().decode(UserProfile.self, from: data)
}

// Wrapping a callback API manually
func legacyFetch() async throws -> Data {
    try await withCheckedThrowingContinuation { continuation in
        LegacyAPI.fetch { data, error in
            if let error { continuation.resume(throwing: error) }
            else if let data { continuation.resume(returning: data) }
        }
    }
}
```

## 💎 Elite Implementation Tips

- ObjC completion-handler methods automatically get `async` overloads in Swift
- Use `withCheckedThrowingContinuation` to wrap legacy callback APIs as async
- Only resume a continuation EXACTLY once — resuming twice crashes

## When to Use

- Calling Objective-C APIs from Swift or vice versa
- Integrating C/C++ libraries into a Swift project
- Migrating an existing Objective-C codebase to Swift incrementally

## Best Practices

- Use a bridging header for Objective-C → Swift; `@objc` attribute for Swift → Objective-C
- Leverage `NS_SWIFT_NAME` in Objective-C headers for clean Swift API names
- Use `async` overloads of Objective-C completion-handler APIs

## Common Pitfalls

- Objective-C generics don't fully map to Swift generics — watch for `Any` erasure
- C pointers require careful memory management — use `withUnsafe*Pointer` wrappers
- KVO from Swift requires `@objc dynamic` properties


