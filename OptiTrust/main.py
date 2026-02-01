import random
import pandas as pd
import os
from typing import Dict
from formulation import Optimization_Modeling
from decomposition import Decomposition
from decomposition_verifier import Decomposition_debug  
from formulation_verifier import Optimization_Modeling_Dubug
from programming import Programming
from utils import save_txt, extract_python_code, safe_exec, safe_exec_with_flag, calculate_mean, read_txt

dataset_path = 'LPWP'
for dir in os.listdir(dataset_path): 
    data_path = os.path.join(dataset_path, dir)
    if not os.path.isdir(data_path):
        continue
    result_dir = data_path
    problem = read_txt(os.path.join(data_path, "description.txt"))

    decompose = Decomposition()
    pre_components = decompose.run(problem)

    decompose_debug = Decomposition_debug()
    verified_components = decompose_debug.run(problem, pre_components)

    formulate = Optimization_Modeling()
    formulation = formulate.run(problem, verified_components)

    formulation_debug = Optimization_Modeling_Dubug()
    verified_formulation = formulation_debug.run(problem, verified_components, formulation)

    program = Programming()
    code_response = program.run(problem, verified_components, verified_formulation)

    code_string = extract_python_code(code_response)
    flag, result = safe_exec_with_flag(code_string)

    save_txt(result, f'{result_dir}/result.txt')
    print("solving finish!")