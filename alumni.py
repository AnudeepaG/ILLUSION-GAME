import os
import platform
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="aldb")
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE ALDB;")
#mycursor.execute("USE ALDB;")
#mycursor.execute("CREATE TABLE alureg (ALU_ID VARCHAR(10), FNAME VARCHAR(30), LNAME VARCHAR(30), DOB DATE, GENDER VARCHAR(10), ADDRESS VARCHAR(50), EMAILADD VARCHAR(50), MOBNO VARCHAR(11), CURRENT_CITY VARCHAR(30), CURRENT_COMPANY VARCHAR(30), DESG VARCHAR(20), SESSFROM YEAR(4), SESSTO YEAR(4), BRANCH VARCHAR(30));")
#mycursor.execute("CREATE TABLE EVENT(EVENT_NAME VARCHAR(100),EVENT_DATE DATE,VENUE VARCHAR(30),STATUS VARCHAR(20),ETIME TIME);")
#mycursor.execute(" CREATE TABLE DONATIONS(ALNAME VARCHAR(30),PAYDATE DATE,PAYTYPE VARCHAR(30),BANKNAME VARCHAR(30),REMARKS VARCHAR(50),PAIDAMOUNT VARCHAR(10));")
#mycursor.execute("CREATE TABLE OPPORTUNITIES(ALNAME VARCHAR(30), COMPANY VARCHAR(30), JOBTITLE VARCHAR(30), KEYSKILLS VARCHAR(30), EXPREQ VARCHAR(5), NVACANCY VARCHAR(5), LASTDATE DATE, LSTATUS VARCHAR(20));")
#mycursor.execute("CREATE TABLE FEEDBACK(ALNAME VARCHAR(30), SUBJECT VARCHAR(30), MESSAGE VARCHAR(100), EMAILADD VARCHAR(30), CONTACTNO VARCHAR(11), POSTDATE DATE);")

def MainMenu():
 print("WELCOME TO ALUMNI MANAGEMENT SYSTEM".center(70))
 print("*"*80)
 print("MAIN MENU".center(70))
 print("Enter 1 : To Login")
 print("Enter 2 : To Register Alumni")
 print("Enter 3 : To View Alumni Details ")
 print("Enter 4 : To Edit Alumni Details ")
 print("Enter 5 : To Search Alumni ")
 print("Enter 6 : To delete Alumni")
 print("Enter 7 : To Add a Event")
 print("Enter 8 : To Search a Event")
 print("Enter 9 : To Delete a Event")
 print("Enter 10: Donations by Alumni")
 print("Enter 11: For Opportunities")
 print("Enter 12: For Feedback")
 print("*"*80)
 try:
  userInput = int(input("Please Select An Above Option: "))
 except ValueError:
  print("You Had Enetered Wrong Choice")
 else:
  print("\n")
  if userInput == 1:
   Login()
  elif userInput==2:
   RegisterAlumni()
  elif userInput==3:
   ViewAlumniDetails()
  elif userInput==4:
   UpdateAlumni()
  elif userInput==5:
   SearchAlumni()
  elif userInput==6:
   DeleteAlumni()
  elif userInput==7:
   ScheduleEvent()
  elif userInput==8:
   ViewEventDetails()
  elif userInput==9:
   DeleteEvent()
  elif userInput==10:
   DonationsAlumni()
  elif userInput==11:
   Opportunities()
  elif userInput==12:
   Feedback()
  else:
   print("Enter valid choice ")

   

def Login():
 print("1.Admin")
 print("2.Alumni")
 print("3.Staff")
 try:
  ch=int(input("Enter your choice :"))
 except ValueError:
  print("You entered wrong choice")
 else:
  if ch==1:
      print("Login successful by Admin")
  elif ch==2:
      print("Login successful by Alumni")
  elif ch==3:
      print("Login successful by Staff")
  else:
      print("Pls choose among 1,2,3")

      

