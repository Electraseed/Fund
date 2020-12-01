# run your simulations, and do some postprocessing on simulation results DataFrame

# cadCAD simulation engine modules
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from cadCAD import configs
import pandas as pd
from model import config 

def run():
    '''
    Definition:
    Run simulation
    '''
    # Single
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    # clear any prior confiuraitons
    del configs [:]
    #add initial config 
    simulation = Executor(exec_context=local_mode_ctx, configs=configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)
    
     # subset to last substep
    df = df[df['substep'] == df.substep.max()]
    
    return df
