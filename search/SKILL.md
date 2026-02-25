---
name: Search
description: Rork-Max Quality skill for Search. Actionable patterns and best practices for SwiftUI development.
---

# Search

Enable people to search for text or other content within your app.
To present a search field in your app, create and manage storage for search
text and optionally for discrete search terms known as *tokens*. Then bind the
storage to the search field by applying the searchable view modifier
to a view in your app.
As people interact with the field, they implicitly modify the underlying
storage and, thereby, the search parameters. Your app correspondingly updates
other parts of its interface. To enhance the search interaction,
you can also:
- Offer suggestions during search, for both text and tokens.
- Implement search scopes that help people to narrow the search space.
- Detect when people activate the search field, and programmatically dismiss
the search field using environment values.
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

struct SearchExample: View {
    @State private var query = ""
    @State private var tokens: [SearchToken] = []

    var body: some View {
        NavigationStack {
            List(filteredItems) { item in
                Text(item.name)
            }
            .searchable(text: $query, tokens: $tokens, prompt: "Search items") { token in
                Label(token.name, systemImage: token.icon)
            }
            .searchSuggestions {
                ForEach(suggestions) { suggestion in
                    Text(suggestion.name).searchCompletion(suggestion.name)
                }
            }
            .navigationTitle("Library")
        }
    }
}
```

## 💎 Elite Implementation Tips

- Place `.searchable()` on the `NavigationStack` content for automatic search bar placement
- Use `.searchSuggestions` for autocomplete and `.searchScopes` for category filtering
- Support search tokens for structured filtering (e.g., tags, categories)


## When to Use

- Building hierarchical drill-down flows (settings, detail views)
- Implementing tab-based or sidebar navigation patterns
- Presenting modal sheets, popovers, alerts, or confirmation dialogs
- Creating deep-linkable navigation paths with `NavigationPath`

## Best Practices

- Use `NavigationStack` with a `path` binding for programmatic, deep-linkable navigation
- Prefer `NavigationSplitView` on iPad/Mac for sidebar + detail layouts
- Model navigation state explicitly so it can be saved, restored, and deep-linked
- Use `.sheet()`, `.fullScreenCover()`, and `.popover()` for modal presentations

## Common Pitfalls

- Using the deprecated `NavigationView` instead of `NavigationStack`/`NavigationSplitView`
- Nesting `NavigationStack` inside another `NavigationStack` causing double navigation bars
- Forgetting to make navigation destination types `Hashable` for `navigationDestination(for:)`

## Key APIs

### Searching your app’s data model

| API | Purpose |
|-----|---------|
| `Adding a search interface to your app` | Present an interface that people can use to search for content in your app. |
| `Performing a search operation` | Update search results based on search text and optional tokens that you store. |
| `searchable(text:placement:prompt:)` | Marks this view as searchable, which configures the display of a |
| `searchable(text:tokens:placement:prompt:token:)` | Marks this view as searchable with text and tokens. |
| `searchable(text:editableTokens:placement:prompt:token:)` | Marks this view as searchable, which configures the display of a |
| `SearchFieldPlacement` | The placement of a search field in a view hierarchy. |

### Making search suggestions

| API | Purpose |
|-----|---------|
| `Suggesting search terms` | Provide suggestions to people searching for content in your app. |
| `searchSuggestions(_:)` | Configures the search suggestions for this view. |
| `searchSuggestions(_:for:)` | Configures how to display search suggestions within this view. |
| `searchCompletion(_:)` | Associates a fully formed string with the value of this view when used |
| `searchable(text:tokens:suggestedTokens:placement:prompt:token:)` | Marks this view as searchable with text, tokens, and suggestions. |
| `SearchSuggestionsPlacement` | The ways that SwiftUI displays search suggestions. |

### Limiting search scope

| API | Purpose |
|-----|---------|
| `Scoping a search operation` | Divide the search space into a few broad categories. |
| `searchScopes(_:scopes:)` | Configures the search scopes for this view. |
| `searchScopes(_:activation:_:)` | Configures the search scopes for this view with the specified |
| `SearchScopeActivation` | The ways that searchable modifiers can show or hide search scopes. |

### Detecting, activating, and dismissing search

| API | Purpose |
|-----|---------|
| `Managing search interface activation` | Programmatically detect and dismiss a search field. |
| `isSearching` | A Boolean value that indicates when the user is searching. |
| `dismissSearch` | An action that ends the current search interaction. |
| `DismissSearchAction` | An action that can end a search interaction. |
| `searchable(text:isPresented:placement:prompt:)` | Marks this view as searchable with programmatic presentation of the |
| `searchable(text:tokens:isPresented:placement:prompt:token:)` | Marks this view as searchable with text and tokens, as well as |
| `searchable(text:editableTokens:isPresented:placement:prompt:token:)` | Marks this view as searchable, which configures the display of a |
| `searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)` | Marks this view as searchable with text, tokens, and suggestions, as |

### Displaying toolbar content during search

| API | Purpose |
|-----|---------|
| `searchPresentationToolbarBehavior(_:)` | Configures the search toolbar presentation behavior for any |
| `SearchPresentationToolbarBehavior` | A type that defines how the toolbar behaves when presenting search. |

### Searching for text in a view

| API | Purpose |
|-----|---------|
| `findNavigator(isPresented:)` | Programmatically presents the find and replace interface for text |
| `findDisabled(_:)` | Prevents find and replace operations in a text editor. |
| `replaceDisabled(_:)` | Prevents replace operations in a text editor. |
| `FindContext` | The status of the find navigator for views which support text editing. |
