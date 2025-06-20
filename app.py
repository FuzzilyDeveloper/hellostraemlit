
# Interactive Storytelling App for Google Colab and Streamlit
# Save as `app.py` for GitHub and Streamlit deployment

import sys
try:
    import streamlit as st
except ImportError:
    st = None  # Streamlit not available in Colab

# Define the story structure as a dictionary
story = {
    "start": {
        "text": "You stand at a crossroad in Eldoria, the air thick with mystery. A dark forest looms to the left, a mountain path rises to the right, and a village glows ahead.",
        "choices": {
            "1": {"text": "Enter the dark forest", "next_scene": "forest"},
            "2": {"text": "Take the mountain path", "next_scene": "mountain"},
            "3": {"text": "Visit the village", "next_scene": "village"}
        }
    },
    "forest": {
        "text": "The forest is dense, and a low growl echoes nearby. A wolf steps into view, its eyes glinting.",
        "choices": {
            "1": {"text": "Fight the wolf", "next_scene": "fight_wolf"},
            "2": {"text": "Flee back to the crossroad", "next_scene": "start"}
        }
    },
    "mountain": {
        "text": "The mountain path is steep, and you find an ancient cave with glowing runes.",
        "choices": {
            "1": {"text": "Enter the cave", "next_scene": "cave"},
            "2": {"text": "Return to the crossroad", "next_scene": "start"}
        }
    },
    "village": {
        "text": "The village is bustling, and a wise elder offers you a magical amulet.",
        "choices": {
            "1": {"text": "Accept the amulet", "next_scene": "amulet"},
            "2": {"text": "Decline and leave", "next_scene": "start"}
        }
    },
    "fight_wolf": {
        "text": "You defeat the wolf and find a glowing amulet in its lair. The amulet hums with power, ending your journey.",
        "choices": {}  # End of story
    },
    "cave": {
        "text": "Inside the cave, you discover a treasure chest guarded by a riddle. You solve it and claim the treasure, ending your quest.",
        "choices": {}  # End of story
    },
    "amulet": {
        "text": "The amulet grants you visions of Eldoria’s future, concluding your adventure with wisdom.",
        "choices": {}  # End of story
    }
}

def run_colab():
    """Run the interactive story in Google Colab."""
    current_scene = "start"
    while True:
        scene = story[current_scene]
        print("\n" + scene["text"] + "\n")
        
        if not scene["choices"]:
            print("The end.")
            break
        for key, choice in scene["choices"].items():
            print(f"{key}. {choice['text']}")
        
        choice = input("\nEnter your choice (number): ").strip()
        if choice in scene["choices"]:
            current_scene = scene["choices"][choice]["next_scene"]
        else:
            print("Invalid choice. Please select a valid option (e.g., 1, 2, 3).")

def run_streamlit():
    """Run the interactive story in Streamlit."""
    if not st:
        print("Streamlit not available. Run this in a Streamlit environment.")
        return
    
    st.title("Interactive Storytelling Adventure in Eldoria")
    st.markdown("Choose your path to continue the adventure!")
    
    # Initialize session state
    if 'current_scene' not in st.session_state:
        st.session_state.current_scene = "start"
    
    current_scene = st.session_state.current_scene
    scene = story[current_scene]
    
    # Display current scene
    st.write("### Current Scene")
    st.write(scene["text"])
    
    # Display choices
    if scene["choices"]:
        st.write("### Your Choices")
        choice_options = [f"{key}. {choice['text']}" for key, choice in scene["choices"].items()]
        selected_option = st.selectbox("Choose your action:", choice_options, key="choice_select")
        
        if st.button("Submit"):
            choice_key = selected_option.split(".")[0]
            if choice_key in scene["choices"]:
                st.session_state.current_scene = scene["choices"][choice_key]["next_scene"]
                st.rerun()
            else:
                st.error("Invalid choice. Please select a valid option.")
    else:
        st.write("### The End")
        if st.button("Restart"):
            st.session_state.current_scene = "start"
            st.rerun()

if __name__ == "__main__":
    if "streamlit" in sys.modules:
        run_streamlit()
    else:
        print("Starting Interactive Storytelling App...")
        run_colab()
