---
name: Apple Intelligence: App Intents
description: Rork-Max Quality skill for Apple Intelligence: App Intents. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: App Intents

Make your app’s content and actions discoverable with system experiences like Spotlight, widgets, and the Shortcuts app.
The App Intents framework provides functionality to deeply integrate your app’s actions and content with system experiences across platforms, including Siri, Spotlight, widgets, controls and more. With Apple Intelligence and enhancements to App Intents, Siri will suggest your app’s actions to help people discover your app’s features and gains the ability to take actions in and across apps.
By adopting the App Intents framework, you allow people to personalize their devices by instantly using your app’s functionality with:
- Interactions with Siri, including those that use the personal context awareness and action capabilities of Apple Intelligence.
- Spotlight suggestions and search.
- Actions and automations in the Shortcuts app.
- Hardware interactions that initiate app actions, like the Action button and squeeze gestures on Apple Pencil.
- Focus to allow people to reduce distractions.
> Note: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.
For example, App Intents enables you to express your app’s actions, by offering an App Shortcut. People can then ask Siri to take those actions on their behalf, whether they’re in your app or elsewhere in the system. Use App Entities to expose content in your app to Spotlight and semantic indexing with Apple Intelligence. People can then ask Siri to retrieve information from your app, like asking Siri to pull up flight information from a travel app to share with a loved one.
You reuse these components with other technologies to offer additional features and experiences that make your app and its functionality even more discoverable and widely available. For example, you reuse modular App Intents code together with WidgetKit to offer:
- Interactive widgets
- Controls
- Live Activities
To learn more about features that the App Intents framework enables and how you can best adopt the framework, see Making actions and content discoverable and widely available.
For design guidance, see Human Interface Guidelines > App Shortcuts, Human Interface Guidelines > Siri, and Human Interface Guidelines > Action Button.

## 🚀 Rork-Max Quality Snippet

```swift
import AppIntents

struct OpenFavoriteIntent: AppIntent {
    static var title: LocalizedStringResource = "Open Favorite"
    static var description = IntentDescription("Opens your favorite item in the app.")

    @Parameter(title: "Item Name")
    var itemName: String

    func perform() async throws -> some IntentResult & ProvidesDialog {
        .result(dialog: "Opening \(itemName)!")
    }
}

struct AppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: OpenFavoriteIntent(),
            phrases: ["Open my favorite in \(.applicationName)"],
            shortTitle: "Open Favorite",
            systemImageName: "star.fill"
        )
    }
}
```

## 💎 Elite Implementation Tips

- Define an `AppIntent` for every major user-facing action — Siri and Shortcuts discover them automatically
- Use `@Parameter(title:)` with clear, short labels — Siri reads these aloud during voice interactions
- Provide `AppShortcutsProvider` with natural phrases so users can invoke intents by voice immediately
- Conform entities to `AppEntity` for deep Spotlight indexing and Siri entity resolution
- Test with Siri end-to-end — intents that work in Shortcuts may fail with voice due to parameter ambiguity
- Available on iOS 16+, macOS 13+, watchOS 9+, and visionOS 1+; Apple Intelligence enhancements require iOS 26+

## When to Use

- Exposing app actions to Siri, Shortcuts, and Spotlight
- Making app features available to the system for proactive suggestions
- Building conversational interactions with App Intent parameters

## Best Practices

- Define `AppIntent` for every user-facing action in your app
- Use `@Parameter` with clear titles and descriptions for Siri dialogue
- Provide `AppShortcutsProvider` for discoverable shortcut suggestions

## Common Pitfalls

- Intents with too many required parameters create frustrating voice interactions
- Not testing with Siri — the intent may work in Shortcuts but fail in voice

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Making actions and content discoverable and widely available` | Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button. |
| `Creating your first app intent` | Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app. |
| `Adopting App Intents to support system experiences` | Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts. |
| `Accelerating app interactions with App Intents` | Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts. |

### Siri and Apple Intelligence

| API | Purpose |
|-----|---------|
| `Integrating actions with Siri and Apple Intelligence` | Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence. |
| `Making onscreen content available to Siri and Apple Intelligence` | Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content. |
| `App intent domains` | Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas. |
| `Making your app’s functionality available to Siri` | Add app intent schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences. |

### Visual intelligence

| API | Purpose |
|-----|---------|
| `IntentValueQuery` | A query that provides entity values to the system; for example, for visual intelligence search. |

### Interactive Snippets

| API | Purpose |
|-----|---------|
| `Displaying static and interactive snippets` | Enable people to view the outcome of an app intent and immediately perform follow-up actions. |
| `SnippetIntent` | An app intent that presents an interactive snippet onscreen. |

### Other system experiences

| API | Purpose |
|-----|---------|
| `Making app entities available in Spotlight` | Allow people to find your app’s content in Spotlight by donating app entities to its semantic index. |
| `Focus` | Adjust your app’s behavior and filter incoming notifications when the |
| `Action button on iPhone and Apple Watch` | Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch. |
| `Launching your voice-based conversational app from the side button of iPhone` | Let people in Japan configure the side button of iPhone to launch your voice-based conversational app. |

### Actions

| API | Purpose |
|-----|---------|
| `App intents` | Define the custom actions your app exposes to the system, and incorporate |
| `Intent discovery` | Donate your app’s intents to the system to help it identify trends and predict |
| `App Shortcuts` | Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models. |

### Parameters, custom data types, and queries

| API | Purpose |
|-----|---------|
| `Adding parameters to an app intent` | Enable people to configure app intents with their custom input values. |
| `Integrating custom data types into your intents` | Provide the system with information about the types your app uses to model its |
| `Parameter resolution` | Define the required parameters for your app intents and specify how to resolve |
| `App entities` | Make core types or concepts discoverable to the system by declaring |
| `Entity queries` | Help the system find the entities your app defines and use |
| `Resolvers` | Resolve the parameters of your app intents, and extend the standard resolution |

### Utility types

| API | Purpose |
|-----|---------|
| `Common types` | Specify common types that your app supports, including currencies, |

### Errors

| API | Purpose |
|-----|---------|
| `AppIntentError` | Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent. |
