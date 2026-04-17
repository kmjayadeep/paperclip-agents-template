# TOOLS.md

## Tool Priority (use in this order)

1. **`paperclip` skill** → control-plane API operations, auth, routing, checkout, status updates
2. **`para-memory-files` skill** → memory operations. Let the skill choose the correct recall/write method and paths.
3. **raw `curl`** → only when a skill is unavailable or explicitly instructed as fallback
