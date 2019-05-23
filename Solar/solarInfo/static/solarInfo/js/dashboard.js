Highcharts.setOptions({
	global: {
		useUTC: false
		}
});
function activeLastPointToolip(chart) {
	var points = chart.series[0].points;
	chart.tooltip.refresh(points[points.length -1]);
}

/* 采用正则表达式获取地址栏参数 (代码简洁，重点正则）
 * 调用方法：
 * let 参数1 = GetQueryString("参数名1"));
*/
function getQueryString(name) {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return unescape(r[2]);
    };
    return null;
 }

// 请求到solar数据后界面更新操作
/*
 * chart 图表对象
 * name 图表DOM id
 * data 请求到的数据 json格式
*/
function flashChart(chart, name, data){
    // 新增点
    var series = chart.series[0];
    var shift = series.data.length > 20;
    var x = (new Date()).getTime(), // 当前时间
              y = data["data"][name];
    series.addPoint([x, y], true, shift);
    if(shift){
    activeLastPointToolip(chart);
    }
    // 3 seconds 重复操作
    setTimeout(function(a,b){
        requestSolar(a, b)
    }, 1000*3, chart, name);
}
// 封装好的api请求函数 请求最新的数据 数据返回为灯杆号对应的data
function requestSolar(number, chart, name) {
    $.ajax({
        url: '/solar/api/solar/',
        type: "GET",
        data: {"number": number},
        success: function(data){
            // 成功后进行图表跟新操作
            flashChart(chart, name, data);
        },
        cache: false
    });
}

// 太阳能板电压 图表显示
var chart_s_voltage = Highcharts.chart('s_voltage', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            var number = window.NUMBER;
            requestSolar(number, chart, "s_voltage"); // 图表加载完毕后执行的回调函数
          }

        }
	},
	title: {
		text: 'Living Data'
	},
	xAxis: {
		type: 'datetime',
        tickPixelInterval: 100
	},
	yAxis: {
		minPadding: 0.2,
        maxPadding: 0.2,
        title: {
          text: 'Value',
        }
	},
	tooltip: {
		formatter: function () {
			return '<b>' + this.series.name + '</b><br/>' +
				Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
				Highcharts.numberFormat(this.y, 2);
		}
	},
	legend: {
		enabled: false
	},
	series: [{
		name: '太阳能板电压 /v',
		data: []
	}]
});

// 太阳能板电流 曲线图显示
var chart_s_current = Highcharts.chart('s_current', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            var number = window.NUMBER;
            requestSolar(number, chart, "s_current"); // 图表加载完毕后执行的回调函数
          }
        }
	},
	title: {
		text: 'Living Data'
	},
	xAxis: {
		type: 'datetime',
        tickPixelInterval: 100
	},
	yAxis: {
		minPadding: 0.2,
        maxPadding: 0.2,
        title: {
          text: 'Value',
        }
	},
	tooltip: {
		formatter: function () {
			return '<b>' + this.series.name + '</b><br/>' +
				Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
				Highcharts.numberFormat(this.y, 2);
		}
	},
	legend: {
		enabled: false
	},
	series: [{
		name: '太阳能板电流 /A',
		data: []
	}]
});
