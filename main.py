from llmeval import LlmEval
eval = LlmEval(model_name="gpt-3.5-turbo-0613", temperature=0.0)


context = """
"""

referense = """
"""

response = """
"""

eval.referencs_free(context, response)
# eval.referencs_base(context, referense, response)