def RegisterAlumni():
 L=[]
 fname=input("Enter Your First Name : ")
 L.append(fname)
 lname=input("Enter Your Last Name :")
 L.append(lname)
 dob=input("Enter Dob in YYYY-MM-DD Format : ")
 L.append(dob)
 gender=input("Enter Your Gender : ")
 L.append(gender)
 address=input("Enter your address : ")
 L.append(address)
 email=input("Enter email add. Ex: aa@gmail.com: ")
 L.append(email)
 mob=input("Enter Your Mobile No: ")
 L.append(mob)
 cur_c=input("Enter City Name: ")
 L.append(cur_c)
 com=input("Enter Company Name : ")
 L.append(com)
 desg=input("Enter Your Desgination: ")
 L.append(desg)
 start_y=input("Enter Session Start Year in College: ")
 L.append(start_y)
 start_e=input("Enter Session End Year in College : ")
 L.append(start_e)
 branch=input("Enter Your Branch in College : ")
 L.append(branch)
 aluid="al"+fname[0:2]+lname[0:2]+mob[0:3]
 L.insert(0,aluid)
 alumni=(L)
 sql="insert into alureg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
 mycursor.execute(sql,alumni)
 mydb.commit()
 print("*"*80)
 print("You Have Been Succesfully Registered: This is Your AlumniID,Use It For Future Reference")
 print(aluid)
 print("*"*80)


 
def ViewAlumniDetails():
 print("Select the search criteria to View Details : ")
 print("1. Fname")
 print("2. Lname")
 print("3. Company")
 print("4. Stream")
 print("5. City")
 print("6. Session Start")
 print("7. To View All Records")
 ch=int(input("Enter your choice : "))
 if ch==1 :
        s=input("Enter First Name to Search : ")
        val=(s,)
        sql="select * from alureg where fname like %s"
        mycursor.execute(sql,val)
 elif ch==2:
        s=input("Enter Last Name to Be Searched For : ")
        val=(s,)
        sql="select * from alureg where lname like %s"
        mycursor.execute(sql,val)
 elif ch==3:
        s=input("Enter Company Name to Be Searched For : ")
        val=(s,)
        sql="select * from alureg where current_company=%s"
        mycursor.execute(sql,val)
 elif ch==4:
        s=input("Enter Stream : ")
        val=(s,)
        sql="select * from alureg where branch=%s"
        mycursor.execute(sql,val)
 elif ch==5:
        s=input("Enter City : ")
        val=(s,)
        sql="select * from alureg where current_city=%s"
        mycursor.execute(sql,val)
 elif ch==6:
        s=input("Enter Session Start Year ")
        val=(s,)
        sql="select * from alureg where sessfrom=%s"
        mycursor.execute(sql,val)
 elif ch==7:
        sql="select * from alureg"
        mycursor.execute(sql)
 print("The Alumni Details are as Follows")
 result=mycursor.fetchall()
 for x in result:
        print(x)
 print("*"*80)


def UpdateAlumni():
 aluid=input("Enter Alumni ID to update : ")
 sql="select * from alureg where alu_id=%s"
 val=(aluid,)
 mycursor.execute(sql,val)
 result=mycursor.fetchall()
 for x in result:
        print(x)
 print("")
 fld=input("Enter field you want to edit : ")
 val=input("Enter the value you want to set : ")
 sql="Update alureg set " + fld +"='" + val + "' where alu_id='" + aluid + "'"
 sq=sql
 mycursor.execute(sql)
 print("Editing Done ")
 print("="*80)
 print("After correction the record is : ")
 sql="select * from alureg where alu_id=%s"
 val=(aluid,)
 mycursor.execute(sql,val)
 result=mycursor.fetchall()
 for x in result:
       print(x)
 mydb.commit()
 print("="*80)

 

def SearchAlumni():
 print("Enter The Alumni ID")
 aluid=input("Enter the Alumni ID for the alumni to be viewed : ")
 sql="select * from alureg where alu_id=%s"
 rl=(aluid,)
 mycursor.execute(sql,rl)
 print("="*80)
 print("The details of the students are : " )
 result=mycursor.fetchall()
 for x in result:
      print(x)
 if result==None:
  print("Record not Found")
  
  
def DeleteAlumni():
 aluid=input("Enter the Alumni ID for alumni to delete : ")
 sql="Delete from alureg where alu_id=%s"
 rl=(aluid,)
 mycursor.execute(sql,rl)
 mydb.commit()

 

def ScheduleEvent():
 E=[]
 ename=input("Enter Event Name to Schedule : ")
 E.append(ename)
 edate=input("Enter Event Date in YYYY-MM-DD :")
 E.append(edate)
 evenue=input("Enter Venue of Event :")
 E.append(evenue)
 estat=input("Enter Event Status as Completed Or Not Completed :")
 E.append(estat)
 etime=input("Enter Event Time :")
 E.append(etime)
 event=(E)
 sql="insert into event values (%s,%s,%s,%s,%s)"
 mycursor.execute(sql,event)
 mydb.commit()
 print("You Have Succesfully Added A Event")
 print("="*80)


