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
    name = input("Enter the name of the anime: ")
    number = int(input("Enter number of recommendations: "))
    print("TV:1 | Movie:2 | Special:3 | OVA:4 | ONA:5 | None:0")
    type_ = int(input("Enter number for type of anime: "))

    #KDtree is used because it is faster in low dimensional datasets
    nbrs = NearestNeighbors(n_neighbors=number, algorithm="kd_tree").fit(fitDf)
    distances, indices = nbrs.kneighbors(fitDf)

    try:
        match type_:
            case 0:
                animeRec(name)
            case 1:
                animeRec(name, "TV")
            case 2:
                animeRec(name, "Movie")
            case 3:
                animeRec(name, "Special")
            case 4:
                animeRec(name, "OVA")
            case 5:
                animeRec(name, "ONA")
            case _:
                print("Invalid Input")
    except IndexError:
        print(f"!!!{name} was not present in the available dataset!!!")
        again = input("would you like to go again?(y|n): ")
        if again == "n":
            break;
        else:
            continue

    again = input("would you like to go again(y|n): ")
    if again == "n":
        break;

print("===DONE===")
