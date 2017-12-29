from highcharts import Highchart

chart = Highchart()
options = {
	'chart': {'type': 'scatter'},
	'title': {'text': 'Highchart scatter'},
	'legend': {'enabled':True},
	'xAxis': {
		'title': {'text': 'Followers (thousands)'}
	},
	'yAxis':{
			'title': {'text': 'Friends (thousands)'}
	},
}

data1 = [[161,51],[167,59],[159,49],[157,63],[155,53]]
data2 = [[174,65],[175,171],[193,100],[186,172],[107,170]]

chart.set_dict_options(options)

chart.add_data_set(data1,'scatter','Celebrity accounts', color='rgba(223,83,83,0.5)')
chart.add_data_set(data2,'scatter','Normal user accounts', color='rgba(119,152,192,191,0.5)')
chart.save_file('./scatter-highcharts')