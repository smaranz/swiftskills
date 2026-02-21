import os

skills = {
    "color_theory_and_palettes": "Mastering color relationships, avoiding generic colors, utilizing HSL, and creating harmonious, modern palettes that evoke a premium feel.",
    "typography_schema": "Using modern fonts (Inter, Roboto, Outfit), establishing clear hierarchy, and ensuring perfect readability and contrast.",
    "spacing_and_grids": "Implementing consistent spacing tokens (4pt/8pt grid systems) to create breathing room and structured layouts.",
    "glassmorphism_and_depth": "Creating stunning translucent layers using backdrop-filter, subtle borders, and layered shadows for a 3D feel.",
    "dark_mode_implementation": "Designing sleek, low-strain dark themes using deep grays/blues rather than pure black, and adjusting text/border contrasts accordingly.",
    "fluid_typography": "Using clamp() and viewport units to create text that scales perfectly across device sizes without media query breakpoints.",
    "css_grid_mastery": "Structuring complex 2D layouts gracefully, utilizing fraction units (fr), minmax(), and auto-fit/auto-fill for responsive grids.",
    "flexbox_mastery": "Mastering 1D alignment, distribution of space, wrapping, and precise centering of elements.",
    "micro_interactions": "Adding subtle, performant hover, focus, and active state animations to make the UI feel alive and responsive.",
    "scroll_animations": "Implementing scroll-linked animations, fading elements in view, and parallax effects using modern CSS/JS APIs.",
    "performance_optimization": "Ensuring fast load times, minimizing layout shifts (CLS), and utilizing hardware acceleration for animations.",
    "responsive_design_patterns": "Moving beyond generic breakpoints to design modular, adaptable components that reflow naturally.",
    "accessibility_and_focus": "Creating beautiful, visible focus rings, ensuring semantic HTML, and meeting WCAG contrast guidelines without sacrificing aesthetics.",
    "state_driven_styling": "Styling components visually based on varying states (loading, error, success, empty) smoothly and clearly.",
    "component_reusability": "Building UI pieces that isolate their own styling and accept variants (primary, secondary, outlined) easily.",
    "svg_animations": "Breathing life into vector graphics, icons, and illustrations using CSS and lightweight JS libraries.",
    "interactive_forms": "Designing forms that feel engaging, with floating labels, real-time validation feedback, and clear input states.",
    "loading_states_and_skeletons": "Using shimmer effects and skeleton screens to provide perceived performance while data fetches.",
    "3d_transforms": "Adding perspective, rotation, and translation to flat elements to create immersive card flips and dynamic depth.",
    "modern_css_features": "Leveraging CSS variables, logical properties, :has(), and container queries to write advanced, maintainable styles."
}

def generate_frontend_skills():
    root_dir = "frontend_skills"
    
    for skill_id, skill_desc in skills.items():
        folder_path = os.path.join(root_dir, skill_id)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create a more detailed markdown file internally
        skill_title = skill_id.replace('_', ' ').title()
        
        content = f"""---
name: {skill_title}
description: {skill_desc}
---

# {skill_title}

{skill_desc}

## Core Principles

1. **Aesthetics First**: The user must be wowed. Do not settle for basic styling.
2. **Modern Implementation**: Rely on modern APIs (Custom Properties, Grid, Flexbox, modern units).
3. **Consistency**: Ensure patterns are applied uniformly across the entire project.

## Implementation Guide

- Start by defining design tokens (variables) before hardcoding values.
- Build from the component level up, ensuring this skill is isolated to relevant UI elements.
- Test variations across different themes (light/dark) if applicable.

*Note: This is an automatically generated elite frontend skill blueprint based on absolute best practices.*
"""
        with open(os.path.join(folder_path, "SKILL.md"), "w") as f:
            f.write(content)
        
        print(f"Generated {skill_title} ({skill_id}/SKILL.md)")

if __name__ == "__main__":
    generate_frontend_skills()
