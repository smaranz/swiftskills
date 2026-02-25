---
name: Distributed
description: Rork-Max Quality skill for Distributed. Actionable Swift language patterns and best practices.
---

# Distributed

Build systems that run distributed code across multiple processes and devices.
Distributed actors share many characteristics with Swift actors,
and include additional isolation checks to ensure
location transparency and safety in a distributed environment.
Similar to how actors make it easier to write concurrent code
that’s safe and correct to run on a single computer,
distributed actors make it easier to write code
that runs across multiple computers.
You use three main parts when writing code with distributed actors:
- Swift language support for actors and distributed actors.
For more information,
see Concurrency in The Swift Programming Language.
- The Distributed module, which includes the types and protocols you need
to declare and use distribute actors.
For example, it has
protocols to which distributed actors and distributed actor systems conform,
and structures that encapsulate information about calls to a distributed actor.
- A *distributed actor system*, also called a cluster runtime,
provides an implementation of the `DistributedActorSystem` protocol
and coordinates between the cluster’s nodes.
A distributed actor is always part of some distributed actor system;
that distributed actor system handles the serialization and networking
necessary to perform remote method calls.
For local testing, you can use `LocalTestingDistributedActorSystem`.
For production,
you can use the distributed actor system
from the Swift Distributed Actors library,
use another library,
or write your own distributed actor system.

## 🚀 Rork-Max Quality Snippet

```swift
import Foundation

// Distributed — idiomatic Swift implementation pattern
// Use modern Swift 6 features: @Observable, async/await, structured concurrency
```

## 💎 Elite Implementation Tips

- Use modern Swift 6 patterns when working with Distributed.
- Prefer value types (structs/enums) unless reference semantics are needed.
- Leverage Swift's type system to catch errors at compile time.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## When to Use

- Performing network requests, file I/O, or database queries off the main thread
- Managing shared mutable state safely with actors
- Running multiple independent tasks in parallel with `TaskGroup`

## Best Practices

- Use `async/await` instead of completion handlers
- Mark UI-updating code as `@MainActor` to ensure it runs on the main thread
- Use `Task { }` to bridge from synchronous to asynchronous contexts
- Prefer structured concurrency (`async let`, `TaskGroup`) over unstructured `Task`

## Common Pitfalls

- Blocking the main actor with synchronous work disguised as async
- Creating unbounded numbers of `Task` instances without cancellation
- Capturing `self` strongly in long-lived tasks causing memory leaks

## Key APIs

### Distributed Actors

| API | Purpose |
|-----|---------|
| `DistributedActor` | Common protocol to which all distributed actors conform implicitly. |
| `DistributedActorSystem` | A distributed actor system underpins and implements all functionality of distributed actors. |
| `Resolvable()` | Enables the attached to protocol to be resolved as remote distributed |
| `buildDefaultDistributedRemoteActorExecutor(_:)` | Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. |

### Remote Calls

| API | Purpose |
|-----|---------|
| `RemoteCallTarget` | Represents a ‘target’ of a distributed call, such as a `distributed func` or |
| `RemoteCallArgument` | Represents an argument passed to a distributed call target. |
| `DistributedTargetInvocationEncoder` | Used to encode an invocation of a distributed target (method or computed property). |
| `DistributedTargetInvocationDecoder` | Decoder that must be provided to `executeDistributedTarget` and is used |
| `DistributedTargetInvocationResultHandler` | Protocol a distributed invocation execution’s result handler. |

### Local Testing

| API | Purpose |
|-----|---------|
| `LocalTestingDistributedActorSystem` | A `DistributedActorSystem` designed for local only testing. |
| `LocalTestingActorID` | — |
| `LocalTestingActorAddress` | — |
| `LocalTestingInvocationEncoder` | — |
| `LocalTestingInvocationDecoder` | — |

### Errors

| API | Purpose |
|-----|---------|
| `DistributedActorCodingError` | Error thrown by distributed actor systems while encountering encoding/decoding |
| `DistributedActorSystemError` | Error protocol to which errors thrown by any `DistributedActorSystem` should conform. |
| `ExecuteDistributedTargetError` | Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](/documentation/Distributed/DistributedActorSystem/executeDistributedTarget(on:target:invocationDecoder:handler:)). |
| `LocalTestingDistributedActorSystemError` | — |
