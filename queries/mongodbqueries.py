# Install pymongo
# pip install pymongo
# importing the required libraries to study our database
import pymongo
import pprint
import json
import warnings
warnings.filterwarnings('ignore')

# connect to the mongoclient
client = pymongo.MongoClient('mongodb://localhost:27017')

# get the database
french_admin_db = client['French_admin']
#
gov_collection = french_admin_db.governments
# First query
gov_collection.find_one({'Name of the Prime Minister': 'Jules Ferry'})

# Second query 
gov_deux_mille_dix = gov_collection.find({
    "Date" : { "$eq" : 1972}
})
for i in gov_deux_mille_dix:
    print(i)
	
# Third query
previous_century_gov = gov_collection.find({“Date” : { "$lt" : 2000, "$gt" : 1901}})
for i in previous_century_gov:
	print(i)

# Fourth query
gov.collection.sort({field: -1})

# Fitfth query
gov.collection.find({}, {
Date: 1}).sort({ Date:-1}).limit(1)
