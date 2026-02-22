---
name: Technology-specific views
description: Rork-Max Quality skill for Technology-specific views. Extracted from Apple SwiftUI Documentation and enhanced for elite development.
---

# Technology-specific views


## 🚀 Rork-Max Quality Snippet

```swift\n// High-end implementation coming soon\n```

## 💎 Elite Implementation Tips

- Always check for `@Observable` (Swift 6) compatibility for optimal performance.\n- Prioritize SF Symbols with hierarchical rendering for all iconography.\n- Ensure all interactive elements have sufficient touch targets (min 44x44pt).


## Documentation

# Technology-specific views

Use SwiftUI views that other Apple frameworks provide.

## Overview

To access SwiftUI views that another framework defines, import both
SwiftUI and the other framework into the file where you use the view. You
can find the framework to import by looking at the availability information
on the view’s documentation page.

![](images/com.apple.SwiftUI/technology-specific-views-hero@2x.png)

For example, to use the
<doc://com.apple.documentation/documentation/MapKit/Map> view in your app,
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
<doc://com.apple.documentation/design/Human-Interface-Guidelines/technologies>
in the Human Interface Guidelines.

## Topics

### Displaying web content

  <doc://com.apple.documentation/documentation/WebKit/WebView-swift.struct>

  <doc://com.apple.documentation/documentation/WebKit/WebPage>

[`webViewBackForwardNavigationGestures(_:)`](/documentation/SwiftUI/View/webViewBackForwardNavigationGestures(_:))

Determines whether horizontal swipe gestures trigger backward and forward page navigation.

[`webViewContentBackground(_:)`](/documentation/SwiftUI/View/webViewContentBackground(_:))

Specifies the visibility of the webpage’s natural background color within this view.

[`webViewContextMenu(menu:)`](/documentation/SwiftUI/View/webViewContextMenu(menu:))

Adds an item-based context menu to a WebView, replacing the default set of context menu items.

[`webViewElementFullscreenBehavior(_:)`](/documentation/SwiftUI/View/webViewElementFullscreenBehavior(_:))

Determines whether a web view can display content full screen.

[`webViewLinkPreviews(_:)`](/documentation/SwiftUI/View/webViewLinkPreviews(_:))

Determines whether pressing a link displays a preview of the destination for the link.

[`webViewMagnificationGestures(_:)`](/documentation/SwiftUI/View/webViewMagnificationGestures(_:))

Determines whether magnify gestures change the view’s magnification.

[`webViewOnScrollGeometryChange(for:of:action:)`](/documentation/SwiftUI/View/webViewOnScrollGeometryChange(for:of:action:))

Adds an action to be performed when a value, created from a scroll geometry, changes.

[`webViewScrollInputBehavior(_:for:)`](/documentation/SwiftUI/View/webViewScrollInputBehavior(_:for:))

Enables or disables scrolling in web views when using particular inputs.

[`webViewScrollPosition(_:)`](/documentation/SwiftUI/View/webViewScrollPosition(_:))

Associates a binding to a scroll position with the web view.

[`webViewTextSelection(_:)`](/documentation/SwiftUI/View/webViewTextSelection(_:))

Determines whether to allow people to select or otherwise interact with text.

### Accessing Apple Pay and Wallet

  <doc://com.apple.documentation/documentation/PassKit/PayWithApplePayButton>

  <doc://com.apple.documentation/documentation/PassKit/AddPassToWalletButton>

  <doc://com.apple.documentation/documentation/PassKit/VerifyIdentityWithWalletButton>

[`addOrderToWalletButtonStyle(_:)`](/documentation/SwiftUI/View/addOrderToWalletButtonStyle(_:))

Sets the button’s style.

[`addPassToWalletButtonStyle(_:)`](/documentation/SwiftUI/View/addPassToWalletButtonStyle(_:))

Sets the style to be used by the button.
(see `PKAddPassButtonStyle`).

[`onApplePayCouponCodeChange(perform:)`](/documentation/SwiftUI/View/onApplePayCouponCodeChange(perform:))

Called when a user has entered or updated a coupon code.
This is required if the user is being asked to provide a coupon code.

