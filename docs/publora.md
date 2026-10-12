# Publora delivery

Connect your own LinkedIn account through Publora and authorize the host's MCP connection. Current server URL: https://mcp.publora.com/mcp. Read https://docs.publora.com/mcp/client-setup for current authentication. Do not copy another user's tokens or IDs.

1. Call `list_connections`, check display name/platform and copy the platform ID verbatim.
2. Reconcile the local occurrence ledger and existing drafts/posts before creating a new record.
3. Call `create_post` with caption and configured platform ID, omitting `scheduledTime` for a draft. Omission does **not** publish.
4. Upload the actual PDF via current documented upload tools (`get_upload_url`, PUT, `complete_media`) or a host-supported browser file chooser. Inspect tool schema for PDF-specific fields instead of inferring them from an image example. A public URL route is usable only when a real authorized public file exists.
5. Verify the saved draft caption, LinkedIn channel and PDF attachment. For browser upload, reload after save completes to confirm persistence.
6. Keep draft mode until the user approves or explicitly authorizes ongoing routine publishing. For an authorized submission, recheck freshness, corrections, caption and media; save pending before writing. Use the current API's scheduling semantics, not an assumption that null scheduledTime publishes immediately.
7. Confirm actual published status and LinkedIn URL/ID. Inspect LinkedIn when needed. An API acknowledgement or scheduled status alone is incomplete evidence.

The free/paid plan and media capabilities may change. Check current account limits. Missing upload permissions are a blocker; alternative routes must not bypass a denial. A published post may require deletion on LinkedIn itself; deleting a Publora record is not proof of removing a public post.

The repository includes no publisher executable or secrets. The agent calls real tools. REST API keys and MCP OAuth are different paths; consult current documentation rather than reusing an OAuth token as an API key.
