import pandas as pd
import random


def generate_payoff_matrix():
    df = pd.read_csv('prisoners_dilemma.csv')
    return df

df = generate_payoff_matrix()



for k,v in df.iterrows():
    print(v['s'])
    print(v['c'])