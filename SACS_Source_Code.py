import pandas as pd
a=pd.read('Attend.csv','w')
b=pd.read('on_site.csv','w')
c=pd.concat([a,b]).drop_duplicates(keep=False)
c.to_csv('Dis.csv',index=False)