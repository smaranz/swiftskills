---
name: IOS App and environment
description: Rork-Max Quality skill for IOS App and environment. Platform-native patterns and best practices for ios development.
---

# IOS App and environment

Manage life-cycle events and your app’s UI scenes, and get information about traits and the environment in which your app runs.

## 🚀 Rork-Max Quality Snippet

```swift
import UIKit

class SceneDelegate: UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = UINavigationController(
            rootViewController: HomeViewController()
        )
        window?.makeKeyAndVisible()
    }

    func sceneDidBecomeActive(_ scene: UIScene) { refreshContent() }
    func sceneWillResignActive(_ scene: UIScene) { saveState() }
}
```

## 💎 Elite Implementation Tips

- Adopt the UIKit scene lifecycle (`UIWindowSceneDelegate`) for multi-window support
- Use `UITraitCollection` to respond to appearance, size class, and accessibility changes
- Check `ProcessInfo.processInfo.isiOSAppOnMac` for Designed for iPad on Mac adjustments

## When to Use

- Building native iOS/iPadOS features using UIKit APIs
- Implementing UIKit-specific interactions not available in SwiftUI
- Working with view controllers, navigation controllers, and UIKit lifecycle

## Best Practices

- Use SwiftUI for new views and bridge UIKit only when necessary
- Adopt modern UIKit APIs: `UICollectionViewCompositionalLayout`, diffable data sources
- Handle all size classes and trait changes for iPhone and iPad adaptivity

## Common Pitfalls

- Mixing UIKit autolayout and SwiftUI layout can cause constraint conflicts
- Forgetting to test on iPad — multitasking changes your window size
- Not adopting the UIKit scene lifecycle for multi-window support

## Key APIs

### Life cycle

| API | Purpose |
|-----|---------|
| `Managing your app’s life cycle` | Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events. |
| `Responding to the launch of your app` | Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system. |
| `UIApplication` | The centralized point of control and coordination for apps running in iOS. |
| `UIApplicationDelegate` | A set of methods to manage shared behaviors for your app. |
| `Scenes` | Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI. |

### Device environment

| API | Purpose |
|-----|---------|
| `UIDevice` | A representation of the current device. |
| `UIStatusBarManager` | An object that describes the configuration of the status bar. |

### Data observation

| API | Purpose |
|-----|---------|
| `Updating views automatically with observation tracking` | Use Swift Observation and UIKit’s automatic tracking to update your views in response to model data updates. |
| `Automatic observation tracking` | Simplify updating views when data changes by making updates in methods that support automatic observation tracking. |

### Adaptivity and traits

| API | Purpose |
|-----|---------|
| `Traits and the trait environment` | Get information about traits and the environment in which your app runs, and share data with your view hierarchy. |
| `Responding to changing display modes on Apple TV` | Change images and resources dynamically when the screen gamut on your device changes. |

### iPad, Mac, and Apple Vision Pro

| API | Purpose |
|-----|---------|
| `Building a desktop-class iPad app` | Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more. |
| `Elevating your iPad app with a tab bar and sidebar` | Provide a compact, ergonomic tab bar for quick access to key parts of your app, and a sidebar for in-depth navigation. |
| `Supporting desktop-class features in your iPad app` | Enhance your iPad app by adding desktop-class features and document support. |
| `Multitasking on iPad, Mac, and Apple Vision Pro` | Implement multitasking APIs to seamlessly integrate your app with iPadOS, macOS, and visionOS. |

### Guided Access

| API | Purpose |
|-----|---------|
| `UIGuidedAccessRestrictionDelegate` | A set of methods you use to add custom restrictions for the Guided Access feature in iOS. |
| `guidedAccessRestrictionState(forIdentifier:)` | Returns the restriction state for the specified guided access restriction. |

### Architecture

| API | Purpose |
|-----|---------|
| `Updating your app from 32-bit to 64-bit architecture` | Ensure that your app behaves as expected by adapting it to support later versions of the operating system. |
| `UIApplicationMain(_:_:_:_:)` | Creates the application object and the application delegate and sets up the event cycle. |
