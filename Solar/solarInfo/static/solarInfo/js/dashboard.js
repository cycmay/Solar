Highcharts.setOptions({
	global: {
		useUTC: false
		}
});
function activeLastPointToolip(chart) {
	var points = chart.series[0].points;
	chart.tooltip.refresh(points[points.length -1]);
}

// 请求到solar数据后界面更新操作
/*
 * chart 图表对象
 * name 图表DOM id
 * data 请求到的数据 json格式
*/
function flashChart(number, chart, name){
    // 请求数据并在表中更新
    requestSolar(number, function(output){
        // here use output/data
        // console.log(output);
        // 新增点
        var series = chart.series[0];
        var shift = series.data.length > 20;
        var x = (new Date()).getTime(), // 当前时间
                  y = output["data"][name];
        series.addPoint([x, y], true, shift);
        if(shift){
            activeLastPointToolip(chart);
        }
    });
    // 3 seconds 重复操作
    setTimeout(function(a,b, c){
        flashChart(a, b, c)
    }, 1000*3, number, chart, name);
}
// 封装好的api请求函数 请求最新的数据 数据返回为灯杆号对应的data
function requestSolar(number, handleData) {
    $.ajax({
        url: '/solar/api/solar/',
        type: "GET",
        data: {"number": number},
        success: function(data){
            // 成功后进行图表跟新操作
            handleData(data);
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
            flashChart(number, chart, "s_voltage"); // 图表加载完毕后执行的回调函数
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
            flashChart(number, chart, "s_current"); // 图表加载完毕后执行的回调函数
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

// 蓄电池电压 曲线图显示
var chart_b_voltage = Highcharts.chart('b_voltage', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            var number = window.NUMBER;
            flashChart(number, chart, "b_voltage"); // 图表加载完毕后执行的回调函数
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
		name: '蓄电池电压 /V',
		data: []
	}]
});

// 负载电流（A） 曲线图显示
var chart_load_current = Highcharts.chart('load_current', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            var number = window.NUMBER;
            flashChart(number, chart, "load_current"); // 图表加载完毕后执行的回调函数
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
		name: '负载电流（A）',
		data: []
	}]
});

// 负载电压(V)曲线图显示
var chart_load_voltage = Highcharts.chart('load_voltage', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            var number = window.NUMBER;
            flashChart(number, chart, "load_voltage"); // 图表加载完毕后执行的回调函数
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
		name: '负载电压 /V',
		data: []
	}]
});
