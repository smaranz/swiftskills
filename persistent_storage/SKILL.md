---
name: Persistent storage
description: Apple SwiftUI Documentation for Persistent storage.
---

# Persistent storage

Store data for use across sessions of your app.

## Overview

The operating system provides ways to store data when your app closes,
so that when people open your app again later, they can continue working without
interruption. The mechanism that you use depends on factors like what and how
much you need to store, whether you need serialized or random access to the
data, and so on.

![](images/com.apple.SwiftUI/persistent-storage-hero@2x.png)

You use the same kinds of storage in a SwiftUI app that you use
in any other app. For example, you can access files on disk using the
<doc://com.apple.documentation/documentation/Foundation/FileManager> interface.
However, SwiftUI also provides conveniences that make it easier to use certain
kinds of persistent storage in a declarative environment. For example, you can
use [`FetchRequest`](/documentation/SwiftUI/FetchRequest) and [`FetchedResults`](/documentation/SwiftUI/FetchedResults) to interact with a Core Data model.

## Topics

### Saving state across app launches

[Restoring your app’s state with SwiftUI](/documentation/SwiftUI/restoring-your-app-s-state-with-swiftui)

Provide app continuity for users by preserving their current activities.

[`defaultAppStorage(_:)`](/documentation/SwiftUI/View/defaultAppStorage(_:))

The default store used by `AppStorage` contained within the view.

[`AppStorage`](/documentation/SwiftUI/AppStorage)

A property wrapper type that reflects a value from `UserDefaults` and
invalidates a view on a change in value in that user default.

[`SceneStorage`](/documentation/SwiftUI/SceneStorage)

A property wrapper type that reads and writes to persisted, per-scene
storage.

### Accessing Core Data

[Loading and displaying a large data feed](/documentation/SwiftUI/loading-and-displaying-a-large-data-feed)

Consume data in the background, and lower memory use by batching imports and preventing duplicate records.

[`managedObjectContext`](/documentation/SwiftUI/EnvironmentValues/managedObjectContext)

[`FetchRequest`](/documentation/SwiftUI/FetchRequest)

A property wrapper type that retrieves entities from a Core Data persistent
store.

[`FetchedResults`](/documentation/SwiftUI/FetchedResults)

A collection of results retrieved from a Core Data store.

[`SectionedFetchRequest`](/documentation/SwiftUI/SectionedFetchRequest)

A property wrapper type that retrieves entities, grouped into sections,
from a Core Data persistent store.

[`SectionedFetchResults`](/documentation/SwiftUI/SectionedFetchResults)

A collection of results retrieved from a Core Data persistent store,
grouped into sections.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
