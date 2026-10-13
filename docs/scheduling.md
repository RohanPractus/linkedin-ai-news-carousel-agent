# Scheduling

A skill defines the procedure; the host schedules execution. Use the [random weekly policy](random-schedule.md): 2 or 3 selected days per week, at least 48 hours between actual publications, maximum 3 weekly and 15 monthly. A daily 09:00 Chicago wake checks the persisted plan; only selected days run the publishing pipeline. Fifteen is a ceiling, not a guaranteed total. Research and review determine the actual publication time.

For Codex desktop, ask the agent to create/update the existing task, using the native automation tool and absolute local repository paths. For Hermes, attach the installed skill and run-prompt.md to a cron task using the current documented interface. Confirm timezone/DST behavior and gateway health. For Claude or other hosts, use the host's supported scheduler or an explicitly supervised external runner. Avoid duplicate schedules on multiple hosts for one account.

Start with draft mode. After explicit account-specific routine autopost authorization, change your local config accordingly. Host tool permission gates still apply. Never auto-approve all commands to make headless publishing work.

Before each external submission acquire a host/process lock or otherwise serialize the account's runner. Record occurrence and content/event hashes; reconcile unknown writes. Missed runs must perform new discovery; they may not publish stale precomputed content. No eligible event means skip, with a saved reason. Rendering, login or upload failure means retained draft plus actionable notification. Analytics failure does not become fabricated metrics.

Check older posts at comparable ages. Irregular publication runs cannot promise a precise 24-hour measurement; record actual observation age unless a separate authorized read-only measurement task exists. A stored cadence does not prove that a run executed or a post was delivered.
