---
name: Apple Intelligence: Foundation Models
description: Rork-Max Quality skill for Apple Intelligence: Foundation Models. Patterns and best practices for Apple Intelligence integration.
---

# Apple Intelligence: Foundation Models

Perform tasks with the on-device model that specializes in language understanding, structured output, and tool calling.
The Foundation Models framework provides access to Apple’s on-device large language
model that powers Apple Intelligence to help you perform intelligent tasks specific
to your use case. The text-based on-device model identifies patterns that
allow for generating new text that’s appropriate for the request you make, and it
can make decisions to call code you write to perform specialized tasks.
Generate text content based on requests you make. The on-device model excels at
a diverse range of text generation tasks, like summarization, entity extraction,
text understanding, refinement, dialog for games, generating creative content,
and more.
Generate entire Swift data structures with guided generation. With the `@Generable` macro,
you can define custom data structures and the framework provides strong guarantees
that the model generates instances of your type.
To expand what the on-device foundation model can do, use `Tool` to create custom
tools that the model can call to assist with handling your request. For example,
the model can call a tool that searches a local or online database for information,
or calls a service in your app.
To use the on-device language model, people need to turn on Apple Intelligence on
their device. For a list of supported devices, see Apple Intelligence.
For more information about acceptable usage of the Foundation Models framework,
see Acceptable use requirements for the Foundation Models framework.

## 🚀 Rork-Max Quality Snippet

```swift
import FoundationModels
import SwiftUI

@Generable
struct MovieRecommendation {
    var title: String
    var genre: String
    var reason: String
}

struct SmartRecommendationView: View {
    @State private var recommendation: MovieRecommendation?
    @State private var isLoading = false

    var body: some View {
        VStack(spacing: 20) {
            if let rec = recommendation {
                VStack(alignment: .leading, spacing: 8) {
                    Text(rec.title).font(.title2.bold())
                    Text(rec.genre).font(.subheadline).foregroundStyle(.secondary)
                    Text(rec.reason).font(.body)
                }
                .padding()
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
            }

            Button("Get Recommendation") {
                Task { await generateRecommendation() }
            }
            .buttonStyle(.borderedProminent)
            .disabled(isLoading)
        }
    }

    func generateRecommendation() async {
        isLoading = true
        defer { isLoading = false }
        let session = LanguageModelSession()
        recommendation = try? await session.respond(
            to: "Suggest a movie for a rainy evening",
            generating: MovieRecommendation.self
        )
    }
}
```

## 💎 Elite Implementation Tips

- Ensure foundation models integration feels seamless by following the HIG for Intelligence.
- Handle fallback cases gracefully where the model or feature may be unavailable.
- Use modern async/await patterns for all AI-triggered operations.
- Always check for `@Observable` (Swift 6) compatibility for optimal performance.
- Prioritize SF Symbols with hierarchical rendering for all iconography.

## When to Use

- Generating text content (summaries, suggestions, creative writing) on-device
- Producing structured Swift data types from natural language with guided generation
- Extending model capabilities with custom tools for domain-specific tasks

## Best Practices

- Use `@Generable` macro to get type-safe structured output from the model
- Create custom `Tool` types to let the model call your app's services
- Always handle model unavailability gracefully (device may not support Apple Intelligence)
- Use `LanguageModelSession` for multi-turn conversations with context

## Common Pitfalls

- Assuming the model is always available — check `SystemLanguageModel.default.availability`
- Sending overly long prompts that exceed token limits
- Not implementing guardrails for sensitive content in user-facing features

## Key APIs

### Essentials

| API | Purpose |
|-----|---------|
| `Generating content and performing tasks with Foundation Models` | Enhance the experience in your app by prompting an on-device large language model. |
| `Adding intelligent app features with generative models` | Build robust apps with guided generation and tool calling by adopting the Foundation Models framework. |
| `SystemLanguageModel` | An on-device large language model capable of text generation tasks. |

### Prompting

| API | Purpose |
|-----|---------|
| `Prompting an on-device foundation model` | Tailor your prompts to get effective results from an on-device model. |
| `Updating prompts for new model versions` | Manage the prompts your app uses by versioning them to make the most out of |
| `Evaluating prompts to measure performance and improve model responses` | Systematically measure and improve the quality of your prompts by using structured evaluation. |
| `Analyzing the runtime performance of your Foundation Models app` | Optimize token consumption and improve response times by profiling your app’s model usage with Instruments. |
| `LanguageModelSession` | An object that represents a session that interacts with a language model. |
| `Instructions` | Details you provide that define the model’s intended behavior on prompts. |
| `Prompt` | A prompt from a person to the model. |
| `Transcript` | A linear history of entries that reflect an interaction with a session. |

### Guided generation

| API | Purpose |
|-----|---------|
| `Generating Swift data structures with guided generation` | Create robust apps by describing output you want programmatically. |
| `Generable` | A type that the model uses when responding to prompts. |

### Tool calling

| API | Purpose |
|-----|---------|
| `Expanding generation with tool calling` | Build tools that enable the model to perform tasks that are specific to your use case. |
| `Generate dynamic game content with guided generation and tools` | Make gameplay more lively with AI generated dialog and encounters personalized to the player. |
| `Tool` | A tool that a model can call to gather information at runtime or perform side effects. |

### Safety

| API | Purpose |
|-----|---------|
| `Improving the safety of generative model output` | Create generative experiences that appropriately handle sensitive inputs and respect people. |
| `SystemLanguageModel.Guardrails` | Guardrails flag sensitive content from model input and output. |

### Language and locales

| API | Purpose |
|-----|---------|
| `Supporting languages and locales with Foundation Models` | Generate content in the language people prefer when they interact with your app. |
| `supportsLocale(_:)` | Returns a Boolean indicating whether the given locale is supported by the model. |
| `LanguageModelSession.GenerationError.unsupportedLanguageOrLocale(_:)` | An error that indicates an error that occurs if the model is prompted to respond in a language |

### Use cases

| API | Purpose |
|-----|---------|
| `Categorizing and organizing data with content tags` | Identify topics, actions, objects, and emotions in input text with a content tagging model. |
| `SystemLanguageModel.UseCase` | A type that represents the use case for prompting. |

### Feedback

| API | Purpose |
|-----|---------|
| `LanguageModelFeedback` | Feedback appropriate for logging or attaching to Feedback Assistant. |
| `logFeedbackAttachment(sentiment:issues:desiredOutput:)` | Logs and serializes data that includes session information that you attach when |
