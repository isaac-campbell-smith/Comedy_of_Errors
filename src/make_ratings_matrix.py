import numpy as np
import pandas as pd

def ratings_mat(titles, reviews_df):
    '''
    Takes a series of titles and sparse dataframe of user reviews
    and transfer data into a user-item dataframe
    INPUT - 
        titles: SERIES
        reviews_df: DATAFRAME 
    OUTPUT -
        ratings_matrix: DATAFRAME 
    '''
    columns = ['user', 'special', 'rating']
    ratings_matrix = pd.DataFrame(columns=columns)
    
    for row in range(reviews_df.shape[0]):
        user_reviews = reviews_df.iloc[row][reviews_df.iloc[row] > 0]
        scores = user_reviews.values
        ids = user_reviews.index
        to_add = np.array([np.array([row]*len(scores)),ids, scores]).T
        ratings_matrix = pd.DataFrame(np.append(ratings_matrix.values, to_add, axis=0), 
                                    columns=columns)
    return ratings_matrix