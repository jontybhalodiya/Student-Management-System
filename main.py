 print(':-:-:-:-:-:SCHOOL MANAGEMENT SYSTEM:-:-:-:-:-:\n----------------------------------------------')
 print("1.STUDENT MANAGEMENT")
 print("2.FEE MANAGEMENT")
 print("3.EXAM MANAGEMENT")
 ch=int(input("\nEnter ur choice (1-3) : "))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 if ch==1:
    print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
    print('A.NEW ADMISSION')
    print('B.UPDATE STUDENT DETAILS')
    print('C.ISSUE TC')
    c=input("Enter ur choice (a-c) : ")
    print('\nInitially the details are..\n')
    display1()
    if c=='a':
       insert1()
       print('\nModified details are..\n')
       display1()
    elif c=='b':
       update1()
       print('\nModified details are..\n')
       display1()
    elif c=='c':
       delete1()
       print('\nModified details are..\n')
       display1()
    else:
       print('Enter correct choice...!!')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 elif ch==2:
    print('WELCOME TO FEE MANAGEMENT SYSTEM')
    print('A.NEW FEE')
    c=input("Enter ur choice : ")
    if c=='a':
       insert2()
    else:
      print('Enter correct choice...!!')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 elif ch==3:
    print('WELCOME TO EXAM MANAGEMENT SYSTEM')
    print('A.EXAM DETAILS')
    print('B.DELETE DETAILS')
    c=input("Enter ur choice : ")
    if c=='a':
       insert3()
    elif c=='b':
       delete3()
    else:
      print('Enter correct choice...!!')
 else:
   print('Enter correct choice..!!')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert1():
   sname=input("Enter Student 's Name : ")
   admno=int(input("Enter Admission No : "))
   dob=input("Enter Date of Birth(yyyy-mm-dd): ")
   cls=input("Enter class for admission: ")
   cty=input("Enter City : ")
   db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
   cursor = db.cursor()
   sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( '%s' ,'%d','%s','%s','%s')"%(sname,admno,dob,cls,cty)
   try:
     cursor.execute(sql)
     db.commit()
   except:
     db.rollback()
     db.close()
 #insert()
def display1():
  try:
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
    cursor = db.cursor()
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
      sname = c[0]
      admno= c[1]
      dob=c[2]
      cls=c[3]
      cty=c[4]
      print ("(sname=%s,admno=%d,dob=%s,cls=%s,cty=%s)" % (sname,admno,dob,cls,cty))
  except:
    print ("Error: unable to fetch data")
    db.close()
def update1():
 try:
   db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
   cursor = db.cursor()
   sql = "SELECT * FROM student"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
     sname = c[0]
     admno= c[1]
     dob=c[2]
     cls=c[3]
     cty=c[4]
 except:
   print ("Error: unable to fetch data")
 print()
 tempst=int(input("Enter Admission No : "))
 temp=input("Enter new class : ")
 try:
   sql = "Update student set cls=%s where admno='%d'" % (temp,tempst)
   cursor.execute(sql)
   db.commit()
 except Exception as e:
   print (e)
   db.close()
def delete1():
  try:
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
    cursor = db.cursor()
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    results = cursor.fetchall()
    for c in results:
      sname = c[0]
      admno= c[1]
      dob=c[2]
      cls=c[3]
      cty=c[4]
  except:
    print ("Error: unable to fetch data")
  temp=int(input("\nEnter adm no to be deleted : "))
  try:
     sql = "delete from student where admno='%d'" % (temp)
     ans=input("Are you sure you want to delete the record(y/n) : ")
     if ans=='y' or ans=='Y':
        cursor.execute(sql)
        db.commit()
  except Exception as e:
    print (e)
    db.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert2():
 admno=int(input("Enter adm no: "))
 fee=float(input("Enter fee amount : "))
 month=input("Enter Month: ")
 db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
 cursor = db.cursor()
 sql="INSERT INTO fee(admno,fee,month) VALUES ( '%d','%d','%s')"%(admno,fee,month)
 try:
   cursor.execute(sql)
   db.commit()
 except:
   db.rollback()
   db.close()
def display2():
 try:
   db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
   cursor = db.cursor()
   sql = "SELECT * FROM fee"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
     admno= c[0]
     fee=c[1]
     month=c[2]
     print ("(admno=%d,fee=%s,month=%s)" % (admno,fee,month))
 except:
   print ("Error: unable to fetch data")
   db.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert3():
 sname=input("Enter Student Name : ")
 admno=int(input("Enter Admission No : "))
 per=float(input("Enter percentage : "))
 res=input("Enter result: ")
 db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
 cursor = db.cursor()
 sql="INSERT INTO exam(sname,admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(sname,admno,per,res)
 try:
   cursor.execute(sql)
   db.commit()
 except:
    db.rollback()
    db.close()
def display3():
 try:
   db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
   cursor = db.cursor()
   sql = "SELECT * FROM exam"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
      sname = c[0]
      admno= c[1]
      dob=c[2]
      cls=c[3]
      cty=c[4]
      print ("(sname,admno,per,res)"%(sname,admno,per,res) )
 except:
   print ("Error: unable to fetch data")
   db.close()
def delete3():
 try:
   db = mysql.connector.connect(user='root', password='root', host='localhost',database='schoolmanagement')
   cursor = db.cursor()
   sql = "SELECT * FROM exam"
   cursor.execute(sql)
   results = cursor.fetchall()
   for c in results:
     sname = c[0]
     admno= c[1]
     dob=c[2]
     cls=c[3]
     cty=c[4]
 except:
   print ("Error: unable to fetch data")
   temp=int(input("\nEnter adm no to be deleted : "))
   try:
     sql = "delete from exam where admno='%d'" % (temp)
     ans=input("Are you sure you want to delete the record(y/n) : ")
     if ans=='y' or ans=='Y':
        cursor.execute(sql)
        db.commit()
   except Exception as e:
     print (e)
     db.close()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
selection()
#---------------------------------------------------------------------------------------------------------------------------
print("*************************\nHave a great day ahead!!!\n*************************")
#---------------------------------------------------------------------------
print("""-----------------------------------------------------\nSchool Management System.
Version: 1.1.3
Developed by:JONTY BHALODIYA\n-----------------------------------------------------""")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
restart=input("do you want to restart the program?").lower()
if restart == "y":
    selection()
else:
    exit()
