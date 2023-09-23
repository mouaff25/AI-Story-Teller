from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional


class Settings(BaseSettings):
    """Base settings class"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App settings
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    APP_DOCS_URL: Optional[str] = "/docs"
    APP_REDOC_URL: Optional[str] = "/redoc"
    APP_OPENAPI_URL: Optional[str] = "/openapi.json"
    APP_DEBUG: bool = False

    # llm settings
    STORY_DESIGNER_MODEL_FILENAME: str = "llama-2-7b-chat.ggmlv3.q2_K.bin"
    STORY_DESIGNER_REPO_ID: str = "TheBloke/Llama-2-7B-Chat-GGML"
    STORY_DESIGNER_STOP: List[str] = ["\n###"]
    STORY_DESIGNER_TEMPERATURE: float = 0
    STORY_DESIGNER_REPEAT_PENALTY: float = 1.1
    STORY_DESIGNER_VERBOSE: bool = False
    STORY_DESIGNER_N_CTX: int = 4096
    STORY_DESIGNER_N_GPU_LAYERS: int = 20
    STORY_DESIGNER_N_BATCH: int = 128
    STORY_DESIGNER_MAX_TOKENS: int = 2048
    STORY_DESIGNER_PROMPT_PATH: str = "./app/prompts/llama2.yaml"
    STORY_DESIGNER_BRAINSTORMING_PROMPT_PATH: str = "./app/prompts/llama2-brainstorming.yaml"
    STORY_DESIGNER_IDEA_CHOICE_PROMPT_PATH: str = "./app/prompts/llama2-idea-choice.yaml"
    STORY_DESIGNER_EVENTS_OUTLINE_PROMPT_PATH: str = "./app/prompts/llama2-events-outline.yaml"
    STORY_DESIGNER_CHARACTERS_DESIGNER_PROMPT_PATH: str = "./app/prompts/llama2-characters-designer.yaml"
    STORY_DESIGNER_INTRODUCTION_PLANNER_PROMPT_PATH: str = "./app/prompts/llama2-introduction-planner.yaml"
    STORY_DESIGNER_INTRODUCTION_WRITER_PROMPT_PATH: str = "./app/prompts/llama2-introduction-writer.yaml"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
