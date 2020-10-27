from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
import numpy as np
import json
import csv
import os
#import pandas as pd
from ibm_watson import ApiException


## Nake it ready for API connect and invoke Watson Discovery from IBM watson.
authenticator = BasicAuthenticator('apikey','98Z--LAY9-a5ommWX0AlFbM8n5jWxfT1N-8kKXenZAyT')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

## Input the correct Url and necessary parameteres to Smart Document understaning.
discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')
environment_id="db7ac563-034e-4238-b434-a2e704572824"
configuration_id="60b1bb05-851a-4a5d-b9db-83321f830ee3"
collection_id="a591d798-c060-4b67-9f9c-90e6974001a6"

## Input the desired word or sentence which you would like to query through SDU.
prefix="Torsk"

## Conduct the query in SDU.
data = discovery.query(environment_id, collection_id, natural_language_query="torsk").get_result()
file=json.dumps(data, indent=2)

#print(type(file))
#print(file["results"].json())


## We have downloaded the json file as a result of query.
## We aims to print out the whole result in form of Excel file.
with open("query.json") as data_file:
    data = json.load(data_file)
    #print(json.dumps(data, indent=2))
#print(data["results"][0]["tables"])
#print(data["results"])
#print(data)
#print("----------------")
#print(data["results"][0]["tables"])
#print("----------------")
##print(data["results"])
#rint(np.size(data["results"]))
print("----------------")
for item in data["results"][0]["tables"]:
    #print(json.dumps(item["table_text"], indent=2))
    print(item["table_text"])
    #data2=item["tables"]
data2=[]



for x in range(0, 5):
    for y in range (0,1):
        print(data["results"][0]["tables"][x]["body_cells"])
        data2.append(data["results"][0]["tables"][x]["body_cells"])
        #print(data["results"][0]["tables"][x]["body_cells"][y])
print("-....------")
print(data2)
for z in range(0,5):
    for i in data2[z]:
        #print(json.dumps(i["row_min"], indent=2),json.dumps(i["column_min"], indent=2),json.dumps(i["row_max"], indent=2),json.dumps(i["column_max"], indent=2))
        print(i["row_max"],i["row_min"],i["column_max"],i["column_min"])
        print("THE ROW IS: ",i["row_max"],i["row_min"], "THE COLUMN IS:",i["column_max"],i["column_min"])
        print("----------")













    #data2=item["tables"]
#print("sdfasdfa",data2)








    

#query=pd.read("query.json")
#print(query)
#print(file)
#print (len(data))
#print(str(data))
#print(data)
#print(data.keys())
#print(data[])
#print(data.get('results'))
#data_results=data.get('results')
#print(type(data_results))
#data_results_tables=data_results[0]['tables']
#print(data_results_tables)
#print(data_results_tables[1])
#rint(type(data_results_tables[0]))
#print (data['results'])
#data.get('tables', default=None)








