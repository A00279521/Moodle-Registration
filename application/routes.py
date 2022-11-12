from application import app, schooldb
from application.models import student,moodle
from flask import request, redirect, url_for
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.forms import NameForm, DelForm, SelectFieldForm, SinForm, MoodleForm

#****************FUNCTION****select_List*********************************************
def select_list(passdata):
        if  passdata.list.data== 'All Student Page':
            return redirect(url_for('read_all_student'))
        elif passdata.list.data== 'All Moodle Page':
             return redirect(url_for('read_all_moodle'))
        elif passdata.list.data== 'Register A Student':
             return redirect(url_for('register_student'))
        elif passdata.list.data=='Register A Moodle':
            return redirect(url_for('register_moodle'))
        elif passdata.list.data=='Delete A Student':
             return redirect(url_for('delstudent'))
        elif passdata.list.data=='Update':
             return redirect(url_for('update'))
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
    pystudentform = NameForm()
    if request.method == 'POST':
        addstudent = student(student_id=pystudentform.Stud_id.data, surname=pystudentform.SName.data,firstName=pystudentform.FName.data )
        schooldb.session.add(addstudent)
        schooldb.session.commit()
        return redirect(url_for('start'))
    return render_template('registerstudent.html', jistudentform=pystudentform)


#******************************************************************************************

#****************DELETE ENTRY FROM THE STUDENT TABLE*******************
@app.route('/A', methods = ['GET','POST'])
def delstudent():
         pyall_students = student.query.all()
         pydelstudentform=DelForm()
         if request.method == 'POST':
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
         pystudentform=SinForm()
         if request.method == 'POST':
          student_id=pystudentform.Stud_id.data
          return redirect(url_for('readresult',student_id1= student_id))
         return render_template('singlestud.html', jistudentform=pystudentform,)

@app.route('/studmod1/<student_id1>', methods=['GET','POST'])
def readresult(student_id1):
         pyoptionform= SelectFieldForm()
         pystudentform=SinForm()
         if request.method == 'GET':
             studmoodle = moodle.query.filter_by(student_id=student_id1).all()
             pystudent = student.query.filter_by(student_id=student_id1).all()
             return render_template('readresult.html', ji_student=pystudent, ji_moodle= studmoodle, jioptionform= pyoptionform)
         if request.method == 'POST':
               return select_list(pyoptionform)

#*****************************************************************************************

 #****************UPDATE ENTRY IN DATABASE***************************************************************

@app.route('/studmodm', methods=['GET','POST'])
def update():
         pystudentform=SinForm()
         if request.method == 'POST':
          student_id=pystudentform.Stud_id.data
          return redirect(url_for('register_student1',student_id1= student_id))
         return render_template('singlestud.html', jistudentform=pystudentform,)

@app.route('/studmod2/<student_id1>', methods=['GET','POST'])
def register_student1(student_id1):
    pyoptionform= SelectFieldForm()
    pystudentform = NameForm()
    if request.method == 'GET':
         studmoodle = moodle.query.filter_by(student_id=student_id1).all()
         pystudent = student.query.filter_by(student_id=student_id1).first()
         return render_template('update.html', ji_student=pystudent, ji_moodle= studmoodle, jioptionform= pyoptionform, jistudentform=pystudentform)
    if request.method == 'POST':
        studmoodle = moodle.query.filter_by(student_id=student_id1).all()
        for k in studmoodle:
            schooldb.session.delete(k)            
            schooldb.session.commit()
        pystudent = student.query.filter_by(student_id=student_id1).first()
        schooldb.session.delete(pystudent)
        schooldb.session.commit()
        addstudent = student(student_id=pystudentform.Stud_id.data, surname=pystudentform.SName.data,firstName=pystudentform.FName.data )
        schooldb.session.add(addstudent)
        schooldb.session.commit()
        return redirect(url_for('start'))
# ***************************************************************************************************

#*****************MOODLE REGISTRATION PAGE***********************************************

@app.route('/regmoodle', methods = ['GET','POST'])
def register_moodle():
    pymodform = MoodleForm()
    if request.method == 'POST':
        addmoodle = moodle(student_id=pymodform.Stud_id.data, moodle_id=pymodform.Modcode.data, moodleName=pymodform.Subname.data )
        schooldb.session.add(addmoodle)
        schooldb.session.commit()
        return redirect(url_for('start'))
    return render_template('regmoodle.html', jimodform=pymodform)


#******************************************************************************************