def ViewEventDetails():
 print("Select the search criteria to View Event Details : ")
 print("1. Event Name")
 print("2. Venue")
 print("3. Status")
 print("4. To View All Records")
 ch=int(input("Enter the choice : "))
 if ch==1 :
      s=input("Enter Event Name to Be Searched For :")
      rl=(s,)
      sql="select * from event where event_name like %s"
      mycursor.execute(sql,rl)
 elif ch==2:
      s=input("Enter Venue Name to Be Searched For :")
      rl=(s,)
      sql="select * from event where venue like %s"
      mycursor.execute(sql,rl)
 elif ch==3:
      s=input("Enter Status to Be Searched For :")
      rl=(s,)
      sql="select * from event where status=%s"
      mycursor.execute(sql,rl)
 elif ch==4:
      sql="select * from event"
      mycursor.execute(sql)
 print("The Event Details are:")
 result=mycursor.fetchall()
 for x in result:
      print(x)
 print("="*80)


def DeleteEvent():
 ename=input("Enter the Event Name to be deleted : ")
 sql="Delete from event where event_name=%s"
 rl=(ename,)
 mycursor.execute(sql,rl)
 mydb.commit()


def DonationsAlumni():
 L=[]
 alname=input("Enter alumni name :")
 L.append(alname)
 paydate=input("Enter date of donation :")
 L.append(paydate)
 paytype=input("Enter Payment type :")
 L.append(paytype)
 bankname=input("Enter Bank name :")
 L.append(bankname)
 remarks=input("Enter Cause of Donation :")
 L.append(remarks)
 paidamount=input("Enter the Amount :")
 L.append(paidamount)
 alumni=(L)
 sql="insert into donations values(%s,%s,%s,%s,%s,%s)"
 mycursor.execute(sql,alumni)
 s="select * from donations"
 mycursor.execute(s)
 print("The Donation Details are:")
 result=mycursor.fetchall()
 for x in result:
      print(x)
 mydb.commit()
 print("="*80)


def Opportunities():
 L=[]
 alname=input("Enter your name:")
 L.append(alname)
 company=input("Enter company name: ")
 L.append(company)
 jobtitle=input("Enter name of job: ")
 L.append(jobtitle)
 keyskills=input("Enter key skills: ")
 L.append(keyskills)
 expreq=input("Enter experience yrs required for the job: ")
 L.append(expreq)
 nvacancy=input("Enter no of vacancy: ")
 L.append(nvacancy)
 lastdate=input("Enter last date to apply: ")
 L.append(lastdate)
 lstatus=input("Enter its status: ")
 L.append(lstatus)
 opp=(L)
 sql="insert into opportunities values(%s,%s,%s,%s,%s,%s,%s,%s)"
 mycursor.execute(sql,opp)
 s="select * from opportunities"
 mycursor.execute(s)
 print("The Opportunities Details are: ")
 result=mycursor.fetchall()
 for x in result:
      print(x)
 mydb.commit()
 print("="*80)


def Feedback():
 L=[]
 alname=input("Enter your name:")
 L.append(alname)
 subject=input("Enter subject of feedback: ")
 L.append(subject)
 message=input("Enter your message: ")
 L.append(message)
 emailadd=input("Enter your email address: ")
 L.append(emailadd)
 contactno=input("Enter your contact no.: ")
 L.append(contactno)
 postdate=input("Enter date on which msg is posted: ")
 L.append(postdate)
 fdback=(L)
 sql="insert into feedback values(%s,%s,%s,%s,%s,%s)"
 mycursor.execute(sql,fdback)
 s="select * from feedback"
 mycursor.execute(s)
 print("The Feedback Details are: ")
 result=mycursor.fetchall()
 for x in result:
      print(x)
 mydb.commit()
 print("="*80)


 
MainMenu()
def AskChoiceAgain():
 AksChcRun = input("want To Run Again Y/n: ")
 while(AksChcRun.lower() == 'y'):
  if(platform.system() == "Windows"):
   print(os.system('cls'))
  else:
   print(os.system('clear'))
  MainMenu()
  AksChcRun = input("want To Run Again Y/n: ")
AskChoiceAgain()


