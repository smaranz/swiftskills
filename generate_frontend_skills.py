import os
from rork_snippets import get_rork_quality_section

skills = {
    "Liquid Glass Architecture": {
        "description": "Depth, translucency, and material hierarchies. Mastering .ultraThinMaterial and layered shadows.",
        "when_to_use": [
            "Creating frosted-glass card overlays on vibrant backgrounds",
            "Building layered UI with depth planes using material blur",
            "Designing modal sheets and floating panels with translucent backgrounds",
        ],
        "best_practices": [
            "Use `.ultraThinMaterial` for topmost glass layers; `.regularMaterial` for deeper layers",
            "Add a 1pt white stroke at 0.2 opacity to define crisp glass edges",
            "Pair `MeshGradient` backgrounds with glass layers for a dynamic, liquid feel",
            "Use `ZStack` ordering to create clear depth planes: background → mid-glass → foreground",
        ],
        "pitfalls": [
            "Stacking too many material layers kills performance — limit to 2-3 glass planes",
            "Materials on opaque backgrounds look like plain gray — always use a vibrant background behind glass",
            "Forgetting dark mode testing — materials adapt automatically but your strokes and shadows may not",
        ],
    },
    "Physics-Driven Motion": {
        "description": "Spring systems, damping, and natural gestures. Moving beyond EaseInOut to physical realism.",
        "when_to_use": [
            "Animating interactive drag, swipe, or bounce interactions",
            "Replacing ease-in/ease-out curves with natural spring physics",
            "Creating rubber-banding, snap-back, and throw-to-dismiss gestures",
        ],
        "best_practices": [
            "Always use `.spring(response:dampingFraction:)` instead of `.easeInOut` for interactive elements",
            "Match spring response to distance — shorter movements need faster response (0.2–0.3s)",
            "Use `dampingFraction` 0.5–0.7 for bouncy UI, 0.8–1.0 for settled, precise motion",
            "Make animations interruptible — never block gesture updates during spring animations",
        ],
        "pitfalls": [
            "Using `.linear` or `.easeInOut` for interactive elements — they feel robotic",
            "Overly bouncy springs (dampingFraction < 0.4) distract from content and annoy users",
            "Not testing with `UIAccessibility.isReduceMotionEnabled` — provide crossfade fallbacks",
        ],
    },
    "Haptic Canvas": {
        "description": "Sensory-integrated feedback. Using CoreHaptics and ImpactGenerators for tactile delight.",
        "when_to_use": [
            "Confirming discrete actions (button press, toggle, delete)",
            "Providing feedback during drag thresholds, snap points, or scroll boundaries",
            "Creating premium tactile experiences for gaming or creative apps",
        ],
        "best_practices": [
            "Use `.soft` and `.light` patterns for frequent interactions to avoid haptic fatigue",
            "Align haptic triggers with the exact peak of a visual animation",
            "Use `.rigid` for physical boundary feedback and `.selection` for scrolling increments",
            "Call `generator.prepare()` ahead of time to eliminate latency",
        ],
        "pitfalls": [
            "Triggering haptics on every frame during a drag — batch to threshold crossings",
            "Using strong haptics for subtle UI — it feels jarring and drains battery",
            "Forgetting that haptics are silent in silent mode on some devices",
        ],
    },
    "Custom Metal Shaders": {
        "description": "Pixel-perfect visual effects. Using iOS 17+ colorEffect and distortionEffect for premium VFX.",
        "when_to_use": [
            "Adding organic noise, grain, or shimmer to backgrounds",
            "Creating custom blur, distortion, or glow effects beyond built-in modifiers",
            "Building real-time animated effects (water ripple, heat haze, light leak)",
        ],
        "best_practices": [
            "Keep shader intensity subtle (0.03–0.08 noise) for premium tactile texture",
            "Shaders are GPU-accelerated — use them for full-screen backgrounds without fear",
            "Pass `Date.now.timeIntervalSince1970` as a float uniform for organic motion",
            "Use `.visualEffect { content, proxy in }` for per-view shader application (iOS 17+)",
        ],
        "pitfalls": [
            "Over-processing — heavy shaders on every view cause GPU throttling on older devices",
            "Not providing a fallback for pre-iOS 17 devices where ShaderLibrary is unavailable",
            "Testing only in Simulator — Metal shaders behave differently on real hardware",
        ],
    },
    "Fluid Navigation Transitions": {
        "description": "Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.",
        "when_to_use": [
            "Creating hero transitions between a thumbnail and a detail view",
            "Building interactive, interruptible navigation animations",
            "Connecting visual elements across navigation stack destinations",
        ],
        "best_practices": [
            "Use `matchedGeometryEffect(id:in:)` with a shared `@Namespace` for hero animations",
            "Apply `.geometryGroup()` to resolve layout conflicts during transitions",
            "Scale the background view to 0.95 when a hero card expands for depth",
            "Use `NavigationTransition.zoom` (iOS 18+) for built-in hero transitions",
        ],
        "pitfalls": [
            "Namespace not shared correctly — the hero effect silently fails",
            "Mismatched view hierarchies cause geometry effects to jump instead of interpolate",
            "Over-animating — subtle transitions (0.3s spring) feel better than dramatic ones",
        ],
    },
    "Dynamic Type & Typography Mastery": {
        "description": "Elite kerning, tracking, and scaleable UI. Apple-native typography schema.",
        "when_to_use": [
            "Building text-heavy screens (articles, settings, onboarding)",
            "Creating branded typography that respects Dynamic Type scaling",
            "Designing typographic hierarchy (headlines, body, captions) for readability",
        ],
        "best_practices": [
            "Use system text styles (`.title`, `.body`, `.caption`) — they scale with Dynamic Type",
            "Apply negative tracking (-0.3 to -0.5) on large headlines for tighter, premium feel",
            "Use `.foregroundStyle(.secondary)` for de-emphasized text instead of lower opacity",
            "Test with 'Extra Extra Large' Dynamic Type to catch layout overflow",
        ],
        "pitfalls": [
            "Hard-coding font sizes — the UI breaks at accessibility text sizes",
            "Using `.foregroundColor` (deprecated) instead of `.foregroundStyle`",
            "Forgetting `@ScaledMetric` for spacing that should scale with Dynamic Type",
        ],
    },
    "Spatial Design": {
        "description": "Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.",
        "when_to_use": [
            "Adding depth cues (parallax, shadow, scale) to flat iOS interfaces",
            "Designing UI that transitions between 2D (iOS) and 3D (visionOS) contexts",
            "Creating hover/focus effects that simulate spatial interaction",
        ],
        "best_practices": [
            "Use `.rotation3DEffect` and `.offset(z:)` to simulate depth on iOS",
            "Implement touch-down scale feedback to mimic spatial hover effects",
            "Maintain consistent shadow offsets across all cards for a unified light source",
            "Use `#if os(visionOS)` to provide true spatial effects when running on Vision Pro",
        ],
        "pitfalls": [
            "Excessive 3D transforms cause disorientation and motion sickness",
            "Inconsistent shadow directions — pick one light source and stick with it",
            "Parallax effects without Reduce Motion support violate accessibility guidelines",
        ],
    },
    "Immersive Audio-Visuals": {
        "description": "UI that reacts to sound and motion sensors. Creating living, reactive interfaces.",
        "when_to_use": [
            "Building music players or audio apps with visualizer elements",
            "Creating motion-reactive backgrounds (gyroscope parallax)",
            "Designing ambient, living UI that responds to environmental input",
        ],
        "best_practices": [
            "Visual pulses should lead haptics by 1–5ms for perceived synchrony",
            "Use `CoreMotion` to tilt background gradients based on device orientation",
            "Cap visual amplitude at 20% scale to avoid overwhelming the content",
            "Always provide a static fallback for Reduce Motion users",
        ],
        "pitfalls": [
            "Continuous sensor polling drains battery — throttle to 30Hz for UI updates",
            "Audio analysis on the main thread causes dropped frames",
            "Motion-reactive UI without opt-out is an accessibility failure",
        ],
    },
    "Interactive Detents & Sheets": {
        "description": "High-end bottom sheet customization. Mastering presentationDetents and background interactions.",
        "when_to_use": [
            "Building mini-player, map overlay, or drawer-style bottom sheets",
            "Allowing interaction with content behind a partially visible sheet",
            "Creating custom sheet heights for context-specific workflows",
        ],
        "best_practices": [
            "Use custom `.height()` detents for context-specific mini-players or drawers",
            "Enable `.presentationBackgroundInteraction(.enabled(upThrough: .medium))` for map-style UIs",
            "Set `.presentationCornerRadius(32–44)` for sheets that feel integrated with the app",
            "Combine detents: `[.height(200), .medium, .large]` for three-stop sheets",
        ],
        "pitfalls": [
            "Forgetting `.presentationDragIndicator(.visible)` — users need affordance to drag",
            "Background interaction enabled at `.large` detent — the sheet covers the content anyway",
            "Not testing with keyboard visible — sheets resize when the keyboard appears",
        ],
    },
    "Native Canvas Drawing": {
        "description": "Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.",
        "when_to_use": [
            "Drawing complex shapes, charts, or visualizations at 120Hz",
            "Rendering large numbers of graphic elements more efficiently than SwiftUI views",
            "Creating custom drawing tools, annotation layers, or game rendering",
        ],
        "best_practices": [
            "Use `Canvas` for any view with > 50 graphic elements — it flattens the hierarchy",
            "Draw paths using normalized coordinates to scale across screen sizes",
            "Leverage `context.drawLayer` for group transforms and clipping",
            "Use `context.resolveSymbol(id:)` to embed SwiftUI views inside Canvas draws",
        ],
        "pitfalls": [
            "Canvas doesn't respond to gestures on individual drawn elements — overlay hit-test views",
            "Forgetting that Canvas redraws entirely on state changes — cache expensive path calculations",
            "Using Canvas for simple layouts where `Path` or `Shape` would be more maintainable",
        ],
    },
    "Scroll-Driven Parallax": {
        "description": "Sticky headers with dynamic opacity, scale, and stretchy effects.",
        "when_to_use": [
            "Building stretchy hero image headers that expand on over-scroll",
            "Creating parallax depth effects in scrollable content",
            "Fading in compact titles as full headers scroll out of view",
        ],
        "best_practices": [
            "Use `GeometryReader` + `.frame(in: .global).minY` to detect over-scroll distance",
            "Implement negative offset for parallax: content moves slower than the scroll",
            "Fade in a compact navigation title by mapping scroll offset to opacity (0→1)",
            "Use `scrollTargetBehavior(.paging)` for snap-to-position scroll effects (iOS 17+)",
        ],
        "pitfalls": [
            "GeometryReader inside LazyVStack recalculates on every scroll frame — profile performance",
            "Stretchy headers without clipping overflow into safe area and status bar",
            "Testing only in one orientation — parallax ratios may need adjustment for landscape",
        ],
    },
    "Micro-interaction Physics": {
        "description": "Button bounce, elasticity, and state morphing. Perfecting the small moments of delight.",
        "when_to_use": [
            "Adding tactile press feedback to buttons and interactive elements",
            "Morphing icons or shapes between states (play → pause, plus → X)",
            "Creating subtle spring responses on toggles, checkboxes, and selection changes",
        ],
        "best_practices": [
            "Scale down to 0.92–0.95 on press; spring back with dampingFraction 0.4",
            "The 'down' animation should be 2x faster than the 'up' animation",
            "Use brightness adjustment (-0.05) on press instead of opacity changes",
            "Trigger `.light` haptic on touch-down for confirming engagement",
        ],
        "pitfalls": [
            "Over-animating every element — micro-interactions should be barely noticed, not distracting",
            "Missing the press-cancel path — if a drag leaves the button, reset without spring",
            "Scale effects on buttons inside scroll views can conflict with scroll gesture detection",
        ],
    },
    "Skeleton & Perceived Performance": {
        "description": "High-end data loading aesthetics. Using animated shimmer gradients and placeholders.",
        "when_to_use": [
            "Showing placeholder UI while network data loads",
            "Replacing spinners with skeleton screens that preview the content layout",
            "Improving perceived performance by showing structure before data arrives",
        ],
        "best_practices": [
            "Match skeleton shapes to actual content layout (image placeholders, text lines)",
            "Use a linear gradient shimmer at 1.5s duration for 'just right' pacing",
            "Apply system colors so skeletons match dark/light mode automatically",
            "Stagger row animation start times by 50–100ms for an organic cascading reveal",
        ],
        "pitfalls": [
            "Skeleton that doesn't match final layout causes a jarring shift when content loads",
            "Shimmer animations without Reduce Motion support — use static placeholders as fallback",
            "Showing skeletons for < 200ms — flash of skeleton is worse than no skeleton",
        ],
    },
    "Card Geometry & Soft Depth": {
        "description": "Advanced shadows and corner-radius logic. Mastering the 'continuous' squircle aesthetic.",
        "when_to_use": [
            "Designing card-based layouts (feeds, dashboards, settings)",
            "Creating Apple-style rounded rectangles with continuous corner curves",
            "Building elevation hierarchy with layered shadows",
        ],
        "best_practices": [
            "Always use `.continuous` corner style for smooth squircle silhouettes",
            "Layer two shadows: one sharp (radius 10, y: 5, 0.05 opacity) and one diffuse (radius 30, y: 15, 0.1 opacity)",
            "Add a 0.5pt white top stroke to simulate light catching the edge",
            "Use 24–32pt corner radius for cards; 12–16pt for smaller elements",
        ],
        "pitfalls": [
            "`.cornerRadius()` (deprecated) doesn't support continuous curves — use `.clipShape(RoundedRectangle(cornerRadius:style:))`",
            "Pure black shadows look harsh — use the accent color with low opacity for a glow effect",
            "Inconsistent corner radii across nested elements (inner radius = outer radius − padding)",
        ],
    },
    "Contextual Haptic Menus": {
        "description": "Polishing the UIContextMenuInteraction and preview feel for elite depth.",
        "when_to_use": [
            "Adding long-press context menus to list items, cards, or media",
            "Providing quick actions (share, delete, favorite) without navigation",
            "Showing rich previews of content before committing to navigation",
        ],
        "best_practices": [
            "Use custom `.contextMenu { } preview: { }` for rich previews with glass materials",
            "Keep menu item titles short — 1-3 words maintain the clean iOS aesthetic",
            "Use SF Symbols for every menu action icon",
            "The system handles press haptic — don't trigger a second one",
        ],
        "pitfalls": [
            "Too many menu items overwhelm users — limit to 5-7 actions maximum",
            "Heavy preview views cause the menu to appear slowly — keep previews lightweight",
            "Forgetting `role: .destructive` on delete actions — it provides the red color and grouping",
        ],
    },
    "Live Activity & Dynamic Island": {
        "description": "Designing for real-time presence. Mastering ActivityKit and Island regions.",
        "when_to_use": [
            "Showing live progress (delivery tracking, sports scores, timers) on the Lock Screen",
            "Occupying Dynamic Island space for ongoing activities",
            "Providing real-time updates without requiring the app to be open",
        ],
        "best_practices": [
            "Use icons and progress bars instead of heavy text — space is extremely limited",
            "Only push updates when state changes significantly (>10% progress change)",
            "Design compact leading/trailing regions as complementary pairs (icon + value)",
            "Test both expanded and minimal presentations on all Dynamic Island sizes",
        ],
        "pitfalls": [
            "Updating too frequently — the system throttles updates and may hide the activity",
            "Complex layouts in compact regions — they get clipped without warning",
            "Forgetting to end the Live Activity when the event completes",
        ],
    },
    "Particle Systems for Delight": {
        "description": "Glitter, celebration, and feedback particles using high-performance emitters.",
        "when_to_use": [
            "Celebrating completion events (purchase, achievement, level up)",
            "Adding ambient effects (snow, confetti, sparkle) to themed screens",
            "Providing visual feedback for destructive or impactful actions",
        ],
        "best_practices": [
            "Limit to 30–50 particles max for performance and visual clarity",
            "Randomize size (±30%), velocity (±20%), and rotation for organic feel",
            "Apply gentle gravity (y acceleration ≈ 0.1 per frame) for realistic falloff",
            "Use `Canvas` for software particles or `CAEmitterLayer` for hardware-accelerated ones",
        ],
        "pitfalls": [
            "Unbounded particle count — always cap maximum and recycle particles",
            "Running particle effects continuously — use them for moments, not backgrounds",
            "Forgetting Reduce Motion — disable particle animations when accessibility setting is on",
        ],
    },
    "Semantic Dynamic Themes": {
        "description": "Beyond Dark Mode—environmental-adaptive UI using system colors and vibrancies.",
        "when_to_use": [
            "Building apps that look correct in both light and dark modes without manual color sets",
            "Creating themed experiences (seasonal, branded) that still respect system appearance",
            "Designing for high-contrast and increased-contrast accessibility modes",
        ],
        "best_practices": [
            "Never use static `.white` or `.black` — use semantic colors (`.label`, `.background`, `.systemBackground`)",
            "Dark mode backgrounds should be dark gray (`.systemBackground`), not pure black",
            "Use `.foregroundStyle(.tertiary)` for visual hierarchy instead of custom opacity values",
            "Define custom colors in Asset Catalog with light/dark variants, not in code",
        ],
        "pitfalls": [
            "Testing only in one appearance mode — always verify both light and dark",
            "Hard-coded colors that break in dark mode or high-contrast mode",
            "Using `.opacity()` for de-emphasis instead of semantic `.secondary`/`.tertiary` styles",
        ],
    },
    "Form Interaction & Validation": {
        "description": "Floating labels with fluid, bouncy feedback and focus-state brilliance.",
        "when_to_use": [
            "Building sign-up, login, or data-entry forms with validation",
            "Creating professional text input experiences with focus management",
            "Implementing inline validation with real-time error feedback",
        ],
        "best_practices": [
            "Use `@FocusState` with an enum to manage focus across fields",
            "Shake the text field on invalid input using offset animation",
            "Add `.ultraThinMaterial` behind focused fields to highlight active input",
            "Add 'Done' or 'Next' toolbar buttons to the keyboard for field navigation",
        ],
        "pitfalls": [
            "Validating on every keystroke — debounce to 300ms or validate on focus loss",
            "Not handling keyboard toolbar for field-to-field navigation",
            "Error messages that push layout around — reserve space or use overlay",
        ],
    },
    "High-Performance List Rendering": {
        "description": "Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization.",
        "when_to_use": [
            "Rendering feeds, timelines, or catalogs with 100+ items",
            "Displaying image-heavy content lists that must scroll at 60fps",
            "Building custom list styles beyond what `List` provides",
        ],
        "best_practices": [
            "Use `LazyVStack(spacing: 0)` inside `ScrollView` for full styling control",
            "Apply `.drawingGroup()` on static rows to flatten the view hierarchy for Metal rendering",
            "Cache thumbnails in memory — avoid decoding images on the main thread",
            "Use `.onAppear` on sentinel rows to trigger pagination/infinite scroll loading",
        ],
        "pitfalls": [
            "Using `VStack` for 50+ items — it renders ALL items upfront, killing performance",
            "Forgetting `.id()` on list items — SwiftUI can't diff correctly and re-renders everything",
            "Wrapping `LazyVStack` without `ScrollView` — lazy loading only works inside a scroll container",
        ],
    },
}


def generate_frontend_skills():
    root_dir = "frontend_skills"

    for skill_title, skill_data in skills.items():
        skill_id = skill_title.lower().replace(' ', '_').replace('&', 'and')
        folder_path = os.path.join(root_dir, skill_id)
        os.makedirs(folder_path, exist_ok=True)

        rork_section = get_rork_quality_section(skill_title)

        when_to_use_md = "\n".join(f"- {item}" for item in skill_data["when_to_use"])
        best_practices_md = "\n".join(f"- {item}" for item in skill_data["best_practices"])
        pitfalls_md = "\n".join(f"- {item}" for item in skill_data["pitfalls"])

        content = f"""---
name: {skill_title}
description: Rork-Max Quality elite iOS frontend skill for {skill_title}. {skill_data["description"]}
---

# {skill_title}

{skill_data["description"]}

{rork_section}

## When to Use

{when_to_use_md}

## Best Practices

{best_practices_md}

## Common Pitfalls

{pitfalls_md}
"""
        with open(os.path.join(folder_path, "SKILL.md"), "w") as f:
            f.write(content)

        print(f"Generated {skill_title} ({skill_id}/SKILL.md)")


if __name__ == "__main__":
    generate_frontend_skills()
