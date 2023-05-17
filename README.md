# kmeow

## The problem
Interfacing with a set of arbitrary tools for metagenome sequence analysis (or, in general, other bioinformatics pipelines) is an imposing problem for users not already familiar with available tools in a given toolset, the ways they are expected to be used together, or their appropriate parameters.
An example: I have sequencing results from an environmental isolate. How do I find out what it is (bacteria, archaea, eukaryote) and whether it’s an auxotroph for a given media component?
Stretch goal: also try to determine if any of the organism’s genes have been altered with synthetic engineering? Or if the genes are just wild type

## The solution
Large language models such as GPT-3+ are capable of translating natural language prompts into structured queries
We may use GPT-3+ as part of a standardized approach for defining appropriate metagenome sequence processing pipelines. 

## The desired outcome
A standard set of reusable code for interfacing with GPT-3+ and an API defining a collection of bioinformatics tools.
An explanation in natural language of how to do what the user wants to do
