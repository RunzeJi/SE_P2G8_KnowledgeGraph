from neo4j import GraphDatabase

# This function creates a new user in neo4j database
def create_user(tx, username, password):
    tx.run("CREATE (u:User {username: $username, password: $password})", username=username, password=password)

# This function creates a new database in neo4j
def create_database(tx, name):
    tx.run("CREATE (d:Database {name: $name})", name=name)