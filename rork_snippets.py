"""
Rork Snippets Library
High-fidelity SwiftUI snippets and elite design tips for agent skills.
"""

RORK_SNIPPETS = {
    "Animations": {
        "snippet": """
```swift
import SwiftUI

struct RorkPremiumAnimation: View {
    @State private var isAnimating = false
    
    var body: some View {
        VStack(spacing: 30) {
            // Glassmorphic Card with Spring Animation
            RoundedRectangle(cornerRadius: 25)
                .fill(.ultraThinMaterial)
                .frame(width: 300, height: 200)
                .overlay {
                    Text("Rork Max Quality")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                        .foregroundStyle(.secondary)
                }
                .scaleEffect(isAnimating ? 1.05 : 1.0)
                .rotation3DEffect(
                    .degrees(isAnimating ? 5 : 0),
                    axis: (x: 1.0, y: 1.0, z: 0.0)
                )
                .shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)
            
            Button {
                withAnimation(.spring(response: 0.5, dampingFraction: 0.6, blendDuration: 0)) {
                    isAnimating.toggle()
                }
            } label: {
                Text("Animate")
                    .font(.headline)
                    .foregroundStyle(.white)
                    .padding()
                    .frame(width: 200)
                    .background(.blue, in: Capsule())
            }
        }
    }
}
```
""",
        "tips": [
            "Use `.spring(response:dampingFraction:)` for all physical movement to feel native and premium.",
            "Combine `scaleEffect` with `shadow` updates to create a sense of 'lifting' off the screen.",
            "Leverage `.ultraThinMaterial` for glassmorphic elements rather than solid colors."
        ]
    },
    "View-styles": {
        "snippet": """
```swift
import SwiftUI

struct PremiumViewStyle: View {
    var body: some View {
        Text("Modern Aesthetic")
            .padding()
            .background {
                Capsule()
                    .fill(
                        LinearGradient(
                            colors: [.blue, .purple],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        )
                    )
                    .overlay {
                        Capsule()
                            .strokeBorder(.white.opacity(0.2), lineWidth: 1)
                    }
            }
            .foregroundStyle(.white)
            .shadow(color: .blue.opacity(0.3), radius: 10, x: 0, y: 5)
    }
}
```
""",
        "tips": [
            "Always add a subtle `.strokeBorder` (0.2 to 0.5 opacity) to gradients to define edges.",
            "Use `foregroundStyle` instead of `foregroundColor` for modern hierarchical styling.",
            "Shadows should match the color of the element (with low opacity) for a 'glow' effect."
        ]
    },
    "Layout-fundamentals": {
        "snippet": """
```swift
import SwiftUI

struct EliteLayout: View {
    var body: some View {
        Grid(alignment: .leading, horizontalSpacing: 20, verticalSpacing: 20) {
            GridRow {
                Color.blue.frame(height: 100).cornerRadius(12)
                Color.purple.frame(height: 100).cornerRadius(12)
            }
            GridRow {
                Color.teal.frame(height: 100).cornerRadius(12)
                    .gridCellColumns(2)
            }
        }
        .padding()
    }
}
```
""",
        "tips": [
            "Use Apple's standard 8pt/16pt/24pt spacing tokens for consistent rhythm.",
            "Leverage `Grid` and `GridRow` (iOS 16+) for precise control over complex layouts.",
            "Ensure all corners have a radius between 12 and 25 for a modern 'squircle' feel."
        ]
    },
    # --- Elite Frontend Expansion ---
    "Liquid Glass Architecture": {
        "snippet": """
```swift
struct LiquidGlassView: View {
    var body: some View {
        ZStack {
            MeshGradient(width: 3, height: 3, points: [
                [0, 0], [0.5, 0], [1, 0],
                [0, 0.5], [0.8, 0.5], [1, 0.5],
                [0, 1], [0.5, 1], [1, 1]
            ], colors: [.blue, .purple, .teal, .indigo, .blue, .blue, .purple, .teal, .blue])
            .ignoresSafeArea()
            
            RoundedRectangle(cornerRadius: 32)
                .fill(.ultraThinMaterial)
                .overlay(
                    RoundedRectangle(cornerRadius: 32)
                        .stroke(.white.opacity(0.2), lineWidth: 1)
                )
                .shadow(color: .black.opacity(0.1), radius: 20, x: 0, y: 10)
                .padding(20)
        }
    }
}
```
""",
        "tips": [
            "Hierarchy: Use varying material thicknesses (.ultraThin vs .regular) to create depth planes.",
            "Stroke: A 1pt white stroke at 0.2 opacity is the secret to crisp 'glass' edges.",
            "Visual: MeshGradients provide the 'liquid' feel behind glass layers."
        ]
    },
    "Physics-Driven Motion": {
        "snippet": """
```swift
struct PhysicsMotionView: View {
    @State private var offset: CGSize = .zero
    
    var body: some View {
        Circle()
            .fill(.blue.gradient)
            .frame(width: 80, height: 80)
            .offset(offset)
            .gesture(
                DragGesture()
                    .onChanged { offset = $0.translation }
                    .onEnded { _ in
                        withAnimation(.spring(response: 0.4, dampingFraction: 0.5)) {
                            offset = .zero
                        }
                    }
            )
    }
}
```
""",
        "tips": [
            "Responsiveness: Always use .spring() instead of .easeInOut for interactive elements.",
            "Naturalism: Match the response to the distance traveled—shorter distances need faster responses.",
            "Interaction: Interruptible animations are key—ensure state updates don't snap back instantly."
        ]
    },
    "Haptic Canvas": {
        "snippet": """
```swift
// Use UIImpactFeedbackGenerator for tactile delight
func triggerEliteHaptic() {
    let generator = UIImpactFeedbackGenerator(style: .rigid)
    generator.prepare()
    generator.impactOccurred(intensity: 0.8)
}
```
""",
        "tips": [
            "Subtlety: Use .soft and .light patterns for frequent interactions to avoid fatigue.",
            "Sync: Align haptic triggers with the exact peak of a fluid animation.",
            "Context: Use .rigid for physical boundaries and .selection for scrolling increments."
        ]
    },
    "Custom Metal Shaders": {
        "snippet": """
```swift
// SwiftUI + Metal Shaders (iOS 17+)
struct ShaderDelightView: View {
    var body: some View {
        Rectangle()
            .fill(.blue)
            .visualEffect { content, proxy in
                content.colorEffect(
                    ShaderLibrary.default.noise(
                        .float(Date.now.timeIntervalSince1970)
                    )
                )
            }
    }
}
```
""",
        "tips": [
            "Grain: A subtle noise shader (0.05 intensity) adds a premium tactile feel.",
            "Performance: Shaders are GPU-accelerated—use them for full-screen background effects.",
            "Dynamics: Pass the current timestamp to shaders for organic transitions."
        ]
    },
    "Fluid Navigation Transitions": {
        "snippet": """
```swift
struct HeroTransition: View {
    @Namespace var namespace
    @State private var isExpanded = false
    
    var body: some View {
        if !isExpanded {
            RoundedRectangle(cornerRadius: 20)
                .matchedGeometryEffect(id: "card", in: namespace)
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        } else {
            Rectangle()
                .matchedGeometryEffect(id: "card", in: namespace)
                .ignoresSafeArea()
                .onTapGesture { withAnimation(.spring()) { isExpanded.toggle() } }
        }
    }
}
```
""",
        "tips": [
            "Consistency: Ensure the namespace is passed down if moving between views.",
            "Smoothing: Use .geometryGroup() to resolve layout conflicts.",
            "Depth: Scale the background view slightly (0.95) when the hero card expands."
        ]
    },
    "Dynamic Type & Typography Mastery": {
        "snippet": """
```swift
Text("Rork Premium")
    .font(.system(size: 32, weight: .black, design: .rounded))
    .tracking(-0.5)
    .foregroundStyle(.primary.gradient)
```
""",
        "tips": [
            "Scale: Always test with 'Extra Extra Large' Dynamic Type.",
            "Hierarchy: Use .foregroundStyle(.secondary) instead of lower opacity.",
            "Aesthetics: .rounded design + .bold weight creates an 'app-like' feel."
        ]
    },
    "Spatial Design": {
        "snippet": """
#if os(visionOS)
Text("Spatial UI")
    .glassBackgroundEffect()
#else
Text("Spatial Style on iOS")
    .background(.ultraThinMaterial, in: Capsule())
#endif
""",
        "tips": [
            "Z-Axis: Use .offset(z:) and .rotation3DEffect to mimic spatial depth.",
            "Interaction: Implement 'hover effects' via touch-down feedback on iOS.",
            "Lighting: Simulate a global light source by consistent shadow X/Y offsets."
        ]
    },
    "Immersive Audio-Visuals": {
        "snippet": """
```swift
struct AudioReactiveView: View {
    @State private var amplitude: CGFloat = 0.5
    var body: some View {
        Circle()
            .scaleEffect(1.0 + amplitude * 0.2)
            .foregroundStyle(.blue.gradient)
    }
}
```
""",
        "tips": [
            "Feedback: Visual pulses should be 1-5ms ahead of haptics for synchrony.",
            "Sensors: Use CoreMotion to tilt the background gradient slightly.",
            "Accessibility: Always provide a way to disable motion-reactive UI."
        ]
    },
    "Interactive Detents & Sheets": {
        "snippet": """
```swift
Text("Content")
    .presentationDetents([.height(200), .medium, .large])
    .presentationBackgroundInteraction(.enabled(upThrough: .medium))
    .presentationCornerRadius(44)
```
""",
        "tips": [
            "Detents: Use custom .height() detents for context-specific mini-players.",
            "Background: .enabled background interaction allows multi-tasking.",
            "Aesthetics: A large corner radius (32-44pt) makes sheets feel integrated."
        ]
    },
    "Native Canvas Drawing": {
        "snippet": """
```swift
Canvas { context, size in
    context.stroke(Path(ellipseIn: CGRect(origin: .zero, size: size)), with: .color(.blue), lineWidth: 2)
}
```
""",
        "tips": [
            "Performance: Use Canvas for complex shapes that update at 120Hz.",
            "Resolution: Draw paths using normalized coordinates to scale perfectly.",
            "Filters: Leverage .blur and .colorMatrix in the Canvas context."
        ]
    },
    "Scroll-Driven Parallax": {
        "snippet": """
```swift
ScrollView {
    GeometryReader { proxy in
        Image("header")
            .offset(y: proxy.frame(in: .global).minY > 0 ? -proxy.frame(in: .global).minY : 0)
    }
}
```
""",
        "tips": [
            "Over-scroll: Use the minY > 0 check to implement 'stretchy' headers.",
            "Opacity: Fade in a compact title as the header scrolls out of view.",
            "Blur: Increase material blur radius as content scrolls underneath."
        ]
    },
    "Micro-interaction Physics": {
        "snippet": """
```swift
struct BouncyButton: View {
    @State private var isPressed = false
    var body: some View {
        Button("Press Me") { }
            .scaleEffect(isPressed ? 0.9 : 1.0)
            .animation(.spring(response: 0.2, dampingFraction: 0.4), value: isPressed)
    }
}
```
""",
        "tips": [
            "Timing: The 'down' animation should be twice as fast as the 'up' animation.",
            "Brightness: A subtle darkening (-0.05) is better than changing opacity.",
            "Haptics: Trigger a .light impact on touch-down."
        ]
    },
    "Skeleton & Perceived Performance": {
        "snippet": """
```swift
RoundedRectangle(cornerRadius: 12)
    .fill(.gray.opacity(0.1))
    .overlay(
        LinearGradient(colors: [.clear, .white.opacity(0.2), .clear], startPoint: .leading, endPoint: .trailing)
            .offset(x: -100 + phase * 200)
    )
```
""",
        "tips": [
            "Animation: Linear shine animations at 1.5s duration feel 'just right'.",
            "Colors: Use the system theme so skeleton matches dark/light mode.",
            "Stagger: Offset row animation start times for an organic feel."
        ]
    },
    "Card Geometry & Soft Depth": {
        "snippet": """
```swift
RoundedRectangle(cornerRadius: 24, style: .continuous)
    .fill(.background)
    .shadow(color: .black.opacity(0.05), radius: 10, y: 5)
    .shadow(color: .black.opacity(0.1), radius: 30, y: 15)
```
""",
        "tips": [
            "Layering: Use two shadows—one sharp and one diffuse for realism.",
            "Shape: Always use .continuous corner style for smooth silhouettes.",
            "Inner-Light: A 0.5pt white stroke on top simulates light-catching."
        ]
    },
    "Contextual Haptic Menus": {
        "snippet": """
```swift
Text("Press for Menu")
    .contextMenu {
        Button(role: .destructive) { } label: { Label("Delete", systemImage: "trash") }
    } preview: {
        PremiumPreviewView()
    }
```
""",
        "tips": [
            "Previews: custom .contextMenu previews should use .ultraThinMaterial.",
            "Haptics: The system handles the press haptic—don't trigger a second one.",
            "Layout: Keep menu titles short to maintain the clean iOS aesthetic."
        ]
    },
    "Live Activity & Dynamic Island": {
        "snippet": """
```swift
DynamicIsland {
    expanded {
        DynamicIslandExpandedRegion(.leading) { Text("Status") }
    }
    compactLeading { Text("L") }
    compactTrailing { Text("T") }
}
```
""",
        "tips": [
            "Content: Avoid heavy text—use icons and progress bars.",
            "Update: Only update when state changes significant (>10%).",
            "Animation: Transitions are handled by system—keep layouts flexible."
        ]
    },
    "Particle Systems for Delight": {
        "snippet": """
```swift
Canvas { context, size in
    // Render particles
    context.fill(Path(CGRect(x: 50, y: 50, width: 4, height: 4)), with: .color(.yellow))
}
```
""",
        "tips": [
            "Optimization: Limit to 50 particles max for high-end feel.",
            "Variance: Randomize size, velocity, and rotation slightly.",
            "Gravity: Apply a gentle downward acceleration (y += 0.1)."
        ]
    },
    "Semantic Dynamic Themes": {
        "snippet": r"""
```swift
struct AdaptiveTheme: ViewModifier {
    @Environment(\.colorScheme) var scheme
    var body(content: Content) -> some View {
        content.foregroundStyle(scheme == .dark ? .white : .black)
    }
}
```
""",
        "tips": [
            "Tokens: Never use static 'Color.white'—always use semantic background/materials.",
            "Contrast: Dark mode backgrounds should be dark gray, not pure black.",
            "Vibrancy: Use .foregroundStyle(.tertiary) for hierarchy."
        ]
    },
    "Form Interaction & Validation": {
        "snippet": """
```swift
TextField("Label", text: $text)
    .focused($isFocused)
    .animation(.spring(response: 0.3), value: isFocused)
```
""",
        "tips": [
            "Feedback: Shake the text field on invalid input using offsets.",
            "Focus: Use .ultraThinMaterial behind focused fields to highlight them.",
            "Keyboard: Add 'Done' or 'Next' button to the keyboard toolbar."
        ]
    },
    "High-Performance List Rendering": {
        "snippet": """
```swift
LazyVStack(spacing: 0) {
    ForEach(items) { item in
        RowView(item: item)
            .drawingGroup()
    }
}
```
""",
        "tips": [
            "Optimization: Use .drawingGroup() on static rows to flatten hierarchy.",
            "Lazy: Never render 50+ views in a standard VStack—always use LazyVStack.",
            "Smoothness: Cache thumbnails; avoid image decoding on main thread."
        ]
    }
}

