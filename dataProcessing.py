import numpy as np
import pandas as pd

animeDf = pd.read_csv("datasets/anime.csv")

# the number of episodes is an issue with the dataset as some are incomplete and are unimportant for the reccomendation so they're just dropped, the anime_id is also umimportant so it is also dropped
animeDf.drop(columns=["anime_id", "episodes"], inplace=True)

# convert string numbers to actual, operable numbers
animeDf["rating"] = pd.to_numeric(animeDf["rating"])
animeDf["members"] = pd.to_numeric(animeDf["members"])

# dropping animes with unknown ratings, filling with an average rating could lead to inncaurate recommendations
animeDf.dropna(how="all", subset=["rating"], inplace=True)

# creating dataframe to use to create the fit for the
fitDataset = animeDf.drop(columns=["name"])

# concatinating the genre and type as dummy vatiables rather than cataigories so that they can be used for calculation
fitDataset = pd.concat(
    [fitDataset.drop("genre", axis=1), fitDataset["genre"].str.get_dummies(sep=", ")],
    axis=1,
)
fitDataset = pd.concat(
    [fitDataset.drop("type", axis=1), pd.get_dummies(fitDataset["type"])], axis=1
)

# create new cleaned dataset for use in the recommendation system
animeDf.to_csv("datasets/cleanedAnime.csv", sep=",")
fitDataset.to_csv("datasets/fitSet.csv", sep=",")
