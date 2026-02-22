---
name: Using Objective-C Runtime Features in Swift
description: Rork-Max Quality skill for Using Objective-C Runtime Features in Swift. Based on official Apple Swift Documentation and enhanced for elite development.
---

# Using Objective-C Runtime Features in Swift

## 🚀 Rork-Max Quality Snippet

```swift
// Premium Using Objective-C Runtime Features in Swift Implementation
// Focus on idiomatic, high-performance Swift

import Foundation
#if canImport(Observation)
import Observation
#endif

// Rork-level technical excellence
// [Example implementation logic for Using Objective-C Runtime Features in Swift]
```

## 💎 Elite Implementation Tips

- Master the language: Use modern Swift 6 features like Concurrency and Observation.
- Performance: Optimize Using Objective-C Runtime Features in Swift usage for high-performance apps.
- Aesthetics: Write clean, idiomatic Swift that is easy to maintain.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.
- Ensure all interactive elements have sufficient touch targets (min 44x44pt).

## Documentation

# Using Objective-C Runtime Features in Swift

Use selectors and key paths to interact with dynamic Objective-C APIs.

## Overview

Some Objective-C APIs—like target-action—accept method or property names as parameters,
then use those names to dynamically call or access the methods or properties. In
Swift, you use the `#selector` and `#keyPath` expressions to represent those method
or property names as selectors or key paths, respectively.

### Use Selectors to Arrange Calls to Objective-C Methods

In Objective-C, a selector is a type that refers to the name of an Objective-C method.
In Swift, Objective-C selectors are represented by the <doc://com.apple.documentation/documentation/ObjectiveC/Selector>
structure, and you create them using the `#selector` expression.

In Swift, you create a selector for an Objective-C method by placing the name of
the method within the `#selector` expression: `#selector(MyViewController.tappedButton(_:))`.
To construct a selector for a property’s Objective-C getter or setter method, prefix
the property name using the `getter:` or `setter:` label, like `#selector(getter: MyViewController.myButton)`. The example below shows a selector being used as part
of the target-action pattern to call a method in response to the <doc://com.apple.documentation/documentation/UIKit/UIControl/Event/touchUpInside>
event.

```swift
import UIKit
class MyViewController: UIViewController {
    let myButton = UIButton(frame: CGRect(x: 0, y: 0, width: 100, height: 50))

    override init(nibName nibNameOrNil: NSNib.Name?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        let action = #selector(MyViewController.tappedButton)
        myButton.addTarget(self, action: action, forControlEvents: .touchUpInside)
    }

    @objc func tappedButton(_ sender: UIButton?) {
        print("tapped button")
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}
```

If you need to disambiguate between overloaded functions, use parenthesized expressions
along with the `as` operator to make the `#selector` expression refer unambiguously
to a specific overload.

### Use Key Paths to Dynamically Access Objective-C Properties

In Objective-C, a key is a string that identifies a specific property of an object.
A key path is a string of dot-separated keys that specifies a sequence of object
properties to traverse. Keys and key paths are frequently used for key-value coding
(KVC), a mechanism for indirectly accessing an object’s attributes and relationships
using string identifiers.

> Important: Objective-C key paths are distinct from, but related to, key-path expressions
> in Swift. For information about key-path expressions,
> see [Key-Path Expression](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/expressions#Key-Path-Expression) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

You use the `#keyPath` string expression to create compiler-checked keys and key
paths that can be used by KVC methods like <doc://com.apple.documentation/documentation/ObjectiveC/NSObject-swift.class/value(forKey:)>
and <doc://com.apple.documentation/documentation/ObjectiveC/NSObject-swift.class/value(forKeyPath:)>.
The `#keyPath` string expression accepts chained method or property references. It
also supports chaining through optional values within a chain, such as `#keyPath(Person.bestFriend.name)`.
Key paths created using the `#keyPath` string expression don’t pass type information
about the properties or methods they reference to the APIs that accept key paths.

The example below defines a `Person` class, creates two instances of it, and uses
several `#keyPath` string expressions to access properties and properties of those
properties:

```swift
class Person: NSObject {
    @objc var name: String
    @objc var friends: [Person] = []
    @objc var bestFriend: Person? = nil

    init(name: String) {
        self.name = name
    }
}

let gabrielle = Person(name: "Gabrielle")
let jim = Person(name: "Jim")
let yuanyuan = Person(name: "Yuanyuan")
gabrielle.friends = [jim, yuanyuan]
gabrielle.bestFriend = yuanyuan

#keyPath(Person.name)
// "name"
gabrielle.value(forKey: #keyPath(Person.name))
// "Gabrielle"
#keyPath(Person.bestFriend.name)
// "bestFriend.name"
gabrielle.value(forKeyPath: #keyPath(Person.bestFriend.name))
// "Yuanyuan"
#keyPath(Person.friends.name)
// "friends.name"
gabrielle.value(forKeyPath: #keyPath(Person.friends.name))
// ["Yuanyuan", "Jim"]
```

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