[`onApplePayPaymentMethodChange(perform:)`](/documentation/SwiftUI/View/onApplePayPaymentMethodChange(perform:))

Called when a payment method has changed and asks for an update payment request.
If this modifier isn’t provided Wallet will assume the payment method is valid.

[`onApplePayShippingContactChange(perform:)`](/documentation/SwiftUI/View/onApplePayShippingContactChange(perform:))

Called when a user selected a shipping address.
This is required if the user is being asked to provide a shipping contact.

[`onApplePayShippingMethodChange(perform:)`](/documentation/SwiftUI/View/onApplePayShippingMethodChange(perform:))

Called when a user selected a shipping method.
This is required if the user is being asked to provide a shipping method.

[`payLaterViewAction(_:)`](/documentation/SwiftUI/View/payLaterViewAction(_:))

Sets the action on the PayLaterView. See `PKPayLaterAction`.

[`payLaterViewDisplayStyle(_:)`](/documentation/SwiftUI/View/payLaterViewDisplayStyle(_:))

Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.

[`payWithApplePayButtonStyle(_:)`](/documentation/SwiftUI/View/payWithApplePayButtonStyle(_:))

Sets the style to be used by the button.
(see `PayWithApplePayButtonStyle`).

[`verifyIdentityWithWalletButtonStyle(_:)`](/documentation/SwiftUI/View/verifyIdentityWithWalletButtonStyle(_:))

Sets the style to be used by the button.
(see `PKIdentityButtonStyle`).

  <doc://com.apple.documentation/documentation/PassKit/AsyncShareablePassConfiguration>

[`transactionTask(_:action:)`](/documentation/SwiftUI/View/transactionTask(_:action:))

Provides a task to perform before this view appears

### Authorizing and authenticating

  <doc://com.apple.documentation/documentation/LocalAuthentication/LocalAuthenticationView>

  <doc://com.apple.documentation/documentation/AuthenticationServices/SignInWithAppleButton>

[`signInWithAppleButtonStyle(_:)`](/documentation/SwiftUI/View/signInWithAppleButtonStyle(_:))

Sets the style used for displaying the control
(see `SignInWithAppleButton.Style`).

[`authorizationController`](/documentation/SwiftUI/EnvironmentValues/authorizationController)

A value provided in the SwiftUI environment that views can use
to perform authorization requests.

[`webAuthenticationSession`](/documentation/SwiftUI/EnvironmentValues/webAuthenticationSession)

A value provided in the SwiftUI environment that views can use to
authenticate a user through a web service.

### Configuring Family Sharing

  <doc://com.apple.documentation/documentation/FamilyControls/FamilyActivityPicker>

[`familyActivityPicker(isPresented:selection:)`](/documentation/SwiftUI/View/familyActivityPicker(isPresented:selection:))

Presents an activity picker view as a sheet.

[`familyActivityPicker(headerText:footerText:isPresented:selection:)`](/documentation/SwiftUI/View/familyActivityPicker(headerText:footerText:isPresented:selection:))

Presents an activity picker view as a sheet.

### Reporting on device activity

  <doc://com.apple.documentation/documentation/DeviceActivity/DeviceActivityReport>

### Working with managed devices

[`managedContentStyle(_:)`](/documentation/SwiftUI/View/managedContentStyle(_:))

Applies a managed content style to the view.

[`automatedDeviceEnrollmentAddition(isPresented:)`](/documentation/SwiftUI/View/automatedDeviceEnrollmentAddition(isPresented:))

Presents a modal view that enables users to add devices to their organization.

### Creating graphics

  <doc://com.apple.documentation/documentation/Charts/Chart>

  <doc://com.apple.documentation/documentation/SceneKit/SceneView>

  <doc://com.apple.documentation/documentation/SpriteKit/SpriteView>

### Getting location information

  <doc://com.apple.documentation/documentation/CoreLocationUI/LocationButton>

  <doc://com.apple.documentation/documentation/MapKit/Map>

[`mapStyle(_:)`](/documentation/SwiftUI/View/mapStyle(_:))

Specifies the map style to be used.

[`mapScope(_:)`](/documentation/SwiftUI/View/mapScope(_:))

