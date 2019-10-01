
import numpy as np
import pandas as pd

## try to maintain a readme file for same 

class MCPNeuron(object):
    
    def __init__(self,w=[1,1],t=1):
            self.w = np.array(w)
            self.t = t
    
    def decide(self,message):
        x= message
    
        sum_=np.inner(self.w,x)
        if sum_>= self.t:
            return 1
        else:
            return 0

    def TruthTable(self, in_signals, in_labels, out_labels):
        table = pd.DataFrame(in_signals ,columns=in_labels)
        out_signals = []
    
        for row in in_signals:
            signal = self.decide(message=row)
            out_signals.append(signal)
            table[out_labels] = pd.Series(out_signals)
        return table
    


in_signals = np.array([[0,0],[0,1],[1,0],[1,1]])
in_labels = ['x1','x2']
out_labels = 'y'
AND = MCPNeuron(w=[1,1], t=2)
AND_Table = AND.TruthTable(in_signals,in_labels=in_labels, out_labels=out_labels)
    
print(AND_Table)
