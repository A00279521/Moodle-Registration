# Moodle-Registration
 The user story is to design web-app where the student   
 can view the number of moodle he/she is registered for in the semester.
   
 * Use jira as a project management tool
 * The requirement is to produce MVP as the starting point
   
 ## The ERD diagram 
   this is based on the customer's requirement to meet a deadline.  
 Therefore the approach is to design two database table with a one to many
  concept or relationship.  
 The two table are  
  * student table comprising of the following   
 student id  
 student surname  
 student forename  
  * moodle table comprising of the following
 moodle id
 moodle name

  PICTURE of the ERD diagram
  https://github.com/A00279521/Moodle-Registration/blob/photoBranch/ERD_diagram.png
  
  Link to Risk Assessment file.
   https://github.com/A00279521/Moodle-Registration/blob/photoBranch/Risk_assessment.xlsx

 
 ##  ADDITIONAL REQUIREMENT FROM PRODUCT OWNER
   * After the MVP the product owner has requested further fuctionality as listed below
   * The ability to delete a student from the student table 
   * The ability to update/modify the student table 
   * The ability to display all registered student in the database
   * The ability to display all registered moodles in the database
   * The student ID must be 8 characters long and can only start with letter 'x' followed by 7 numbers
   * Deleting from the student database must be validated b re-entering the student ID twice
   * The intention is to create a login page for all users at a letter sprint 
   * Navigating across different pages should be very easy using different options
   * The student ID in the student table should be the foreign key in the moodle table but not necessary the primary key
    
 
