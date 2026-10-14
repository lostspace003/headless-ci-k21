import json
import sys

event = json.load(sys.stdin)                      # Claude Code sends the tool call as JSON
path = event.get("tool_input", {}).get("file_path", "")

if path.endswith("prices.csv"):
    print("Blocked: prices.csv is managed by the finance team. Do not edit it.", file=sys.stderr)
    sys.exit(2)                                    # 2 = block the action

sys.exit(0)                                        # 0 = no objection
