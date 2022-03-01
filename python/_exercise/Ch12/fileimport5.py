import pandas as pd
df1 = pd.read_html("brics.html", index_col=0, header=0)  
print(df1)
print('--------------------------')
df2 = pd.read_html('area.html', encoding='cp950')
print(df2)
print('--------------------------')
