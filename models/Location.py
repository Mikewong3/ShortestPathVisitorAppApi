class Location:
    def __init__(self, geoCordinates, placeId):
        self.geoCordinates = tuple(geoCordinates)
        self.placeId = placeId

    def getGeoCordinates(self):
        return self.geoCordinates

    def getPlaceId(self):
        return self.placeId
