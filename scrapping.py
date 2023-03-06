import glassdoor_scrapper as gs 
import pandas as pd 

path = "D:/DS/proj-1/chromedriver.exe"

df = gs.get_jobs('data scientist',100 , False, path, 15)
df
df.to_csv('glassdoor_jobs.csv', index = False)
