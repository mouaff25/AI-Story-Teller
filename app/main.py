from app.story_designer import LlamaStoryTeller
from fastapi import FastAPI
import uvicorn

story_teller = LlamaStoryTeller()

story_teller.load_llm()

app = FastAPI()

@app.post("/brainstorming")
async def brainstorming(prompt: str):
    return story_teller.brainstorm(prompt)

@app.post("/idea_choice")
async def idea_choice(story_topic: str, ideas: str):
    return story_teller.choose_idea(story_topic=story_topic, ideas=ideas)

@app.post("/events_outline")
async def events_outline(story_topic: str, story_idea: str):
    return story_teller.outline_sequence_of_events(story_topic=story_topic, idea=story_idea)

@app.post("/characters_designer")
async def characters_designer(story_topic: str, events_outline: str):
    return story_teller.design_characters(story_topic=story_topic, events_outline=events_outline)

@app.post("/introduction_planner")
async def introduction_planner(events_outline: str):
    return story_teller.plan_introduction(events_outline=events_outline)

if __name__ == "__main__":
    uvicorn.run(app)
