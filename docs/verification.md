# Verification status

As of October 12, 2026:

- Five slides were generated using Codex's built-in ImageGen and visually checked for wording, labels, legibility and narrative order.
- The source PNGs were packaged as one five-page PDF. Embedded PDF images matched the ordered PNGs pixel-for-pixel.
- The separate humanizer regression retained factual/hypothetical qualifiers and passed its specified checks.
- The active Codex schedule was configured for fresh-only AI developments and ImageGen PDF carousels.
- Local helper scripts have offline tests for freshness boundaries and ordering/hashes, and the included real PDF is verified.
- The five-page PDF was uploaded into a Publora draft with the LinkedIn channel and reviewed caption. The saved document attachment persisted on reopening. No claim of confirmed LinkedIn publication is made here.
- Claude, Hermes and other hosts have setup guides based on official documentation; their live image/auth/scheduling integrations have not been executed in this repository.

The sample is historical public-source content, not a live feed or performance benchmark. No analytics-derived reach gain is established.

The latest workflow varies templates by theme and supports PDF or 3–5-image delivery. Offline tests pass for freshness boundaries, missing evidence and ordering/hash failures. The existing five-page example passed pixel/order verification.

GitHub Actions is provided as examples/ci-workflow.yml, not enabled. The existing GitHub OAuth credential lacked workflow scope; the example was kept outside .github/workflows so repository publishing required no broader credential access. Local checks passed.
