import json, os, sys
from neo4j import GraphDatabase

credentialsDict = {"username":"password",
                   "admin":"password"} 

def addUser(username='', password=''):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    with driver.session() as session:
        session.run("CREATE (n:User {name: $name, password: $password})", name=username, password=password)
    print(f'created new user:[{username}, {password}]')
    driver.close()
    return 0

def addCredentials(credentialsDict):
    with open('credentials.json', 'a') as f:
        json.dump(credentialsDict, f)

def deleteCredentials(credentialsDict, delName):
    with open('credentials.json', 'r') as f:
        credentialsDict = json.load(f)
        del credentialsDict[delName]
    with open('credentials.json', 'w') as f:
        json.dump(credentialsDict, f)

def loginHelper(username='public', password='public'):
    return 

if __name__ == "__main__":
    addUser(username='adduser', password='password')