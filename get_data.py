from scrapy import *
import pandas as pd
import os

### Glassdoor #########################

ds_links_gd, ds_ids_gd = crawl_gd()
stats_links_gd, stats_ids_gd = crawl_gd(q='stats')
ds_links_gd, stats_links_gd = remove_duplicates(ds_links_gd,stats_links_gd,ds_ids_gd,stats_ids_gd)

ds_df_gd = get_gd_df(ds_links_gd)
stats_df_gd = get_gd_df(stats_links_gd)


### Kaggle ############################

ds_links_kg, ds_ids_kg = crawl_kg()
ds_df_kg = get_kg_df(ds_links_kg)


### LinkedIn ##########################

ds_links_li, ds_ids_li = crawl_li()
stats_links_li, stats_ids_li = crawl_li(q='stats')

ds_links_li, stats_links_li = remove_duplicates(ds_links_li,stats_links_li,ds_ids_li,stats_ids_li)

ds_df_li = get_li_df(ds_links_li)
stats_df_li = get_li_df(stats_links_li)



### Update tables #####################

files= {'DS_Kaggle.csv':ds_df_kg,
       'DS_Glassdoor.csv':ds_df_gd,
       'DS_LinkedIn.csv':ds_df_li,
       'STATS_Glassdoor.csv':stats_df_gd,
       'STATS_LinkedIn.csv':stats_df_li}


for file in files.keys():
    if os.path.isfile(file):
        df_big = pd.read_csv(file)
        df_new = files[file]
        df_updated = remove_dup_rows(df_big,df_new)
        df_updated.to_csv(file)
    else:
        files[file].to_csv(file)
