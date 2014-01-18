def generate_session_graph(data_by_week_date, data_by_week_marginal, data_by_week_totals):
	#Create the dictionary
	graph_dict = {
		'chart': {
                'zoomType': 'xy'
            },
            'title': {
                'text': 'Total Workouts - Weekly Basis'
            },
            'xAxis': [{
                
                'categories': data_by_week_date
                            }],
            'yAxis': [{ #Primary yAxis
                'labels': {
                    'format': '{value}',
                    'style': {
                        'color': '#89A54E'
                    }
                },
                'title': {
                    'text': 'Total Workouts',
                    'style': {
                        'color': '#89A54E'
                    }
                },
                'min':0,
            }, { #Secondary yAxis
                'title': {
                    'text': 'Workouts per week',
                    'style': {
                        'color': '#4572A7'
                    }
                },
                'labels': {
                    'format': '{value}',
                    'style': {
                        'color': '#4572A7'
                    }
                },
                'opposite': 'true',
                'minTickInterval':1,
            }],
            'tooltip': {
                'shared': 'true'
            },
            'legend': {
                'layout': 'vertical',
                'align': 'left',
                'x': 120,
                'verticalAlign': 'top',
                'y': 100,
                'floating': 'true',
                'backgroundColor': '#FFFFFF'
            },
            'series': [{
                'name': 'Weekly Workouts',
                'color': '#4572A7',
                'type': 'column',
                'yAxis': 1,
                'data': data_by_week_marginal,
                'tooltip': {
                    'valueSuffix': ''
                }
    
            }, {
                'name': 'Total Workouts',
                'color': '#89A54E',
                'type': 'spline',
                'data': data_by_week_totals,
                'tooltip': {
                    'valueSuffix': ''
                }
            }]
        }

	return graph_dict



def generate_exercise_detail_graph(weight_rep_data, exercise_name):

    #Create the dictionary
    graph_dict = {
        'chart': {
            'type': 'bubble',
            'zoomType': 'xy',
        },

        'xAxis': {
            'type': 'datetime',
        },

        'yAxis': {
            'title': {
                'text': 'Weight'
            },
            'min':0,
            'minTickInterval':1
        },

        'title': {
            'text': 'Exercise Detail'
        },
    
        'series': [{
            'data': weight_rep_data,
            'sizeBy': 'width',
            'name': exercise_name
        }]
    
    }

    return graph_dict

def generate_weight_graph(weight_list, target_weight_list):

    #Create the dictionary
    graph_dict = {

        'chart': {
            'type': 'spline'
        },
        'title': {
            'text': 'Weight Log'
        },
        'xAxis': {
            'type': 'datetime',
            'dateTimeLabelFormats': { 
                'month': '%b',
                'year': '%b'
            }
        },
        'yAxis': {
            'title': {
                'text': 'Weight (lbs)'
            },
            'min': 130,
            'max': 170
        },
                
       'series': [
       {
            'name': 'Actual Weight',
            'data': weight_list                   
            }, 
        {
            'name': 'Target Weight',
            'data': target_weight_list
            },     

            ]  
    }

    return graph_dict