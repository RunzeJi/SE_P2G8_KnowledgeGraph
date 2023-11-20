import json, os, sys
from neo4j import GraphDatabase, basic_auth

credentialsDict = {"username":"password",
                   "admin":"password"} 

def addUser(username='', password=''): # Working
    sudoDriver = GraphDatabase.driver("bolt://localhost:7687/neo4j", auth=("neo4j", "sudoDriver"))
    try:
        with sudoDriver.session() as session:
            session.run(f"CREATE USER {username} SET PASSWORD '{password}'")
            #session.run(f"ALTER USER {username} SET PASSWORD '{password}'")
            print(f'created new user:[{username}, {password}]')
            sudoDriver.close()
    except Exception as e:
        print(e)



def addCredentials(credentialsDict):
    with open('credentials.json', 'a') as f:
        json.dump(credentialsDict, f)

def deleteCredentials(credentialsDict, delName):
    with open('credentials.json', 'r') as f:
        credentialsDict = json.load(f)
        del credentialsDict[delName]
    with open('credentials.json', 'w') as f:
        json.dump(credentialsDict, f)

if __name__ == "__main__":
    addUser('niggass', 'password')