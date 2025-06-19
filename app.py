
import streamlit as st
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("✨ Interactive Storyteller")
st.write("Choose your path and let the story unfold...")

# Initialize session state
if "story" not in st.session_state:
    st.session_state.story = "Once upon a time in a glowing forest..."

# User input
user_input = st.text_input("What happens next?")

if st.button("Continue the story"):
    prompt = f"""{st.session_state.story}\n\nUser: {user_input}\nStoryteller:"""  # Use triple quotes for multiline f-string
    response = openai.Completion.create(
        engine="text-davinci-003",  # or "gpt-3.5-turbo" with Chat API
        prompt=prompt,
        max_tokens=150,
        temperature=0.8,
        stop=["User:"]
    )
    new_text = response.choices[0].text.strip()
    st.session_state.story += f"\n\nYou: {user_input}\n{new_text}"

st.markdown("### 📖 Your Story So Far")
st.write(st.session_state.story)
