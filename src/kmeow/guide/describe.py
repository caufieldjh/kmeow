"""Query GPT-3+ to retrieve details about a sequence processing pipeline."""
import os

from langchain.llms import OpenAI


def describe_workflow():
    """Describe workflow(s)."""

    api_key = os.environ.get("POETRY_OPENAI_API_KEY")

    prompt = """
    I am a DOE computational biologist and I have a set of
    sequencing results from an environmental isolate.
    My results are in FASTQ format.
    I would like to use the KBase tools to process and analyze
    my sequences. What is the first tool I should use,
    and what parameters should I use?
    """

    print(api_key)
    llm = OpenAI(temperature=0.9, model_name="text-davinci-003", openai_api_key=api_key)

    response = llm(prompt)

    print(response)