# Default filler for missing snippets to ensure quality everywhere
DEFAULT_RORK_TIPS = [
    "Always check for `@Observable` (Swift 6) compatibility for optimal performance.",
    "Prioritize SF Symbols with hierarchical rendering for all iconography.",
    "Ensure all interactive elements have sufficient touch targets (min 44x44pt)."
]

def get_rork_quality_section(topic_key):
    data = RORK_SNIPPETS.get(topic_key, {})
    snippet = data.get("snippet", "```swift\\n// High-end implementation coming soon\\n```")
    tips = data.get("tips", DEFAULT_RORK_TIPS)
    
    tips_md = "\n".join([f"- {tip}" for tip in tips])
    
    return f"""
## 🚀 Rork-Max Quality Snippet

{snippet}

## 💎 Elite Implementation Tips

{tips_md}
"""


# ---------------------------------------------------------------------------
# Documentation parsing utilities
# ---------------------------------------------------------------------------

import re

SWIFTUI_TOPIC_CATEGORIES = {
    "app_organization": "app_structure", "scenes": "app_structure",
    "windows": "app_structure", "immersive_spaces": "app_structure",
    "documents": "app_structure",
    "navigation": "navigation", "modal_presentations": "navigation",
    "toolbars": "navigation", "search": "navigation",
    "app_extensions": "extensions",
    "model_data": "data", "environment_values": "data",
    "preferences": "data", "persistent_storage": "data",
    "view_fundamentals": "view_basics", "view_configuration": "view_basics",
    "view_styles": "view_basics",
    "animations": "animation",
    "text_input_and_output": "content", "images": "content",
    "controls_and_indicators": "content", "menus_and_commands": "content",
    "shapes": "drawing", "drawing_and_graphics": "drawing",
    "layout_fundamentals": "layout", "layout_adjustments": "layout",
    "custom_layout": "layout", "lists": "layout", "tables": "layout",
    "view_groupings": "layout", "scroll_views": "layout",
    "gestures": "input", "input_events": "input",
    "clipboard": "input", "drag_and_drop": "input",
    "focus": "focus",
    "system_events": "system",
    "accessibility_fundamentals": "accessibility",
    "accessible_appearance": "accessibility",
    "accessible_controls": "accessibility",
    "accessible_descriptions": "accessibility",
    "accessible_navigation": "accessibility",
    "appkit_integration": "integration", "uikit_integration": "integration",
    "watchkit_integration": "integration",
    "technology_specific_views": "integration",
    "previews_in_xcode": "tooling",
    "xcode_library_customization": "tooling",
    "performance_analysis": "tooling",
}

