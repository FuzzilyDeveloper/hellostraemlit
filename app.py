
import streamlit as st
import openai
import os

# Initialize OpenAI client with API key from environment variable
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.title("✨ Interactive Storyteller")
st.write("Choose your path and let the story unfold...")

# Initialize session state
if "story" not in st.session_state:
    st.session_state.story = "Once upon a time in a glowing forest..."

# User input
user_input = st.text_input("What happens next?")

if st.button("Continue the story"):
    prompt = f"""You are a creative storyteller. Continue the story based on the user's input.
Story so far: {st.session_state.story}
User input: {user_input}
Storyteller:"""  # Fixed multiline f-string
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.8,
        stop=["User:"]
    )
    new_text = response.choices[0].message.content.strip()
    st.session_state.story += f"\n\nYou: {user_input}\n{new_text}"

st.markdown("### 📖 Your Story So Far")
st.write(st.session_state.story)
