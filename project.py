import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv('Data.csv')

student_df = df.loc[df['student_id'] == "trl_987"]


print(student_df.groupby("level")["atttempt"].mean())

fig = go.Figure(go.scatter(
    x=student_df.groupby("level")["attempt"].mean(),
    y=['level 1', 'level 2', 'level 3', 'level 4'],
    orientation='h'
))


fig.show()