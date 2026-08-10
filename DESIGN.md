---
name: Sentinel Security System
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bcc7de'
  primary: '#bcc7de'
  on-primary: '#263143'
  primary-container: '#1e293b'
  on-primary-container: '#8590a6'
  inverse-primary: '#545f73'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#ddc39d'
  on-tertiary: '#3e2e13'
  tertiary-container: '#35260c'
  on-tertiary-container: '#a38c6a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e3fb'
  primary-fixed-dim: '#bcc7de'
  on-primary-fixed: '#111c2d'
  on-primary-fixed-variant: '#3c475a'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#fadfb8'
  tertiary-fixed-dim: '#ddc39d'
  on-tertiary-fixed: '#271902'
  on-tertiary-fixed-variant: '#564427'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max-width: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for a security-first environment where clarity, authority, and precision are paramount. The brand personality is stoic and reliable, aiming to instill a sense of calm and control in high-stakes technical environments. 

The aesthetic is **Refined Minimalism**. It leverages a high-density information architecture balanced by expansive whitespace to prevent cognitive overload. The UI avoids unnecessary ornamentation, focusing instead on structural integrity through a card-based layout, subtle depth, and purposeful color application. The target audience—security professionals and IT administrators—requires a tool that feels more like a precision instrument than a social application.

## Colors

The palette is anchored in a dark-mode-first approach to reduce eye strain during prolonged monitoring sessions. 

- **Primary & Secondary:** Utilize deep slates and charcoals to create a sophisticated, layered environment. The primary background is nearly black, while surfaces use slightly lighter slates to establish hierarchy.
- **Accent & Action:** Use a crisp, neutral white or light slate for primary actions to ensure high contrast against the dark background.
- **Semantic Feedback:** These are the only vibrant colors allowed in the system. Emerald Green denotes "Secure" or "Pass," Amber signifies "Potential Risk" or "Warning," and Crimson is reserved strictly for "Critical Failures" or "Insecure" states. These colors must maintain a minimum 4.5:1 contrast ratio against the slate surfaces.

## Typography

This design system uses a dual-font approach to maximize utility. 

**Inter** serves as the primary typeface for all interface elements, headings, and body copy. It is selected for its exceptional legibility and neutral tone. To maintain a professional look, tracking is slightly tightened on large headings and opened up on small labels.

**JetBrains Mono** is used exclusively for technical data, password inputs, recovery keys, and code snippets. The monospaced nature ensures that characters like '1', 'l', and 'I' or '0' and 'O' are easily distinguishable—a critical requirement for security tools. 

On mobile devices, `display-lg` should scale down to `32px` to ensure text remains within the viewport without excessive wrapping.

## Layout & Spacing

The system follows a strict **12-column fluid grid** for desktop and a **single-column vertical stack** for mobile. 

A "Generous Whitespace" philosophy is applied: 
- **Vertical Rhythm:** Use `stack-lg` (32px) between major sections and `stack-md` (16px) between related card components.
- **Padding:** Internal card padding should never be less than 24px to give data "room to breathe."
- **Alignment:** All elements must align to a 4px baseline grid to ensure mathematical precision in the layout.

On mobile, margins are reduced to 16px to maximize the utility of the screen real estate, while maintaining large touch targets for actionable security alerts.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows**. 

1. **Base Layer:** The darkest shade (`#020617`), used for the background.
2. **Surface Layer (Level 1):** Card containers use `#0F172A`. These have a subtle 1px border of `#1E293B` to define edges.
3. **Elevated Layer (Level 2):** Modals or active cards use a slightly lighter slate and an extra-diffused shadow (0px 10px 30px rgba(0,0,0,0.5)) to appear as if they are floating closer to the user.

Shadows should be cold-tinted (using deep blues instead of pure black) to remain cohesive with the charcoal palette. No heavy, sharp borders or "skeuomorphic" extrusions are used.

## Shapes

The shape language is **Soft (0.25rem)**. This provides a modern, approachable feel while maintaining the structural "seriousness" of a security tool. 

- **Cards & Inputs:** Use the base `rounded` (4px) value.
- **Buttons:** Can use `rounded-lg` (8px) to make them more distinct and tactile.
- **Status Badges:** Use a full pill shape (rounded-full) to differentiate them from interactive buttons and input fields.

## Components

- **Buttons:** Primary buttons use a high-contrast slate-to-white background. Secondary buttons use an outline style with 1px slate-600 borders.
- **Status Badges:** Compact labels with a low-opacity semantic background (e.g., 10% Crimson) and a full-opacity semantic text color.
- **Progress Bars:** Thin (4px - 8px) tracks with a solid semantic color fill. For password strength, the bar color should transition dynamically from Crimson to Emerald.
- **Input Fields:** Darker than the card surface to create a "well" effect. Monospaced font for password fields. On focus, the border transitions to a subtle glow of the primary slate color.
- **Actionable Alerts:** Large, surface-level containers with a thick (4px) left-accent border in the semantic color (Emerald, Amber, or Crimson). These must include a clear icon and a bold title.
- **Data Tables:** High-density with `body-sm` text. Rows should have a subtle hover state (`#1E293B`) to assist with horizontal tracking.