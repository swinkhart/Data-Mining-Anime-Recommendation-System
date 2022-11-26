import pandas as pd
from sklearn.preprocessing import MaxAbsScaler
from sklearn.neighbors import NearestNeighbors

mainDf = pd.read_csv("datasets/cleanedAnime.csv")
fitDf = pd.read_csv("datasets/fitSet.csv")

# using maxabsscalar now might change later after more resaerch
max_abs_scaler = MaxAbsScaler()
fitData = max_abs_scaler.fit_transform(fitDf)

# gotta play around with this some more, may switch it up by calling the algorithm directly, ripped from scikit learn example
nbrs = NearestNeighbors(n_neighbors=6, algorithm="auto").fit(fitDf)
distances, indices = nbrs.kneighbors(fitDf)


def getIndexFromName(name):
    return mainDf[mainDf["name"] == name].index[0]


def getSimlarAnimes(name, type=None):
    found_id = getIndexFromName(name)
    for id in indices[found_id][1:]:
        print(mainDf.iloc[id]["name"])


getSimlarAnimes("Majo no Takkyuubin")
