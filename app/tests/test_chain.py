from app.chain.steps import (
    PromptBuilder,
    PromptInput
)


def test_prompt_builder_includes_question_and_stats():

    builder = PromptBuilder()

    result = builder.invoke(
        PromptInput(
            question="Vilken stad är varmast?",
            stats={
                "temp_c": {
                    "mean": 8.3
                }
            }
        )
    )

    assert "Vilken stad är varmast?" in result.prompt
    assert "8.3" in result.prompt