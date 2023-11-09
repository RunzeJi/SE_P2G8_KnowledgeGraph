// 获取JSON文件的数据
$.getJSON("/fetchData", function(data) {
  // 赋值给option变量
  var option = data;
  // 其他代码不变
  var dom = document.getElementById('container');
  var myChart = echarts.init(dom, null, {
    renderer: 'canvas',
    useDirtyRect: false
  });
  var app = {};
  // 使用JSON文件中的数据
  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }
  window.addEventListener('resize', myChart.resize);
});


