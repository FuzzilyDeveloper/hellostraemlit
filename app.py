
# Interactive Storytelling App for Google Colab (Static, No API)
# Save as `app.py` for GitHub

def run_story():
    """Run the interactive story in Google Colab."""
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

    current_scene = "start"
    while True:
        # Display current scene
        scene = story[current_scene]
        print("\n" + scene["text"] + "\n")
        
        # Display choices
        if not scene["choices"]:
            print("The end.")
            break
        for key, choice in scene["choices"].items():
            print(f"{key}. {choice['text']}")
        
        # Get user input
        choice = input("\nEnter your choice (number): ").strip()
        if choice in scene["choices"]:
            current_scene = scene["choices"][choice]["next_scene"]
        else:
            print("Invalid choice. Please select a valid option (e.g., 1, 2, 3).")

if __name__ == "__main__":
    print("Starting Interactive Storytelling App...")
    run_story()
