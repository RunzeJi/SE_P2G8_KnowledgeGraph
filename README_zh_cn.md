# SE_Graphy
##### 此Repo还提供其他语言: [English][en]
## I. 准备工作
### 对于 Windows 10 及更新版本
1.从 [官网][n4jsite] 下载 Neo4j Community Server 或者在[这里][n4jwindl]直接下载。

2.将下载的zip文件解压缩，你将得到包含Neo4j Server安装的必要文件的文件夹。

3.前往名为 **/bin** 的目录，并使用命令提示符（CMD）打开 **neo4j.bat**

4.执行下列命令:
    
    neo4j.bat install-service
    neo4j.bat start

5.检查是否启动并运行:
    
    neo4j.bat status
    
如果看到： **"Neo4j is running"**，那么代表你成功了！

### 对于 Linux
#### Debian 和 Ubuntu
1.在终端中执行下列命令:

    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
    echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
    sudo apt-get update

2.然后执行:

    sudo apt-get install neo4j

3.然后检查 Neo4j Server 是否成功安装并运行:

    sudo systemctl status neo4j

4.在浏览器中前往:

    http://localhost:7474/

如果界面正常显示，那么你成功了！

[n4jsite]: https://neo4j.com/deployment-center/

[en]: https://github.com/Sthrumbee/SE_Graphy/blob/main/README.md

[n4jwindl]: https://go.neo4j.com/download-thanks.html?edition=community&release=5.12.0&flavour=winzip
