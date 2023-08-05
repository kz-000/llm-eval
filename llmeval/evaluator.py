import json
from langchain.chat_models import ChatOpenAI
from prompt import Prompt
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)


class LlmEval:
    def __init__(self, score_min: int | float = 0, score_max: int | float = 5, **kwargs) -> None:
        self._model = ChatOpenAI(**kwargs)

        self._score_min, self._score_max = score_min, score_max
        self._type = "float" if type(score_min) == float or type(
            score_max) == float else "integer"

        self._referencs_base_prompt = ChatPromptTemplate.from_messages([
            HumanMessagePromptTemplate.from_template(
                Prompt.EVALUATION_SCHEMA+Prompt.REFERENCE_BASE)
        ])

        self._referencs_free_prompt = ChatPromptTemplate.from_messages([
            HumanMessagePromptTemplate.from_template(
                Prompt.EVALUATION_SCHEMA+Prompt.REFERENCE_FREE)
        ])

        self._dialog_level_prompt = ChatPromptTemplate.from_messages([
            HumanMessagePromptTemplate.from_template(
                Prompt.EVALUATION_SCHEMA+Prompt.DIALOGUE_LEVEL)
        ])

    def referencs_base(self, context, referense, response):
        request = self._referencs_base_prompt.format_prompt(
            context=context, reference=referense, response=response,
            score_min=self._score_min, score_max=self._score_max, type=self._type)
        content, grammer, relevance, appropriateness = self._run(
            request.to_messages())
        return content, grammer, relevance, appropriateness

    def referencs_free(self, context, response):
        request = self._referencs_free_prompt.format_prompt(
            context=context, response=response,
            score_min=self._score_min, score_max=self._score_max, type=self._type)
        content, grammer, relevance, appropriateness = self._run(
            request.to_messages())
        return content, grammer, relevance, appropriateness

    def dialog_level(self, dialog):
        request = self._dialog_level_prompt.format_prompt(
            dialog=dialog, score_min=self._score_min, score_max=self._score_max, type=self._type)
        content, grammer, relevance, appropriateness = self._run(
            request.to_messages())
        return content, grammer, relevance, appropriateness

    def _run(self, messages):
        response = self._model(messages)
        data = json.loads(response.content)
        return data.values()
