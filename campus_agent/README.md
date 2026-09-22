# Campus Resource Assistant

Agent Lab Part 2 project for SUNY Jamestown Community College.

## Files
- `agent.py` — instructor-supplied ADK agent/tool code
- `campus_resources.json` — verified campus resource data
- `DESIGN_NOTES.md` — design worksheet, research table, sources, and workflow diagram
- `__init__.py` — makes the agent discoverable by ADK
- `.gitignore` — prevents `.env` from being committed
- `.env.example` — safe template only; do not put a real API key in GitHub

## Run from the parent `ai-programming` folder

```bash
conda activate ai-agents
pip install google-adk
adk run campus_agent
```

For the web interface:

```bash
adk web
```

Never commit the real `.env` file.
