from langchain.prompts.prompt import PromptTemplate


skill_development_template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
Current conversation:
{history}
Human: {input}
AI:"""
skill_development_prompt = PromptTemplate(
    input_variables=["history", "input"], template=skill_development_template
)


training_evaluation_template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
Current conversation:
{history}
Human: {input}
AI:"""
training_evaluation_prompt = PromptTemplate(
    input_variables=["history", "input"], template=training_evaluation_template
)
