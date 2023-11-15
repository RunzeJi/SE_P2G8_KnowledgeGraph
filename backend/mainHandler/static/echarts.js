var dom = document.getElementById('container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

  let data = {
  nodes: [{
		"cNumber": 20207,
		"category": 0,
		"name": "custom/data/service1-aliyun/vault-activemq"
	}, {
		"cNumber": 20207,
		"category": 1,
		"name": "service1-aliyun"
	}, {
		"cNumber": 2248,
		"category": 2,
		"name": "192.168.44.73"
	}, {
		"cNumber": 2247,
		"category": 2,
		"name": "192.168.44.76"
	}, {
		"cNumber": 2247,
		"category": 2,
		"name": "192.168.48.186"
	}, {
		"cNumber": 2246,
		"category": 2,
		"name": "192.168.44.77"
	}, {
		"cNumber": 2244,
		"category": 2,
		"name": "192.168.44.74"
	}, {
		"cNumber": 2244,
		"category": 2,
		"name": "192.168.44.75"
	}, {
		"cNumber": 2244,
		"category": 2,
		"name": "192.168.48.184"
	}, {
		"cNumber": 2244,
		"category": 2,
		"name": "192.168.48.187"
	}, {
		"cNumber": 2243,
		"category": 2,
		"name": "192.168.48.185"
	}, {
		"cNumber": 9743,
		"category": 0,
		"name": "cloud/data/devops-service1/tencent-service2"
	}, {
		"cNumber": 9743,
		"category": 1,
		"name": "devops-service1"
	}, {
		"cNumber": 2244,
		"category": 2,
		"name": "192.168.129.172"
	}, {
		"cNumber": 1893,
		"category": 2,
		"name": "192.168.0.117"
	}, {
		"cNumber": 1844,
		"category": 2,
		"name": "192.168.6.149"
	}, {
		"cNumber": 3869,
		"category": 0,
		"name": "custom/data/service1-tencent/vault-activemq"
	}, {
		"cNumber": 3869,
		"category": 1,
		"name": "service1-tencent"
	}, {
		"cNumber": 1926,
		"category": 2,
		"name": "192.169.35.217"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.32.2"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.33.118"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.33.59"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.34.153"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.34.99"
	}, {
		"cNumber": 150,
		"category": 2,
		"name": "192.169.35.122"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.32.151"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.33.165"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.33.197"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.33.238"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.33.84"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.35.152"
	}, {
		"cNumber": 149,
		"category": 2,
		"name": "192.169.35.172"
	}, {
		"cNumber": 9743,
		"category": 0,
		"name": "custom/data/devops-service1/ci-jiratool"
	}, {
		"cNumber": 1906,
		"category": 2,
		"name": "192.168.13.11"
	}, {
		"cNumber": 1856,
		"category": 2,
		"name": "192.168.13.95"
	}, {
		"cNumber": 9743,
		"category": 0,
		"name": "cloud/data/devops-service1/tencent-service1"
	}],
	links: [{
		"name": "20207",
		"source": "service1-aliyun",
		"target": "custom/data/service1-aliyun/vault-activemq"
	}, {
		"name": "2248",
		"source": "192.168.44.73",
		"target": "service1-aliyun"
	}, {
		"name": "2247",
		"source": "192.168.44.76",
		"target": "service1-aliyun"
	}, {
		"name": "2247",
		"source": "192.168.48.186",
		"target": "service1-aliyun"
	}, {
		"name": "2246",
		"source": "192.168.44.77",
		"target": "service1-aliyun"
	}, {
		"name": "2244",
		"source": "192.168.44.74",
		"target": "service1-aliyun"
	}, {
		"name": "2244",
		"source": "192.168.44.75",
		"target": "service1-aliyun"
	}, {
		"name": "2244",
		"source": "192.168.48.184",
		"target": "service1-aliyun"
	}, {
		"name": "2244",
		"source": "192.168.48.187",
		"target": "service1-aliyun"
	}, {
		"name": "2243",
		"source": "192.168.48.185",
		"target": "service1-aliyun"
	}, {
		"name": "9743",
		"source": "devops-service1",
		"target": "cloud/data/devops-service1/tencent-service2"
	}, {
		"name": "2244",
		"source": "192.168.129.172",
		"target": "devops-service1"
	}, {
		"name": "1893",
		"source": "192.168.0.117",
		"target": "devops-service1"
	}, {
		"name": "1844",
		"source": "192.168.6.149",
		"target": "devops-service1"
	}, {
		"name": "3869",
		"source": "service1-tencent",
		"target": "custom/data/service1-tencent/vault-activemq"
	}, {
		"name": "1926",
		"source": "192.169.35.217",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.32.2",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.33.118",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.33.59",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.34.153",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.34.99",
		"target": "service1-tencent"
	}, {
		"name": "150",
		"source": "192.169.35.122",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.32.151",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.33.165",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.33.197",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.33.238",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.33.84",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.35.152",
		"target": "service1-tencent"
	}, {
		"name": "149",
		"source": "192.169.35.172",
		"target": "service1-tencent"
	}, {
		"name": "9743",
		"source": "devops-service1",
		"target": "custom/data/devops-service1/ci-jiratool"
	}, {
		"name": "1906",
		"source": "192.168.13.11",
		"target": "devops-service1"
	}, {
		"name": "1856",
		"source": "192.168.13.95",
		"target": "devops-service1"
	}, {
		"name": "9743",
		"source": "devops-service1",
		"target": "cloud/data/devops-service1/tencent-service1"
	}]
 
}
 
const color1 = '#006acc';
const color2 = '#ff7d18';
const color3 = '#45b97c';
 
data.nodes.forEach(node => {
  if (node.category === 0) {
    node.symbolSize = 70;
    node.itemStyle = {
      color: color1
    };
  } else if (node.category === 1) {
    node.symbolSize = 50;
    node.itemStyle = {
      color: color2
    };
  } else if (node.category === 2) {
    node.symbolSize = 30;
    node.itemStyle = {
      color: color3
    };
  }
  node.symbolSize = node.symbolSize + node.cNumber/1000
  node.open = false
});
 
data.links.forEach(link => {
  link.label = {
    align: 'center',
    fontSize: 12
  };
 
});
 
let categories = [{
    name: '路径',
    itemStyle: {
        color: color1
    }
  },
  {
    name: '目标对象',
    itemStyle: {
        color: color2
    }
},
{
    name: '客户端IP',
    itemStyle: {
        color: color3
    }
}]
 
option = {
  title: {
    text: '关系图谱',
  },
  legend: [{
    data: categories.map(x => x.name),
  }],
  series: [{
    type: 'graph',
    layout: 'force',
    symbolSize: 58,
    draggable: true,
    roam: true,
    focusNodeAdjacency: true,
    categories: categories,
    edgeSymbol: ['', 'arrow'],
    // edgeSymbolSize: [80, 10],
    edgeLabel: {
      normal: {
        show: true,
        textStyle: {
          fontSize: 20
        },
        formatter(x) {
          return x.data.name;
        }
      }
    },
    label: {
      fontSize: 12,
        show: true
    },
    force: {
      repulsion: 2000,
      edgeLength: 120
    },
    data: data.nodes,
    links: data.links
  }]
}
 
myChart.setOption(option);
bindChartClickEvent(myChart);
 
/**
 * 绑定图表的点击事件
 * @param chart
 */
function bindChartClickEvent(chart) {
    chart.on('click', function (params) {
        var category = params.data.category,
            nodeType = params.data.nodeType;
            toggleShowNodes(chart, params);
    });
    
    for (var j = 0; j < data.nodes.length; j++) {
      if (data.nodes[j].category !==  0 ) {
          data.nodes[j].data = {};
          data.nodes[j].seriesIndex=0;
          data.nodes[j].open=false;
          data.nodes[j].category=-1;
          toggleShowNodes(chart, data.nodes[j]);
      }
    }
}
 
/**
 * 展开或关闭节点
 * @param chart
 * @param params
 */
function toggleShowNodes(chart, params) {
    var open = !!params.data.open,
        options = chart.getOption(),
        seriesIndex = params.seriesIndex,
        srcLinkName = params.name,
        serieLinks = options.series[seriesIndex].links,
        serieData = options.series[seriesIndex].data,
        serieDataMap = new Map(),
        serieLinkArr = [];
    // 当前根节点是展开的，那么就需要关闭所有的根节点
    if (open) {
        // 递归找到所有的link节点的target的值
        findLinks(serieLinkArr, srcLinkName, serieLinks, true);
        if (serieLinkArr.length) {
            serieData.forEach(sd => serieDataMap.set(sd.name, sd));
            for (var i = 0; i < serieLinkArr.length; i++) {
                if (serieDataMap.has(serieLinkArr[i])) {
                    var currentData = serieDataMap.get(serieLinkArr[i]);
                    currentData.category = -Math.abs(currentData.category);
                }
            }
            
            serieDataMap.get(srcLinkName).open = false;
            chart.setOption(options);
        }
    } else {
        // 当前根节点是关闭的，那么就需要展开第一层根节点
        findLinks(serieLinkArr, srcLinkName, serieLinks, true);
        if (serieLinkArr.length) {
            serieData.forEach(sd => serieDataMap.set(sd.name, sd));
            for (var j = 0; j < serieLinkArr.length; j++) {
                if (serieDataMap.has(serieLinkArr[j])) {
                    var currentData = serieDataMap.get(serieLinkArr[j]);
                    currentData.category = Math.abs(currentData.category);
                }
            }
            serieDataMap.get(srcLinkName).open = true;
            chart.setOption(options);
        }
    }
}
 
/**
 * 查找连接关系
 * @param links 返回的节点放入此集合
 * @param srcLinkName 源线的名称
 * @param serieLinks 需要查找的集合
 * @param deep 是否需要递归进行查找
 */
function findLinks(links, srcLinkName, serieLinks, deep) {
    var targetLinks = [];
    serieLinks.filter(link => link.target === srcLinkName).forEach(link => {
        targetLinks.push(link.source);
        links.push(link.source)
    });
    if (deep) {
        for (var i = 0; i < targetLinks.length; i++) {
            findLinks(links, targetLinks[i], serieLinks, deep);
        }
    }
}

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);