test_marks  = {
    'Alex' : 50,
    'Adam' : 43,
    'Eva' : 96,
    'Smith' : 66,
    'Andrew' : 74
}

greater_than_60 = { key:value for key, value in test_marks.items() if value > 60 }
print(greater_than_60)

students = { 'Alex', 'Adam', 'Andrew'}
a_students_dict = { key:value for key,value in test_marks.items() if key in students }
print(a_students_dict)