Creates a mapScope that SwiftUI uses to connect map controls to an associated map.

[`mapFeatureSelectionDisabled(_:)`](/documentation/SwiftUI/View/mapFeatureSelectionDisabled(_:))

Specifies which map features should have selection disabled.

[`mapFeatureSelectionAccessory(_:)`](/documentation/SwiftUI/View/mapFeatureSelectionAccessory(_:))

Specifies the selection accessory to display for a `MapFeature`

[`mapFeatureSelectionContent(content:)`](/documentation/SwiftUI/View/mapFeatureSelectionContent(content:))

Specifies a custom presentation for the currently selected feature.

[`mapControls(_:)`](/documentation/SwiftUI/View/mapControls(_:))

Configures all `Map` views in the associated environment to have
standard size and position controls

[`mapControlVisibility(_:)`](/documentation/SwiftUI/View/mapControlVisibility(_:))

Configures all Map controls in the environment to have the specified
visibility

[`mapCameraKeyframeAnimator(trigger:keyframes:)`](/documentation/SwiftUI/View/mapCameraKeyframeAnimator(trigger:keyframes:))

Uses the given keyframes to animate the camera of a `Map` when the
given trigger value changes.

[`lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)`](/documentation/SwiftUI/View/lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:))

[`lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)`](/documentation/SwiftUI/View/lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:))

[`onMapCameraChange(frequency:_:)`](/documentation/SwiftUI/View/onMapCameraChange(frequency:_:))

Performs an action when Map camera framing changes

[`mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)`](/documentation/SwiftUI/View/mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:))

Presents a map item detail popover.

[`mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)`](/documentation/SwiftUI/View/mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:))

Presents a map item detail popover.

[`mapItemDetailPopover(item:displaysMap:attachmentAnchor:)`](/documentation/SwiftUI/View/mapItemDetailPopover(item:displaysMap:attachmentAnchor:))

Presents a map item detail popover.

[`mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)`](/documentation/SwiftUI/View/mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:))

Presents a map item detail popover.

[`mapItemDetailSheet(isPresented:item:displaysMap:)`](/documentation/SwiftUI/View/mapItemDetailSheet(isPresented:item:displaysMap:))

Presents a map item detail sheet.

[`mapItemDetailSheet(item:displaysMap:)`](/documentation/SwiftUI/View/mapItemDetailSheet(item:displaysMap:))

Presents a map item detail sheet.

### Displaying media

  <doc://com.apple.documentation/documentation/HomeKit/CameraView>

  <doc://com.apple.documentation/documentation/WatchKit/NowPlayingView>

  <doc://com.apple.documentation/documentation/AVKit/VideoPlayer>

[`continuityDevicePicker(isPresented:onDidConnect:)`](/documentation/SwiftUI/View/continuityDevicePicker(isPresented:onDidConnect:))

A `continuityDevicePicker` should be used to discover and connect
nearby continuity device through a button interface or other form of activation.
On tvOS, this presents a fullscreen continuity device picker experience when selected.
The modal view covers as much the screen of `self` as possible when a given condition is true.

[`cameraAnchor(isActive:)`](/documentation/SwiftUI/View/cameraAnchor(isActive:))

Specifies the view that should act as the virtual camera for Apple Vision Pro
2D Persona stream.

### Selecting photos

  <doc://com.apple.documentation/documentation/PhotosUI/PhotosPicker>

[`photosPicker(isPresented:selection:matching:preferredItemEncoding:)`](/documentation/SwiftUI/View/photosPicker(isPresented:selection:matching:preferredItemEncoding:))

Presents a Photos picker that selects a `PhotosPickerItem`.

[`photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)`](/documentation/SwiftUI/View/photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:))

Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.

[`photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)`](/documentation/SwiftUI/View/photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:))

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

[`photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)`](/documentation/SwiftUI/View/photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:))

Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.

[`photosPickerAccessoryVisibility(_:edges:)`](/documentation/SwiftUI/View/photosPickerAccessoryVisibility(_:edges:))

Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.

