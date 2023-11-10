# SE_P2G8_KnowledgeGraph
##### This repo is also in other languages: [简体中文](https://github.com/Sthrumbee/SE_P2G8_KnowledgeGraph/blob/main/README_zh_cn.md)

#### Usage - 使用方法
0.Follow **I.Pre-Installation** Steps and configure environments like Neo4j Server and JDK17.

&ensp;&ensp;&ensp;&ensp;(跟随**I.Pre-Installation**中介绍的步骤配置Neo4j Server 和 JDK17 等软件环境。)

1.Entrypoint: Run **"../backend/mainHandler/mainHandler.py"**. Make sure you have installed the required modules using **pip**.

&ensp;&ensp;&ensp;&ensp;(程序入口：运行 **"../backend/mainHandler/mainHandler.py"**。确保已经使用 **pip**安装了必须的Python模块。)

2.Go to [http://localhost:8000/login](http://localhost:8000/login) on your local machine.

&ensp;&ensp;&ensp;&ensp;(在本地宿主机上打开[http://localhost:8000/login](http://localhost:8000/login))


## I. Pre-Installation
### For Windows 10 and later
0.Download and install JDK17 from Oracle or OpenJDK（在Oracle或者OpenJDK官网下载JDK17并安装）

1.Download the Neo4j Community Server from [Official Website](https://neo4j.com/deployment-center/) or download directly from [here(Windows)](https://go.neo4j.com/download-thanks.html?edition=community&release=5.12.0&flavour=winzip)（在Neo4j Deployment Center中，前往"Graph DatabaseSelf-Managed"区域，"Community"标签下下载适用于Windows的zip压缩包，或者点击[此链接](https://go.neo4j.com/download-thanks.html?edition=community&release=5.12.0&flavour=winzip)直接下载Windows版）

2.Unzip the downloaded zip file, you'll get a folder containing the essential files for installing the Neo4j Server.（解压下载好的zip文件）

3.Go to the **\bin** directory and open the **neo4j.bat** file with Command Prompt (CMD.exe)（前往该文件夹的中的 **\bin** 目录，将命令提示符（cmd.exe）的工作路径改为当前文件夹的路径，（或者在 **\bin** 文件夹的地址栏键入cmd然后Enter））

4.Execute these commands:（执行下列指令）
    
    neo4j.bat install-service
    neo4j.bat start

5.Check if service up and running:（检查Neo4j Service 是否启动）
    
    neo4j.bat status
if **"Neo4j is running"** is shown, then you are all set.🎉（如果显示 **"Neo4j is running"**，那么你就成功了！）

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
### For macOS (Server Only, No Desktop Env)
#### First Go to the Neo4j [Deployment Center](https://neo4j.com/deployment-center/)
0.Download and install JDK17 from Oracle or OpenJDK

1.Download the macOS Version of Neo4j.

2.Extract all files.

3.Open Terminal under the extracted directory.

4.Execute commands:
    
    ./bin/neo4-admin server console

5.In browser, open [http://localhost:7474](http://localhost:7474)

6.Use [bolt://localhost:7687](bolt://localhost:7687) to connect to database.

7.To terminate server, Press **'Ctrl + C'**.
