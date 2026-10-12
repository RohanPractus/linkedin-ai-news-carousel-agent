# Setup across agent hosts

Documentation checked October 12, 2026. Host capabilities and commands change; follow official linked docs for authentication and version-specific flags. The compatibility matrix describes requirements, not a claim that every host was tested.

| Host | Skill loading | Images | Scheduling | Status |
|---|---|---|---|---|
| Codex desktop | Copy skill to local skills directory or read it explicitly | Built-in ImageGen when exposed | Native scheduled task | Preparation/media workflow tested |
| Claude Code | `.claude/skills/<name>/SKILL.md` | Explicit image MCP/API needed | Available host scheduler or supervised external runner | Documented, not live-tested |
| Claude Desktop/Cowork | Supported skill upload or explicit instructions | Connected image tool needed | Version-dependent host capability | Capability-dependent |
| Hermes | Agent Skills installation | Configured image tool/API needed | Hermes cron/gateway | Documented, not live-tested |
| Cursor/other MCP agents | Supported Agent Skills or explicit instruction files | Configured image tool | Host scheduler/external runner | Capability-dependent |
| Agents without tools | Can draft text | Cannot create actual slides | Cannot publish | Draft assistance only |

## Codex

Copy `skills/linkedin-ai-news-carousel/` into your configured Codex skills directory (commonly `~/.codex/skills/`) or ask Codex to read the repository skill explicitly. Do not replace existing skills silently. Configure Publora with the current official client setup; a CLI path is:

```bash
codex mcp add publora --url https://mcp.publora.com/mcp
```

Complete the authorized sign-in flow. Confirm `list_connections` and create one draft/document upload before scheduling. Ask the desktop agent to create or update its scheduled task using run-prompt.md and your absolute repository/config path. Refer to official [skills](https://learn.chatgpt.com/docs/build-skills) and [scheduled tasks](https://learn.chatgpt.com/docs/automations). Keep the required execution environment available. Do not treat CLI setup as an automatic desktop connection guarantee.

## Claude Code

```bash
mkdir -p .claude/skills
cp -R skills/linkedin-ai-news-carousel .claude/skills/
claude mcp add --transport http publora https://mcp.publora.com/mcp
```

Use `/mcp` to authenticate according to the provider's current flow. Invoke `/linkedin-ai-news-carousel` with draft-only instructions. Configure an image tool separately: installing this skill does not expose Codex ImageGen to Claude. Use [Claude skills](https://code.claude.com/docs/en/skills) and [MCP](https://code.claude.com/docs/en/mcp). Desktop/Cowork skill import is product/version-specific; use supported import rather than assuming Code's directory works everywhere.

## Hermes

```bash
hermes skills install roronoa2003/linkedin-ai-news-carousel-agent/skills/linkedin-ai-news-carousel
```

Review the installation scan; do not bypass a dangerous verdict. Confirm the skill appears in the installed list. Configure Publora using the current [Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp); transport/auth support must be checked for your version. If remote OAuth is unsupported, use the documented API-key route through a supported secret store instead of copying browser tokens. Configure image generation explicitly. Read [skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) and [cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron), then ask Hermes to create a task from run-prompt.md with your desired timezone. Ensure the gateway/scheduler is running and verify `hermes cron status`.

## Other platforms

Read the same SKILL.md and reference file. Wire equivalent capabilities: real web search/page retrieval, filesystem, image generation, Publora MCP or documented REST, durable ledger, scheduling and user approvals. A model-only API has no browsing/images/publishing by default. Agent frameworks need explicit tool implementations and credentials; this repository does not supply universal adapters. If separate agents are unsupported, use sequential passes. Test draft creation and media attachment before enabling autopost. Do not claim portability means identical permission or execution behavior.
