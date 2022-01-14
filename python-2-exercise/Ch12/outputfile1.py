import pandas as pd
data = {"country":["Brazil","Russia","India","China","South Africa"],
        "population":[200,144,1252,1357,55],
        "area":[8515767,17098242,3287590,9596961,1221037],
        "capital":["Brasilia","Moscow","New Delhi","Beijing","Pretoria"]}
df = pd.DataFrame(data, index=['BR','RU','IN','CH','SA'])
print(df)
df.to_html("brics.html")
df.to_csv("brics.csv")
df.to_csv("brics2.csv", header=False)
df.to_json("brics.json")
