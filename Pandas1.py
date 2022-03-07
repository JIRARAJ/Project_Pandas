"""import pandas as pd
Raji_web = {'Day' : [1, 2, 3, 4, 5], 'Visitors' : [500,1000,1500,600,4000], 'Bouncerate' : [15,18,20,26,30]}
df = pd.DataFrame(Raji_web)
print(df.head(2))
print(df.tail(3))"""

import pandas as pd
df1 = {'HPI': [50,69,74,88,55], 'Int_rate' : [2,1,2,6,4], 'IND_GDP' : [84,76,93,62,41], 'index': [2000,2001,2002,2003,2004]}
df2 = {'HPI': [50,69,74,88,55], 'Int_rate' : [2,1,2,6,4], 'IND_GDP' : [84,76,93,62,41]}, 'index' : [2005,2006,2007,2008,2009]}:
merge = pd.merge(df1,df2)
print(merge)
