Highcharts.setOptions({
	global: {
		useUTC: false
		}
});
function activeLastPointToolip(chart) {
	var points = chart.series[0].points;
	chart.tooltip.refresh(points[points.length -1]);
}

var chart_s_voltage = Highcharts.chart('s_voltage', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: function(){
            var chart = this;
            requestSolar(chart, "s_voltage"); // 图表加载完毕后执行的回调函数
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

/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 1 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */
function requestData() {
  $.ajax({
    url: '/solar/api/solar/',
    success: function(data) {
      // 新增点
      var series = chart_s_voltage.series[0];
      var shift = series.data.length > 20;
	  var x = (new Date()).getTime(), // 当前时间
                  y = data["data"][0]["s_voltage"];
      series.addPoint([x, y], true, shift);
	  if(shift){
	    activeLastPointToolip(chart_s_voltage);
      }
	  // 3mins 重复操作
      setTimeout(requestData, 1000*3);
    },
    cache: false
  });
}

function requestSolar(chart, name) {
    $.ajax({
        url: '/solar/api/solar/',
        success: function(data){
            // 新增点
            var series = chart.series[0];
            var shift = series.data.length > 20;
            var x = (new Date()).getTime(), // 当前时间
                      y = data["data"][0][name];
            series.addPoint([x, y], true, shift);
            if(shift){
            activeLastPointToolip(chart);
            }
            // 3 seconds 重复操作
            setTimeout(function(a,b){
                requestSolar(a, b)
            }, 1000*3, chart, name);
        },
        cache: false
    });
}

var chart_s_current = Highcharts.chart('s_current', {
	chart: {
		type: 'spline',
		marginRight: 10,
		events: {
          load: requestDataVol // 图表加载完毕后执行的回调函数
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

/**
 * Ajax 请求数据接口，并通过 Highcharts 提供的函数进行动态更新
 * 接口调用完毕后间隔 1 s 继续调用本函数，以达到实时请求数据，实时更新的效果
 */
function requestDataVol() {
  $.ajax({
    url: '/solar/api/solar/',
    success: function(data) {
      // 新增点
      var series = chart_s_current.series[0];
      var shift = series.data.length > 20;
	  var x = (new Date()).getTime(), // 当前时间
                  y = data["data"][0]["s_current"];
      series.addPoint([x, y], true, shift);
	  if(shift){
	    activeLastPointToolip(chart_s_current);
      }
	  // 3mins 重复操作
      setTimeout(requestDataVol, 1000*3);
    },
    cache: false
  });
}