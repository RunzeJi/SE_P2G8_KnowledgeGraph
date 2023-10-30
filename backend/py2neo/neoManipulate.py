import py2neo

neoHost = "localhost"
p2nUsername = "py2neo"
p2nPassword = "password"

# Initializes the connection to Neo4j and creates an 'graph' object (创建'graph'对象)
graph = py2neo.Graph(host="localhost", user=p2nUsername, password=p2nPassword)

def sendCypherQL(cypherQL="MATCH (n) RETURN n LIMIT 5"):#
    graph = py2neo.Graph(host="localhost", user=p2nUsername, password=p2nPassword)
    graph.run(cypherQL)
    print(f'cypher ==> {cypherQL}')

# Connect neo4j & Create a node (创建一个节点)
def createNeoNode():
    # connect to neo4j
    graph = py2neo.Graph(host="localhost", user=p2nUsername, password=p2nPassword)
    # create a node
    graph.run("CREATE (n:Person {name:'Alice', age:33})")
    # return the results
    return graph.run("MATCH (n) RETURN n LIMIT 5")

# this function uses module 'py2neo' to connect to neo4j and get the results of a query(获取结果)
def getNeoResult(numOfReturns=5, numOfReturnLimit=5):
    # connect to neo4j
    graph = py2neo.Graph(host="localhost", user=p2nUsername, password=p2nPassword)
    # get the results of the query
    result = graph.run(f"MATCH (n) RETURN n LIMIT {numOfReturnLimit}")
    
    print(f'getNeoResult() ==> {cmd}')
    # return the results
    return result

def clearDatabase():
    graph = py2neo.Graph(host="localhost", user=p2nUsername, password=p2nPassword)
    graph.run("MATCH (n) DETACH DELETE n")

#print(getNeoResult())
#print(type(getNeoResult()))
#getNeoResult()
#clearDatabase()
sendCypherQL(cypherQL="CREATE (n:Person {name:'Alice', age:33})")
getNeoResult()