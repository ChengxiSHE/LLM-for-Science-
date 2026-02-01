import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import MYLLM

class Optimization_Modeling(MYLLM):

    SYSTEM = """
    You are an expert in mathematical optimization, and your task is to model an optimization problem.
    """

    TASK = """
    Upon receiving the description of an optimization problem, you should:
    
    1. Carefully analyze and comprehend the problem.
    2. Carefully review the decision variables previously identified. Define symbols representing the decision variables and indicate whether each of the decision variables is required to be integer, real or binary based on the context of the problem.
    3. Indicate whether any decision variables are required to be non-negative based on the context of the problem.
    4. Carefully review the previously identified objectives, and prepare a mathematical formulation representing the objective. If the optimization problem has multiple objectives, convert a multi-objective optimization problem into a single-objective optimization problem using linear scalarization with the weights of the objectives.
    5. Carefully review the previously identified constraints, and prepare a mathematical formulation representing each of the constraints.
    6. Prepare a mathematical formulation of the problem using LaTeX.
    7. Verify if any numerical values or parameters defined in the problem description are missing from the formulation, and update the mathematical formulation to include them, if necessary.
    
    Note that:
    - Try to mathematically represent constraints and objectives as close to their natural language description as possible.
    - You do not need to simplify any constraints or objectives.
    - Your formulation should be in LaTeX mathematical format.
    - The final mathematical formulation should be enclosed between the "'''" lines.
    
    Here is a description of the problem we need you to model:
    ----
    {description}
    ----
    
    The following components have been previously identified:
    ----
    {components}
    ----
    
    Now, solve the problem step by step. Explain your reasoning and remember to enclose the final list of components between the "'''" lines.
    """
        
    def __init__(self):
        super().__init__()
        prompt = ChatPromptTemplate([
            ("system",self.SYSTEM), 
            ("human", self.TASK),
        ])
        self.chain = prompt | self.llm | StrOutputParser()

    def run(self, description: str, components: str) -> str:
        return self.chain.invoke({"description" : description, "components": components})