CATEGORY_GUIDANCE = {
    "app_structure": {
        "when_to_use": [
            "Defining the entry point and top-level structure of a SwiftUI app",
            "Managing multiple windows, scenes, or document-based workflows",
            "Configuring app-wide lifecycle events and state restoration",
            "Building multi-platform apps that adapt their structure per platform",
        ],
        "best_practices": [
            "Keep `@main` App structs thin — delegate complex logic to dedicated model objects",
            "Use `@Environment(\\.scenePhase)` to react to foreground/background transitions",
            "Prefer `WindowGroup` for document-based apps and `Window` for utility panels",
            "Store app-level state in an `@Observable` singleton injected via `.environment()`",
        ],
        "pitfalls": [
            "Putting heavy initialization in the App `init()` delays launch",
            "Forgetting that each `WindowGroup` can spawn multiple instances on macOS/iPadOS",
            "Using `@StateObject` in the App struct when `@State` with `@Observable` is simpler in Swift 6",
        ],
    },
    "navigation": {
        "when_to_use": [
            "Building hierarchical drill-down flows (settings, detail views)",
            "Implementing tab-based or sidebar navigation patterns",
            "Presenting modal sheets, popovers, alerts, or confirmation dialogs",
            "Creating deep-linkable navigation paths with `NavigationPath`",
        ],
        "best_practices": [
            "Use `NavigationStack` with a `path` binding for programmatic, deep-linkable navigation",
            "Prefer `NavigationSplitView` on iPad/Mac for sidebar + detail layouts",
            "Model navigation state explicitly so it can be saved, restored, and deep-linked",
            "Use `.sheet()`, `.fullScreenCover()`, and `.popover()` for modal presentations",
        ],
        "pitfalls": [
            "Using the deprecated `NavigationView` instead of `NavigationStack`/`NavigationSplitView`",
            "Nesting `NavigationStack` inside another `NavigationStack` causing double navigation bars",
            "Forgetting to make navigation destination types `Hashable` for `navigationDestination(for:)`",
        ],
    },
    "extensions": {
        "when_to_use": [
            "Adding widgets, watch complications, or share extensions to an app",
            "Exposing app functionality to Shortcuts, Siri, or Spotlight",
            "Implementing App Intents for system-level integration",
        ],
        "best_practices": [
            "Share data between app and extensions using App Groups and shared containers",
            "Keep extension targets lightweight — factor shared code into a framework",
            "Use `WidgetKit` timeline providers for efficient widget updates",
        ],
        "pitfalls": [
            "Extensions have strict memory limits — avoid loading large assets",
            "Forgetting to configure App Group entitlements for shared UserDefaults or files",
            "Over-scheduling widget timeline reloads, wasting battery",
        ],
    },
    "data": {
        "when_to_use": [
            "Sharing state between views without explicit prop drilling",
            "Persisting user preferences or small data sets across launches",
            "Injecting dependencies (services, repositories) into the view hierarchy",
            "Propagating theme, locale, or feature-flag values through the environment",
        ],
        "best_practices": [
            "Use `@Observable` (Swift 6) instead of `ObservableObject` for finer-grained updates",
            "Prefer `@Environment` for dependency injection over singletons",
            "Use `@AppStorage` for simple UserDefaults-backed preferences",
            "Model domain data as value types (structs) and wrap in `@Observable` classes for mutation tracking",
        ],
        "pitfalls": [
            "Storing large data in `@AppStorage` — it's backed by UserDefaults, not a database",
            "Creating `@Observable` objects inside `body` — they get recreated every render",
            "Using `@EnvironmentObject` when `@Environment` with `@Observable` is cleaner in iOS 17+",
        ],
    },
    "view_basics": {
        "when_to_use": [
            "Creating reusable UI components with customizable appearance",
            "Applying consistent styling across an app using view modifiers",
            "Configuring view behavior like disabled state, tint, and redaction",
            "Building design-system components (buttons, cards, badges) with custom styles",
        ],
        "best_practices": [
            "Extract reusable view modifiers instead of duplicating modifier chains",
            "Use `ViewModifier` protocol for complex, reusable modifier bundles",
            "Prefer `.foregroundStyle()` over `.foregroundColor()` for hierarchical tinting",
            "Apply `.compositingGroup()` before opacity to treat a view subtree as one layer",
        ],
        "pitfalls": [
            "Modifier order matters — `.padding().background()` differs from `.background().padding()`",
            "Creating views that are too large — break them into smaller extracted views",
            "Using `AnyView` for type erasure when `@ViewBuilder` or generics work better",
        ],
    },
    "animation": {
        "when_to_use": [
            "Providing visual feedback when state changes (toggle, expand, select)",
            "Creating smooth transitions when views appear, disappear, or move",
            "Building custom loading indicators, progress animations, or onboarding sequences",
            "Adding hero transitions between navigation destinations with matched geometry",
        ],
        "best_practices": [
            "Use `.spring(response:dampingFraction:)` for all interactive motion — it feels native",
            "Prefer `withAnimation` for explicit state-driven animations over implicit `.animation()`",
            "Use `PhaseAnimator` for multi-step sequential animations (iOS 17+)",
            "Test with Reduce Motion enabled — provide `UIAccessibility.isReduceMotionEnabled` fallbacks",
            "Keep durations under 0.4s for responsive UI; longer only for decorative animations",
        ],
        "pitfalls": [
            "Using `.animation(_:)` without a `value:` parameter — deprecated and causes unpredictable animations",
            "Animating too many properties simultaneously degrades performance",
            "Matched geometry effects break when the namespace isn't shared correctly across views",
            "Forgetting `.geometryGroup()` when child animations fight parent layout changes",
        ],
    },
    "content": {
        "when_to_use": [
            "Displaying text with rich formatting, markdown, or attributed strings",
            "Rendering images from assets, SF Symbols, or async URLs",
            "Building interactive controls: buttons, toggles, pickers, sliders, steppers",
            "Creating menus, context menus, and keyboard shortcuts",
        ],
        "best_practices": [
            "Use SF Symbols with `.symbolRenderingMode(.hierarchical)` for polished iconography",
            "Prefer `AsyncImage` for remote images with placeholder and error states",
            "Use `Label` to pair text with icons — it adapts to context (list rows, menus, toolbars)",
            "Support Dynamic Type by using system text styles (`.title`, `.body`, `.caption`)",
        ],
        "pitfalls": [
            "Hard-coding font sizes instead of using Dynamic Type styles",
            "Loading large images synchronously on the main thread",
            "Forgetting to provide accessibility labels for image-only buttons",
        ],
    },
    "drawing": {
        "when_to_use": [
            "Creating custom shapes beyond the built-in Rectangle, Circle, Capsule",
            "Drawing complex graphics, charts, or data visualizations",
            "Applying gradients, blend modes, or visual effects to views",
            "Building performant 2D rendering with SwiftUI `Canvas`",
        ],
        "best_practices": [
            "Use `Canvas` for high-performance drawing that updates at 120Hz",
            "Prefer `Shape` protocol for reusable, animatable custom shapes",
            "Use `.fill()` with `ShapeStyle` (gradients, materials) instead of flat colors",
            "Leverage `.drawingGroup()` to flatten complex view hierarchies into Metal-backed layers",
        ],
        "pitfalls": [
            "Overusing `GeometryReader` for simple measurements — it can cause layout issues",
            "Creating `Path` objects inside `body` without caching — they're recalculated each render",
            "Forgetting to close paths when creating custom shapes",
        ],
    },
    "layout": {
        "when_to_use": [
            "Arranging views in stacks, grids, or custom layout containers",
            "Building responsive layouts that adapt to different screen sizes",
            "Creating scrollable lists, tables, or collection-style interfaces",
            "Implementing custom layout algorithms with the `Layout` protocol",
        ],
        "best_practices": [
            "Use `LazyVStack`/`LazyHStack` inside `ScrollView` for large data sets",
            "Prefer `Grid` (iOS 16+) over nested stacks for tabular 2D layouts",
            "Use `ViewThatFits` to automatically choose between layout variants",
            "Apply `.frame(maxWidth: .infinity)` for full-width sections rather than hard-coding widths",
        ],
        "pitfalls": [
            "Putting `LazyVStack` without a `ScrollView` — it won't scroll",
            "Using `List` when you want custom styling — `LazyVStack` gives more control",
            "Nesting `ScrollView`s in the same axis causes confusing scroll behavior",
            "Forgetting `.listRowInsets(EdgeInsets())` when you want edge-to-edge list content",
        ],
    },
    "input": {
        "when_to_use": [
            "Handling tap, long press, drag, magnification, or rotation gestures",
            "Implementing drag-and-drop between views or apps",
            "Reading clipboard content or providing copy/paste support",
            "Processing keyboard, pencil, or game controller input events",
        ],
        "best_practices": [
            "Use `.onTapGesture` for simple taps; `DragGesture` for custom interactive motion",
            "Combine `.gesture()` with `.simultaneously()` or `.sequenced()` for complex interactions",
            "Prefer `Transferable` protocol (iOS 16+) for modern drag-and-drop and sharing",
            "Always provide visual feedback during gesture recognition (scale, opacity, highlight)",
        ],
        "pitfalls": [
            "Gesture conflicts with `ScrollView` — use `.simultaneousGesture()` or `.highPriorityGesture()`",
            "Forgetting minimum distance on `DragGesture` when used inside scroll views",
            "Not testing gestures with VoiceOver — ensure all gesture-driven actions have accessible alternatives",
        ],
    },
    "focus": {
        "when_to_use": [
            "Managing keyboard focus in forms and text input flows",
            "Implementing tab-order or focus-based navigation (tvOS, macOS)",
            "Highlighting the currently focused element for accessibility",
        ],
        "best_practices": [
            "Use `@FocusState` with an enum to manage focus across multiple fields",
            "Add Next/Done buttons to keyboard toolbars for field-to-field navigation",
            "Programmatically dismiss the keyboard by setting `@FocusState` to `nil`",
        ],
        "pitfalls": [
            "Forgetting to set `@FocusState` to `nil` when the user submits a form",
            "Not handling hardware keyboard tab navigation on iPad",
        ],
    },
    "system": {
        "when_to_use": [
            "Responding to scene phase changes (active, inactive, background)",
            "Handling app lifecycle events like `onOpenURL` or Handoff",
            "Reacting to system notifications like low memory or locale changes",
        ],
        "best_practices": [
            "Use `.onChange(of: scenePhase)` to pause/resume work when backgrounded",
            "Handle `onOpenURL` at the top-level scene for deep link routing",
            "Use `.onContinueUserActivity()` for Handoff and Spotlight integration",
        ],
        "pitfalls": [
            "Assuming the app is always in the foreground — save state on `.inactive`",
            "Blocking the main thread in lifecycle handlers delays the transition",
        ],
    },
    "accessibility": {
        "when_to_use": [
            "Ensuring VoiceOver users can navigate and interact with all app features",
            "Supporting Dynamic Type, Reduce Motion, and high-contrast modes",
            "Providing accessible labels, hints, and traits for custom controls",
            "Implementing accessible drag-and-drop or custom gesture alternatives",
        ],
        "best_practices": [
            "Add `.accessibilityLabel()` to every image, icon, and custom control",
            "Use `.accessibilityAddTraits(.isButton)` for interactive non-button elements",
            "Group related elements with `.accessibilityElement(children: .combine)`",
            "Test with VoiceOver enabled — it reveals issues no other tool catches",
            "Support Dynamic Type by never hard-coding font sizes",
        ],
        "pitfalls": [
            "Decorative images without `.accessibilityHidden(true)` clutter VoiceOver",
            "Custom gestures with no accessible action alternative lock out VoiceOver users",
            "Using color alone to convey information (red = error) without text/shape cues",
        ],
    },
    "integration": {
        "when_to_use": [
            "Embedding UIKit views/controllers in SwiftUI with `UIViewRepresentable`",
            "Using SwiftUI views inside UIKit with `UIHostingController`",
            "Wrapping AppKit views for macOS SwiftUI apps",
            "Integrating MapKit, WebKit, or other framework views into SwiftUI",
        ],
        "best_practices": [
            "Use `UIViewRepresentable` / `NSViewRepresentable` for UIKit/AppKit views in SwiftUI",
            "Implement `Coordinator` for delegate callbacks flowing back into SwiftUI",
            "Keep bridge code minimal — move logic into shared `@Observable` models",
            "Prefer native SwiftUI equivalents when available (e.g., `Map` over `MKMapView` wrapper)",
        ],
        "pitfalls": [
            "Forgetting to implement `updateUIView()` — state changes won't propagate to the UIKit view",
            "Creating a new `UIHostingController` every time instead of updating the existing root view",
            "Memory leaks from strong reference cycles between Coordinator and SwiftUI state",
        ],
    },
    "tooling": {
        "when_to_use": [
            "Previewing views in Xcode with different configurations (dark mode, device sizes)",
            "Adding custom views and modifiers to the Xcode Library for drag-and-drop",
            "Profiling view rendering performance with Instruments",
        ],
        "best_practices": [
            "Create multiple `#Preview` blocks for different states (empty, loading, error, populated)",
            "Use `@Previewable @State` for interactive previews with mutable state",
            "Profile with the SwiftUI Instruments template to find slow `body` evaluations",
        ],
        "pitfalls": [
            "Preview-only code leaking into production builds — use `#if DEBUG` guards",
            "Previews failing silently because of missing environment values or data",
            "Ignoring Instruments' 'View body evaluated' count — high counts signal unnecessary re-renders",
        ],
    },
}

