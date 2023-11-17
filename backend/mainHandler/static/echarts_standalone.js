var dom = document.getElementById('container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    var option;
	let data = 
	{
		nodes: 
  		[
			{
				"cNumber": 114,
				"category": 0,
				"name": "A"
			},
			{
				"cNumber": 114,
				"category": 1,
				"name": "B"
			},
			{
				"cNumber": 114,
				"category": 2,
				"name": "C"
			},
			{
				"cNumber": 114,
				"category": 2,
				"name": "D"
			},
    	],

		links:
		[
			{
				"name": "TO",
				"source": "B",
				"target": "A"
			},
			{
				"name": "TO",
				"source": "C",
				"target": "B"
			},
			{
				"name": "TO",
				"source": "D",
				"target": "B"
			},
		],
	};
 
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
  node.open = true
});
 
data.links.forEach(link => {
  link.label = {
    align: 'center',
    fontSize: 12
  };
 
});
 
let categories = [{
    name: '层级1',
    itemStyle: {
        color: color1
    }
  },
  {
    name: '层级2',
    itemStyle: {
        color: color2
    }
},
{
    name: '层级3',
    itemStyle: {
        color: color3
    }
}]
 
option = {
	title: {text: 'Knowledge Graph',},
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
    chart.on('click', function (params){
        var category = params.data.category,
            nodeType = params.data.nodeType;
            toggleShowNodes(chart, params);
    });
    
    for (var j = 0; j < data.nodes.length; j++)
	{
		if (data.nodes[j].category !==  0 )
		{
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
function toggleShowNodes(chart, params)
{
    var open = !!params.data.open,
        options = chart.getOption(),
        seriesIndex = params.seriesIndex,
        srcLinkName = params.name,
        serieLinks = options.series[seriesIndex].links,
        serieData = options.series[seriesIndex].data,
        serieDataMap = new Map(),
        serieLinkArr = [];
    // 当前根节点是展开的，那么就需要关闭所有的根节点
    if (open)
	{
        // 递归找到所有的link节点的target的值
        findLinks(serieLinkArr, srcLinkName, serieLinks, true);
        if (serieLinkArr.length)
		{
            serieData.forEach(sd => serieDataMap.set(sd.name, sd));
            for (var i = 0; i < serieLinkArr.length; i++)
			{
                if (serieDataMap.has(serieLinkArr[i]))
				{
                    var currentData = serieDataMap.get(serieLinkArr[i]);
                    currentData.category = -Math.abs(currentData.category);
                }
            }

            serieDataMap.get(srcLinkName).open = false;
            chart.setOption(options);
        }
    }
	else
	{
        // 当前根节点是关闭的，那么就需要展开第一层根节点
        findLinks(serieLinkArr, srcLinkName, serieLinks, true);
        if (serieLinkArr.length)
		{
            serieData.forEach(sd => serieDataMap.set(sd.name, sd));
            for (var j = 0; j < serieLinkArr.length; j++)
			{
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
function findLinks(links, srcLinkName, serieLinks, deep)
{
    var targetLinks = [];
    serieLinks.filter(link => link.target === srcLinkName).forEach(link => {
        targetLinks.push(link.source);
        links.push(link.source)
    });
    if (deep) 
	{
        for (var i = 0; i < targetLinks.length; i++)
		{
            findLinks(links, targetLinks[i], serieLinks, deep);
        }
    }
}

    if (option && typeof option === 'object')
	{
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);