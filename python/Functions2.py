def student_data(*args,**kargs):
    print(args)
    print(kargs)

student_data('Math','Art',name='Pawni',age=18)

courses = ['Math','Art']
data = {'name':'Pawni','age':18}
student_data(*courses,**data)