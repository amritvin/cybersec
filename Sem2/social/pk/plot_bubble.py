from highcharts import Highchart
import datetime

chart = Highchart()
options = {
	'chart': {'type': 'bubble'},
	'title': {'text': 'Highchart bubble'},
	'legend': {'enabled':True},
	'xAxis': {
		'type':'datetime',
		'dateTimeLabelFormats':{
			'day': '%e %b',
			'month': '%b %y',
			'year': '%Y'
		},
		}
	}
# }

data1 = [[datetime.datetime(2017,5,9),1,20],[datetime.datetime(2017,5,10),1,44],[datetime.datetime(2017,5,11),1,21],[datetime.datetime(2017,5,12),1,19],[datetime.datetime(2017,5,13),1,17],[datetime.datetime(2017,5,17),1,35]]
data2 = [[datetime.datetime(2017,5,13),1,5],[datetime.datetime(2017,6,6),1,6],[datetime.datetime(2017,6,7),1,16],[datetime.datetime(2017,6,8),1,2],[datetime.datetime(2017,6,9),1,12]]
data3 = [[datetime.datetime(2017,5,9),1,63],[datetime.datetime(2017,5,10),1,77],[datetime.datetime(2017,5,11),1,15],[datetime.datetime(2017,5,17),1,120],[datetime.datetime(2017,5,18),1,51],[datetime.datetime(2017,5,19),1,79],]
data4 = [[datetime.datetime(2017,5,9),1,30],[datetime.datetime(2017,5,10),1,16],[datetime.datetime(2017,5,11),1,15],[datetime.datetime(2017,5,13),1,30],[datetime.datetime(2017,5,25),1,5],]

chart.set_dict_options(options)

chart.add_data_set(data1,'bubble','User 1')
chart.add_data_set(data2,'bubble','User 2')
chart.add_data_set(data3,'bubble','User 3')
chart.add_data_set(data4,'bubble','User 4')

chart.save_file('./bubble-highcharts')