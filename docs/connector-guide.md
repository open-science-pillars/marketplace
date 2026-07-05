# Connector guide

MCP connectors per plugin: `.mcp.json` registers servers; CONNECTORS.md
documents them per SPECIFICATION.md v0.5.1 §3.1.

- Verify server entries against the provider's live repository AT
  AUTHORING TIME; never trust URLs from earlier drafts (the
  earthdata-mcp hosted endpoint was already stale by build day one).
- Document graceful degradation: which workflows need the connector,
  what the named fallback is (discover-data's knowledge-based fallback
  with archive URLs), and the rule that degradation is always named,
  never silent.
- Per-surface reality: Claude Code and Cowork read the plugin's
  .mcp.json; Claude Science configures connectors per session; state
  this in CONNECTORS.md.
- Credentials never appear in any repo (§5.8): Earthdata Login lives
  in ~/.netrc or connector configuration.
