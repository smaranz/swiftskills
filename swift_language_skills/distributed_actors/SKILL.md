---
name: Distributed
description: Apple Distributed Documentation for Distributed.
---

# Distributed

Build systems that run distributed code across multiple processes and devices.

## Overview

Distributed actors share many characteristics with Swift actors,
and include additional isolation checks to ensure
location transparency and safety in a distributed environment.
Similar to how actors make it easier to write concurrent code
that’s safe and correct to run on a single computer,
distributed actors make it easier to write code
that runs across multiple computers.

![A diagram showing two columns of actors. The left column includes a remote actor reference. The right column includes a local distributed actor. An arrow points from the remote actor reference to the local distributed actor that it refers to.](images/com.apple.Swift/distributed-module@2x.png)

You use three main parts when writing code with distributed actors:

- Swift language support for actors and distributed actors.
  For more information,
  see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).
- The Distributed module, which includes the types and protocols you need
  to declare and use distribute actors.
  For example, it has
  protocols to which distributed actors and distributed actor systems conform,
  and structures that encapsulate information about calls to a distributed actor.
- A *distributed actor system*, also called a cluster runtime,
  provides an implementation of the ``doc://com.apple.Swift/documentation/Distributed/DistributedActorSystem`` protocol
  and coordinates between the cluster’s nodes.
  A distributed actor is always part of some distributed actor system;
  that distributed actor system handles the serialization and networking
  necessary to perform remote method calls.
  For local testing, you can use ``doc://com.apple.Swift/documentation/Distributed/LocalTestingDistributedActorSystem``.
  For production,
  you can use the distributed actor system
  from the [Swift Distributed Actors](https://github.com/apple/swift-distributed-actors/) library,
  use another library,
  or write your own distributed actor system.

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors>

### Distributed Actors

[`DistributedActor`](/documentation/Distributed/DistributedActor)

Common protocol to which all distributed actors conform implicitly.

[`DistributedActorSystem`](/documentation/Distributed/DistributedActorSystem)

A distributed actor system underpins and implements all functionality of distributed actors.

[`Resolvable()`](/documentation/Distributed/Resolvable())

Enables the attached to protocol to be resolved as remote distributed
actor reference.

[`buildDefaultDistributedRemoteActorExecutor(_:)`](/documentation/Distributed/buildDefaultDistributedRemoteActorExecutor(_:))

Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references.
The executor is shared between all remote default executor remote distributed actors,
and it will crash if any job is enqueued on it.

### Remote Calls

[`RemoteCallTarget`](/documentation/Distributed/RemoteCallTarget)

Represents a ‘target’ of a distributed call, such as a `distributed func` or
`distributed` computed property. Identification schemes may vary between
systems, and are subject to evolution.

[`RemoteCallArgument`](/documentation/Distributed/RemoteCallArgument)

Represents an argument passed to a distributed call target.

[`DistributedTargetInvocationEncoder`](/documentation/Distributed/DistributedTargetInvocationEncoder)

Used to encode an invocation of a distributed target (method or computed property).

[`DistributedTargetInvocationDecoder`](/documentation/Distributed/DistributedTargetInvocationDecoder)

Decoder that must be provided to `executeDistributedTarget` and is used
by the Swift runtime to decode arguments of the invocation.

[`DistributedTargetInvocationResultHandler`](/documentation/Distributed/DistributedTargetInvocationResultHandler)

Protocol a distributed invocation execution’s result handler.

### Local Testing

[`LocalTestingDistributedActorSystem`](/documentation/Distributed/LocalTestingDistributedActorSystem)

A `DistributedActorSystem` designed for local only testing.

[`LocalTestingActorID`](/documentation/Distributed/LocalTestingActorID)

[`LocalTestingActorAddress`](/documentation/Distributed/LocalTestingActorAddress)

[`LocalTestingInvocationEncoder`](/documentation/Distributed/LocalTestingInvocationEncoder)

[`LocalTestingInvocationDecoder`](/documentation/Distributed/LocalTestingInvocationDecoder)

[`LocalTestingInvocationResultHandler`](/documentation/Distributed/LocalTestingInvocationResultHandler)

### Errors

[`DistributedActorCodingError`](/documentation/Distributed/DistributedActorCodingError)

Error thrown by distributed actor systems while encountering encoding/decoding
issues.

[`DistributedActorSystemError`](/documentation/Distributed/DistributedActorSystemError)

Error protocol to which errors thrown by any `DistributedActorSystem` should conform.

[`ExecuteDistributedTargetError`](/documentation/Distributed/ExecuteDistributedTargetError)

Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](/documentation/Distributed/DistributedActorSystem/executeDistributedTarget(on:target:invocationDecoder:handler:)).

[`LocalTestingDistributedActorSystemError`](/documentation/Distributed/LocalTestingDistributedActorSystemError)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
