---
name: Search
description: Apple SwiftUI Documentation for Search.
---

# Search

Enable people to search for text or other content within your app.

## Overview

To present a search field in your app, create and manage storage for search
text and optionally for discrete search terms known as *tokens*. Then bind the
storage to the search field by applying the searchable view modifier
to a view in your app.

![](images/com.apple.SwiftUI/search-hero@2x.png)

As people interact with the field, they implicitly modify the underlying
storage and, thereby, the search parameters. Your app correspondingly updates
other parts of its interface. To enhance the search interaction,
you can also:

- Offer suggestions during search, for both text and tokens.
- Implement search scopes that help people to narrow the search space.
- Detect when people activate the search field, and programmatically dismiss
  the search field using environment values.

For design guidance, see
<doc://com.apple.documentation/design/Human-Interface-Guidelines/searching>
in the Human Interface Guidelines.

## Topics

### Searching your app’s data model

[Adding a search interface to your app](/documentation/SwiftUI/Adding-a-search-interface-to-your-app)

Present an interface that people can use to search for content in your app.

[Performing a search operation](/documentation/SwiftUI/Performing-a-search-operation)

Update search results based on search text and optional tokens that you store.

[`searchable(text:placement:prompt:)`](/documentation/SwiftUI/View/searchable(text:placement:prompt:))

Marks this view as searchable, which configures the display of a
search field.

[`searchable(text:tokens:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:tokens:placement:prompt:token:))

Marks this view as searchable with text and tokens.

[`searchable(text:editableTokens:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:editableTokens:placement:prompt:token:))

Marks this view as searchable, which configures the display of a
search field.

[`SearchFieldPlacement`](/documentation/SwiftUI/SearchFieldPlacement)

The placement of a search field in a view hierarchy.

### Making search suggestions

[Suggesting search terms](/documentation/SwiftUI/Suggesting-search-terms)

Provide suggestions to people searching for content in your app.

[`searchSuggestions(_:)`](/documentation/SwiftUI/View/searchSuggestions(_:))

Configures the search suggestions for this view.

[`searchSuggestions(_:for:)`](/documentation/SwiftUI/View/searchSuggestions(_:for:))

Configures how to display search suggestions within this view.

[`searchCompletion(_:)`](/documentation/SwiftUI/View/searchCompletion(_:))

Associates a fully formed string with the value of this view when used
as a search suggestion.

[`searchable(text:tokens:suggestedTokens:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:tokens:suggestedTokens:placement:prompt:token:))

Marks this view as searchable with text, tokens, and suggestions.

[`SearchSuggestionsPlacement`](/documentation/SwiftUI/SearchSuggestionsPlacement)

The ways that SwiftUI displays search suggestions.

### Limiting search scope

[Scoping a search operation](/documentation/SwiftUI/Scoping-a-search-operation)

Divide the search space into a few broad categories.

[`searchScopes(_:scopes:)`](/documentation/SwiftUI/View/searchScopes(_:scopes:))

Configures the search scopes for this view.

[`searchScopes(_:activation:_:)`](/documentation/SwiftUI/View/searchScopes(_:activation:_:))

Configures the search scopes for this view with the specified
activation strategy.

[`SearchScopeActivation`](/documentation/SwiftUI/SearchScopeActivation)

The ways that searchable modifiers can show or hide search scopes.

### Detecting, activating, and dismissing search

[Managing search interface activation](/documentation/SwiftUI/Managing-search-interface-activation)

Programmatically detect and dismiss a search field.

[`isSearching`](/documentation/SwiftUI/EnvironmentValues/isSearching)

A Boolean value that indicates when the user is searching.

[`dismissSearch`](/documentation/SwiftUI/EnvironmentValues/dismissSearch)

An action that ends the current search interaction.

[`DismissSearchAction`](/documentation/SwiftUI/DismissSearchAction)

An action that can end a search interaction.

[`searchable(text:isPresented:placement:prompt:)`](/documentation/SwiftUI/View/searchable(text:isPresented:placement:prompt:))

Marks this view as searchable with programmatic presentation of the
search field.

[`searchable(text:tokens:isPresented:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:tokens:isPresented:placement:prompt:token:))

Marks this view as searchable with text and tokens, as well as
programmatic presentation.

[`searchable(text:editableTokens:isPresented:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:editableTokens:isPresented:placement:prompt:token:))

Marks this view as searchable, which configures the display of a
search field.

[`searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)`](/documentation/SwiftUI/View/searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:))

Marks this view as searchable with text, tokens, and suggestions, as
well as programmatic presentation.

### Displaying toolbar content during search

[`searchPresentationToolbarBehavior(_:)`](/documentation/SwiftUI/View/searchPresentationToolbarBehavior(_:))

Configures the search toolbar presentation behavior for any
searchable modifiers within this view.

[`SearchPresentationToolbarBehavior`](/documentation/SwiftUI/SearchPresentationToolbarBehavior)

A type that defines how the toolbar behaves when presenting search.

### Searching for text in a view

[`findNavigator(isPresented:)`](/documentation/SwiftUI/View/findNavigator(isPresented:))

Programmatically presents the find and replace interface for text
editor views.

[`findDisabled(_:)`](/documentation/SwiftUI/View/findDisabled(_:))

Prevents find and replace operations in a text editor.

[`replaceDisabled(_:)`](/documentation/SwiftUI/View/replaceDisabled(_:))

Prevents replace operations in a text editor.

[`FindContext`](/documentation/SwiftUI/FindContext)

The status of the find navigator for views which support text editing.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
