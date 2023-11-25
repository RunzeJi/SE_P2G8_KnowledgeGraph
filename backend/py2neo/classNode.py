import neo4j

class node:
    def __init__(self,label,property,relationship,nodeOfRelation=""):
        self.label = label
        self.property = property
        self.relationship = relationship
        self.nodeOfRelation = nodeOfRelation
    
    def __str__(self):
        return f"[\n{self.label}:{self.property},{self.relationship},{self.nodeOfRelation}\n]"
    
    def setLabel(self, settedLabel):
        self.label = settedLabel

    def addProperty(self, addedPropertyName, addedPropertyValue):
        if self.property == "":
            self.property = self.property + f"{addedPropertyName}:{addedPropertyValue}"
        else:
            self.property = self.property + f", {addedPropertyName}:'{addedPropertyValue}'"
    
    def command(self):
        return "CREATE (:" + self.label + " {" + self.property + "})"


n1 = node("Person", "name: 'Alice'", "eats", "apple")
n1.addProperty("amount_of_apples", "32")

print(n1.command())