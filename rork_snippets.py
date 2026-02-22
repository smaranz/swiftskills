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
        "snippet": """
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
    
    tips_md = "\\n".join([f"- {tip}" for tip in tips])
    
    return f"""
## 🚀 Rork-Max Quality Snippet

{snippet}

## 💎 Elite Implementation Tips

{tips_md}
"""
