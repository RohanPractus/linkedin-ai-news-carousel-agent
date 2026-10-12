# Workflow contract

## Per-run artifacts

Create a run folder under runtime/<timestamp>/. Keep discovery.json, event.json, caption.txt, slide-copy.json, image-prompts.json, numbered PNGs, manifest.json, carousel.pdf, review.md, submission.json and metrics.json. References use relative paths where possible. Event records require event_at with timezone, primary_source_urls and the concrete change. This timestamp records the original event, not a repost. If only a calendar date is known, mark precision=date and treat it conservatively; do not invent a release hour. Freshness checks are performed at publication, not merely discovery.

Discovery candidates contain original/discussion URLs, dates, observed community signals and reject reasons. Choose by fresh evidence, audience consequence and novelty; popularity does not establish accuracy. Compare against ledger event/version identifiers for duplicates.

## Writing and review

Writer explains the actual new delta before providing background. Humanizer removes filler, forced fragments and staged sincerity while preserving facts. Reviewer checks AI scope, source grounding, recency, useful implications, natural keywords and relevant tags. A clean draft needs few edits; never fabricate stylistic details. No detector score certifies authenticity.

## Slide continuity

Use a manifest with consecutive page integers, exact display labels, relative files and SHA-256 hashes. Maintain one argument across all pages. Page 1 announces a fresh event, middle pages advance evidence and limitations, final page connects the takeaway to a useful question. Preserve source dates and inference labels. Visual QA covers text, margins, mobile legibility, footer consistency and page labels. Packaging scripts cannot perform semantic or spelling review.

## External writes

Keep a local durable ledger with occurrence, content hash, event/version, asset hash, review result, status and external identifiers. Parent alone writes. Draft → prepared → pending → confirmed is conceptual state; failed and unknown are distinct. Confirmed delivery requires the platform URL/ID and published status. A scheduled record is not published; a missing record is not permission to recreate it. Resolve pending using current platform state before retrying.

Autopost scope must be explicitly granted for a specific account. Installation has no such authority. Default config is draft mode. New permissions, payments or account creation require the host's normal controls. No comments, DMs or outreach.

Latest media policy: choose a theme-specific template each run; use either a 5–7-page PDF or 3–5 images, selected by story suitability and format history. Images can display as a grid. Verify manifest/visible numbering and attachment order. Read docs/carousels.md for adaptive templates, relevant mentions/hashtags, comment-review boundaries and controller-security research lens.
