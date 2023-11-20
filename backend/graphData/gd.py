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
