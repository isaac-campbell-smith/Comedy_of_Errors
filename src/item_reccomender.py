from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

class ItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self):
        pass

    
    def fit(self, X, titles, clusters):
        '''
        Takes a numpy array of the item attributes and creates the similarity matrix

        INPUT -
            X: NUMPY ARRAY - Rows are items, columns are feature values
            titles: ARRAY - List of the item names/titles in order of the numpy arrray
            genres: ARRAY - List of corresponding genres pseudo-scientifically derived in Clustering Analysis notebook
        OUTPUT - None
        '''
        self.sim = cosine_similarity(X)
        self.titles = titles
        self.clusters = clusters
        
    def get_group_cluster(self, idx):
        '''
        Takes a title index which maps to the corresponding genre and returns all titles w/in
        INPUT - 
            idx: INT
        OUTPUT - 
            cluster_titles: ARRAY - List of titles within cluster
        '''
        cluster_marker = self.clusters[idx]
        cluster_mask = (self.clusters == cluster_marker)
        return cluster_mask
    
    def get_recommendations(self, item, neighborhood=True, top=True, n=5):
        '''
        Returns the top n items related to the item passed in if top=True, returns the most dissimilar if False
        INPUT:
            item         - STRING - Name of item in the original DataFrame 
            n            - INT    - Number of top related items to return 
            neighborhood - BOOL   - If true, looks at items in the same genre, otherwise absolute dissimilarity
        OUTPUT:
            items - List of the top n related item names

        For a given item find the n most similar items to it (this can be done using the similarity matrix created in the fit method)
        '''
        title_index = np.where(self.titles == item)[0][0]
        similarities = self.sim[title_index]
        
        if neighborhood:
            mask = self.get_group_cluster(title_index)
            similarities = similarities[mask]
            group_titles = self.titles[mask]

        if top:
            args = np.argsort(similarities)[-2:-n-2:-1]
        else:
            args = np.argsort(similarities)[:n]

        return list(group_titles[args]) if neighborhood else list(self.titles[args])