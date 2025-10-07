from cmath import nan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import warnings
import seaborn as sns


datasets = [
    ('awards_players', pd.read_csv("awards_players.csv")),
    ('coaches', pd.read_csv("coaches.csv")),
    ('players_teams', pd.read_csv("players_teams.csv")),
    ('players', pd.read_csv("players.csv")),
    ('series_post', pd.read_csv("series_post.csv")),
    ('teams_post', pd.read_csv("teams_post.csv")),
    ('teams', pd.read_csv("teams.csv"))
]