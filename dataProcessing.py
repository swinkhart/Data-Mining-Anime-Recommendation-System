import pandas as pd

animeDf = pd.read_csv("datasets/Anime.csv")

# the number of episodes is an issue with the dataset as some are incomplete and are unimportant for the reccomendation so they're just dropped, the anime_id is also umimportant so it is also dropped
animeDf.drop(columns=["Japanese_name", "Episodes", "Studio", "Release_season", "Release_year", "End_year", "Description", "Content_Warning", "Related_Mange", "Related_anime", "Voice_actors", "staff"], inplace=True)

# convert string numbers to actual, operable numbers
animeDf["Rating"] = pd.to_numeric(animeDf["Rating"])
animeDf["Rank"] = pd.to_numeric(animeDf["Rank"])

# dropping animes with unknown ratings and tags, filling with an average rating could lead to inaccurate recommendations and it is not possible to guess tags
animeDf.dropna(axis=0, how="all", subset=["Tags"], inplace=True)
animeDf.dropna(axis=0, how="all", subset=["Rating"], inplace=True)

#dropping odd or uncatigorized types
animeDf.drop(animeDf.loc[animeDf["Type"] == "TV Sp"].index, inplace=True)
animeDf.drop(animeDf.loc[animeDf["Type"] == "DVD S"].index, inplace=True)
animeDf.drop(animeDf.loc[animeDf["Type"] == "Other"].index, inplace=True)

# creating dataframe to use to create the fit for the
fitDataset = animeDf.drop(columns=["Name"])

# concatinating the genre and type as dummy vatiables rather than cataigories so that they can be used for calculation
fitDataset = pd.concat(
    [fitDataset.drop("Tags", axis=1), fitDataset["Tags"].str.get_dummies(sep=", ")],
    axis=1,
)
fitDataset = pd.concat(
    [fitDataset.drop("Type", axis=1), pd.get_dummies(fitDataset["Type"])], axis=1
)

# create new cleaned dataset for use in the recommendation system
animeDf.to_csv("datasets/cleanedAnime.csv", sep=",")
fitDataset.to_csv("datasets/fitSet.csv", sep=",")