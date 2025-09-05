import pandas as pd
import os

# create a sample data with coluns name
data = {'Name':['Alice','Bob','charlie'],
        'Age':[25,28,30],
        'city':['New York','Los Angeles','Chicago']
        }
df =pd.DataFrame(data)

data_dir ='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"CSV FIle saved to{file_path}")