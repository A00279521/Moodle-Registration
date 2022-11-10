from application import app, schooldb
from application.models import student,moodle
from flask import request, redirect, url_for
from flask import render_template
from flask_wtf import FlaskForm
#from flask import flask_wtf,wtforms
from wtforms import StringField, SubmitField
from application.forms import NameForm, DelForm

@app.route('/', methods = ['GET','POST','DELETE'])
def read():
    # query list of staff from db
    #pystaff = Staff.query.join(Subjects).all()
    pyall_students = student.query.all()
    # query subjects
    #pysubjects = Subjects.query.all()
    pyall_moodle = moodle.query.all()
    # instantiate empty subject form 
    # pysubjectform = SubjectList()
    # # append query to choices
    # for subj in pysubjects:
    #     pysubjectform.subjlist.choices.append(
    #        (subj.id,subj.subject_name)
    #     )

    # instantiate student input form so that i can use it
    pystudentform = NameForm()
    pydelstudentform=DelForm()
    # Grab stuff from the POST
    if request.method == 'POST':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
        addstudent = student(student_id=pystudentform.Stud_id.data, surname=pystudentform.SName.data,firstName=pystudentform.FName.data )
        schooldb.session.add(addstudent)
        schooldb.session.commit()
        #breakpoint()
        # Send the user back to the frontpage

    #****************DELETE ENTRY FROM THE STUDENT TABLE*******************
    if request.method == 'DELETE':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
        delmoodle = moodle(studentbr=pydelstudentform.Stud_id.data)
        schooldb.session.delete(delmoodle)
        schooldb.session.commit()
        delstudent = student(student_id=pydelstudentform.Stud_id.data)
        schooldb.session.delete(delstudent)
        schooldb.session.commit()

        return redirect(url_for('read'))
    return render_template('front.html', ji_all_student=pyall_students, jistudentform=pystudentform,
                          ji_all_moodle=pyall_moodle, jidelstudentform=pydelstudentform )


#************GET ALL STUDENT FROM DATABASE*******************************************
@app.route('/students', methods=["GET"])
def read_all_student():
    all_students = student.query.all()
    # my_string=' '
    # for stud in all_students:
    #     my_string += f"{stud.student_id} {stud.surname} {stud.firstName}\n"
    #return my_string
    #return render_template('front.html', res=my_string)
    return render_template('front.html', res=all_students)

#@app.route('/students', methods=["GET"])
# def read_all_student1():
#     all_students = student.query.all()
#     # my_string= " "
#     # for stud in all_students:
#     #     my_string += "<br>"+ f"{stud.student_id} {stud.surname} {stud.firstName}"
#     #return my_string
#     #return render_template('front.html', res=my_string)
#     return render_template('front.html', res=all_students)

#**************************************************************************************

#**************GET SPECIFIC STUDENT FROM DATABASE**************************************

@app.route('/students/<st_id>', methods=["GET"])
def readstudent(st_id):
    val1=student.query.filter_by(student_id=st_id).first()
    result= f"{val1.student_id} {val1.surname} {val1.firstName}"
    return result

    # my_string=" "
    # for num in all_students:
    #      if num.student_id==st_id:
    #my_string[] = my_string.append()    "<br>"+ f"{student_id} {num.surname} {num.firstName}"
    #return oneStudent

# @app.route('/students/<st_id>', methods=["GET"])
# def readstudent(st_id):
#     ans = student.query.filter_by(student_id=st_id).all()
#     return render_template('front.html', res1=ans)
#*****************************************************************************************

#************GET ALL MOODLE FROM DATABASE*******************************************

@app.route('/moodle', methods=["GET"])
def read_all_moodle():
    all_moodle = moodle.query.all()
    my_string=" "
    for modl in all_moodle:
        my_string += "<br>"+ f"{modl.moodle_id} {modl.moodleName} {modl.student_id}"
    return my_string

#********************************************************************************************

#**************GET SPECIFIC STUDENT MOODLE FROM DATABASE**************************************

@app.route('/moodle/<st_id>', methods=["GET"])
def read_stud_mod(st_id):
    val1=moodle.query.filter_by(student_id=st_id).all()
    result =" "
    for k in range(len(val1)):
        result+= f"{val1[k].moodle_id} {val1[k].moodleName}\n"
    return result
#********************************************************************************************

#*********************GET STUDENTS TAKING A SPECIFIC MOODLE**************************************

@app.route('/mood/<mod_id>', methods=["GET"])
def read_mod_stud(mod_id):
    all_moodle = moodle.query.all()
    my_string=" "
    for num in all_moodle:
         if num.moodle_id==mod_id:
            my_string += "<br>"+ f"{num.student_id}"
    return f"student taking this {mod_id} are\n {my_string}"

#***************************************************************************************************
@app.route('/studentupdate', methods=["POST"])
def update(str1,str2,str3):
    # first_game = Games.query.first()
    studVal=student(student_id=str1.student_id ,surname= str2.surname,firstName=str3.firstName)
     #first_game.name = name
    schooldb.session.add(studVal)
    schooldb.session.commit()
    #return first_game.name
 #    

#@app.route('/update/<name>'methods=["POST"])
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     crud_db.session.commit()
#     return first_game.name
 # result= student(student_id=val1.student_id ,surname= val1.surname,firstName=val1.firstName)/database

 #***********************************************************************************************************

 #****************DELETE ENTRY FROM DATABASE***************************************************************

# @app.route('/<st_id>', methods=["DELETE"])
# def read_stud_mod(st_id):
#     val1=moodle.query.filter_by(student_id=st_id).all()
#     result =" "
#     for k in range(len(val1)):
#         result+= f"{val1[k].moodle_id} {val1[k].moodleName}\n"
#     return result
# #******************


