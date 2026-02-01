import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils import MYLLM

class Decomposition_debug(MYLLM):

    SYSTEM = """
    You are an expert in mathematical optimization. Your task is to review previously identified components of an optimization problem.
    """

    TASK = """
    Upon receiving the description of an optimization problem and a list of previously identified components of the optimization problem, you should:
    
    1. Carefully analyze and comprehend the problem.
    2. Verify if the decision variables, objectives and constraints listed in the previously prepared list of components have been identified correctly.
    3. Verify if any decision variables, objectives or constraints in the description of the optimization problem are missing from the previously prepared list of components and update the list, if necessary.
    4. Verify if any numerical values or parameters defined in the problem description are missing from the components you identified, and update the list of components you prepared to include those, if necessary.
    5. Prepare a final, revised list with the components of the optimization problem (including objectives, constraints and decision variables) in natural language. Make sure to avoid repeating components.
     
    Note that:
    - You should include any implicit constraints such as non-negativity
    - If adding any mathematical expressions, try to mathematically represent constraints and objectives as close to their natural language description as
    possible; you do not need to simplify any constraints or objectives.
    You should indicate whether each of the decision variables is required to be integer, real or binary based on the context of the problem.
    - The final list of components should be enclosed between the "'''" lines.

    Here is a description of the problem we need you to find the components for:
    
    {description}
    ----
    
    And here is the list of previously identified components:
    ----
    {previous_components}
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

    def run(self, description: str, previous_components:str) -> str:
        return self.chain.invoke({"description" : description, "previous_components": previous_components})