---
name: Model data
description: Rork-Max Quality skill for Model data. Actionable patterns and best practices for SwiftUI development.
---

# Model data

Manage the data that your app uses to drive its interface.
SwiftUI offers a declarative approach to user interface design. As you compose a
hierarchy of views, you also indicate data dependencies for the views.
When the data changes, either due to an external event or because of an action
that the user performs, SwiftUI automatically updates the affected parts of the
interface. As a result, the framework automatically performs most of the work
that view controllers traditionally do.
The framework provides tools, like state variables and bindings, for connecting
your app’s data to the user interface. These tools help you maintain a single
source of truth for every piece of data in your app, in part by reducing the
amount of glue logic you write. Select the tool that best suits the task you
need to perform:
- Manage transient UI state locally within a view by wrapping value types as
`State` properties.
- Share a reference to a source of truth, like local state, using the
`Binding` property wrapper.
- Connect to and observe reference model data in views by applying the
macro to the model data type. Instantiate an observable model data type
directly in a view using a `State` property. Share the observable model data
with other views in the hierarchy without passing a reference using the
`Environment` property wrapper.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI

@Observable
class ShoppingCart {
    var items: [CartItem] = []

    var total: Decimal {
        items.reduce(0) { $0 + $1.price * Decimal($1.quantity) }
    }

    func add(_ product: Product) {
        if let index = items.firstIndex(where: { $0.product.id == product.id }) {
            items[index].quantity += 1
        } else {
            items.append(CartItem(product: product, quantity: 1))
        }
    }
}

struct CartView: View {
    @Environment(ShoppingCart.self) private var cart

    var body: some View {
        List(cart.items) { item in
            HStack {
                Text(item.product.name)
                Spacer()
                Text("×\(item.quantity)")
            }
        }
        .safeAreaInset(edge: .bottom) {
            Text("Total: \(cart.total, format: .currency(code: "USD"))")
                .font(.headline)
                .padding()
        }
    }
}
```

## 💎 Elite Implementation Tips

- Use `@Observable` (Swift 6) instead of `ObservableObject` for automatic fine-grained updates
- Inject models via `.environment()` and read with `@Environment(Model.self)`
- Computed properties on `@Observable` classes automatically trigger view updates


## When to Use

- Sharing state between views without explicit prop drilling
- Persisting user preferences or small data sets across launches
- Injecting dependencies (services, repositories) into the view hierarchy
- Propagating theme, locale, or feature-flag values through the environment

## Best Practices

- Use `@Observable` (Swift 6) instead of `ObservableObject` for finer-grained updates
- Prefer `@Environment` for dependency injection over singletons
- Use `@AppStorage` for simple UserDefaults-backed preferences
- Model domain data as value types (structs) and wrap in `@Observable` classes for mutation tracking

## Common Pitfalls

- Storing large data in `@AppStorage` — it's backed by UserDefaults, not a database
- Creating `@Observable` objects inside `body` — they get recreated every render
- Using `@EnvironmentObject` when `@Environment` with `@Observable` is cleaner in iOS 17+

## Key APIs

### Creating and sharing view state

| API | Purpose |
|-----|---------|
| `Managing user interface state` | Encapsulate view-specific data within your app’s view hierarchy to make your |
| `State` | A property wrapper type that can read and write a value managed by SwiftUI. |
| `Bindable` | A property wrapper type that supports creating bindings to the mutable |
| `Binding` | A property wrapper type that can read and write a value owned by a source of |

### Creating model data

| API | Purpose |
|-----|---------|
| `Managing model data in your app` | Create connections between your app’s data model and views. |
| `Migrating from the Observable Object protocol to the Observable macro` | Update your existing app to leverage the benefits of Observation in Swift. |
| `Monitoring data changes in your app` | Show changes to data in your app’s user interface by using observable |
| `StateObject` | A property wrapper type that instantiates an observable object. |
| `ObservedObject` | A property wrapper type that subscribes to an observable object and |

### Responding to data changes

| API | Purpose |
|-----|---------|
| `onChange(of:initial:_:)` | Adds a modifier for this view that fires an action when a specific |
| `onReceive(_:perform:)` | Adds an action to perform when this view detects data emitted by the |

### Distributing model data throughout your app

| API | Purpose |
|-----|---------|
| `environmentObject(_:)` | Supplies an observable object to a view’s hierarchy. |
| `environmentObject(_:)` | Supplies an `ObservableObject` to a view subhierarchy. |
| `EnvironmentObject` | A property wrapper type for an observable object that a parent or ancestor |

### Managing dynamic data

| API | Purpose |
|-----|---------|
| `DynamicProperty` | An interface for a stored variable that updates an external property of a |
