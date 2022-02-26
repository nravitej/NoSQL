import pymongo as pymongo

client = pymongo.MongoClient("mongodb+srv://nravitej:1234@cluster0.m0suk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['myFirstDatabase']
country_set = db.countries
conti=db.continents
#List of countries starting with Letter 'I'
print("List of countries starting with Letter 'I'")
resultu=country_set.find({"name":{"$regex":'^I'}})
for doc in resultu:
    print(doc["name"])
#List of countries ending with Letter 'A'
print("List of countries ending with Letter 'A'")
resultu=country_set.find({"name":{"$regex":'A$'}})
for doc in resultu:
    print(doc["name"])

#List of countries having fr in their name
print("List of countries having fr in their name")
resultu=country_set.find({"name":{"$regex":'fr',"$options":'i'}})
for doc in resultu:
    print(doc["name"])

#Count of countries continents wise
print("Count of countries continents wise")
resultu=conti.find()
for doc in resultu:
    print("Continent:"+doc["name"]+", Number of Countries:"+" ",len(doc["countries"]))

#Fetch Continents and countries in alphabetical order
print("\n \n Fetch Continents and countries in alphabetical order\n")
result=conti.find()
CL=[]
for doc in result:
    countries=country_set.find({"_id":{"$in":doc["countries"]}}).sort("name")
    dl=[]
    for d in countries:
        dl.append(d["name"])
    print("Continent:"+doc["name"]+","+"Countries"+"[",dl,"]")




#Drop a column from Mongo DB
#resultu=country_set.update_many( { }, { '$unset': { "population": '' } } )

#Add a column to the Mongo DB
#resultu=country_set.update_many( { }, { '$set': { "population": 0 } } )

#The less populated to Most populated
print("\n \n The less populated to Most populated\n")
resultCountry=country_set.find().sort("population")
countryList=[]
for doc in resultCountry:
    print("country:"+doc["name"],","+"population:",doc["population"])

#Get countries having u in name with more than 100000
print("\n \n Get countries having u in name with more than 100000\n")
result=country_set.find({"name":{"$regex":'u',"$options":'i' } ,"population":{'$gt':100000}})
for doc in result:
    print("country:"+doc["name"],","+"population:",doc["population"])