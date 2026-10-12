# Scheduling

A skill defines the procedure; the host schedules its execution. The reference cadence is Tuesday and Thursday at 09:00 America/Chicago (about 104 occurrences/year). The 180-domain inventory is not a commitment to 180 posts. Research starts at the scheduled time; publishing follows completed review and media generation, so exact 09:00 publication is not guaranteed.

For Codex desktop, ask the agent to create/update the existing task, using the native automation tool and absolute local repository paths. For Hermes, attach the installed skill and run-prompt.md to a cron task using the current documented interface. Confirm timezone/DST behavior and gateway health. For Claude or other hosts, use the host's supported scheduler or an explicitly supervised external runner. Avoid duplicate schedules on multiple hosts for one account.

Start with draft mode. After explicit account-specific routine autopost authorization, change your local config accordingly. Host tool permission gates still apply. Never auto-approve all commands to make headless publishing work.

Before each external submission acquire a host/process lock or otherwise serialize the account's runner. Record occurrence and content/event hashes; reconcile unknown writes. Missed runs must perform new discovery; they may not publish stale precomputed content. No eligible event means skip, with a saved reason. Rendering, login or upload failure means retained draft plus actionable notification. Analytics failure does not become fabricated metrics.

Check older posts at comparable ages. Twice-weekly runs cannot promise a precise 24-hour measurement; record actual observation age unless a separate authorized read-only measurement task exists. A stored cadence does not prove that a run executed or a post was delivered.
