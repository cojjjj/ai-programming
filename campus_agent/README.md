# Campus Resource Assistant

Lab 3 adds a Streamlit conversation interface to the Lab 2 Google ADK agent.
The directory currently contains four campus resources. Additional discussion-board
resources must be added to `campus_resources.json` before final submission.

## Local use

From the repository root, with your Python environment active:

```bash
pip install -r requirements.txt
streamlit run campus_agent/app.py
```

Keep your local key in `campus_agent/.env` as `GOOGLE_API_KEY=your-key`.
Never commit that file or `.streamlit/secrets.toml`.

## Streamlit Community Cloud

Select repository `cojjjj/ai-programming`, branch `main`, and entry point
`campus_agent/app.py`. Use Python 3.11 or later. Add this in the app's
Advanced settings or Secrets panel, replacing the placeholder privately:

```toml
GOOGLE_API_KEY = "your-key"
```

Live app URL: pending deployment and testing.

## Behavior and verification

The UI keeps messages, the runner, and the ADK session in `st.session_state`.
Session creation is awaited before the first message. Clear Conversation
resets both displayed messages and the ADK session service. Memory lasts only
for the browser session, and is not saved to a database.

Before submission, test a resource question and a follow-up locally and in
the deployed app. Capture both conversations. Confirm Clear Conversation
starts a fresh conversation. Check that your configured Gemini model is
available to your API key. The Lab 2 model setting is preserved in `agent.py`.

## Files

- `agent.py`: agent definition and resource lookup tool
- `app.py`: Streamlit interface and ADK integration
- `campus_resources.json`: resource records and verification metadata
- `requirements.txt`: reference to root deployment dependencies
- `../.streamlit/config.toml`: theme and server configuration

## References

- https://google.github.io/adk-docs/sessions/session/
- https://docs.streamlit.io/develop/concepts/connections/secrets-management

## Author

Tyler Deppa — AI Programming
