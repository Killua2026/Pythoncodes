# student = {'name':'Ikechukwu', 'age': 18, 'level': 200}
#alternative method
student = dict(name="Ikechukwu", age = '18', level='200')
student['age']= '19'
student.update({'level':'300'})
student['gender'] = 'male'
student.update({'gender':'sigma_male'})
print(student)