from app.story_designer import LlamaStoryTeller

story_teller = LlamaStoryTeller()

print("Loading llm...")
story_teller.load_llm()

print("Finished loading llm.")


while True:
    input_text = input("Enter the topic of the story: ")
    if input_text == "exit":
        break
    ideas = story_teller.brainstorm(input_text)
    idea = story_teller.choose_idea(input_text, ideas)
    idea = input("Enter idea: ")
    sequence_of_events = story_teller.outline_sequence_of_events(input_text, idea)
    characters = story_teller.design_characters(input_text, sequence_of_events)
