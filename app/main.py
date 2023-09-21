from app.story_designer import LlamaStoryTeller
from fastapi import FastAPI
import uvicorn
from app import __version__
from app.config.settings import get_settings

app_settings = get_settings()

story_teller = LlamaStoryTeller()

story_teller.load_llm()

app = FastAPI(
    title="AI Story Teller",
    description="Unleash Creativity with AI-Powered Storytelling. Craft captivating stories from basic prompts, enriched with compelling narratives and vivid imagery. Embark on limitless literary journeys and nurture a passion for storytelling and imagination. 📖✨🌟",
    version=__version__,
    docs_url=app_settings.APP_DOCS_URL,
    redoc_url=app_settings.APP_REDOC_URL,
    openapi_url=app_settings.APP_OPENAPI_URL,
    debug=app_settings.APP_DEBUG
)

@app.post(
        "/brainstorming",
        summary="Brainstorming",
        description="""This endpoint is used to brainstorm ideas for a story.

The input text should be a prompt that describes the story topic. The output is a list of 5 creative ideas for the story.""",
    )
async def brainstorming(prompt: str):
    return story_teller.brainstorm(prompt)


@app.post(
        "/idea_choice",
        summary="Idea Choice",
        description="""This endpoint is used to choose one of the ideas for a story.
        
The input text should be a prompt that describes the story topic and the list of ideas. The output is an idea choice.""",)
async def idea_choice(story_topic: str, ideas: str):
    return story_teller.choose_idea(story_topic=story_topic, ideas=ideas)

@app.post(
        "/events_outline",

        summary="Events Outline",
        description="""This endpoint is used to outline the sequence of events for a story.
        
The input text should be a prompt that describes the story topic and the idea. The output is a sequence of events.""",)
async def events_outline(story_topic: str, story_idea: str):
    return story_teller.outline_sequence_of_events(story_topic=story_topic, idea=story_idea)

@app.post(
        "/characters_designer",
        summary="Characters Designer",
        description="""This endpoint is used to design the characters for a story.
        
        The input text should be a prompt that describes the story topic and the sequence of events. The output is a list of characters with a detailed description of their appearance, personality and relationships with each other.""",)
async def characters_designer(story_topic: str, events_outline: str):
    return story_teller.design_characters(story_topic=story_topic, events_outline=events_outline)

@app.post(
        "/introduction_planner",
        summary="Introduction Planner",
        description="""This endpoint is used to plan the introduction for a story.
        
        The input text should be a prompt that describes the sequence of events. The output is a plan for the introduction.""",)
async def introduction_planner(events_outline: str):
    return story_teller.plan_introduction(events_outline=events_outline)

if __name__ == "__main__":
    uvicorn.run(app, host=app_settings.APP_HOST, port=app_settings.APP_PORT)
