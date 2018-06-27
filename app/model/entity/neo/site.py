from py2neo.ogm import GraphObject,Property

class Site(GraphObject):
    
    id = Property()
    siteId = Property()

    def __init__(self, id, siteId):
        self.id = id
        self.siteId = siteId