[`photosPickerDisabledCapabilities(_:)`](/documentation/SwiftUI/View/photosPickerDisabledCapabilities(_:))

Disables capabilities of the Photos picker.

[`photosPickerStyle(_:)`](/documentation/SwiftUI/View/photosPickerStyle(_:))

Sets the mode of the Photos picker.

### Previewing content

[`quickLookPreview(_:)`](/documentation/SwiftUI/View/quickLookPreview(_:))

Presents a Quick Look preview of the contents of a single URL.

[`quickLookPreview(_:in:)`](/documentation/SwiftUI/View/quickLookPreview(_:in:))

Presents a Quick Look preview of the URLs you provide.

### Interacting with networked devices

  <doc://com.apple.documentation/documentation/DeviceDiscoveryUI/DevicePicker>

[`devicePickerSupports`](/documentation/SwiftUI/EnvironmentValues/devicePickerSupports)

Checks for support to present a DevicePicker.

### Configuring a Live Activity

[`activitySystemActionForegroundColor(_:)`](/documentation/SwiftUI/View/activitySystemActionForegroundColor(_:))

The text color for the auxiliary action button that the system shows next to a Live Activity on the
Lock Screen.

[`activityBackgroundTint(_:)`](/documentation/SwiftUI/View/activityBackgroundTint(_:))

Sets the tint color for the background of a Live Activity that appears on the Lock Screen.

[`isActivityFullscreen`](/documentation/SwiftUI/EnvironmentValues/isActivityFullscreen)

A Boolean value that indicates whether the Live Activity appears in a
full-screen presentation.

[`activityFamily`](/documentation/SwiftUI/EnvironmentValues/activityFamily)

The size family of the current Live Activity.

### Interacting with the App Store and Apple Music

[`appStoreOverlay(isPresented:configuration:)`](/documentation/SwiftUI/View/appStoreOverlay(isPresented:configuration:))

Presents a StoreKit overlay when a given condition is true.

[`manageSubscriptionsSheet(isPresented:)`](/documentation/SwiftUI/View/manageSubscriptionsSheet(isPresented:))

[`refundRequestSheet(for:isPresented:onDismiss:)`](/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:))

Display the refund request sheet for the given transaction.

[`offerCodeRedemption(isPresented:onCompletion:)`](/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:))

Presents a sheet that enables customers to redeem offer
codes that you configure in App Store Connect.

[`musicSubscriptionOffer(isPresented:options:onLoadCompletion:)`](/documentation/SwiftUI/View/musicSubscriptionOffer(isPresented:options:onLoadCompletion:))

Initiates the process of presenting a sheet with subscription offers
for Apple Music when the `isPresented` binding is `true`.

[`currentEntitlementTask(for:priority:action:)`](/documentation/SwiftUI/View/currentEntitlementTask(for:priority:action:))

Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a
modified view.

[`inAppPurchaseOptions(_:)`](/documentation/SwiftUI/View/inAppPurchaseOptions(_:))

Add a function to call before initiating a purchase from StoreKit view within this view, providing a set
of options for the purchase.

[`manageSubscriptionsSheet(isPresented:subscriptionGroupID:)`](/documentation/SwiftUI/View/manageSubscriptionsSheet(isPresented:subscriptionGroupID:))

[`onInAppPurchaseCompletion(perform:)`](/documentation/SwiftUI/View/onInAppPurchaseCompletion(perform:))

Add an action to perform when a purchase initiated from a StoreKit view within this view completes.

[`onInAppPurchaseStart(perform:)`](/documentation/SwiftUI/View/onInAppPurchaseStart(perform:))

Add an action to perform when a user triggers the purchase button on a StoreKit view within this
view.

[`productIconBorder()`](/documentation/SwiftUI/View/productIconBorder())

Adds a standard border to an in-app purchase product’s icon .

[`productViewStyle(_:)`](/documentation/SwiftUI/View/productViewStyle(_:))

Sets the style for In-App Purchase product views within a view.

[`productDescription(_:)`](/documentation/SwiftUI/View/productDescription(_:))

Configure the visibility of labels displaying an in-app purchase product description within the view.

[`storeButton(_:for:)`](/documentation/SwiftUI/View/storeButton(_:for:))

Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.

