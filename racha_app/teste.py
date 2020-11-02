import pandas as pd
import numpy as np
import datetime

stats = ['Sérgio', '1', '0', '1', '0', '1', '0', 'DJ', '2', '0', '2', '0', '2', '0', 'Sérgio', '3', '0', '3', '0', '3', '0', 'DJ', '4', '0', '4', '0', '4', '0', 'Sérgio', '5', '0', '05', '0', '5', '0', 'DJ', '06', '0', '6', '0', '6', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0',
'0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0', '', '0', '0', '0', '0', '0', '0']
# a = stats[0:7]
stats = [stats[x:x+7] for x in range(0,len(stats),7)]

df = pd.DataFrame(stats, columns = ["Jogador", "Jogo 1", "Jogo 2", "Jogo 3", "Jogo 4", "Jogo 5", "Jogo 6"])
a, b, c, d = np.array_split(df, 4)

a = a.to_json(orient="records", force_ascii=False)
b = b.to_json(orient="records", force_ascii=False)
c = c.to_json(orient="records", force_ascii=False)
d = d.to_json(orient="records", force_ascii=False)

json = {"team_a": a, "team_b": b, "team_c": c, "team_d": d}
print(json["team_a"])