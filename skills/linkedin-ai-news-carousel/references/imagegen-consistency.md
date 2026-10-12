# Reference-anchored ImageGen workflow

Choose a design for the verified event, then freeze it for the entire post. This procedure applies to both PDF and multi-image output. The host's built-in ImageGen is the default in Codex; other hosts need an equivalent actual image tool. Prompts alone are not generated slides.

## Lock the design before generating

Save design-lock.json alongside the slide script using examples/design-lock.json as a starting structure. Select one font family and fixed role-based sizes, weights, line heights, capitalization and alignment. A headline and a footnote have different roles, but the same role keeps the same size on every slide, including the cover. Save canvas ratio, margins, grid, text regions, palette, illustration treatment, source footer and page-number position. No per-slide type shrinking, font substitution, palette swaps or new template. Shorten overflowing copy instead. Use identical canvas dimensions throughout.

Choose a theme based on the actual subject: editorial lab notes for research; architectural blueprints for infrastructure; cinematic product cutaways for hardware; restrained security dossiers for vulnerabilities; modular flow diagrams for agents; bold editorial comparisons for market changes. These are starting ideas, not a fixed rotation. Prefer useful evidence and legibility over decorative complexity. Do not fabricate screenshots, interfaces, logos or benchmark plots. Any conceptual illustration must be distinguishable from evidence.

## Generate a master, then reference it

1. Finish factual review and humanization of caption and all slide text first. Save exact text, page labels and intended narrative sequence.
2. Generate one representative slide with the complete design lock. Inspect spelling, mobile readability, margins and hierarchy. Correct it before generating the rest; save this accepted image as the master reference. A content-heavy slide can be a better master than a sparse cover.
3. Generate each remaining slide in its own ImageGen call, providing the accepted master as an actual image reference and repeating the same design lock verbatim. In Codex, inspect a local reference with view_image before using its path in imagegen. Reference the master directly for every slide, rather than chaining slide 2 to slide 3 and accumulating drift. Change only reviewed text, page number and the subject illustration inside its allocated region.
4. Record the master file/hash, design-lock hash and per-slide prompts with the manifest. If a design decision changes, review all existing slides against the revised lock before proceeding.
5. Compare the complete deck side by side and inspect every slide at mobile viewing scale. Check role-by-role type size, font shape/weight, baselines, line spacing, margins, colors, footer, number position, exact text and narrative continuity. A consistent prompt is not proof of consistent output. Record slide-level pass/fix in visual-review.json with reviewer and timestamp. Repair only failing slides against the same master; after two unsuccessful repair attempts keep the draft and report the defect.
6. Only then package the PDF or upload 3–5 images in manifest order. Reopen the saved Publora draft and verify the actual attachments and order. Recheck news age and corrections immediately before submission.

ImageGen's font names and pixel sizes are visual targets, not a deterministic font-rendering guarantee. Do not claim exact font metrics from a prompt or JSON check. Visible drift fails review. If exact measurable typography cannot be achieved, retain the draft and explain the limitation; do not silently change the user's ImageGen-only workflow.

## Per-slide prompt scaffold

Use case: productivity-visual / infographic-diagram as appropriate.
Asset: one portrait LinkedIn slide, not a contact sheet.
Reference: the attached accepted master is the style and layout reference.
Design lock: <identical full serialized design-lock.json>.
Text verbatim: <reviewed headline, body, source footer, NN/TOTAL>.
Illustration: <this slide's supported visual, confined to the locked illustration region>.
Invariants: preserve font family, size per text role, weight, line height, alignment, palette, margins, grid, footer and page-number placement. No autofit or extra text. Preserve the reference treatment; only the specified text and illustration content change.

## Evidence-informed inspiration

Reviewed 2026-10-12. These are useful design references, not a tested ranking or promises of virality. Their installers were not executed and their code is not vendored here.

- [nopefallacy/carousel-generator-skill](https://github.com/nopefallacy/carousel-generator-skill): uses a master visual to guide subsequent slide prompts. Adapt that anchor approach to real ImageGen calls and a mandatory inspection step; omit its marketing claims about virality.
- [mayorXBT/carousel-claude-skill](https://github.com/mayorXBT/carousel-claude-skill): separates style choices and content layouts. Use that distinction when choosing a theme across posts; retain a frozen design within each post. Its renderer is not our image-generation backend.
- [Slashgear/linkedin-carousel-gen themes](https://github.com/Slashgear/linkedin-carousel-gen/blob/main/docs/THEMES.md): supports one coherent theme per carousel. Apply that discipline to every page.
- [moihars/carousel-skill](https://github.com/moihars/carousel-skill): copy budgets and preflight help avoid shrinking text to fit. Our ImageGen and adaptive PDF/3–5-image policy take precedence over its renderer and feed-wide fixed brand defaults.

Review source changes when adopting a new technique; do not automatically install or execute upstream code during scheduled posting. Save the reference URL and concrete technique adopted in the run's design rationale.
