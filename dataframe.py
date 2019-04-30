import pandas as pd


URL = ('https://data.wprdc.org/dataset/ad5bd3d6-1b53-4ed0-8cd9-157a985bd0bd'
       '/resource/53211313-01c9-46e2-b520-a5748a10fd7c/download/2018.csv')


data = pd.read_csv(URL)


headers = ['Breed', 'Color', 'DogName', 'ExpYear', 'LicenseType', 'OwnerZip', 'ValidDate']


if set(list(data.columns.values)) != set(headers):
    raise ValueError('Column names do not meet expectations.')
