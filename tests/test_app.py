from runapp import read

#def read():
#   all_students = student.query.all()
#     my_string=" "
#     for stud in all_students:
#         my_string += "<br>"+ f"{stud.student_id} {stud.surname} {stud.firstName}"
#     return my_string

student_id = "x0000we"
surname= "same"
firstName= "peter"
my_string =  f"{student_id} {surname} {firstName}"
def test_read():
    # my_string =  f"{student_id} {surname} {firstName}"
    assert read() == "x0000we" 
