from datetime import datetime

str = '2022-01-03'
print(str)
print(type(str))

datetime_object = datetime.strptime(str, '%Y-%m-%d')
print(datetime_object)
print(type(datetime_object))