[`storeProductTask(for:priority:action:)`](/documentation/SwiftUI/View/storeProductTask(for:priority:action:))

Declares the view as dependent on an In-App Purchase product and returns a modified view.

[`storeProductsTask(for:priority:action:)`](/documentation/SwiftUI/View/storeProductsTask(for:priority:action:))

Declares the view as dependent on a collection of In-App Purchase products and returns a
modified view.

[`subscriptionStatusTask(for:priority:action:)`](/documentation/SwiftUI/View/subscriptionStatusTask(for:priority:action:))

Declares the view as dependent on the status of an auto-renewable subscription group, and
returns a modified view.

[`subscriptionStoreButtonLabel(_:)`](/documentation/SwiftUI/View/subscriptionStoreButtonLabel(_:))

Configures subscription store view instances within a view to use the provided button label.

[`subscriptionStoreControlIcon(icon:)`](/documentation/SwiftUI/View/subscriptionStoreControlIcon(icon:))

Sets a view to use to decorate individual subscription options within a subscription store view.

[`subscriptionStoreControlStyle(_:)`](/documentation/SwiftUI/View/subscriptionStoreControlStyle(_:))

Sets the control style for subscription store views within a view.

[`subscriptionStoreControlStyle(_:placement:)`](/documentation/SwiftUI/View/subscriptionStoreControlStyle(_:placement:))

Sets the control style and control placement for subscription store views within a view.

[`subscriptionStoreOptionGroupStyle(_:)`](/documentation/SwiftUI/View/subscriptionStoreOptionGroupStyle(_:))

Sets the style subscription store views within this view use to display groups of subscription options.

[`subscriptionStorePickerItemBackground(_:)`](/documentation/SwiftUI/View/subscriptionStorePickerItemBackground(_:))

Sets the background style for picker items of the subscription store view instances within a view.

[`subscriptionStorePickerItemBackground(_:in:)`](/documentation/SwiftUI/View/subscriptionStorePickerItemBackground(_:in:))

Sets the background shape and style for subscription store view picker items within a view.

[`subscriptionStorePolicyDestination(for:destination:)`](/documentation/SwiftUI/View/subscriptionStorePolicyDestination(for:destination:))

Configures a view as the destination for a policy button action in subscription store views.

[`subscriptionStorePolicyDestination(url:for:)`](/documentation/SwiftUI/View/subscriptionStorePolicyDestination(url:for:))

Configures a URL as the destination for a policy button action in subscription store views.

[`subscriptionStorePolicyForegroundStyle(_:)`](/documentation/SwiftUI/View/subscriptionStorePolicyForegroundStyle(_:))

Sets the style for the terms of service and privacy policy buttons within a subscription store view.

[`subscriptionStorePolicyForegroundStyle(_:_:)`](/documentation/SwiftUI/View/subscriptionStorePolicyForegroundStyle(_:_:))

Sets the primary and secondary style for the terms of service and privacy policy buttons within
a subscription store view.

[`subscriptionStoreSignInAction(_:)`](/documentation/SwiftUI/View/subscriptionStoreSignInAction(_:))

Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.

[`subscriptionStoreControlBackground(_:)`](/documentation/SwiftUI/View/subscriptionStoreControlBackground(_:))

Set a standard effect to use for the background of subscription store view controls within the view.

[`subscriptionPromotionalOffer(offer:signature:)`](/documentation/SwiftUI/View/subscriptionPromotionalOffer(offer:signature:))

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

[`preferredSubscriptionOffer(_:)`](/documentation/SwiftUI/View/preferredSubscriptionOffer(_:))

Selects a subscription offer to apply to a purchase that a customer makes from a subscription
store view, a store view, or a product view.

### Accessing health data

[`healthDataAccessRequest(store:objectType:predicate:trigger:completion:)`](/documentation/SwiftUI/View/healthDataAccessRequest(store:objectType:predicate:trigger:completion:))

Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).

[`healthDataAccessRequest(store:readTypes:trigger:completion:)`](/documentation/SwiftUI/View/healthDataAccessRequest(store:readTypes:trigger:completion:))

