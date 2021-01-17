import pandas as pd
lat = pd.read_csv('uscities.csv')
lat.head()

city_dict = dict(pd.concat([lat['city_ascii']+","+lat['state_id'].values,lat['lat'].astype(str)+","+lat['lng'].astype(str)+","+"50km"],axis=1).values)

query = {'search':['trump','biden'],#,'#biden','#trump2020','#biden2020'],
         'geoid':city_dict}
ls = []
for location,geoid in query['geoid'].items():
    for sq in query['search']:
        ls.append('twint -s "{}" -g="{}" -o {}.json --since 2020-01-01 --json\n'.format(sq,geoid,sq+"_"+location))

file1 = open("tweet_scrap.txt","a") 
file1.writelines(ls)