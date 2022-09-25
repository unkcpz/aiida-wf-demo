from aiida.engine import submit
from aiida.orm import load_code, Str, load_node
from aiida.plugins import WorkflowFactory

EquationOfState =  WorkflowFactory("wf_demo.eos")

submit(
    EquationOfState, 
    code=load_code('pw-7.0@localhost'), 
    pseudo_family_label=Str('SSSP/1.1/PBE/efficiency'), 
    structure=load_node(pk=195),
)