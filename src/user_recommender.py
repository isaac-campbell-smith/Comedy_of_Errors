import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from .item_reccomender import ItemRecommender
from time import time

class ReviewRecommender(object):
    """Item-item similarity recommender."""

    def __init__(self, neighborhood_size=75):
        """Initialize the parameters of the model."""
        self.neighborhood_size = neighborhood_size
        self.item_recommender = ItemRecommender()

    def fit(self, ratings_mat, specials, genres, corpus_vector):
        """Fit the model to the data specified as an argument.
        Store objects for describing model fit as class attributes.
        """
        self.specials = specials

        self.item_recommender.fit(corpus_vector, specials.values, genres.values)

        self.ratings_mat = csr_matrix(ratings_mat)

        self.n_items = self.ratings_mat.shape[1]
        
        self.items_cos_sim, self.neighborhoods = self._set_neighborhoods()

    def _set_neighborhoods(self):
        """Get the items most similar to each other item.
        Should set a class attribute with a matrix with number of rows
        equal to number of items, and number of columns equal to
        neighborhood size. Entries in this matrix will be indices of other
        items.
        You will call this in your fit method.
        """
        items_cos_sim = cosine_similarity(self.ratings_mat.T)
        least_to_most_sim_indexes = np.argsort(items_cos_sim, 1)
        neighborhoods = least_to_most_sim_indexes[:, -self.neighborhood_size:]
        return items_cos_sim, neighborhoods

    def pred_one_user(self, user_id, timeit=False):
        """Accept user id as arg. Return the predictions for a single user.
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        start_time = time()
        items_rated_by_this_user = self.ratings_mat[user_id].nonzero()[1]
        # Just initializing so we have somewhere to put rating preds
        output = np.zeros(self.n_items)
        for item_to_rate in range(self.n_items):
            relevant_items = np.intersect1d(self.neighborhoods[item_to_rate],
                                            items_rated_by_this_user,
                                            assume_unique=True)
            # assume_unique speeds up intersection op
            # note: ratings_mat has data type `sparse_lil_matrix`, while
            # items_cos_sim is a numpy array. Luckily for us, multiplication
            # between these two classes is defined, and even more luckily,
            # it is defined to as the dot product. So the numerator
            # in the following expression is an array of a single float
            # (not an array of elementwise products as you would expect
            #  if both things were numpy arrays)
            output[item_to_rate] = (
                self.ratings_mat[user_id, relevant_items] * 
                self.items_cos_sim[item_to_rate, relevant_items] / 
                (self.items_cos_sim[item_to_rate, relevant_items].sum())
                )
                
        if timeit:
            print("Execution time: %f seconds" % (time()-start_time))

        return np.nan_to_num(output)

    def pred_all_users(self, timeit=False):
        """Return a matrix of predictions for all users.
        Repeated calls of pred_one_user, are combined into a single matrix.
        Return value is matrix of users (rows) items (columns) and
        predicted ratings (values).
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        start_time = time()
        users = self.ratings_contents.user.unique()
        output = np.zeros((users.size, self.n_items))
        for i in range(len(users)):
            output[i, :] = self.pred_one_user(users[i], timeit)
        if timeit:
            print("Execution time: %f seconds" % (time()-start_time))
        return output



    def top_n_recs(self, user_id, n_recs=5):
        """Take user_id argument and number argument.
        Return that number of items with the highest predicted ratings,
        after removing items that user has already rated.
        """
        preds = self.pred_one_user(user_id)
        item_index_sorted_by_pred_rating = list(np.argsort(preds))
        items_rated_by_this_user = self.ratings_mat[user_id].nonzero()[1]

        unrated_items_by_pred_rating = [item for item in item_index_sorted_by_pred_rating
                                        if item not in items_rated_by_this_user]

        if preds[items_rated_by_this_user].max() < 7: #make this more sophisticated
            recs = []
            for special in self.specials.iloc[items_rated_by_this_user]:
                item_recs = self.item_recommender.get_recommendations(special, top=False, n=n_recs)
                recs.extend(item_recs)
            ## NEED TO FIGURE OUT WAY TO CUT THIS DOWN IF IT GOES OVER
            return recs
        
        recs = self.specials.iloc[unrated_items_by_pred_rating[-n_recs:]]
        return list(recs)

