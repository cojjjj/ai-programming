"""Streamlit interface for the Lab 2 campus resource agent."""
import asyncio
import os
import re
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google.adk.artifacts import InMemoryArtifactService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

st.set_page_config(page_title="Campus Resource Assistant", page_icon="🏛️", layout="centered")

# Cloud secrets take priority; the ignored .env supports local development.
try:
    cloud_key = st.secrets.get("GOOGLE_API_KEY", "")
except (FileNotFoundError, KeyError):
    cloud_key = ""
if cloud_key:
    os.environ["GOOGLE_API_KEY"] = cloud_key
else:
    load_dotenv(Path(__file__).parent / ".env")

st.title("Campus Resource Assistant")
st.write("Find campus services, locations, hours, and contact information.")
if not os.environ.get("GOOGLE_API_KEY"):
    st.error("Add GOOGLE_API_KEY to Streamlit secrets, or to your local campus_agent/.env file.")
    st.stop()

# Import after loading credentials so the agent sees the configuration.
from agent import root_agent, RESOURCE_FILE

APP_NAME = "campus_resource_agent"
USER_ID = "student_user"


def get_runner():
    """Keep the runner and its session service across UI reruns."""
    if "runner" not in st.session_state:
        service = InMemorySessionService()
        st.session_state.session_service = service
        st.session_state.runner = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=service,
            artifact_service=InMemoryArtifactService(),
        )
    return st.session_state.runner


async def call_agent(prompt):
    runner = get_runner()
    if "session_id" not in st.session_state:
        session = await st.session_state.session_service.create_session(
            app_name=APP_NAME, user_id=USER_ID
        )
        st.session_state.session_id = session.id
    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    answer = []
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=st.session_state.session_id,
        new_message=message,
    ):
        if event.is_final_response() and event.content:
            answer.extend(part.text for part in event.content.parts or []
                          if part.text and not part.thought)
    return "".join(answer) or "I could not generate an answer. Please try again."


if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("About")
    st.write("Ask about the library, tutoring, advising, financial aid, or other resources in the campus directory.")
    st.caption(f"Data source: {RESOURCE_FILE.name}")
    st.write('Try asking: "Where is the library?" Then: "What is its phone number?"')
    if st.button("Clear Conversation"):
        # Discard the service as well as the UI history for a fresh conversation.
        for key in ("messages", "session_id", "runner", "session_service"):
            st.session_state.pop(key, None)
        st.rerun()

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.write("Hello! I can help you find campus resources. What would you like to know?")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about campus resources..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                response = asyncio.run(call_agent(prompt))
        except Exception as exc:
            response = "The assistant could not connect. Please retry, or check the API configuration and quota."
            # Temporary local diagnostics: mask credentials before display.
            detail = str(exc)
            key = os.environ.get("GOOGLE_API_KEY", "")
            if key:
                detail = detail.replace(key, "[REDACTED]")
            detail = re.sub(r"AIza[0-9A-Za-z_-]+", "[REDACTED]", detail)
            with st.expander("Connection error details"):
                st.code(f"{type(exc).__name__}: {detail}")
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
