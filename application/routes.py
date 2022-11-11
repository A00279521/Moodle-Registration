from application import app, schooldb
from application.models import student,moodle
from flask import request, redirect, url_for
from flask import render_template
from flask_wtf import FlaskForm
#from flask import flask_wtf,wtforms
from wtforms import StringField, SubmitField
from application.forms import NameForm, DelForm, SelectFieldForm, SinForm

#****************FUNCTION****select_List*********************************************
def select_list(passdata):
       # pyoptionform= SelectFieldForm()
        if  passdata.list.data== 'All Student Page':
            return redirect(url_for('read_all_student'))
        elif passdata.list.data== 'All Moodle Page':
             return redirect(url_for('read_all_moodle'))
        elif passdata.list.data== 'Register A Student':
             return redirect(url_for('register_student'))
        elif passdata.list.data=='Delete A Student':
             return redirect(url_for('delstudent'))
        elif passdata.list.data=='Enter Student ID':
             return redirect(url_for('readstudent'))
        elif passdata.list.data=='Home Page':
             return redirect(url_for('start'))  


#*****************************************************************************************

#*******************ENTRY POINT***********************************************
@app.route('/', methods = ['GET','POST'])
def start():
    pyoptionform= SelectFieldForm()
   # return redirect(url_for('read'))
    if request.method == 'POST':
       return select_list(pyoptionform)
    return render_template('home.html', jioptionform=pyoptionform)

#*****************************************************************************************

#************GET ALL STUDENT FROM DATABASE*******************************************
@app.route('/students', methods= ['GET','POST'])
def read_all_student():
    pyall_students = student.query.all()
    pyoptionform= SelectFieldForm()
    if request.method == 'POST':
        return select_list(pyoptionform)
    return render_template('allstudent.html', ji_all_student=pyall_students, jioptionform=pyoptionform)

#**************************************************************************************

#************GET ALL MOODLE FROM DATABASE*******************************************

@app.route('/moodle', methods= ['GET','POST'])
def read_all_moodle():
    pyall_moodle = moodle.query.all()
    pyoptionform1= SelectFieldForm()
    if request.method == 'POST':
      return select_list(pyoptionform1)
    return render_template('allmoodle.html', ji_all_moodle= pyall_moodle, jioptionform1=pyoptionform1)

#********************************************************************************************

#*****************STUDENT REGISTRATION PAGE***********************************************

@app.route('/regstudent', methods = ['GET','POST'])
def register_student():
    # query list of staff from db
    pyoptionform= SelectFieldForm()
    # instantiate student input form so that i can use it
    pystudentform = NameForm()
    # Grab stuff from the POST
    if request.method == 'POST':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
        addstudent = student(student_id=pystudentform.Stud_id.data, surname=pystudentform.SName.data,firstName=pystudentform.FName.data )
        schooldb.session.add(addstudent)
        schooldb.session.commit()
        #breakpoint()
        # Send the user back to the frontpage
        return select_list(pyoptionform)
        #return redirect(url_for('start'))
    return render_template('registerstudent.html', jistudentform=pystudentform)


#******************************************************************************************

#****************DELETE ENTRY FROM THE STUDENT TABLE*******************
@app.route('/A', methods = ['GET','POST'])
def delstudent():
         pyall_students = student.query.all()
         pydelstudentform=DelForm()
         if request.method == 'POST':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
            delmoodle = moodle.query.filter_by(student_id=pydelstudentform.Stud_id.data).all()
            for k in delmoodle:
              schooldb.session.delete(k)            
            schooldb.session.commit()
            delstudent = student.query.filter_by(student_id=pydelstudentform.Stud_id.data).first()
            schooldb.session.delete(delstudent)
            schooldb.session.commit()
            return redirect(url_for('start'))
         return render_template('deletebut.html', ji_all_student=pyall_students,jidelstudentform=pydelstudentform )

                                                                            
#********************************************************************************************

#**************GET SPECIFIC STUDENT FROM DATABASE**************************************

@app.route('/studmod', methods=['GET','POST'])
def readstudent():
        # pyoptionform= SelectFieldForm()
         pystudentform=SinForm()
         if request.method == 'POST':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
          student_id=pystudentform.Stud_id.data
         # breakpoint()
          return redirect(url_for('readresult',student_id1= student_id))
         return render_template('singlestud.html', jistudentform=pystudentform,)

@app.route('/studmod1/<student_id1>', methods=['GET','POST'])
def readresult(student_id1):
         #pyoptionform= SelectFieldForm()
         pystudentform=SinForm()
         if request.method == 'GET':
             studmoodle = moodle.query.filter_by(student_id=student_id1).all()
             pystudent = student.query.filter_by(student_id=student_id1).all()
            # if request.method =='POST':
           #  return redirect(url_for('readresult1',stud_id1= student_id1))
         return render_template('readresult.html', ji_student=pystudent, ji_moodle= studmoodle)


@app.route('/studmod2/<stud_id1>', methods=['GET','POST'])
def readresult1(stud_id1):
         may= stud_id1
         pyoptionform= SelectFieldForm()
         pystudentform=SinForm()
         if request.method == 'POST':
               return redirect(url_for('start'))
         #return render_template('home.html')

#*****************************************************************************************



@app.route('/A', methods = ['GET','POST'])
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

#*****************************************************************************************************

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


