import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
from sdk.bb_runner import bulk_infer_capable

regr = pickle.load(open("model.pkl", 'rb'))
col_name = ["c"+str(x) for x in range(1,34)]
# ["c1", "c2", ... "c33"]
def predict(inMap):
    in_df = pd.DataFrame([inMap])
    # select the column that needed by model, there are extra columns added by AAW, etc guid..
    out_df = regr.predict(in_df[col_name])
    return {"prediction":out_df[0]}

@bulk_infer_capable
def predict_batch(inMap):
    in_df = pd.DataFrame(inMap)
    # select the column that needed by model, there are extra columns added by AAW, etc guid..
    in_df["prediction"] = regr.predict(in_df[col_name])
    return in_df.to_dict("records")
