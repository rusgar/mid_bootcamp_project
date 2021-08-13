import pandas as pd
url = "https://github.com/rusgar/mid_bootcamp_project/blob/master/data/clean_euro_data.csv"
df = pd.read_csv(url,parse_dates=["Paises"])