import os,sys

import pandas as pd
import numpy as np
from getTI import getFutureRows
from joblib import load
import warnings
import sys


f = open('output.txt','w')
sys.stdout = f
warnings.filterwarnings("ignore")
company=['marutisuzuki','hdfc','infosys']
output=[]

for i in company:
    model=load(i+'.joblib')
    X=getFutureRows(i)
    scaler=load(i+'_scaler.joblib')
    X_scaled=scaler.transform(X)
    X_scaled = pd.DataFrame(data=X_scaled, index=X.index, columns=X.columns)
    output.extend(model.predict(X_scaled))

print(*output)    

