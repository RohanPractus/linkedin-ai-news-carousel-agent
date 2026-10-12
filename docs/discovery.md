# Live discovery and freshness

At each actual run, scan accessible public Hacker News threads, r/LocalLLaMA, r/MachineLearning, Hugging Face community/Papers and relevant GitHub releases. These are lead sources. Verify the original paper/model card/release/announcement before drafting. Scan more than one accessible community surface where practical and log blocked sources honestly.

Select a substantive change in models, agents, multimodal AI, inference economics, infrastructure, robotics or AI-related industry workflows. Prefer the last 72 hours; 96 hours is a hard upper bound. News about an older release, reposts and an updated roundup do not reset its age. Unknown/future event dates fail. With calendar-date-only evidence, use the beginning of that source date conservatively for the gate and declare the precision; a boundary item may be rejected.

A new research paper establishes a research result, not market adoption. A vendor benchmark remains attributed and limited to its reported setup. Describe availability and limitations, not just headline claims. The draft must state what changed and the concrete audience consequence. Recheck for corrections and age immediately before publication after image generation finishes. If the story expires, retain the draft and choose a new event on the next run.

Run the helper on an event record:

```bash
python scripts/check_freshness.py runtime/run/event.json --now 2026-10-12T10:00:00Z
```

The `--now` flag is for reproducible tests; production defaults to actual UTC now. It does not grant permission to falsify freshness. The helper trusts input facts and URLs; the agent must verify them independently.
