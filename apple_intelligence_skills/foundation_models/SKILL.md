---
name: Apple Intelligence: Foundation Models
description: Specialized skill for Apple Intelligence: Foundation Models based on official Apple Developer Documentation.
---

# Foundation Models

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.

## Overview

The Foundation Models framework provides access to Apple’s on-device large language
model that powers Apple Intelligence to help you perform intelligent tasks specific
to your use case. The text-based on-device model identifies patterns that
allow for generating new text that’s appropriate for the request you make, and it
can make decisions to call code you write to perform specialized tasks.

![An illustration that represents a foundation model.](images/com.apple.foundationmodels/foundation-models-framework-hero@2x.png)

Generate text content based on requests you make. The on-device model excels at
a diverse range of text generation tasks, like summarization, entity extraction,
text understanding, refinement, dialog for games, generating creative content,
and more.

Generate entire Swift data structures with guided generation. With the `@Generable` macro,
you can define custom data structures and the framework provides strong guarantees
that the model generates instances of your type.

To expand what the on-device foundation model can do, use [`Tool`](/documentation/FoundationModels/Tool) to create custom
tools that the model can call to assist with handling your request. For example,
the model can call a tool that searches a local or online database for information,
or calls a service in your app.

To use the on-device language model, people need to turn on Apple Intelligence on
their device. For a list of supported devices, see [Apple Intelligence](https://www.apple.com/apple-intelligence/).

For more information about acceptable usage of the Foundation Models framework,
see [Acceptable use requirements for the Foundation Models framework](https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework).

### Related videos

  <doc://com.apple.documentation/videos/play/wwdc2025/286>

  <doc://com.apple.documentation/videos/play/wwdc2025/301>

  <doc://com.apple.documentation/videos/play/wwdc2025/259>

## Topics

### Essentials

  <doc://com.apple.documentation/documentation/Updates/FoundationModels>

[Generating content and performing tasks with Foundation Models](/documentation/FoundationModels/generating-content-and-performing-tasks-with-foundation-models)

Enhance the experience in your app by prompting an on-device large language model.

[Adding intelligent app features with generative models](/documentation/FoundationModels/adding-intelligent-app-features-with-generative-models)

Build robust apps with guided generation and tool calling by adopting the Foundation Models framework.

[`SystemLanguageModel`](/documentation/FoundationModels/SystemLanguageModel)

An on-device large language model capable of text generation tasks.

### Prompting

[Prompting an on-device foundation model](/documentation/FoundationModels/prompting-an-on-device-foundation-model)

Tailor your prompts to get effective results from an on-device model.

[Updating prompts for new model versions](/documentation/FoundationModels/updating-prompts-for-new-model-versions)

Manage the prompts your app uses by versioning them to make the most out of
model improvements.

[Evaluating prompts to measure performance and improve model responses](/documentation/FoundationModels/evaluating-prompts-to-measure-performance-and-improve-model-responses)

Systematically measure and improve the quality of your prompts by using structured evaluation.

[Analyzing the runtime performance of your Foundation Models app](/documentation/FoundationModels/analyzing-the-runtime-performance-of-your-foundation-models-app)

Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.

[`LanguageModelSession`](/documentation/FoundationModels/LanguageModelSession)

An object that represents a session that interacts with a language model.

[`Instructions`](/documentation/FoundationModels/Instructions)

Details you provide that define the model’s intended behavior on prompts.

[`Prompt`](/documentation/FoundationModels/Prompt)

A prompt from a person to the model.

[`Transcript`](/documentation/FoundationModels/Transcript)

A linear history of entries that reflect an interaction with a session.

[`GenerationOptions`](/documentation/FoundationModels/GenerationOptions)

Options that control how the model generates its response to a prompt.

### Guided generation

[Generating Swift data structures with guided generation](/documentation/FoundationModels/generating-swift-data-structures-with-guided-generation)

Create robust apps by describing output you want programmatically.

[`Generable`](/documentation/FoundationModels/Generable)

A type that the model uses when responding to prompts.

### Tool calling

[Expanding generation with tool calling](/documentation/FoundationModels/expanding-generation-with-tool-calling)

Build tools that enable the model to perform tasks that are specific to your use case.

[Generate dynamic game content with guided generation and tools](/documentation/FoundationModels/generate-dynamic-game-content-with-guided-generation-and-tools)

Make gameplay more lively with AI generated dialog and encounters personalized to the player.

[`Tool`](/documentation/FoundationModels/Tool)

A tool that a model can call to gather information at runtime or perform side effects.

### Safety

[Improving the safety of generative model output](/documentation/FoundationModels/improving-the-safety-of-generative-model-output)

Create generative experiences that appropriately handle sensitive inputs and respect people.

[`SystemLanguageModel.Guardrails`](/documentation/FoundationModels/SystemLanguageModel/Guardrails)

Guardrails flag sensitive content from model input and output.

### Language and locales

[Supporting languages and locales with Foundation Models](/documentation/FoundationModels/supporting-languages-and-locales-with-foundation-models)

Generate content in the language people prefer when they interact with your app.

[`supportsLocale(_:)`](/documentation/FoundationModels/SystemLanguageModel/supportsLocale(_:))

Returns a Boolean indicating whether the given locale is supported by the model.

[`LanguageModelSession.GenerationError.unsupportedLanguageOrLocale(_:)`](/documentation/FoundationModels/LanguageModelSession/GenerationError/unsupportedLanguageOrLocale(_:))

An error that indicates an error that occurs if the model is prompted to respond in a language
that it does not support.

### Use cases

[Categorizing and organizing data with content tags](/documentation/FoundationModels/categorizing-and-organizing-data-with-content-tags)

Identify topics, actions, objects, and emotions in input text with a content tagging model.

[`SystemLanguageModel.UseCase`](/documentation/FoundationModels/SystemLanguageModel/UseCase)

A type that represents the use case for prompting.

### Feedback

[`LanguageModelFeedback`](/documentation/FoundationModels/LanguageModelFeedback)

Feedback appropriate for logging or attaching to Feedback Assistant.

[`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](/documentation/FoundationModels/LanguageModelSession/logFeedbackAttachment(sentiment:issues:desiredOutput:))

Logs and serializes data that includes session information that you attach when
reporting feedback to Apple.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
