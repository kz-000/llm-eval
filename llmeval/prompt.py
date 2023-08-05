class Prompt:
    EVALUATION_SCHEMA = """
The output should be formatted as a JSON instance that conforms to the JSON schema below.
As an example, for the schema
{{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}}}
the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema.
The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.
Here is the output schema:
{{
    "properties": {{
        "content": {{
            "title": "Content",
            "description": "content score in the range of {score_min} to {score_max}", 
            "type":"{type}"
        }},
        "grammar": {{
            "title": "Grammar",
            "description": "grammar score in the range of {score_min} to {score_max}", 
            "type": "{type}"
        }}, 
        "relevance": {{
            "title": "Relevance",
            "description": "relevance score in the range of {score_min} to {score_max}",
            "type": "{type}"
        }},
        "appropriateness": {{
            "title": "Appropriateness",
            "description": "appropriateness score in the range of {score_min} to {score_max}", 
            "type": "{type}"
        }}
    }}, 
    "required":["content", "grammar", "relevance", "appropriateness"]
}}
    """

    REFERENCE_BASE = """
Score the following dialogue response generated on a continuous scale from {score_min} to {score_max}.
Context: {context}
Reference: {reference}
Dialogue response: {response}
    """

    REFERENCE_FREE = """
Score the following dialogue response generated on a continuous scale from {score_min} to {score_max}.
Context: {context}
Dialogue response: {response}
    """

    DIALOGUE_LEVEL = """
Score the following dialogue generated on a continuous scale from {score_min} to {score_max}.
Dialogue: {dialog}
    """
