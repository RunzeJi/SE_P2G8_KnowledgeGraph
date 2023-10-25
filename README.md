# SE_P2G8_KnowledgeGraph
##### This repo is also in other languages: [简体中文](https://github.com/Sthrumbee/SE_P2G8_KnowledgeGraph/blob/main/README_zh_cn.md)

## I. Pre-Installation
### For Windows 10 and later
1.Download the Neo4j Community Server from [Official Website](https://neo4j.com/deployment-center/) or download directly from [here(Windows)](https://go.neo4j.com/download-thanks.html?edition=community&release=5.12.0&flavour=winzip)

2.Unzip the downloaded zip file, you'll get a folder containing the essential files for installing the Neo4j Server.

3.Go to the **/bin** directory and open the **neo4j.bat** file with Command Prompt (CMD.exe)

4.Execute these commands:
    
    neo4j.bat install-service
    neo4j.bat start

5.Check if service up and running:
    
    neo4j.bat status
if **"Neo4j is running"** is shown, then you are all set.🎉

### For Linux
#### Debian and Ubuntu
1.Execute the following code in your terminal:

    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
    echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
    sudo apt-get update

2.Then execute:

    sudo apt-get install neo4j

3.Then check if Neo4j Server is correctly installed and running:

    sudo systemctl status neo4j

4.Go to:

    http://localhost:7474/

and you are ready go.🎉
### For macOS
1.
2.
