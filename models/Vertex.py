class Vertex:
    def __init__(self, node):
        super().__init__()
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def get_all_weights(self):
        for key in self.get_connections():
            keyId = key.get_id()
            print(str(self.id) + " adjacent: [" + str(keyId
                                                      ) + ":" + str(self.get_weight(key)) + "]")
