import pandas as pd
from sklearn.preprocessing import MaxAbsScaler
from sklearn.neighbors import NearestNeighbors

mainDf = pd.read_csv("datasets/cleanedAnime.csv")
fitDf = pd.read_csv("datasets/fitSet.csv")

def animeRec(name, type=None):
    if type:
        found_id = mainDf[mainDf["Name"] == name].index[0]
        for id in indices[found_id][1:]:
            dfToListDf = mainDf.loc[
                (mainDf["Unnamed: 0"] == id) & (mainDf["Type"] == type)
            ]
            for item in dfToListDf["Name"].values.tolist():
                print(item)
    else:
        found_id = mainDf[mainDf["Name"] == name].index[0]
        for id in indices[found_id][1:]:
            print(mainDf.iloc[id]["Name"])


while True:
    name = input("Enter the name of the anime: ")
    number = int(input("Enter number of recommendations: "))
    print("TV:1 | Movie:2 | Music:3 | OVA:4 | Web:5 | None:0")
    type_ = int(input("Enter number for type of anime: "))
    print()

    #KDtree is used because it is faster in low dimensional datasets
    nbrs = NearestNeighbors(n_neighbors=number, algorithm="kd_tree").fit(fitDf)
    distances, indices = nbrs.kneighbors(fitDf)

    try:
        match type_:
            case 0:
                print("Recommendations: ")
                animeRec(name)
            case 1:
                print("Recommended TV Shows: ")
                animeRec(name, "TV   ")
            case 2:
                print("Recommended Movies: ")
                animeRec(name, "Movie")
            case 3:
                print("Recommended Music: ")
                animeRec(name, "Music")
            case 4:
                print("Recommended OVA's: ")
                animeRec(name, "OVA  ")
            case 5:
                print("Recommended Web Shows: ")
                animeRec(name, "Web  ")
            case _:
                print("Invalid Input")
    except IndexError:
        print(f"--!\"{name}\" was not present in the available dataset!--")
        again = input("would you like to go again?(y|n): ")
        if again == "n":
            break;
        else:
            print()
            continue

    again = input("would you like to go again(y|n): ")
    if again == "n":
        break;
    print()

print("==========DONE==========")
