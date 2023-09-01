import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix
from implicit.als import AlternatingLeastsquares

saved_model_fname = "model_inflaized_model.sav"
date_fname = "app/data/ratings.csv"
item_fname = "app/data/movies_final.csv"
weight = 10

def model_train():
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    
    ratings_matrix = coo_matrix(
        (
            ratings_df["rating"].astype(np.float32),
            (
                ratings_df["movieId"].cat.codes.copy(),
                ratings_df["userId"].cat.codes.copy(),
            )
        )
    )