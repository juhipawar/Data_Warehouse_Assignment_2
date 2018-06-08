from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv

es = Elasticsearch('http://35.183.98.221:9200')
with open ("File_sentimental.csv") as elasticfilecsv:
	filereader = csv.DictReader(elasticfilecsv)
	helpers.bulk(es,filereader, index='ds', doc_type='ts')
