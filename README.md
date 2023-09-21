# AI Story Teller

Unleash Creativity with AI-Powered Storytelling. Craft captivating stories from basic prompts, enriched with compelling narratives and vivid imagery. Embark on limitless literary journeys and nurture a passion for storytelling and imagination. 📖✨🌟

## Inspiration

This project was inspired by the [AI Dungeon](https://play.aidungeon.io/) game, which is a text-based adventure game that uses the OpenAI GPT-3 API to generate a story based on the user's input. The game is a lot of fun to play, but it is limited to a single-player experience. I wanted to create a multiplayer version of the game, where multiple users can collaborate to create a story together. I also wanted to add a few more features to the game, such as the ability to save and load stories, and the ability to generate a story from a prompt.

## What it does

The AI Story Teller is an API that allows users to create stories together. The API has several endpoints that allow users to brainstorm story ideas, choose a story idea, write the events outline of a story, generate characters' designs (appearance, personality, etc.), and plan introductions.

## How I built it

I built the API using Python and Flask. I used Meta's Llama 2 chat 7b as the base large language model for the API.

## Getting started

### Prerequisites

- Python 3.10
- Pip

### Installation

1. Clone the repo

    ```sh
   git clone https://github.com/mouaff25/AI-story-teller.git
    ```

2. Install dependencies

   ```sh
    pip install -r requirements.txt
    ```

3. Run the app

    ```sh
     python -m app.main
     ```

## Usage

You can use Swagger to test the API. Go to `http://localhost:8000/docs` to access the Swagger UI.
