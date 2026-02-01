import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import MYLLM

class Programming(MYLLM):

    SYSTEM = """
    You are an expert in mathematical optimization, and your objective is to create a Python script to solve an optimization problem using gorubi.
    """

    TASK = """
    When solving an optimization problem, you should follow a structured approach:
    
    1. Carefully analyze and comprehend the problem description.
    2. Carefully analyze and comprehend the provided decomposition of the problem into a detailed list of decision variables, objective(s) and constraints.
    3. Carefully analyze and comprehend the previously prepared mathematical formulation of the optimization problem.
    4. Prepare a well-documented Python script to solve the optimization problem using gorubi. Anchor your implementation on the context, the detailed decomposition, and the formulation of the optimization problem. Pay special attention to the domain of each decision variable, implicit constraints such as non-negativity, and that all relevant parameters are included in the script you generate.
    Note that
    - You should clearly explain your reasoning and the steps you take to solve the problem.
    - You should enclose the final code between "'''" lines, as in the provided examples.
    - You should print the optimal value of the optimization problem using 'Optimal value: ', as in the provided examples.
    Let's think step by step and clearly describe our reasoning.
    
    
    Here is the problem description:
    ----
    {description}
    ----
    
    The following components have been extracted from the problem description:
    ----
    {components}
    ----
    
    And the following mathematical formulation to represent the optimization problem has been prepared:
    ----
    {formulation}
    ----
    
    Now, follow the steps outlined above. Explain your reasoning and remember to enclose the generated code between "'''" lines.
    """
        
    def __init__(self):
        super().__init__()
        prompt = ChatPromptTemplate([
            ("system",self.SYSTEM), 
            ("human", self.TASK),
        ])
        self.chain = prompt | self.llm | StrOutputParser()

    def run(self, description: str, components: str, formulation:str) -> str:
        return self.chain.invoke({"description" : description, "components": components, "formulation": formulation})