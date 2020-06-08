from fastapi import FastAPI
from pymongo import MongoClient
from pprint import pprint
import googlemaps
from models.Graph import Graph
from models.Location import Location
# Data Connection
client = MongoClient(
    'mongodb+srv://mikewong3:Mikewong1234@visitorappdb-h5z9b.mongodb.net')
db = client.VisitorApp
savedLocationsCollection = db["savedLocations"]
gmaps = googlemaps.Client(key="AIzaSyDB0vvrNozsGFZD6lD97DTD3oKhtHTZRxk")

# for x in savedLocationsCollection.find():
#     print(x)

locations_dic = {}


def generateGraph():
    locations_graph = Graph()
    for location in savedLocationsCollection.find():
        locations_graph.add_vertex(location["locationId"])
        if location['locationId'] not in locations_dic:
            locations_dic[location['locationId']] = tuple(
                location['geoCordinates'])
    distance_matrix = gmaps.distance_matrix(locations_dic.values(
    ), locations_dic.values(), units="imperial", mode="walking")
    vertexCounter = 0
    list_loc_keys = list(locations_dic.keys())
    for row in distance_matrix['rows']:
        edgesCounter = 0
        for element in row['elements']:
            if edgesCounter != vertexCounter:
                distance = float(element['distance']['text'][:4].strip())
                locations_graph.add_edge(
                    list_loc_keys[vertexCounter], list_loc_keys[edgesCounter], distance)
            edgesCounter += 1
        vertexCounter += 1
    return locations_graph


Graph = generateGraph()

for vertex in Graph:
    vertex.get_all_weights()


# Google map distnace calls
# geocode_result = gmaps.distance_matrix([(
#     38.9993857, -77.40703049999999), ((39.1711123, -77.2615837))], [(39.1711123, -77.2615837)], units="imperial")

# print(geocode_result)
# API Route
# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
