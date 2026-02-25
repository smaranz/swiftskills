---
name: Technology-specific views
description: Rork-Max Quality skill for Technology-specific views. Actionable patterns and best practices for SwiftUI development.
---

# Technology-specific views

Use SwiftUI views that other Apple frameworks provide.
To access SwiftUI views that another framework defines, import both
SwiftUI and the other framework into the file where you use the view. You
can find the framework to import by looking at the availability information
on the view’s documentation page.
For example, to use the
import both SwiftUI and MapKit.
```
import SwiftUI
import MapKit
struct MyMapView: View {
// Center the map on Joshua Tree National Park.
var region = MKCoordinateRegion(
center: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868),
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)
var body: some View {
Map(initialPosition: .region(region))
}
}
```
For design guidance, see
in the Human Interface Guidelines.


## 🚀 Rork-Max Quality Snippet

```swift
import SwiftUI
import MapKit

struct MapExample: View {
    @State private var position: MapCameraPosition = .automatic

    var body: some View {
        Map(position: $position) {
            Marker("Apple Park", coordinate: CLLocationCoordinate2D(
                latitude: 37.3346, longitude: -122.0090
            ))
            .tint(.blue)
        }
        .mapControls {
            MapCompass()
            MapScaleView()
        }
        .mapStyle(.standard(elevation: .realistic))
    }
}
```

## 💎 Elite Implementation Tips

- Use the native SwiftUI `Map` view (iOS 17+) instead of `MKMapView` wrappers
- Add `MapControls` for compass, scale, and user location buttons
- Use `Marker`, `Annotation`, and `MapPolyline` for map content


## When to Use

- Embedding UIKit views/controllers in SwiftUI with `UIViewRepresentable`
- Using SwiftUI views inside UIKit with `UIHostingController`
- Wrapping AppKit views for macOS SwiftUI apps
- Integrating MapKit, WebKit, or other framework views into SwiftUI

## Best Practices

- Use `UIViewRepresentable` / `NSViewRepresentable` for UIKit/AppKit views in SwiftUI
- Implement `Coordinator` for delegate callbacks flowing back into SwiftUI
- Keep bridge code minimal — move logic into shared `@Observable` models
- Prefer native SwiftUI equivalents when available (e.g., `Map` over `MKMapView` wrapper)

## Common Pitfalls

- Forgetting to implement `updateUIView()` — state changes won't propagate to the UIKit view
- Creating a new `UIHostingController` every time instead of updating the existing root view
- Memory leaks from strong reference cycles between Coordinator and SwiftUI state

## Key APIs

### Displaying web content

| API | Purpose |
|-----|---------|
| `webViewBackForwardNavigationGestures(_:)` | Determines whether horizontal swipe gestures trigger backward and forward page navigation. |
| `webViewContentBackground(_:)` | Specifies the visibility of the webpage’s natural background color within this view. |
| `webViewContextMenu(menu:)` | Adds an item-based context menu to a WebView, replacing the default set of context menu items. |
| `webViewElementFullscreenBehavior(_:)` | Determines whether a web view can display content full screen. |
| `webViewLinkPreviews(_:)` | Determines whether pressing a link displays a preview of the destination for the link. |
| `webViewMagnificationGestures(_:)` | Determines whether magnify gestures change the view’s magnification. |
| `webViewOnScrollGeometryChange(for:of:action:)` | Adds an action to be performed when a value, created from a scroll geometry, changes. |
| `webViewScrollInputBehavior(_:for:)` | Enables or disables scrolling in web views when using particular inputs. |

### Accessing Apple Pay and Wallet

