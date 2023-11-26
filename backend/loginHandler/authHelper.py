import json, os, sys
from neo4j import GraphDatabase, basic_auth, exceptions

credentialsDict = {"username":"password",
                   "admin":"password"} 
userlist_path = "../SE_P2G8_KnowledgeGraph/backend/db_manipulate/userList.json"

def addUser(username='', password=''):

    with open(userlist_path, 'r') as f:
        userDict = json.loads(f.read())
        userDict[username] = password
        print(userDict)
        f.close()
    
    with open(userlist_path, 'w') as f:
        json.dump(userDict, f, indent=4)
        f.close()

    sudoDriver = GraphDatabase.driver("bolt://localhost:7687/neo4j", auth=("neo4j", "sudoDriver"))
    try:
        with sudoDriver.session() as session:
            session.run(f"CREATE USER {username} SET PASSWORD '{password}' CHANGE NOT REQUIRED")
            #session.run(f"ALTER USER {username} SET PASSWORD '{password}'")
            print(f'created new user:[{username}, {password}]')
            sudoDriver.close()

        with open(userlist_path, 'r') as f:
            userDict = json.loads(f.read())
            userDict[username] = password
            print(userDict)

    except Exception as e:
        print(e)

def detectLogin(user, password):
    with open(userlist_path, 'r') as f:
        userDict = json.loads(f.read())
        print(userDict)
        try:
            if password == userDict[user]:
                print(f"\n{user} ==> Login Success\n")
                try:
                    userDriver = GraphDatabase.driver("bolt://localhost:7687/neo4j", auth=(user, password))
                    print(f"sudoDriver connected as {user}\n")
                    return True
                except exceptions as e:
                    print(e)
                    return False
            else:
                print(f"\n{user} ==> Login Failed\n")
                return False
        except KeyError as e:
            if e != 0:
                print(f"\n{user} ==> Login Failed\n")
                return False

###########################################################################
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
    #addUser('ni', 'password')
    print(detectLogin('admin', 'password'))
    