---
name: Apple Intelligence: App Intents
description: Specialized skill for Apple Intelligence: App Intents based on official Apple Developer Documentation.
---

# App Intents

Make your app’s content and actions discoverable with system experiences like Spotlight, widgets, and the Shortcuts app.

## Overview

The App Intents framework provides functionality to deeply integrate your app’s actions and content with system experiences across platforms, including Siri, Spotlight, widgets, controls and more. With Apple Intelligence and enhancements to App Intents, Siri will suggest your app’s actions to help people discover your app’s features and gains the ability to take actions in and across apps.

![A hero image of an App Intents framework icon.](images/com.apple.AppIntents/app-intents-hero@2x.png)

By adopting the App Intents framework, you allow people to personalize their devices by instantly using your app’s functionality with:

- Interactions with Siri, including those that use the personal context awareness and action capabilities of Apple Intelligence.
- Spotlight suggestions and search.
- Actions and automations in the Shortcuts app.
- Hardware interactions that initiate app actions, like the Action button and squeeze gestures on Apple Pencil.
- Focus to allow people to reduce distractions.

> Note: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, App Intents enables you to express your app’s actions, by offering an App Shortcut. People can then ask Siri to take those actions on their behalf, whether they’re in your app or elsewhere in the system. Use App Entities to expose content in your app to Spotlight and semantic indexing with Apple Intelligence. People can then ask Siri to retrieve information from your app, like asking Siri to pull up flight information from a travel app to share with a loved one.

You reuse these components with other technologies to offer additional features and experiences that make your app and its functionality even more discoverable and widely available. For example, you reuse modular App Intents code together with <doc://com.apple.documentation/documentation/WidgetKit> to offer:

- Interactive widgets
- Controls
- Live Activities

To learn more about features that the App Intents framework enables and how you can best adopt the framework, see [Making actions and content discoverable and widely available](/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available).

For design guidance, see [Human Interface Guidelines > App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts), [Human Interface Guidelines > Siri](https://developer.apple.com/design/human-interface-guidelines/siri), and [Human Interface Guidelines > Action Button](https://developer.apple.com/design/human-interface-guidelines/action-button).

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/Updates/AppIntents>

[Making actions and content discoverable and widely available](/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available)

Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.

[Creating your first app intent](/documentation/AppIntents/Creating-your-first-app-intent)

Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.

[Adopting App Intents to support system experiences](/documentation/AppIntents/adopting-app-intents-to-support-system-experiences)

Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.

[Accelerating app interactions with App Intents](/documentation/AppIntents/AcceleratingAppInteractionsWithAppIntents)

Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.

### Siri and Apple Intelligence

[Integrating actions with Siri and Apple Intelligence](/documentation/AppIntents/Integrating-actions-with-siri-and-apple-intelligence)

Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.

[Making onscreen content available to Siri and Apple Intelligence](/documentation/AppIntents/Making-onscreen-content-available-to-siri-and-apple-intelligence)

Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content.

[App intent domains](/documentation/AppIntents/app-intent-domains)

Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.

[Making your app’s functionality available to Siri](/documentation/AppIntents/making-your-app-s-functionality-available-to-siri)

Add app intent schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.

### Visual intelligence

  <doc://com.apple.documentation/documentation/VisualIntelligence/integrating-your-app-with-visual-intelligence>

  <doc://com.apple.documentation/documentation/VisualIntelligence>

[`IntentValueQuery`](/documentation/AppIntents/IntentValueQuery)

A query that provides entity values to the system; for example, for visual intelligence search.

### Interactive Snippets

[Displaying static and interactive snippets](/documentation/AppIntents/displaying-static-and-interactive-snippets)

Enable people to view the outcome of an app intent and immediately perform follow-up actions.

[`SnippetIntent`](/documentation/AppIntents/SnippetIntent)

An app intent that presents an interactive snippet onscreen.

### Other system experiences

[Making app entities available in Spotlight](/documentation/AppIntents/making-app-entities-available-in-spotlight)

Allow people to find your app’s content in Spotlight by donating app entities to its semantic index.

[Focus](/documentation/AppIntents/focus)

Adjust your app’s behavior and filter incoming notifications when the
current Focus changes.

[Action button on iPhone and Apple Watch](/documentation/AppIntents/ActionButton)

Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.

[Launching your voice-based conversational app from the side button of iPhone](/documentation/AppIntents/Launching-your-voice-based-conversational-app-from-the-side-button-of-iPhone)

Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.

  <doc://com.apple.documentation/documentation/WidgetKit/Developing-a-WidgetKit-strategy>

### SiriKit migration

  <doc://com.apple.documentation/documentation/SiriKit/soup-chef-with-app-intents-migrating-custom-intents>

### Actions

[App intents](/documentation/AppIntents/app-intents)

Define the custom actions your app exposes to the system, and incorporate
support for existing SiriKit intents.

[Intent discovery](/documentation/AppIntents/intent-discovery)

Donate your app’s intents to the system to help it identify trends and predict
future behaviors.

[App Shortcuts](/documentation/AppIntents/app-shortcuts)

Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.

### Parameters, custom data types, and queries

[Adding parameters to an app intent](/documentation/AppIntents/Adding-parameters-to-an-app-intent)

Enable people to configure app intents with their custom input values.

[Integrating custom data types into your intents](/documentation/AppIntents/Integrating-custom-types-into-your-intents)

Provide the system with information about the types your app uses to model its
data so that your intents can use those types as parameters.

[Parameter resolution](/documentation/AppIntents/parameter-resolution)

Define the required parameters for your app intents and specify how to resolve
those parameters at runtime.

[App entities](/documentation/AppIntents/app-entities)

Make core types or concepts discoverable to the system by declaring
them as app entities.

[Entity queries](/documentation/AppIntents/entity-queries)

Help the system find the entities your app defines and use
them to resolve parameters.

[Resolvers](/documentation/AppIntents/resolvers)

Resolve the parameters of your app intents, and extend the standard resolution
types to include your app’s custom types.

### Utility types

[Common types](/documentation/AppIntents/common-data-types)

Specify common types that your app supports, including currencies,
files, and contacts.

### Errors

[`AppIntentError`](/documentation/AppIntents/AppIntentError)

Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
