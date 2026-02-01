import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import MYLLM

class Decomposition(MYLLM):

    SYSTEM = """
    You are an expert in mathematical optimization. Your task is to identify and prepare natural language descriptions of components of an optimization problem.
    """

    TASK = """
    Upon receiving a problem description, you should:
    
    1. Carefully analyze and comprehend the problem.
    2. Summarize the decision variables related to the problem. Indicate whether each of the decision variables is required to be integer, real or binary based on the context of the problem.
    3. Summarize and define the objective of the problem. Indicate any parameters or numerical values needed to define the objective.
    4. Identify and list all constraints, including any implicit ones like non negativity. List and summarize the constraints using natural language. Indicate any parameters or numerical values needed to define each of the constraints
    5. Verify if any numerical values or parameters defined in the problem description are missing from the objective or constraints you identified, and update the list of components you prepared, if necessary.

    Note that:
    If adding any mathematical expressions, try to mathematically represent constraints and objectives as close to their natural language description as possible; you do not need to simplify any constraints or objectives.
    The final list of components should be enclosed between the "'''" lines.
    
    Here is a description of the problem we need you to find the components for:

    {description}
    ----

    Now, follow the steps outlined above. Explain your reasoning and remember to enclose the final list of components between the "'''" lines.
    """
        
    def __init__(self):
        super().__init__()
        prompt = ChatPromptTemplate([
            ("system",self.SYSTEM), 
            ("human", self.TASK),
        ])
        self.chain = prompt | self.llm | StrOutputParser()

    def run(self, description: str) -> str:
        return self.chain.invoke({"description" : description})