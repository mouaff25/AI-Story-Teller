from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Base settings class"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App settings
    APP_NAME: str = "My App"
    APP_DESCRIPTION: str = "My App Description"
    APP_VERSION: str = "0.0.1"
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    APP_DOCS_URL: str = "/docs"
    APP_REDOC_URL: str = "/redoc"
    APP_OPENAPI_URL: str = "/openapi.json"
    APP_DEBUG: bool = False

    # llm settings
    STORY_DESIGNER_MODEL_FILENAME: str = "llama-2-13b-chat.ggmlv3.q3_K_L.bin"
    LLM_MODEL_DIR: str = "./llms"
    STORY_DESIGNER_REPO_ID: str = "TheBloke/Llama-2-13B-chat-GGML"
    STORY_DESIGNER_STOP: list = []
    STORY_DESIGNER_TEMPERATURE: float = 0
    STORY_DESIGNER_REPEAT_PENALTY: float = 1.1
    STORY_DESIGNER_VERBOSE: bool = False
    STORY_DESIGNER_N_CTX: int = 4096
    STORY_DESIGNER_N_GPU_LAYERS: int = 50
    STORY_DESIGNER_N_BATCH: int = 512
    STORY_DESIGNER_MAX_TOKENS: int = 2048
    STORY_DESIGNER_PROMPT_PATH: str = "./app/prompts/llama2.yaml"
    STORY_DESIGNER_BRAINSTORMING_PROMPT_PATH: str = "./app/prompts/llama2-brainstorming.yaml"
    STORY_DESIGNER_IDEA_CHOICE_PROMPT_PATH: str = "./app/prompts/llama2-idea-choice.yaml"
    STORY_DESIGNER_EVENTS_OUTLINE_PROMPT_PATH: str = "./app/prompts/llama2-events-outline.yaml"
    STORY_DESIGNER_CHARACTERS_DESIGNER_PROMPT_PATH: str = "./app/prompts/llama2-characters-designer.yaml"
    STORY_DESIGNER_INTRODUCTION_PLANNER_PROMPT_PATH: str = "./app/prompts/llama2-introduction-planner.yaml"
    STORY_DESIGNER_INTRODUCTION_WRITER_PROMPT_PATH: str = "./app/prompts/llama2-introduction-writer.yaml"
    STORY_WRITER_REPO_ID: str = "TheBloke/MPT-7B-Storywriter-GGML"
    STORY_WRITER_MODEL_FILENAME: str = "mpt-7b-storywriter.ggmlv3.fp16.bin"
    STORY_WRITER_MAX_NEW_TOKENS: int = 65000
    STORY_WRITER_GPU_LAYERS: int = 50
    STORY_WRITER_BATCH_SIZE: int = 128
    STORY_WRITER_REPETITION_PENALTY: float = 1.1
    STORY_WRITER_TEMPERATURE: float = 0.5
    STORY_WRITER_STOP: list = ["\n\n\n\n\n"]
    STORY_WRITER_VERBOSE: bool = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
