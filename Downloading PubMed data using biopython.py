# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:53:18 2022

@author: Andrew
"""
# This script allows you to perform a keyword search with BioPython and download all data into a csv file
# Script was modified from here: https://towardsdatascience.com/network-analysis-to-quickly-get-insight-into-an-academic-field-with-python-cd891717d547

from Bio import Entrez
from Bio import Medline
from tqdm import tqdm
import pandas as pd 

# Change this email to your email address
Entrez.email = "my_email@gmail.com"

# Add keyword here
keyword = "Staphylococcus aureus"

# Change retmax if you want more publications returned from your search
result = Entrez.read(Entrez.esearch(db="pubmed", retmax=200, term=keyword))
print(
    "Total number of publications that contain the term {}: {}".format(
        keyword, result["Count"]
    )
)

# Fetch all ids
MAX_COUNT = result["Count"]
result = Entrez.read(
    Entrez.esearch(db="pubmed", retmax=result["Count"], term=keyword)
)

ids = result["IdList"]

batch_size = 100
batches = [ids[x: x + 100] for x in range(0, len(ids), batch_size)]

record_list = []
for batch in tqdm(batches):
    h = Entrez.efetch(db="pubmed", id=batch, rettype="medline", retmode="text")
    records = Medline.parse(h)
    record_list.extend(list(records))
print("Complete.")

#%%
# Export publication data into a dataframe and into a csv file
publication_data = pd.DataFrame(record_list)
publication_data.dropna(subset=['EDAT'], inplace=True)
publication_data["Year"] = (
    publication_data["EDAT"].astype(str).str[0:4].astype(int)
)


publication_data.to_csv("pubmed_data.csv")