SWIFT_CATEGORY_GUIDANCE = {
    "essentials": {
        "when_to_use": [
            "Migrating a project from Swift 5 to Swift 6 strict concurrency",
            "Adopting `@Observable`, `async/await`, and structured concurrency",
        ],
        "best_practices": [
            "Enable strict concurrency checking incrementally — start with warnings, then errors",
            "Mark shared mutable state as `@MainActor` or protect with actors",
            "Replace Combine-based data flows with `@Observable` and `AsyncSequence`",
        ],
        "pitfalls": [
            "Turning on strict concurrency globally before auditing existing code",
            "Assuming `@Sendable` closures can capture mutable state",
        ],
    },
    "standard_library": {
        "when_to_use": [
            "Working with fundamental types: strings, numbers, collections",
            "Choosing between value types (structs/enums) and reference types (classes)",
            "Implementing protocols like `Codable`, `Hashable`, `Equatable`, `Comparable`",
        ],
        "best_practices": [
            "Use `Int` unless you have a specific reason for sized integers",
            "Prefer `[Element]` array literal syntax over `Array<Element>`",
            "Use `guard let` for early exits and `if let` for optional binding",
            "Leverage `Codable` for JSON parsing instead of manual dictionary access",
        ],
        "pitfalls": [
            "Floating-point equality checks — use `isApproximatelyEqual(to:)` or tolerances",
            "Force-unwrapping optionals (`!`) without safety checks",
            "String index arithmetic — Swift strings are not random-access, use `String.Index`",
        ],
    },
    "data_modeling": {
        "when_to_use": [
            "Designing app data models with structs, classes, and enums",
            "Choosing between value semantics (struct) and reference semantics (class)",
            "Implementing protocol conformances for custom types",
        ],
        "best_practices": [
            "Default to structs — use classes only when identity or inheritance is needed",
            "Implement `Equatable` and `Hashable` for types used in collections or SwiftUI",
            "Use enums with associated values for state machines and API responses",
        ],
        "pitfalls": [
            "Using classes when structs would be simpler and safer",
            "Forgetting that struct mutations create new copies — this matters for large data",
            "Not implementing `Hashable` on types used as `ForEach` identifiers",
        ],
    },
    "concurrency": {
        "when_to_use": [
            "Performing network requests, file I/O, or database queries off the main thread",
            "Managing shared mutable state safely with actors",
            "Running multiple independent tasks in parallel with `TaskGroup`",
        ],
        "best_practices": [
            "Use `async/await` instead of completion handlers",
            "Mark UI-updating code as `@MainActor` to ensure it runs on the main thread",
            "Use `Task { }` to bridge from synchronous to asynchronous contexts",
            "Prefer structured concurrency (`async let`, `TaskGroup`) over unstructured `Task`",
        ],
        "pitfalls": [
            "Blocking the main actor with synchronous work disguised as async",
            "Creating unbounded numbers of `Task` instances without cancellation",
            "Capturing `self` strongly in long-lived tasks causing memory leaks",
        ],
    },
    "interop": {
        "when_to_use": [
            "Calling Objective-C APIs from Swift or vice versa",
            "Integrating C/C++ libraries into a Swift project",
            "Migrating an existing Objective-C codebase to Swift incrementally",
        ],
        "best_practices": [
            "Use a bridging header for Objective-C → Swift; `@objc` attribute for Swift → Objective-C",
            "Leverage `NS_SWIFT_NAME` in Objective-C headers for clean Swift API names",
            "Use `async` overloads of Objective-C completion-handler APIs",
        ],
        "pitfalls": [
            "Objective-C generics don't fully map to Swift generics — watch for `Any` erasure",
            "C pointers require careful memory management — use `withUnsafe*Pointer` wrappers",
            "KVO from Swift requires `@objc dynamic` properties",
        ],
    },
}

