import pymongo as pymongo
client = pymongo.MongoClient("mongodb+srv://nravitej:1234@cluster0.m0suk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['myFirstDatabase']
country_set = db.countries
conti=db.continents
Fconti = conti.find() #cursor holding continent data
FcontiL = []
NoneType=type(None) #variable to store type of None
for doc in Fconti:
    FcontiL.append(doc)
for k in range(len(FcontiL)):
    CL= []
    CountryList = country_set.find({"continent": FcontiL[k]["_id"]}) #cursor to hold country data per continent
    for doc in CountryList:
        if type(doc) != NoneType:
            CL.append(doc)
    CLL=[] # List to Hold group of id's belonging to a Single country
    for i in  range(len(CL)):
        CLL.append(CL[i]["_id"])
    if len(CL)!=0:
        print(CLL)
        ContiCountryAppend = conti.update_one({"_id": FcontiL[k]["_id"]},
                                              {'$set': {"countries": CLL}})


