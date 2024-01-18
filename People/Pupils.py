import pandas as pd


class Pupil:
    def __init__(self, name: str, likes: list, dislikes: list):
        self.name = name
        self.likes = likes
        self.dislikes = dislikes


def create_pupils_from_dataframe(dataframe):
    pupils = []
    for index, row in dataframe.iterrows():
        # remove \t from the string in name
        name = row["name"].strip().replace('\t', '').replace(' ', '')
        # Reset likes and dislikes to empty lists for each iteration
        likes = []
        dislikes = []
        # see if there is an entry, if yes, add ", " as delimiter between names
        if not pd.isna(row["like"]):
            likes = [like.strip() for like in row["like"].split(", ")]
        else:
            print(f"{name} doesn't like anyone")
        if not pd.isna(row["dislike"]):
            dislikes = [dislike.strip() for dislike in row["dislike"].split(", ")]
        else:
            print(f"{name} doesn't like anyone")
        pupil = Pupil(name=name, likes=likes, dislikes=dislikes)
        pupils.append(pupil)
    return pupils