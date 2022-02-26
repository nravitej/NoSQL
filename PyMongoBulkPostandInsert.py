import pymongo as pymongo
import pprint as pprint
def connection():
    client = pymongo.MongoClient("mongodb+srv://nravitej:1234@cluster0.m0suk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #db = client.test
    db=client['myFirstDatabase']
    print(db.list_collection_names())

def continentspost(continents1):
    client = pymongo.MongoClient("mongodb+srv://nravitej:1234@cluster0.m0suk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['myFirstDatabase']
    posts=db.continents
    result=posts.insert_many(continents1)
    #print(result.inserted_ids)
    return 1
def countriespost(countries):
    client = pymongo.MongoClient("mongodb+srv://nravitej:1234@cluster0.m0suk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['myFirstDatabase']
    conti=db.continents
    country_set=db.countries
    f=conti.find_one({"name": "AUSTRALIA"})
    NoneType=type(None)
    #print()
    #pprint.pprint(f)

    for k in range(len(countries)):
        contiId=conti.find_one({"name": countries[k]["continent"]})
        if type(contiId)!=NoneType:
            print((countries[k]["continent"]))
            print(contiId['_id'])
            countries[k]["continent"]=contiId["_id"]
            #insid=country_set.insert_one(countries[k])
            #conti.update({"name": countries[k]["continent"]},{'$set':{contiId}})
    result = country_set.insert_many(countries)



    #ConCountry=conti.find({"name":continame})

    #print(result.inserted_ids)
    return 1

connection()
continents_post=[{"name":"Asia","countries":[]},
            {"name":"Europe","countries":[]},
            {"name":"Africa","countries":[]},
            {"name":"Australia","countries":[]},
            {"name":"NorthAmerica","countries":[]},
            {"name":"SouthAmerica","countries":[]}]

countries_post=[{"name":"INDIA","isocode":"IN","continent":"Asia","population":""},
                {"name":"CHINA","isocode":"CN","continent":"Asia","population":""},
                {"name":"AUSTRALIA","isocode":"AU","continent":"AUSTRALIA","population":""},
                {"name":"JAPAN","isocode":"JP","continent":"Asia","population":""},
                {"name":"FRANCE","isocode":"FR","continent":"Europe","population":""},
                {"name":"GERMANY","isocode":"DE","continent":"Europe","population":""},
                {"name":"ITALY","isocode":"IT","continent":"Europe","population":""},
                {"name":"IRELAND","isocode":"IE","continent":"Europe","population":""},
                {"name":"UnitedStates","isocode":"US","continent":"NorthAmerica","population":""},
                {"name":"CANADA","isocode":"CN","continent":"NorthAmerica","population":""},
                {"name":"Mexico","isocode":"MX","continent":"NorthAmerica","population":""},
                {"name":"Camero","isocode":"CA","continent":"Africa","population":""},
                {"name":"Nigeria","isocode":"NG","continent":"Africa","population":""},
                {"name":"SouthAfrica","isocode":"SA","continent":"Africa","population":""},
                {"name":"Egypt","isocode":"EG","continent":"Africa","population":""},
                {"name":"Brazil","isocode":"BR","continent":"SouthAmerica","population":""},
                {"name":"Argentina","isocode":"AR","continent":"SouthAmerica","population":""},
                {"name":"CHILE","isocode":"CL","continent":"SouthAmerica","population":""}]
print(countries_post[0]["continent"])
print(len(countries_post))
continentspost(continents_post)
countriespost(countries_post)