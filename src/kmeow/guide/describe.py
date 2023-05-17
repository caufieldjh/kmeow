"""Query GPT-3+ to retrieve details about a sequence processing pipeline."""
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

def describe_workflow(params: dict):
    """Describe workflow(s)."""

    api_key = os.environ.get("POETRY_OPENAI_API_KEY")

    intro_template = PromptTemplate(input_variables=['format'],
                                    template="""
                                    I am a computational biologist and I have a set of
                                    sequencing results from an environmental isolate.
                                    My results are in {format} format.
                                    I would like to use the KBase tools to process and analyze
                                    my sequences. What is the first tool I should use,
                                    and what parameters should I use?
                                    """)

    llm = OpenAI(
        temperature=0.9,
        model_name="text-davinci-003",
        openai_api_key=api_key,
    )

    workflow_chain = LLMChain(llm=llm, prompt=intro_template, verbose=True)

    response = workflow_chain.run(format=params['format'])

    print(response)
