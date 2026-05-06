from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a CV expert.

CV:
{cv}

JOB:
{job_ad}

Return an optimized CV in structured JSON format.
""")