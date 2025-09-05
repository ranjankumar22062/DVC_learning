import pandas as pd
import os

# create a sample data with coluns name
data = {'Name':['Alice','Bob','charlie'],
        'Age':[25,28,30],
        'city':['New York','Los Angeles','Chicago']
        }
df =pd.DataFrame(data)
new_row_loc ={'Name':'GF','Age':20,'city':'city1'}
df.loc[len(df.index)]=new_row_loc
new_row_loc2 ={'Name':'gf2','Age':22,'city': 'newyork'}
df.loc[len(df.index)]=new_row_loc2

data_dir ='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"CSV FIle saved to{file_path}")