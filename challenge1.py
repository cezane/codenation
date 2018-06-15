import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")
pd.options.display.max_colwidth = 100

data["NOTA_FINAL"] = 0
for i in range(1, len(data.index)):
    row = data.loc[i]
    data.loc[data.index==i, "NOTA_FINAL"] = ((row.NU_NOTA_MT * 3 + \
                               row.NU_NOTA_CN * 2 + \
                               row.NU_NOTA_LC * 1.5 + \
                               row.NU_NOTA_CH * 1 + \
                               row.NU_NOTA_REDACAO * 3) / 10)

#format = '{"NU_INSCRICAO": "{NU_INSCRICAO}", "NOTA_FINAL": {NOTA_FINAL}}'.format
#print('{"NU_INSCRICAO": "%s", "NOTA_FINAL": %1f}'.format(data.sort_values(["NOTA_FINAL"], ascending=[False])[["NU_INSCRICAO", "NOTA_FINAL"]].head(1)))
print((data.sort_values(["NOTA_FINAL"], ascending=[False])[["NU_INSCRICAO", "NOTA_FINAL"]].head(20)).to_string(formatters={'NU_INSCRICAO':'{{"NU_INSCRICAO": "{}",'.format, 'NOTA_FINAL':'"NOTA_FINAL": {:.1f}}},'.format})) #.style.format({'NU_INSCRICAO': '{"NU_INSCRICAO": "{}",', 'NOTA_FINAL': '"NOTA_FINAL": {}}'})) #apply(lambda x: format(**x), 1))

