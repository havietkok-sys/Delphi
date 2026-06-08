from pydantic import BaseModel
from .runnable import Runnable
from ..llm import ask_model
from ..schemas import AskResponse


class PromptInput(BaseModel):
    question: str
    stats: dict

class PromptOutput(BaseModel):
    question: str
    prompt: str


class LLMOutput(BaseModel):
    question: str
    answer: str


class PromptBuilder(Runnable[PromptInput, PromptOutput]):
    name: str = "prompt_builder"
    

    def invoke(self, data: PromptInput) -> PromptOutput:

        prompt = f"""
        You are a data analyst.

        Dataset statistics:

        {data.stats}

        Question:
        {data.question}

        Answer:
        """
        return PromptOutput(question=data.question, prompt=prompt)


class LLMRunner(Runnable[PromptOutput, LLMOutput]):
    name: str = "llm_runner"

    def invoke(self, data: PromptOutput) -> LLMOutput:

        answer = ask_model(data.prompt)

        return LLMOutput(question=data.question, answer=answer)


class ResponseParser(Runnable[LLMOutput, AskResponse]):
    name: str = "response_parser"

    def invoke(self, data: LLMOutput) -> AskResponse:

        return AskResponse(
            question=data.question, answer=data.answer, model="SmolLM2-135M-Instruct"
        )