PLATFORM_CATEGORY_GUIDANCE = {
    "ios": {
        "when_to_use": [
            "Building native iOS/iPadOS features using UIKit APIs",
            "Implementing UIKit-specific interactions not available in SwiftUI",
            "Working with view controllers, navigation controllers, and UIKit lifecycle",
        ],
        "best_practices": [
            "Use SwiftUI for new views and bridge UIKit only when necessary",
            "Adopt modern UIKit APIs: `UICollectionViewCompositionalLayout`, diffable data sources",
            "Handle all size classes and trait changes for iPhone and iPad adaptivity",
        ],
        "pitfalls": [
            "Mixing UIKit autolayout and SwiftUI layout can cause constraint conflicts",
            "Forgetting to test on iPad — multitasking changes your window size",
            "Not adopting the UIKit scene lifecycle for multi-window support",
        ],
    },
    "macos": {
        "when_to_use": [
            "Building native macOS features with AppKit",
            "Implementing menu bar items, dock menus, and macOS-specific UI",
            "Working with NSWindow, NSViewController, and AppKit patterns",
        ],
        "best_practices": [
            "Support keyboard shortcuts and menu bar commands for every major action",
            "Use NSToolbar for window-level controls; avoid floating toolbars",
            "Support trackpad gestures and the Magic Mouse for natural interactions",
        ],
        "pitfalls": [
            "Ignoring the menu bar — macOS users expect all actions available via menus",
            "Not testing with multiple windows open simultaneously",
            "Forgetting to handle the app running without any windows (macOS apps don't quit on last window close)",
        ],
    },
    "watchos": {
        "when_to_use": [
            "Building watchOS apps with glanceable, quick interactions",
            "Implementing complications, background refresh, and workout tracking",
            "Optimizing for the small screen and limited resources of Apple Watch",
        ],
        "best_practices": [
            "Keep interactions under 5 seconds — watchOS is for glances, not sessions",
            "Use `.digitalCrownRotation()` for scroll and value adjustment",
            "Schedule background refresh tasks for up-to-date complications",
        ],
        "pitfalls": [
            "Trying to replicate the iPhone UI on watch — design for the wrist",
            "Ignoring battery constraints — minimize animations and network requests",
            "Forgetting that watchOS apps have very limited background execution time",
        ],
    },
    "visionos": {
        "when_to_use": [
            "Building spatial computing experiences for Apple Vision Pro",
            "Adding 3D content with RealityKit and volumetric windows",
            "Creating fully immersive experiences with `ImmersiveSpace`",
        ],
        "best_practices": [
            "Start with a window-based app, then add volumetric or immersive content",
            "Use `.glassBackgroundEffect()` for windows to feel native in the shared space",
            "Design for indirect input (eye tracking + hand pinch) as the primary interaction",
        ],
        "pitfalls": [
            "Assuming direct touch — visionOS primarily uses indirect gaze-and-pinch input",
            "Making UI elements too small for comfortable eye targeting (minimum 60pt touch targets)",
            "Ignoring the shared space — immersive content should not disorient the user",
        ],
    },
    "ipados": {
        "when_to_use": [
            "Implementing iPad-specific features like Apple Pencil, Stage Manager, or drag-and-drop",
            "Building productivity interfaces with multi-column navigation",
        ],
        "best_practices": [
            "Support Apple Pencil with `PKCanvasView` for drawing and handwriting",
            "Design for keyboard and trackpad in addition to touch",
            "Use `NavigationSplitView` for two- or three-column layouts",
        ],
        "pitfalls": [
            "Testing only in portrait — iPad apps must handle all orientations and multitasking sizes",
            "Not supporting external keyboard shortcuts — iPad power users expect them",
        ],
    },
}

