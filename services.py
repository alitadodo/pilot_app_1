from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId
fake = Faker()
mongo_uri = "mongodb+srv://admin:admin@c4e28-cluster-725hk.mongodb.net/test?retryWrites=true"

#1. Collect to cluster
client = MongoClient(mongo_uri)

#2. Get / Create database
service_database = client.db_service

3#. Get / Create collection
Services = service_database["services"]

#4. Create document, insert document
# for i in range(50):
#     new_service = {
#         "name":fake.name(),
#         "age": randint(18, 30),
#         "address": fake.address(),
#         "gender": choice(["male", "female"]),
#         "available": choice([True, False]),
#     }
#     service_collection.insert_one(new_service)
#     print("Saving document {0}.....".format(i+1))

# 5.Read
# 5.1 Read all
# all_services = Services.find() #Lazy loading
# print(all_services) #Same list
# print(all_services[0])
# for services in all_services:
#     print(services["name"])

# 5.2 Read only One
# one_service = Services.find_one({"name": "Laura Lee"})
# one_service = Services.find_one({"_id": ObjectId("5c9a1d6fc054f410b8505bec")})
# print(one_service)


#6. DELETE
# service = Services.find_one({"_id": ObjectId("5c9a1d6fc054f410b8505bee")})
# if service is not None:
#     Services.delete_one(service)
# else:
#     print("Not found document!")
# print(service)

#7. Update

one_service = Services.find_one({"_id": ObjectId("5c9a1d70c054f410b8505bf0")})
new_value = { "$set": { "gender": "male" } }
Services.update_one(one_service, new_value)

