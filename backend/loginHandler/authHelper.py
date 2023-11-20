import json, os, sys
from neo4j import GraphDatabase, basic_auth

credentialsDict = {"username":"password",
                   "admin":"password"} 
userlist_path = "../SE_P2G8_KnowledgeGraph/backend/db_manipulate/userList.json"

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

def detectLogin(user, password): # Working
    with open(userlist_path, 'r') as f:
        userDict = json.loads(f.read())
        print(userDict)
        try:
            if password == userDict[user]:
                print(f"\n{user} ==> Login Success\n")
                return True
            else:
                print(f"\n{user} ==> Login Failed\n")
                return False
        except KeyError as e:
            if e != 0:
                print(f"\n{user} ==> Login Failed\n")
                return False
        

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
    #addUser('niggass', 'password')
    print(detectLogin('admin', 'password'))
    