AI_CATEGORY_GUIDANCE = {
    "foundation_models": {
        "when_to_use": [
            "Generating text content (summaries, suggestions, creative writing) on-device",
            "Producing structured Swift data types from natural language with guided generation",
            "Extending model capabilities with custom tools for domain-specific tasks",
        ],
        "best_practices": [
            "Use `@Generable` macro to get type-safe structured output from the model",
            "Create custom `Tool` types to let the model call your app's services",
            "Always handle model unavailability gracefully (device may not support Apple Intelligence)",
            "Use `LanguageModelSession` for multi-turn conversations with context",
        ],
        "pitfalls": [
            "Assuming the model is always available — check `SystemLanguageModel.default.availability`",
            "Sending overly long prompts that exceed token limits",
            "Not implementing guardrails for sensitive content in user-facing features",
        ],
    },
    "app_intents": {
        "when_to_use": [
            "Exposing app actions to Siri, Shortcuts, and Spotlight",
            "Making app features available to the system for proactive suggestions",
            "Building conversational interactions with App Intent parameters",
        ],
        "best_practices": [
            "Define `AppIntent` for every user-facing action in your app",
            "Use `@Parameter` with clear titles and descriptions for Siri dialogue",
            "Provide `AppShortcutsProvider` for discoverable shortcut suggestions",
        ],
        "pitfalls": [
            "Intents with too many required parameters create frustrating voice interactions",
            "Not testing with Siri — the intent may work in Shortcuts but fail in voice",
        ],
    },
    "image_playground": {
        "when_to_use": [
            "Letting users generate images from text descriptions within your app",
            "Adding AI-generated stickers, avatars, or illustrations",
        ],
        "best_practices": [
            "Present the Image Playground sheet for the best user experience",
            "Provide suggested concepts to guide generation toward relevant results",
        ],
        "pitfalls": [
            "Not checking device capability — Image Playground requires Apple Intelligence hardware",
        ],
    },
    "writing_tools": {
        "when_to_use": [
            "Integrating system writing tools (rewrite, proofread, summarize) into text views",
            "Enhancing text editing experiences with AI-powered writing assistance",
        ],
        "best_practices": [
            "Adopt `UIWritingToolsCoordinator` for custom text views",
            "Standard `UITextView` gets Writing Tools automatically — avoid disabling it",
        ],
        "pitfalls": [
            "Custom text views that don't adopt `UITextInteraction` won't get Writing Tools",
        ],
    },
    "genmoji": {
        "when_to_use": [
            "Supporting user-generated emoji (Genmoji) in text rendering and input",
            "Handling `NSAdaptiveImageGlyph` in attributed strings",
        ],
        "best_practices": [
            "Use `NSAttributedString` with adaptive image glyph support for rich text",
            "Ensure Genmoji render at appropriate sizes in your text layout",
        ],
        "pitfalls": [
            "Stripping Genmoji when serializing text — preserve `NSAdaptiveImageGlyph` data",
        ],
    },
}


