import os
from rork_snippets import get_rork_quality_section

skills = {
    "Liquid Glass Architecture": "Depth, translucency, and material hierarchies. Mastering .ultraThinMaterial and layered shadows.",
    "Physics-Driven Motion": "Spring systems, damping, and natural gestures. Moving beyond EaseInOut to physical realism.",
    "Haptic Canvas": "Sensory-integrated feedback. Using CoreHaptics and ImpactGenerators for tactile delight.",
    "Custom Metal Shaders": "Pixel-perfect visual effects. Using iOS 17+ colorEffect and distortionEffect for premium VFX.",
    "Fluid Navigation Transitions": "Interactive hero-style view transitions. Mastering matchedGeometryEffect and custom transition phases.",
    "Dynamic Type & Typography Mastery": "Elite kerning, tracking, and scaleable UI. Apple-native typography schema.",
    "Spatial Design": "Depth-focused layout systems. Adapting visionOS principles to the iOS canvas.",
    "Immersive Audio-Visuals": "UI that reacts to sound and motion sensors. Creating living, reactive interfaces.",
    "Interactive Detents & Sheets": "High-end bottom sheet customization. Mastering presentationDetents and background interactions.",
    "Native Canvas Drawing": "Complexity through direct shape manipulation. High-performance 2D drawing with SwiftUI Canvas.",
    "Scroll-Driven Parallax": "Sticky headers with dynamic opacity, scale, and stretchy effects.",
    "Micro-interaction Physics": "Button bounce, elasticity, and state morphing. Perfecting the small moments of delight.",
    "Skeleton & Perceived Performance": "High-end data loading aesthetics. Using animated shimmer gradients and placeholders.",
    "Card Geometry & Soft Depth": "Advanced shadows and corner-radius logic. Mastering the 'continuous' squircle aesthetic.",
    "Contextual Haptic Menus": "Polishing the UIContextMenuInteraction and preview feel for elite depth.",
    "Live Activity & Dynamic Island": "Designing for real-time presence. Mastering ActivityKit and Island regions.",
    "Particle Systems for Delight": "Glitter, celebration, and feedback particles using high-performance emitters.",
    "Semantic Dynamic Themes": "Beyond Dark Mode—environmental-adaptive UI using system colors and vibrancies.",
    "Form Interaction & Validation": "Floating labels with fluid, bouncy feedback and focus-state brilliance.",
    "High-Performance List Rendering": "Strategies for large-scale 'wow' lists. Using LazyVStack and drawingGroup optimization."
}

def generate_frontend_skills():
    root_dir = "frontend_skills"
    
    for skill_title, skill_desc in skills.items():
        skill_id = skill_title.lower().replace(' ', '_').replace('&', 'and')
        folder_path = os.path.join(root_dir, skill_id)
        os.makedirs(folder_path, exist_ok=True)
        
        rork_section = get_rork_quality_section(skill_title)
        
        content = f"""---
name: {skill_title}
description: Rork-Max Quality elite iOS frontend skill for {skill_title}. {skill_desc}
---

# {skill_title}

{skill_desc}

{rork_section}

## Core Principles

1. **Native Polish**: Always prioritize system-standard feel (springs, materials, haptics) before custom art.
2. **Visual Depth**: Use Z-axis hierarchy (shadows, blurs) to guide user focus.
3. **Responsiveness**: Every touch and state change MUST have an immediate, physical response.

---
*Created with ❤️ by Antigravity for Rork-Quality Apps.*
"""
        with open(os.path.join(folder_path, "SKILL.md"), "w") as f:
            f.write(content)
        
        print(f"Generated {skill_title} ({skill_id}/SKILL.md)")

if __name__ == "__main__":
    generate_frontend_skills()
