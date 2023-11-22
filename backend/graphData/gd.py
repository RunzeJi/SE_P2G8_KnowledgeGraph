import json

json_path = "../SE_P2G8_KnowledgeGraph/backend/graphData/gd.json"

graphDataPy = {
    "nodes": [
        {"cNumber": 120, "category": 0, "name": "A1"},
        {"cNumber": 120, "category": 0, "name": "A2"},
        {"cNumber": 100, "category": 1, "name": "B1"},
        {"cNumber": 100, "category": 1, "name": "B2"},
        {"cNumber": 80, "category": 2, "name": "C1"},
        {"cNumber": 80, "category": 2, "name": "D1"},
        {"cNumber": 80, "category": 3, "name": "E1"},
        {"cNumber": 80, "category": 3, "name": "F1"},
        {"cNumber": 80, "category": 2, "name": "C2"},
        {"cNumber": 80, "category": 2, "name": "D2"},
        {"cNumber": 80, "category": 3, "name": "E2"},
        {"cNumber": 80, "category": 3, "name": "F2"},
    ],
    "links": [
        {"name": "TO", "source": "B1", "target": "A1"},
        {"name": "TO", "source": "C1", "target": "B1"},
        {"name": "TO", "source": "D1", "target": "B1"},
        {"name": "TO", "source": "E1", "target": "D1"},
        {"name": "TO", "source": "F1", "target": "D1"},
        {"name": "TO", "source": "B2", "target": "A2"},
        {"name": "TO", "source": "C2", "target": "B2"},
        {"name": "TO", "source": "D2", "target": "B2"},
        {"name": "TO", "source": "E2", "target": "D2"},
        {"name": "TO", "source": "F2", "target": "D2"},
        {"name": "TO", "source": "F2", "target": "D1"},
    ]
}

def readGD():
    with open(json_path, "r") as f:
        return json.loads(f.read())

############################## Experimental ################################
def getNodes():
    with open(json_path, "r") as f:
        return json.loads(f.read())["nodes"]

def getLinks():
    with open(json_path, "r") as f:
        return json.loads(f.read())["links"]
    
def appendNode_(cNumber, category, name):
    allNodes = getNodes()
    nodeToAppend = {'cNumber': cNumber, 'category': category, 'name': name}
    allNodes.append(nodeToAppend)
    uniqueNodes = list(set(allNodes))

    if cNumber or category or name != None:
        print('Node Added\n')
        return uniqueNodes
    else:
        print('Cannot Add EMPTY Node\n')
        return getNodes()

def appendNode(cNumber, category, name):
    allNodes = getNodes()
    nodeToAppend = {'cNumber': cNumber, 'category': category, 'name': name}
    
    # Convert each dictionary to a tuple
    allNodes_tuples = [tuple(node.values()) for node in allNodes]
    nodeToAppend_tuple = tuple(nodeToAppend.values())
    
    # Add the tuple to the list
    allNodes_tuples.append(nodeToAppend_tuple)
    
    # Convert the list of tuples back to a list of dictionaries
    uniqueNodes = [dict(zip(['cNumber', 'category', 'name'], tpl)) for tpl in set(allNodes_tuples)]

    if cNumber or category or name is not None:
        print('Node Added\n')
        return uniqueNodes
    else:
        print('Cannot Add EMPTY Node')
        return getNodes()



def appendLink_(name, source, target):
    allLinks = getLinks()
    linkToAppend = {'name': name, 'source': source, 'target': target}
    allLinks.append(linkToAppend)
    uniqueLinks = list.set(allLinks)
    
    if name and source and target != None:
        print('Link Added\n')
        return uniqueLinks
    else:
        print('Cannot Add EMPTY Link\n')
        return getLinks()
    
def appendLink(name, source, target):
    allLinks = getLinks()
    linkToAppend = {'name': name, 'source': source, 'target': target}
    
    # Convert each dictionary to a tuple
    allLinks_tuples = [tuple(link.values()) for link in allLinks]
    linkToAppend_tuple = tuple(linkToAppend.values())
    
    # Add the tuple to the list
    allLinks_tuples.append(linkToAppend_tuple)
    
    # Convert the list of tuples back to a list of dictionaries
    uniqueLinks = [dict(zip(['name', 'source', 'target'], tpl)) for tpl in set(allLinks_tuples)]
    
    if name and source and target != None:  
        print('Link Added\n')
        return uniqueLinks
    else:
        print('Cannot Add EMPTY Link')
        return getLinks()


def appendGD(nodes, links):
        with open(json_path, "w") as f:
            f.write(json.dumps({"nodes": nodes, "links": links}, indent=4))


if __name__ == "__main__":
    #print(getNodes())

    #appendNode(cNumber=1000, category='0', name='default node')
    #appendLink(name="TO", source="default node", target='A1')
    appendGD(appendNode(cNumber=1145, category=0, name='default node'), appendLink(name="TO", source="sad", target='bad'))