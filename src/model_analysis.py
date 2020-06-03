import numpy as np

def print_top_words(model, n_tops, topics, n_words=30, start=0):
    if type(model).__name__ == 'NMF':
        order = model.components_.argsort()[:, ::-1]
    else:
        order = model.cluster_centers_.argsort()[:, ::-1]
    for i in range(n_tops):
        print("Topic %d:" % i)
        print ((', '.join([topics[ind] for ind in order[i, start:start+n_words]])))

def get_n_latent_topics(W, n_components, n=2):
    corresponding_tops = W.argsort(axis=1)
    primary = (corresponding_tops == n_components).argmax(axis=1)
    secondary = (corresponding_tops == (n_components-1)).argmax(axis=1)
    return primary, secondary