from highcharts import Highchart

chart = Highchart()
options = {
	'chart': {'type': 'line'},
	'title': {'text': 'Highchart line'},
	'legend': {'enabled':True},
	'xAxis': {
		'categories': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	},
	'yAxis':{
			'title': {'text': 'Number of followers'}
	},
}

data1 = [7,7,9,14,18,21,25,26,30,55]
data2 = [13,16,22,25,56,76,91]
data3 = [3,4,5,8,11,15,17,36,42,103]

chart.set_dict_options(options)

chart.add_data_set(data1,'line','User 1')
chart.add_data_set(data2,'line','User 2')
chart.add_data_set(data3,'line','User 3')

chart.save_file('./line-highcharts')