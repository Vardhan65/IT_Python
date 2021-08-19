# Assign String to x variable in DD-MM-YYYY format  extract and Print Year From String .....






import datetime
x_str = '19/08/2021'
y_str = '%d/%m/%Y' 
datetime_obj = datetime.datetime.strptime(x_str, y_str)
print(datetime_obj.date())