Requests permission to read the specified HealthKit data types.

[`healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)`](/documentation/SwiftUI/View/healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:))

Requests permission to save and read the specified HealthKit data types.

[`workoutPreview(_:isPresented:)`](/documentation/SwiftUI/View/workoutPreview(_:isPresented:))

Presents a preview of the workout contents as a modal sheet

### Providing tips

[`popoverTip(_:arrowEdge:action:)`](/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:))

Presents a popover tip on the modified view.

[`tipBackground(_:)`](/documentation/SwiftUI/View/tipBackground(_:))

Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips.

[`tipCornerRadius(_:antialiased:)`](/documentation/SwiftUI/View/tipCornerRadius(_:antialiased:))

Sets the corner radius for an inline tip view.

[`tipImageSize(_:)`](/documentation/SwiftUI/View/tipImageSize(_:))

Sets the size for a tip’s image.

[`tipViewStyle(_:)`](/documentation/SwiftUI/View/tipViewStyle(_:))

Sets the given style for TipView within the view hierarchy.

[`tipImageStyle(_:)`](/documentation/SwiftUI/View/tipImageStyle(_:))

Sets the style for a tip’s image.

[`tipImageStyle(_:_:)`](/documentation/SwiftUI/View/tipImageStyle(_:_:))

Sets the style for a tip’s image.

[`tipImageStyle(_:_:_:)`](/documentation/SwiftUI/View/tipImageStyle(_:_:_:))

Sets the style for a tip’s image.

### Showing a translation

[`translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)`](/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:))

Presents a translation popover when a given condition is true.

[`translationTask(_:action:)`](/documentation/SwiftUI/View/translationTask(_:action:))

Adds a task to perform before this view appears or when the translation configuration changes.

[`translationTask(source:target:action:)`](/documentation/SwiftUI/View/translationTask(source:target:action:))

Adds a task to perform before this view appears or when the specified source or target
languages change.

[`translationTask(source:target:preferredStrategy:action:)`](/documentation/SwiftUI/View/translationTask(source:target:preferredStrategy:action:))

Adds a task to perform before this view appears or when the specified source or target
languages change.

### Presenting journaling suggestions

[`journalingSuggestionsPicker(isPresented:onCompletion:)`](/documentation/SwiftUI/View/journalingSuggestionsPicker(isPresented:onCompletion:))

Presents a visual picker interface that contains events and images that a person can select
to retrieve more information.

### Managing contact access

[`contactAccessButtonCaption(_:)`](/documentation/SwiftUI/View/contactAccessButtonCaption(_:))

[`contactAccessButtonStyle(_:)`](/documentation/SwiftUI/View/contactAccessButtonStyle(_:))

[`contactAccessPicker(isPresented:completionHandler:)`](/documentation/SwiftUI/View/contactAccessPicker(isPresented:completionHandler:))

Modally present UI which allows the user to select which
contacts your app has access to.

### Handling game controller events

[`handlesGameControllerEvents(matching:)`](/documentation/SwiftUI/View/handlesGameControllerEvents(matching:))

Specifies the game controllers events which should be delivered through
the GameController framework when the view, or one of its descendants
has focus.

### Creating a tabletop game

[`tabletopGame(_:parent:automaticUpdate:)`](/documentation/SwiftUI/View/tabletopGame(_:parent:automaticUpdate:))

Adds a tabletop game to a view.

[`tabletopGame(_:parent:automaticUpdate:interaction:)`](/documentation/SwiftUI/View/tabletopGame(_:parent:automaticUpdate:interaction:))

Supplies a closure which returns a new interaction whenever needed.

### Configuring camera controls

[`realityViewCameraControls`](/documentation/SwiftUI/EnvironmentValues/realityViewCameraControls)

The camera controls for the reality view.

[`realityViewCameraControls(_:)`](/documentation/SwiftUI/View/realityViewCameraControls(_:))

Adds gestures that control the position and direction of a virtual camera.

### Interacting with transactions

[`transactionPicker(isPresented:selection:)`](/documentation/SwiftUI/View/transactionPicker(isPresented:selection:))

Presents a picker that selects a collection of transactions.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
