from langchain_core.runnables import RunnablePassthrough

from llm import get_llm
from prompt import prompt
from schema import CVSchema

def build_chain():
    llm = get_llm()
    structured_llm = llm.with_structured_output(CVSchema)

    return (
        {"cv": RunnablePassthrough(), "job_ad": RunnablePassthrough()}
        | prompt
        | structured_llm
    )