from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

class ItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self, similarity_measure=None):
        pass

    
    def fit(self, X, titles):
        '''
        Takes a numpy array of the item attributes and creates the similarity matrix

        INPUT -
            X: NUMPY ARRAY - Rows are items, columns are feature values
            titles: LIST - List of the item names/titles in order of the numpy arrray
        
        OUTPUT - None


        Notes:  You might want to keep titles and X as attributes to refer to them later

        Create the a similarity matrix of item to item similarity
        '''
        self.sim = cosine_similarity(X)
        self.titles = titles
        
    def get_recommendations(self, item, n=5):
        '''
        Returns the top n items related to the item passed in
        INPUT:
            item    - STRING - Name of item in the original DataFrame 
            n       - INT    - Number of top related items to return 
        OUTPUT:
            items - List of the top n related item names

        For a given item find the n most similar items to it (this can be done using the similarity matrix created in the fit method)
        '''
        title_index = self.titles.index(item)
        selected = self.sim[title_index] 
        top = np.argsort(selected)[-2:-n-2:-1]
        return list(np.array(self.titles)[top])