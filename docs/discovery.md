# Live discovery and freshness

At each actual run, scan accessible public Hacker News threads, r/LocalLLaMA, r/MachineLearning, Hugging Face community/Papers and relevant GitHub releases. These are lead sources. Verify the original paper/model card/release/announcement before drafting. Scan more than one accessible community surface where practical and log blocked sources honestly.

Select a substantive change in models, agents, multimodal AI, inference economics, infrastructure, robotics or AI-related industry workflows. Prefer the last 72 hours; 96 hours is a hard upper bound. News about an older release, reposts and an updated roundup do not reset its age. Unknown/future event dates fail. With calendar-date-only evidence, use the beginning of that source date conservatively for the gate and declare the precision; a boundary item may be rejected.

A new research paper establishes a research result, not market adoption. A vendor benchmark remains attributed and limited to its reported setup. Describe availability and limitations, not just headline claims. The draft must state what changed and the concrete audience consequence. Recheck for corrections and age immediately before publication after image generation finishes. If the story expires, retain the draft and choose a new event on the next run.

Run the helper on an event record:

```bash
python scripts/check_freshness.py runtime/run/event.json --now 2026-10-12T10:00:00Z
```

The `--now` flag is for reproducible tests; production defaults to actual UTC now. It does not grant permission to falsify freshness. The helper trusts input facts and URLs; the agent must verify them independently.

## Discovery quality and novelty review

At execution time, search at least two accessible lead surfaces where possible and original release channels. Use date-bounded queries for the actual preceding 96 hours, then open each selected primary source; search snippets and a fresh discussion timestamp are insufficient. Record inaccessible sources instead of claiming coverage. Target three candidate events when available; fewer is acceptable if documented, and no eligible event means skip.

For each candidate save: original event timestamp and precision, first announcement/release URL, release/version identifier, discussion URL/time, concrete before→after change, availability, affected AI audience, caveats, corrections checked_at, and rejected/selected reason. Deduplicate by event/version against the ledger, not headline phrasing. A follow-up to an older release qualifies only if it contains its own substantive new dated change.

Select on verified novelty, practical impact and explainability. Votes and comments are leads, never factual verification. Seek independent technical corroboration where accessible; if only the vendor establishes the claim, label it explicitly and narrow the claim. Keep research results separate from production availability and adoption. Save a claim-to-source map for every number, benchmark and capability mentioned in the caption or images.

After humanization compare names, dates, numbers, qualifiers and source attribution against that map. After image generation, rerun the hard 96-hour freshness gate and check the original source for corrections. If the event expires or a material claim fails, do not publish the prepared asset. Reuse neither a stale headline nor a cached draft to fill a schedule slot.