| API | Purpose |
|-----|---------|
| `addOrderToWalletButtonStyle(_:)` | Sets the button’s style. |
| `addPassToWalletButtonStyle(_:)` | Sets the style to be used by the button. |
| `onApplePayCouponCodeChange(perform:)` | Called when a user has entered or updated a coupon code. |
| `onApplePayPaymentMethodChange(perform:)` | Called when a payment method has changed and asks for an update payment request. |
| `onApplePayShippingContactChange(perform:)` | Called when a user selected a shipping address. |
| `onApplePayShippingMethodChange(perform:)` | Called when a user selected a shipping method. |
| `payLaterViewAction(_:)` | Sets the action on the PayLaterView. See `PKPayLaterAction`. |
| `payLaterViewDisplayStyle(_:)` | Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`. |

### Authorizing and authenticating

| API | Purpose |
|-----|---------|
| `signInWithAppleButtonStyle(_:)` | Sets the style used for displaying the control |
| `authorizationController` | A value provided in the SwiftUI environment that views can use |
| `webAuthenticationSession` | A value provided in the SwiftUI environment that views can use to |

### Configuring Family Sharing

| API | Purpose |
|-----|---------|
| `familyActivityPicker(isPresented:selection:)` | Presents an activity picker view as a sheet. |
| `familyActivityPicker(headerText:footerText:isPresented:selection:)` | Presents an activity picker view as a sheet. |

### Working with managed devices

| API | Purpose |
|-----|---------|
| `managedContentStyle(_:)` | Applies a managed content style to the view. |
| `automatedDeviceEnrollmentAddition(isPresented:)` | Presents a modal view that enables users to add devices to their organization. |

### Getting location information

| API | Purpose |
|-----|---------|
| `mapStyle(_:)` | Specifies the map style to be used. |
| `mapScope(_:)` | Creates a mapScope that SwiftUI uses to connect map controls to an associated map. |
| `mapFeatureSelectionDisabled(_:)` | Specifies which map features should have selection disabled. |
| `mapFeatureSelectionAccessory(_:)` | Specifies the selection accessory to display for a `MapFeature` |
| `mapFeatureSelectionContent(content:)` | Specifies a custom presentation for the currently selected feature. |
| `mapControls(_:)` | Configures all `Map` views in the associated environment to have |
| `mapControlVisibility(_:)` | Configures all Map controls in the environment to have the specified |
| `mapCameraKeyframeAnimator(trigger:keyframes:)` | Uses the given keyframes to animate the camera of a `Map` when the |

### Displaying media

| API | Purpose |
|-----|---------|
| `continuityDevicePicker(isPresented:onDidConnect:)` | A `continuityDevicePicker` should be used to discover and connect |
| `cameraAnchor(isActive:)` | Specifies the view that should act as the virtual camera for Apple Vision Pro |

### Selecting photos

| API | Purpose |
|-----|---------|
| `photosPicker(isPresented:selection:matching:preferredItemEncoding:)` | Presents a Photos picker that selects a `PhotosPickerItem`. |
| `photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)` | Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library. |
| `photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)` | Presents a Photos picker that selects a collection of `PhotosPickerItem`. |
| `photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)` | Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library. |
| `photosPickerAccessoryVisibility(_:edges:)` | Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar. |
| `photosPickerDisabledCapabilities(_:)` | Disables capabilities of the Photos picker. |
| `photosPickerStyle(_:)` | Sets the mode of the Photos picker. |

### Previewing content

| API | Purpose |
|-----|---------|
| `quickLookPreview(_:)` | Presents a Quick Look preview of the contents of a single URL. |
| `quickLookPreview(_:in:)` | Presents a Quick Look preview of the URLs you provide. |

### Interacting with networked devices

| API | Purpose |
|-----|---------|
| `devicePickerSupports` | Checks for support to present a DevicePicker. |

### Configuring a Live Activity

| API | Purpose |
|-----|---------|
| `activitySystemActionForegroundColor(_:)` | The text color for the auxiliary action button that the system shows next to a Live Activity on the |
| `activityBackgroundTint(_:)` | Sets the tint color for the background of a Live Activity that appears on the Lock Screen. |
| `isActivityFullscreen` | A Boolean value that indicates whether the Live Activity appears in a |
| `activityFamily` | The size family of the current Live Activity. |

### Interacting with the App Store and Apple Music

| API | Purpose |
|-----|---------|
| `appStoreOverlay(isPresented:configuration:)` | Presents a StoreKit overlay when a given condition is true. |
| `manageSubscriptionsSheet(isPresented:)` | — |
| `refundRequestSheet(for:isPresented:onDismiss:)` | Display the refund request sheet for the given transaction. |
| `offerCodeRedemption(isPresented:onCompletion:)` | Presents a sheet that enables customers to redeem offer |
| `musicSubscriptionOffer(isPresented:options:onLoadCompletion:)` | Initiates the process of presenting a sheet with subscription offers |
| `currentEntitlementTask(for:priority:action:)` | Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a |
| `inAppPurchaseOptions(_:)` | Add a function to call before initiating a purchase from StoreKit view within this view, providing a set |
| `manageSubscriptionsSheet(isPresented:subscriptionGroupID:)` | — |

### Accessing health data

| API | Purpose |
|-----|---------|
| `healthDataAccessRequest(store:objectType:predicate:trigger:completion:)` | Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions). |
| `healthDataAccessRequest(store:readTypes:trigger:completion:)` | Requests permission to read the specified HealthKit data types. |
| `healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)` | Requests permission to save and read the specified HealthKit data types. |
| `workoutPreview(_:isPresented:)` | Presents a preview of the workout contents as a modal sheet |

### Providing tips

| API | Purpose |
|-----|---------|
| `popoverTip(_:arrowEdge:action:)` | Presents a popover tip on the modified view. |
| `tipBackground(_:)` | Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips. |
| `tipCornerRadius(_:antialiased:)` | Sets the corner radius for an inline tip view. |
| `tipImageSize(_:)` | Sets the size for a tip’s image. |
| `tipViewStyle(_:)` | Sets the given style for TipView within the view hierarchy. |
| `tipImageStyle(_:)` | Sets the style for a tip’s image. |
| `tipImageStyle(_:_:)` | Sets the style for a tip’s image. |
| `tipImageStyle(_:_:_:)` | Sets the style for a tip’s image. |

### Showing a translation

| API | Purpose |
|-----|---------|
| `translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)` | Presents a translation popover when a given condition is true. |
| `translationTask(_:action:)` | Adds a task to perform before this view appears or when the translation configuration changes. |
| `translationTask(source:target:action:)` | Adds a task to perform before this view appears or when the specified source or target |
| `translationTask(source:target:preferredStrategy:action:)` | Adds a task to perform before this view appears or when the specified source or target |

### Presenting journaling suggestions

| API | Purpose |
|-----|---------|
| `journalingSuggestionsPicker(isPresented:onCompletion:)` | Presents a visual picker interface that contains events and images that a person can select |

### Managing contact access

| API | Purpose |
|-----|---------|
| `contactAccessButtonCaption(_:)` | — |
| `contactAccessButtonStyle(_:)` | — |
| `contactAccessPicker(isPresented:completionHandler:)` | Modally present UI which allows the user to select which |

### Handling game controller events

| API | Purpose |
|-----|---------|
| `handlesGameControllerEvents(matching:)` | Specifies the game controllers events which should be delivered through |

### Creating a tabletop game

| API | Purpose |
|-----|---------|
| `tabletopGame(_:parent:automaticUpdate:)` | Adds a tabletop game to a view. |
| `tabletopGame(_:parent:automaticUpdate:interaction:)` | Supplies a closure which returns a new interaction whenever needed. |

### Configuring camera controls

| API | Purpose |
|-----|---------|
| `realityViewCameraControls` | The camera controls for the reality view. |
| `realityViewCameraControls(_:)` | Adds gestures that control the position and direction of a virtual camera. |

### Interacting with transactions

| API | Purpose |
|-----|---------|
| `transactionPicker(isPresented:selection:)` | Presents a picker that selects a collection of transactions. |
