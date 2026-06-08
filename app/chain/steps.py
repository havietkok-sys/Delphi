from pydantic import BaseModel
from .runnable import Runnable

class PromptInput(BaseModel):
	question: str

class PromptOutput(BaseModel):
	prompt: str



class PromptBuilder(
    Runnable[
        PromptInput,
        PromptOutput
    ]
):
    name: str = "prompt_builder"

    def invoke(
        self,
        data: PromptInput
    ) -> PromptOutput:

        prompt = f"""
You are a helpful assistant.

Question:
{data.question}

Answer:
"""