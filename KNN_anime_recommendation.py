import pandas as pd
from sklearn.preprocessing import MaxAbsScaler
from sklearn.neighbors import NearestNeighbors

mainDf = pd.read_csv("datasets/cleanedAnime.csv")
fitDf = pd.read_csv("datasets/fitSet.csv")

# need to modify to accept types(OVA, ONA, Movie, ect)
def animeRec(name, type=None):
    if type:
        found_id = mainDf[mainDf["name"] == name].index[0]
        for id in indices[found_id][1:]:
            dfToListDf = mainDf.loc[
                (mainDf["Unnamed: 0"] == id) & (mainDf["type"] == type)
            ]
            for item in dfToListDf["name"].values.tolist():
                print(item)
    else:
        found_id = mainDf[mainDf["name"] == name].index[0]
        for id in indices[found_id][1:]:
            print(mainDf.iloc[id]["name"])


while True:
    name, number, ty = input(
        "Enter the name of the anime, number of recommendations, and type of anime(name number type), enter(d d d) to quit: "
    ).split()

    nbrs = NearestNeighbors(n_neighbors=number, algorithm="kd_tree").fit(fitDf)
    distances, indices = nbrs.kneighbors(fitDf)

    animeRec("Toki wo Kakeru Shoujo")
