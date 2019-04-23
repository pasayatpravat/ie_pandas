from ie_pandas import DataFrame

def test_colnames():
	dict_x = {'name':["Tom", "Harry", "Dick", "Jerry"], 'age':[10, 20, 30, 40]}
    
	df1 = DataFrame(dict_x)
	
    expected_output = ['name', 'age']
    
    actual_output = df1.colnames()
    
    assert actual_output == expected_output
