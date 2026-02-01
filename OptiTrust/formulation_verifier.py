import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import MYLLM

class Optimization_Modeling_Dubug(MYLLM):

    SYSTEM = """
    You're an expert in mathematical optimization. You need to revise the mathematical formulation of an optimization problem prepared by a student.
    """

    TASK = """
    Here is a description of the problem we need you to model:
    
    {description}
    ----
    
    The following components have been previously identified:
    ----
    {components}
    ----
    
    And here is the mathematical formulation we need you to verify:
    ----
    {previous_formulation}
    ----
    
    Solve the problem step by step. Explain your reasoning and remember to enclose the final list of components between the "'''" lines.
    """
        
    def __init__(self):
        super().__init__()
        prompt = ChatPromptTemplate([
            ("system",self.SYSTEM), 
            ("human", self.TASK),
        ])
        self.chain = prompt | self.llm | StrOutputParser()

    def run(self, description: str, components: str, previous_formulation:str) -> str:
        return self.chain.invoke({"description" : description, "components": components, "previous_formulation": previous_formulation})