# The partial state update blocks (PSUB) order the execution, and group State Update Functions (SUF) are independente from other SUF. 
# Policies within the block are independent from other Policies and indepentent from SUF. 
# This is to make sure that an updated state_variable in this PSUB, the update cannot affect SUF and Policies in this PSUB.
# Side effects are avoided, execution logic is parallelized.

from .parts.system import *

partial_state_update_block = [
    #run behaviros and mechanisms first   
    {
        # Behaviors in system.py
        'policies': {
            #TODO
        },
        # Mechanisms in system.py
        'variables': {
             'funding_pool': s_update_funds,
            # 'reserve_pool' :  s_update_funds, 
             'flexibility_pool': s_update_usage,
            # 'clean_air' : s_update_usage             
        }
    }
    #calculate metrics in next substep
]