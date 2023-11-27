# 软件工程_题目2第8组_知识图谱
小组成员：纪润泽、田家硕、杨澍萌、吴一迪、谭维岳
[项目GitHub地址](https://github.com/RunzeJi/SE_P2G8_KnowledgeGraph)

    本README.txt的目录：
        使用方法
        I. 程序运行前准备：
            对于Windows：
            对于Linux：
            对于macOS：

        II. 代码文件目录：

        III. 第三方库：
            Python库：
                flask：
                neo4j：
                py2neo：
            JavaScript库：
                BootstrapJS：
                Nifty Stylesheet：
                Nifty Premium Icon：
                Font Awesome：
                jQuery：
                Apache ECharts：
    
    
    ### Usage - 使用方法
    0.跟随**I.Pre-Installation**中介绍的步骤配置并启动Neo4j Server 和 JDK17 等软件环境。

    1.程序入口：运行 **"../backend/mainHandler/mainHandler.py"**。运行之前确保已经使用 **pip** 安装了必须的Python模块。
    可在项目文件夹下打开终端，并执行：
        pip install -r requirements.txt

    2.在本地宿主机上打开[http://localhost:8000/login](http://localhost:8000/login)，或者在同一局域网上的其他计算机上通过该宿主机的IP访问（会在终端中的DEBUG信息中显示）


    ## I. Pre-Installation - 程序运行前准备
        
        ### 对于Windows 10 或更新版本：

            0.在Oracle或者OpenJDK官网下载JDK17并安装

            1.前往[Neo4j官网](https://neo4j.com/deployment-center/)或者直接在[这里下载适用于Windows版](https://go.neo4j.com/download-thanks.html?edition=community&release=5.12.0&flavour=winzip)，或者手动前往Neo4j Deployment Center，前往"Graph DatabaseSelf-Managed"区域，"Community"标签下下载适用于Windows的zip压缩包。

            2.解压下载好的zip文件，会得到Neo4j的程序文件。

            3.前往该文件夹的中的 **\bin** 目录，将命令提示符（cmd.exe）的工作路径改为当前文件夹的路径，（或者在 **\bin** 文件夹的地址栏键入cmd然后Enter）

            4.执行下列命令
                neo4j.bat install-service
                neo4j.bat start

            5.检查Neo4j Service 是否启动
                neo4j.bat status

            如果显示 **"Neo4j is running"**，那么你就成功了!

        
        ### 对于 Linux
            #### Debian and Ubuntu
                1.在终端中执行:
                    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
                    echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
                    sudo apt-get update

                2.然后执行:
                    sudo apt-get install neo4j

                3.检查Neo4j Server是否运行:
                    sudo systemctl status neo4j

                4.前往:
                    http://localhost:7474/

                大功告成！

        
        ### 对于 macOS (仅在Apple Silicon ARM64架构下测试，未对Intel x86架构进行测试)
            #### 首先，前往 [Neo4j Deployment Center](https://neo4j.com/deployment-center/)
                0. 下载安装JDK17

                1. 下载适用于 macOS 版的 Neo4j.

                2. 解压所有文件.

                3. 在解压好的文件夹下打开终端。

                4. 执行下列命令:
                    ./bin/neo4-admin server console

                5. 在浏览器中打开 [http://localhost:7474](http://localhost:7474)

                6.Use [bolt://localhost:7687](bolt://localhost:7687) to connect to database.

                7.To terminate server, Press **'Ctrl + C'**.
    
    
    ## II. 代码文件目录：
        backend                    存放flask、数据库操作、软件登陆等后端逻辑。
        |
        |-- db_manipulate          存放Neo4j数据库相关Driver函数。
        |   |-- db_account.py      用于Neo4j账户操作
        |   |-- db_writeNode.py    用于Neo4j数据库节点控制
        |   |-- userList.json      存放软件用户名和密码
        |
        |-- graphData              前端图谱展示相关代码和数据
        |   |-- gd.json            存放用于Apache ECharts图标的节点链接信息
        |   |-- gd.py              用于操作Apache ECharts图标的节点链接信息
        |
        |-- loginHelper            用于软件登录
        |   |-- authHelper.py      登录相关函数
        |
        |-- mainHandler            存放软件后端逻辑
        |   |-- mainHandler.py     用于定义Flask Web App的 endpoint 信息，定义全局路由
        |   |-- static             存放 Web 静态资源 （CSS、JS、字体、图片等...）
        |   |   |-- css            
        |   |   |-- fonts          
        |   |   |-- images         
        |   |   |-- js             
        |   |
        |   |-- templates          存放 HTML 文件
        |
        |-- py2neo
            |-- classNode          用于构建Node结构体
            |-- neoManipulate      用于操作Neo4j数据库


    ## III. 第三方库：
        Python库：
            flask：用于构建 Web 应用程序的Python库
            neo4j：Neo4j官方Python Driver
            py2neo：开源的Neo4j Driver

        JavaScript库：
            BootstrapJS：一个包含许多样式元素的前端HTML, CSS, JS库
            Nifty Stylesheet：一个导航式主页Bootstrap库
            Nifty Premium Icon：图标库
            Font Awesome：字体库
            jQuery：主要使用Ajax服务器相关库
            Apache ECharts：前端图谱绘制库