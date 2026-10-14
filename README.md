# Lab 9: Package a trusted set-up as a plugin

**Goal:** share a skill and a hook with your whole team as one installable plugin.
**Tool:** Claude Code · **Time:** 20 minutes

## Before you start

**1. Claude Code is installed.** In your terminal:
```bash
claude --version
```
Not installed? Run one of these, then open a new terminal:
- Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`
- Mac / Linux: `curl -fsSL https://claude.ai/install.sh | bash`

**2. Your Claude API key is set** in the terminal you will use:

Windows (PowerShell):
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-...your key..."
```
Mac / Linux:
```bash
export ANTHROPIC_API_KEY="sk-ant-...your key..."
```
**3. Python is installed** (the plugin's hook is a Python script).

**4. First start:** the first time you run `claude` in this folder, choose **Yes** when it asks to use your API key, and **Yes** when it asks whether you trust this folder.

> Mac / Linux: if `python` is not found, change `python` to `python3` in `team-marketplace/plugins/team-tools/hooks/hooks.json`.

## Files in this folder

| File | What it is |
|---|---|
| `orders.py`, `billing.py`, `prices.csv` | A tiny shop app to try the plugin on |
| `team-marketplace/` | A marketplace containing one plugin, `team-tools` |

```text
team-marketplace/
├── .claude-plugin/
│   └── marketplace.json        ← the catalogue (lists the plugins)
└── plugins/
    └── team-tools/
        ├── .claude-plugin/
        │   └── plugin.json     ← the manifest (name, version)
        ├── skills/
        │   └── review/SKILL.md ← a review skill (runs in a fork)
        ├── hooks/
        │   └── hooks.json      ← blocks edits to prices.csv
        └── scripts/
            └── protect_files.py
```
Rules to remember:
- Only `plugin.json` goes inside `.claude-plugin/`. Skills and hooks sit at the plugin's root.
- The `name` in `plugin.json` (`team-tools`) becomes the prefix: `/team-tools:review`.
- `hooks.json` uses `${CLAUDE_PLUGIN_ROOT}`, so the script is found wherever the plugin is installed.

## Steps

### Step 1: Look inside

Open these three files and read them. They are short:
- `team-marketplace/plugins/team-tools/.claude-plugin/plugin.json`
- `team-marketplace/plugins/team-tools/skills/review/SKILL.md`
- `team-marketplace/.claude-plugin/marketplace.json`

### Step 2: Validate

In your terminal:
```bash
cd lab09-plugin
claude plugin validate ./team-marketplace
claude plugin validate ./team-marketplace/plugins/team-tools
```
✅ `Validation passed` for both.

### Step 3: Try the plugin without installing it

```bash
claude --plugin-dir ./team-marketplace/plugins/team-tools
```
In Claude Code:
```text
/team-tools:review billing.py
```
✅ A short review (no check on `percent`, floats, and so on). It comes from the plugin's skill.

Switch to **accept edits** with `Shift+Tab` and ask:
```text
Change the Pen price in prices.csv to 150.
```
✅ Blocked by the plugin's hook. Type `/exit`.

### Step 4: Install it from the marketplace

In your terminal:
```bash
claude plugin marketplace add ./team-marketplace
claude plugin install team-tools@team-marketplace
claude plugin list
```
✅ `team-tools@team-marketplace` is installed. Start `claude` in any folder: `/team-tools:review` is available.

To share it with your team, put `team-marketplace` in a git repository. Each person then runs `claude plugin marketplace add <owner>/<repo>` and installs it the same way.

## What you learned
- A plugin bundles skills, hooks and more, with a `plugin.json` manifest.
- A marketplace lists plugins, so a team can install the same tested set-up.
- Use `claude plugin validate` to check it, `--plugin-dir` to test it, and `install` to use it.

## Clean up
```bash
claude plugin uninstall team-tools@team-marketplace
claude plugin marketplace remove team-marketplace
```
