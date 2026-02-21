---
name: Apple Intelligence: Image Playground
description: Specialized skill for Apple Intelligence: Image Playground based on official Apple Developer Documentation.
---

# Image Playground

Present a system interface to generate images based on descriptive information.

## Overview

Use the `ImagePlayground` framework to generate custom images using
system-supported styles. To generate images, you specify a text
description of what you want, an optional image, and the style you want
the image to adopt. Use that information to present a system sheet from your
SwiftUI view, or present a system view controller from your UIKit or AppKit interface.
The system interface manages all interactions with the person, and upon
success delivers an image for you to incorporate into your content.
You can also use a programmatic interface to generate images without
interactions.

## Topics

### SwiftUI presentation

  <doc://com.apple.documentation/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)>

  <doc://com.appledocumentation/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:)>

  <doc://com.apple.documentation/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)>

  <doc://com.apple.documentation/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)>

### UIKit and AppKit presentation

[`ImagePlaygroundViewController`](/documentation/ImagePlayground/ImagePlaygroundViewController)

Displays a standard system interface to generate images from
the provided input.

### Programmatic creation

[`ImageCreator`](/documentation/ImagePlayground/ImageCreator)

Generates images programmatically from the description and style information
you specify.

### Platform support

[`ImagePlaygroundConcept`](/documentation/ImagePlayground/ImagePlaygroundConcept)

Text elements that specify the content to include in the image.

[`ImagePlaygroundStyle`](/documentation/ImagePlayground/ImagePlaygroundStyle)

Style options that determine the appearance of generated images.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