def parse_apple_docs(md_content):
    """Parse Apple documentation markdown into structured data.

    Returns a dict with 'title', 'overview', and 'topics' (list of
    category dicts each containing 'category' name and 'apis' list of
    dicts with 'name' and 'description').
    """
    lines = md_content.split('\n')

    title = ""
    overview_lines = []
    topics = []
    current_topic = None
    section = "pre"
    pending_api_name = None

    for line in lines:
        stripped = line.strip()

        # Copyright / footer — stop processing
        if stripped.startswith('---') and section == "topics":
            break
        if 'Copyright' in stripped:
            break

        # Title
        if stripped.startswith('# ') and not title:
            title = stripped[2:].strip()
            section = "overview"
            continue

        # Section headers
        if stripped.startswith('## Topics'):
            section = "topics"
            continue
        if stripped.startswith('## Overview'):
            section = "overview"
            continue
        if stripped.startswith('## ') and section == "overview":
            section = "other"
            continue

        # Collect overview
        if section == "overview":
            if stripped.startswith('##'):
                section = "other"
                continue
            if stripped and not stripped.startswith('![') and not stripped.startswith('<doc:'):
                overview_lines.append(stripped)
            continue

        # Topic categories and API entries
        if section == "topics":
            if stripped.startswith('### '):
                cat_name = stripped[4:].strip()
                current_topic = {"category": cat_name, "apis": []}
                topics.append(current_topic)
                pending_api_name = None
                continue

            if current_topic is None:
                continue

            # Match API links: [`Name`](url) or [Name](url)
            api_match = re.match(r'\[`?([^`\]]+)`?\]\([^)]+\)', stripped)
            if api_match:
                # Save any pending API that didn't get a description
                if pending_api_name:
                    current_topic["apis"].append({"name": pending_api_name, "description": ""})
                pending_api_name = api_match.group(1)
                continue

            # If we have a pending API name and this line is a description
            if pending_api_name and stripped and not stripped.startswith('[') and not stripped.startswith('<doc:'):
                current_topic["apis"].append({"name": pending_api_name, "description": stripped})
                pending_api_name = None
                continue

            # Doc reference links (articles) — skip
            if stripped.startswith('<doc:') or stripped.startswith('  <doc:'):
                if pending_api_name:
                    current_topic["apis"].append({"name": pending_api_name, "description": ""})
                    pending_api_name = None
                continue

    # Flush last pending API
    if pending_api_name and current_topic:
        current_topic["apis"].append({"name": pending_api_name, "description": ""})

    # Clean overview text
    overview = '\n'.join(overview_lines)
    # Preserve API names from doc:// backtick links: ``doc://...SwiftUI/View/foo``) -> `foo`
    overview = re.sub(r'``doc://[^`]+/(\w[\w()/:_-]*)``\)?', r'`\1`', overview)
    overview = re.sub(r'``doc://[^`]+``\)?', '', overview)
    # Standard markdown links (handle URLs that contain balanced parens)
    overview = re.sub(r'!\[.*?\]\(.*?\)', '', overview)
    overview = re.sub(r'\[`([^`]+)`\]\((?:[^()]*|\([^()]*\))*\)', r'`\1`', overview)
    overview = re.sub(r'\[(.*?)\]\((?:[^()]*|\([^()]*\))*\)', r'\1', overview)
    # Inline doc references
    overview = re.sub(r'<doc://[^>]+/([^/>]+)>', r'\1', overview)
    overview = re.sub(r'<doc://[^>]+>', '', overview)
    # Clean up whitespace artifacts
    overview = re.sub(r'  +', ' ', overview)
    overview = re.sub(r'\n{3,}', '\n\n', overview).strip()

    return {"title": title, "overview": overview, "topics": topics}


def format_api_reference(topics, max_per_category=8):
    """Format parsed API topics into a concise reference section."""
    if not topics:
        return ""

    sections = []
    for topic in topics:
        apis = topic["apis"]
        if not apis:
            continue
        cat = topic["category"]
        rows = []
        for api in apis[:max_per_category]:
            name = api["name"]
            desc = api["description"]
            if desc:
                rows.append(f"| `{name}` | {desc} |")
            else:
                rows.append(f"| `{name}` | — |")
        table = "| API | Purpose |\n|-----|---------|"
        sections.append(f"### {cat}\n\n{table}\n" + "\n".join(rows))

    if not sections:
        return ""
    return "## Key APIs\n\n" + "\n\n".join(sections)


def format_guidance_section(header, items):
    """Format a list of guidance items as a markdown section."""
    if not items:
        return ""
    bullets = "\n".join(f"- {item}" for item in items)
    return f"## {header}\n\n{bullets}"


def get_category_guidance(topic_key, guidance_dict, category_map=None):
    """Look up guidance for a topic, falling back to generic content."""
    if category_map:
        category = category_map.get(topic_key, "")
        guidance = guidance_dict.get(category, {})
    else:
        guidance = guidance_dict.get(topic_key, {})
    return guidance
