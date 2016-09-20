
import sqlite3 as mysql
import os,sys
from encryption import my_encryption

dir = os.path.split(sys.argv[0])[0]
Mydb=dir+'/Resources/revised.sql'


if os.path.exists(Mydb):
    
    pass
    
else:
    
    print "DB not existin"
    
print dir


#Lang Index 4,6
#Mal 8,10
#Eng 12,14

class db_operations():

    def __init__(self):
        
        
        self.con=mysql.connect(Mydb)
        self.cur = self.con.cursor()
        

        
        '''path='tables.sql'
        f=open(path)
        sql = f.read()
        self.cur.executescript(sql)
        '''
    def CreateTables(self):

        # DIV TABLE
        q="CREATE TABLE DIV(ID INTEGER PRIMARY KEY   AUTOINCREMENT,YEAR  TEX NOT NULL,CLASS   TEXT "
        q+="NOT NULL,DIV TEXT NOT NULL)"
        self.cur.execute(q)
        self.con.commit()

        # STUDENT TABLE
        q="CREATE TABLE STUDENT(ID INTEGER PRIMARY KEY   AUTOINCREMENT,ADMISSION_NO  TEXT NOT NULL,NAME   TEXT  NOT NULL)"

        self.cur.execute(q)
        self.con.commit()
        # Score tables
        query="(ID INTEGER PRIMARY KEY   AUTOINCREMENT, STUDENT_ID INTEGER,DIV_ID INTEGER, ROLL TEXT,"

        query+="LANG_CE INT,LANG_MAX_CE INT,LANG_TE INT,LANG_MAX_TE INT,"

        query+="MAL_CE INT,MAL_MAX_CE INT,MAL_TE INT, MAL_MAX_TE INT,"

        query+="ENGLISH_CE INT,ENGLISH_MAX_CE INT,ENGLISH_TE INT,ENGLISH_MAX_TE INT,"

        query+="HINDI_CE INT,HINDI_MAX_CE INT,HINDI_TE	INT,HINDI_MAX_TE	INT,"

        query+="SS_CE INT,SS_MAX_CE INT,SS_TE INT,SS_MAX_TE INT,"

        query+="PHYSICS_CE INT,PHYSICS_MAX_CE INT,PHYSICS_TE INT,PHYSICS_MAX_TE INT,"

        query+="CHEMISTRY_CE INT,CHEMISTRY_MAX_CE INT,CHEMISTRY_TE INT,CHEMISTRY_MAX_TE INT,"

        query+="BIOLOGY_CE INT,BIOLOGY_MAX_CE INT,BIOLOGY_TE INT,BIOLOGY_MAX_TE INT,"

        query+="MATHEMATICS_CE INT,MATHEMATICS_MAX_CE INT,MATHEMATICS_TE INT,MATHEMATICS_MAX_TE INT,"

        query+="IT_CE INT,IT_MAX_CE INT,IT_TE INT,IT_MAX_TE INT,"

        query+="ATTENDANCE INT,MAX_ATTENDANCE INT)"

        t1="CREATE TABLE T1 "
        t2="CREATE TABLE T2 "
        t3="CREATE TABLE T3 "



        self.cur.execute(t1+ query)

        self.con.commit()

        self.cur.execute(t2+ query)

        self.con.commit()

        self.cur.execute(t3+ query)

        self.con.commit





    def InitialPopulation_Div(self):

        cls=("8","9","10")
        div=("A","B","C","D","E","F","G")
        year="2014"
        #,?, ?, ?,"+125*"'',"+"''#"+")"
        for c in cls:
            for d in div:

                query="INSERT INTO  DIV (YEAR,CLASS,DIV) VALUES(?,?,?)"                
                self.cur.execute(query,(year,c,d,))
                
        self.con.commit()    

        
    def Populate_All(self):

        #print "in populare all"
        self.cur2.execute('SELECT * FROM Students')

        #for row in self.cur2.execute('SELECT * FROM Students'):
        for row in self.cur2.fetchall():




            self.Populate_Student(row[3],row[5])
            last_row_id=self.cur.lastrowid # last row id of student table provides student id

            query="SELECT ID FROM DIV WHERE CLASS='"+row[1]+"' AND DIV='"+ row[2]+"'"       # find div id
            #print query

            self.cur.execute(query)

            #print " row id",last_row_id,row[1],row[2],self.cur.fetchone()[0]

            self.Populate_Score(last_row_id,self.cur.fetchone()[0],str(row[4]),row[3])



    def Add(self):
        pass


    def Populate_Student(self,ad_no,name):

        query="INSERT INTO  STUDENT (ADMISSION_NO,NAME) VALUES(?,?)"
        self.cur.execute(query,(ad_no,name))
        self.con.commit()
        #print " added",ad_no,name

    def Populate_Score(self,student_id,div_id,roll_no,admission_no):

        #print student_id,div_id,roll_no



        index=6

        query='''INSERT INTO  T1 (STUDENT_ID,DIV_ID,ROLL,LANG_CE,LANG_TE,MAL_CE,MAL_TE,ENGLISH_CE,ENGLISH_TE,HINDI_CE,HINDI_TE,SS_CE,SS_TE,


        PHYSICS_CE,PHYSICS_TE,CHEMISTRY_CE,CHEMISTRY_TE,BIOLOGY_CE,BIOLOGY_TE,MATHEMATICS_CE,MATHEMATICS_TE,IT_CE,IT_TE,ATTENDANCE)
         VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)


        '''
        #Start to Fecth Score

        for row in self.cur2.execute('SELECT * FROM Students WHERE Admission_NO="'+admission_no+'"'):

            #print (student_id,div_id,row[6],row[8],row[10],row[12],row[14],row[16],row[18],row[20],row[22],row[24],row[26],row[28],row[30],row[32],row[34],row[36],row[38],row[40],row[42],row[44],row[46])
            self.cur.execute(query,(student_id,div_id,roll_no,row[6],row[8],row[10],row[12],row[14],row[16],row[18],row[20],row[22],row[24],row[26],row[28],row[30],row[32],row[34],row[36],row[38],row[40],row[42],row[44],row[46]))
            self.con.commit()
            #print "added one score"


        #End of Fetching Score


    '''def Get_Working_Days(self,year,term):
        query="SELECT WORKING_DAYS FROM attendance WHERE YEAR=? AND TERM=?"
        print year,term
        self.cur.execute(query,(year,term,))
        result=self.cur.fetchone()
        if result:
            return result[0]
        else:
            
            return -1
    '''
    
    def Get_School_Name(self):
        E=my_encryption()
        query="SELECT NAME FROM institution"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result:
            return self.decrypt(E.decrypt(result[0]))
        else:
            return ""
    def Set_School_Name(self,name):
        
        E=my_encryption()
        query="UPDATE institution SET NAME=?"
        self.cur.execute(query,(E.encrypt(name),))
        self.con.commit()
    def Get_School_Code(self):
        
        query="SELECT CODE FROM institution"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result:
            return (result[0])
        else:
            return ""
        
    def Set_School_Code(self,code):
        query="UPDATE institution SET CODE=?"
        self.cur.execute(query,(code,))
        self.con.commit()
    def Get_School_Email(self):
        query="SELECT EMAIL FROM institution"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result:
            return (result[0])
        else:
            return ""
    def Set_School_Email(self,email):
        query="UPDATE institution SET EMAIL=?"
        self.cur.execute(query,(email,))
        self.con.commit()
    def Get_School_DEO(self):
        query="SELECT DEO FROM institution"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result:
            return (result[0])
        else:
            return ""
    def Set_School_DEO(self,place):
        query="UPDATE institution SET DEO=?"
        self.cur.execute(query,(place,))
        self.con.commit()
    def Get_School_Contact(self):
        query="SELECT CONTACT FROM institution"
        self.cur.execute(query)
        result=self.cur.fetchone()
        if result:
            return (result[0])
        else:
            return ""
    def Set_School_Contact(self,contact):
        query="UPDATE institution SET CONTACT=?"
        self.cur.execute(query,(contact,))
        self.con.commit()
        
    def Get_Working_Days(self,year,term):
        term='TERM'+str(term)
        query="SELECT  "+term +" FROM working_days WHERE YEAR=?"
        self.cur.execute(query,(year,))
        result=self.cur.fetchone()
        if result:
            return (result[0])
        else:
            return ""
    def Set_Working_Days(self,year,term,days):
                
        term='TERM'+str(term)
        
        # TESTING IF EXISTS
        query="SELECT  "+term +" FROM working_days WHERE YEAR=?"
        self.cur.execute(query,(year,))
        result=self.cur.fetchone()
        if result: #exists
            query='UPDATE working_days SET '+term+'=? WHERE YEAR=?'
            
            
        else:
            query='INSERT INTO working_days('+term+',YEAR) VALUES(?,?)'
        self.cur.execute(query,(days,year))
        return self.con.commit()
    def Get_Div_Id(self,year,clas,div):
        
        
        query="SELECT ID FROM DIV WHERE YEAR=? AND CLASS=? AND DIV=?"       # find div id
            #print query

        self.cur.execute(query,(year,clas,div,))

        #print " row id",last_row_id,row[1],row[2],self.cur.fetchone()[0]
        result=self.cur.fetchone()
        if result:
            
            return result[0]
        else:
            
            return -1
    
    def Get_Student_Id(self,div_id): #returns the List of Student id of a particular division
        
        query="SELECT DISTINCT STUDENT_ID FROM T1 WHERE DIV_ID=" + str(div_id)    
            

        self.cur.execute(query)

        
        ids=[]
        
        for each_row in self.cur.fetchall():
            if each_row[0]:
                
                ids.append(each_row[0])
            
        return ids
    def Get_Student_Id_By_Admission_No(self,admission_no):
        
        
        query="SELECT ID FROM STUDENT WHERE ADMISSION_NO=" + str(admission_no)   
            
            

        self.cur.execute(query)

        
        
        
        return self.cur.fetchone()[0]
    
    def Get_Student_List(self,year,class_,div):
        # returns the list containing student id, ad_no, and name of students of a division
        div_id=self.Get_Div_Id(year,class_,div)
        student_list=self.Get_Student_Id(div_id)
        my_list=[]
        for each in student_list:
            info=self.Get_Student_Info(each)
            if (info[0] and info[1] ):    
                my_list.append([each]+list(info))
        return my_list
        
        
    def Score_and_Roll(self,term,div_id,subject_index,student_id="All"): # Returns name, adno,roll,the score and roll no of one or all students
        
        # Gathrs info from T1,T2 ot T3 and Returns a tuple
        
        
        SUBJ=["LANG","MAL","ENGLISH","HINDI","SS","PHYSICS","CHEMISTRY","BIOLOGY","MATHEMATICS","IT","ATTENDANCE"]
        score=[
                ["Edited_STATUS","STUDENT_ID","ADMISSION_NO","NAME","SCORE_ID","ROLL","CE","MAX_CE","TE","MAX_TE"]
                
            ]
        
        subject_index=int(subject_index)
        if term!="1" and term!="2" and term!="3": # if term is wrongly passed by default takes TermI
            
            
            term="1"
        
        query="SELECT STUDENT_ID,ID,ROLL,"
        if subject_index==10: # Attendance
            query+="ATTENDANCE,MAX_ATTENDANCE"#SUBJ[subject_index]+",
        else:
            query+=SUBJ[subject_index]+"_CE,"+SUBJ[subject_index]+"_MAX_CE,"
            query+=SUBJ[subject_index]+"_TE,"+SUBJ[subject_index]+"_MAX_TE"
        
        query+=" FROM T"+term+" WHERE DIV_ID="+str(div_id  )
        
        if student_id!="All":
            
            query+=" AND STUDENT_ID="+str(student_id)
                 
            
        query+=' ORDER BY ROLL'
        self.cur.execute(query)

        
        score_row=0
        score_col=0
        
        for each_row in self.cur.fetchall():
            
            ad_no,name= self.Get_Student_Info(each_row[0])
            
            if ad_no==None:ad_no=''
            if name==None:name=''
                
                
            if subject_index==10: #Attendance
                r1=each_row[0]
                r2=each_row[1]
                r3=each_row[2]
                r4=each_row[3]
                r5=each_row[4]
                if r1==None:r1=''
                if r2==None:r2=''
                if r3==None:r3=''
                if r4==None:r4=''
                if r5==None:r5=''
                score.append([False,r1,ad_no,name,r2,r3,r4,r5])

            else:
                r1=each_row[0]
                r2=each_row[1]
                r3=each_row[2]
                r4=each_row[3]
                r5=each_row[4]
                r6=each_row[5]
                r7=each_row[6]
                if r1==None:r1=''
                if r2==None:r2=''
                if r3==None:r3=''
                if r4==None:r4=''
                if r5==None:r5=''
                if r6==None:r6=''
                if r7==None:r7=''
                
                score.append([False,r1,ad_no,name,r2,r3,r4,r5,r6,r7])
        
        return score
    def Get_Unpromoted(self,div_id,student_id="All"):
        #result format
        #["STUDENT_ID","DIV_ID","SCORE_ID","ADMISSION_NO","NAME",","ROLL"]
        
        query="SELECT STUDENT_ID,ID,ROLL FROM T1 WHERE PROMOTED=0 AND DIV_ID="+str(div_id  )
        
        
        if student_id!="All":
            
            query+=" AND STUDENT_ID="+str(student_id)            
            
        self.cur.execute(query)
        
        score_row=0
        score_col=0
        list=[]
        for each_row in self.cur.fetchall():
            
            ad_no,name= self.Get_Student_Info(each_row[0])
            list.append([each_row[0],div_id,each_row[1],ad_no,name,each_row[2]])
           
                
        return list
    def Get_Student_Info(self,student_id):
        
        query="SELECT ADMISSION_NO,NAME FROM STUDENT WHERE ID="+str(student_id)
        self.cur.execute(query)
        row= self.cur.fetchone()
        if row:
            return row[0],row[1]
        else:
            return "",""
        
    
    def Get_Class_Strength(self,year,clas,div):
        div_id=self.Get_Div_Id(year,clas,div)
        
        if div_id==-1:
            
            return 0
        query="SELECT COUNT (ID) FROM T1 WHERE DIV_ID="+str(div_id)
        self.cur.execute(query)
        row= self.cur.fetchone()
        if row:
            return row[0]
        else:
            return 0
    def Get_CE_TE(self,year,std,subject_index):
        
        '''if std=="10":
            std="9"
        '''
        if subject_index==11:
            subject_index=5
        SUBJ=["LANG","MAL","ENGLISH","HINDI","SS","PHYSICS","CHEMISTRY","BIOLOGY","MATHEMATICS","IT","ATTENDANCE"]
        
        query="SELECT CE,TE FROM CE_TE WHERE YEAR=? AND STD=? AND SUBJECT=?"
        #print "in ce\n",query,"\n",std,SUBJ[subject_index]
        self.cur.execute(query,(year,std,SUBJ[subject_index],))
        
       
        result=self.cur.fetchone()
        if result:
            
            return result[0],result[1]
        else:
            
            return -1,-1
        
    def Set_CE_TE(self,year,std,subject_index,ce,te):
        '''if std=="10":
            std="9"
        '''
        if subject_index==11:
            subject_index=5
        SUBJ=["LANG","MAL","ENGLISH","HINDI","SS","PHYSICS","CHEMISTRY","BIOLOGY","MATHEMATICS","IT"]
        
        
        #Checks if a year xists
        
        query='SELECT * FROM CE_TE WHERE YEAR=?'
        self.cur.execute(query,(year,))
        row= self.cur.fetchone()
       
        if not row:
           
            for all_std in ['8','9','10']:
                for item in SUBJ:
                
                
                    query='INSERT INTO CE_TE (YEAR,STD,SUBJECT,CE,TE) VALUES(?,?,?,?,?)'
                    self.cur.execute(query,(year,all_std,item,'',''))
            self.con.commit()
        
            
        query="UPDATE ce_te SET CE =?, TE=? WHERE YEAR=? AND STD=? AND SUBJECT=?"
        self.cur.execute(query,(str(ce),str(te),str(year),str(std),SUBJ[subject_index],))
        self.con.commit()
    def Get_Years(self):
        query="SELECT DISTINCT YEAR FROM DIV"
        self.cur.execute(query)
        result=self.cur.fetchall()
        years=[]
        for year in result:
            years.append(year[0])
        return years
    def get_academic_year_list(self):
        # returns a list to be added to combo box
        #["2014-15","2016-17"]
        years=self.Get_Years()
        years.sort()
        list=[]
        for each in years:
            
            list.append(str(each)+"-"+str(int(str(each)[2:])+1))
        return list
    def Add_Div(self,year,class_,div):
        query="INSERT INTO DIV (YEAR,CLASS,DIV) VALUES(?,?,?)"
        self.cur.execute(query,(year,class_,div))
        self.con.commit()
    def Get_Div(self,year,class_):
        query='SELECT DIV FROM DIV WHERE YEAR=? AND CLASS=? ORDER BY DIV'
        self.cur.execute(query,(year,class_))
        result=self.cur.fetchall()
        div=[]
        for item in result:
            div.append(item[0])
        return div
    def Div_Exists(self,year,class_,div):
        query='SELECT ID FROM DIV WHERE YEAR=? AND CLASS=? AND DIV=?'
        self.cur.execute(query,(year,class_,div))
        result=self.cur.fetchone()
        if result:
            return True
        return False
    def Student_Exists(self,admission_no):
        query='SELECT ID FROM STUDENT WHERE ADMISSION_NO=?'
        self.cur.execute(query,(admission_no,))
        if self.cur.fetchone():
            return True
        else:
            return False
        
    def Execute(self,query,args=()):
        
        return self.cur.execute(query,args)
    
    def Commit(self):
        return self.con.commit()
    
    
    
        
    def Update(self):

        pass

    def RemoveStudent(self,student_id):
        

        query="DELETE FROM STUDENT WHERE ID=?"
        self.cur.execute(query,(student_id,))
        self.con.commit()
        
    def RemoveScore(self,score_id):
        
        query="DELETE FROM T1 WHERE ID=?"
        self.cur.execute(query,(score_id,))
        
        query="DELETE FROM T2 WHERE ID=?"
        self.cur.execute(query,(score_id,))
        
        query="DELETE FROM T3 WHERE ID=?"
        self.cur.execute(query,(score_id,))
        
        
        self.con.commit()
    def Remove_Student_Full(self,adno):
        student_id=self.Get_Student_Id_By_Admission_No(adno)
        
        query="DELETE FROM STUDENT WHERE ID=?"
        self.cur.execute(query,(student_id,))
        #print "del q",query(student_id,)
        #print "adno",adno    
        query="DELETE FROM T1 WHERE STUDENT_ID=?"
        self.cur.execute(query,(student_id,))
        
        query="DELETE FROM T2 WHERE STUDENT_ID=?"
        self.cur.execute(query,(student_id,))
        
        query="DELETE FROM T3 WHERE STUDENT_ID=?"
        self.cur.execute(query,(student_id,))
        

        
        self.con.commit()        
    def Close(self):
        self.con.commit()
        self.con.close()
        #print "con closed"
    def Admission_Exists(self,ad_no):
        #if exixts return True,and name, if not return false
        query='SELECT NAME FROM STUDENT WHERE ADMISSION_NO=?'
        self.cur.execute(query,(ad_no,))
        result=self.cur.fetchone()
        if result:
            return [True,result[0]]
        else:
            return False
        
    def Print(self):

        #print "in print"

        for row in self.cur.execute('SELECT * FROM STUDENT'):

            #print row
            pass

        print "End Print"
    def Add_Student(self,roll,ad_no,name,year,class_,div):
        
        
        query="INSERT INTO STUDENT (ADMISSION_NO,NAME) VALUES(?,?)"
        self.Execute(query,(ad_no,name,))
        student_id=self.cur.lastrowid
        div_id=self.Get_Div_Id(year,class_,div)
        
        
        query="INSERT INTO T1 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term1_id=self.cur.lastrowid
        
        query="INSERT INTO T2 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term2_id=self.cur.lastrowid
        
        query="INSERT INTO T3 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term3_id=self.cur.lastrowid
        self.con.commit()
        return student_id, term1_id,term2_id,term3_id
    def Add_Student_Full(self,year,student_details,commit=True):
        
        #ORDER OF LIST
        #SL No. 	Class 	Division 	Admission_No 	Name 	UID 	Gender 	DOB 	Category 	Religion 	Caste 	First_Language 	Father 	Mother 	Phone
        # fro the form email also
        # Commit argument stops from invoking commit function of sqlite when bulk data is updated with sampoorna
        # It finally calls user deifned Commit function
        
            
        query="INSERT INTO STUDENT (ADMISSION_NO,NAME,UID,GENDER,DOB,CATEGORY,RELIGION,CASTE,FIRST_LANGUAGE,FATHER,MOTHER,PHONE,EMAIL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
        
        
        class_=student_details[1]
        div=student_details[2]
        ad_no=student_details[3]
        name=student_details[4]
        uid=student_details[5]
        gender=student_details[6]
        dob=student_details[7]
        category=student_details[8]
        religion=student_details[9]
        caste=student_details[10]
        lang=student_details[11]
        father=student_details[12]
        mother=student_details[13]
        phone=student_details[14]
        email=student_details[15]
        roll=student_details[16]
        #print query,(ad_no,name,uid,gender,dob,category,religion,caste,lang,father,mother,phone,email)

        self.Execute(query,(ad_no,name,uid,gender,dob,category,religion,caste,lang,father,mother,phone,email))

        student_id=self.cur.lastrowid
        if (not self.Div_Exists(year,class_,div)):
            self.Add_Div(year,class_,div)
        div_id=self.Get_Div_Id(year,class_,div)
        
        query="INSERT INTO T1 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term1_id=self.cur.lastrowid
        
        #print "term q",query,(student_id,div_id,roll,)

        
        query="INSERT INTO T2 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term2_id=self.cur.lastrowid
        
        query="INSERT INTO T3 (STUDENT_ID,DIV_ID,ROLL) VALUES(?,?,?)"
        self.Execute(query,(student_id,div_id,roll,))
        term3_id=self.cur.lastrowid
        if commit:
            self.con.commit()
        
        return student_id, term1_id,term2_id,term3_id
        # Adds all details of new students 
    
        
    def Update_Student_Full(self,year,student_details,previous_ad_no=0,commit=True):
        
        # if students alredy exists compltes their profiels and updates their present class
        # When admsssion no updates students id woudnt exists ffor new id.
        # Commit argument stops from invoking commit function of sqlite when bulk data is updated with sampoorna
        # It finally calls user deifned Commit function
        query="UPDATE STUDENT SET ADMISSION_NO=?,NAME=?,UID=?,GENDER=?,DOB=?,CATEGORY=?,RELIGION=?,CASTE=?,FIRST_LANGUAGE=?,FATHER=?,MOTHER=?,PHONE=?,EMAIL=? WHERE ADMISSION_NO=? "

        class_=student_details[1]
        div=student_details[2]
        ad_no=student_details[3]        
        name=student_details[4]
        uid=student_details[5]
        gender=student_details[6]
        dob=student_details[7]
        category=student_details[8]
        religion=student_details[9]
        caste=student_details[10]
        lang=student_details[11]
        father=student_details[12]
        mother=student_details[13]
        phone=student_details[14]
        email=student_details[15]
        roll=student_details[16]
        if previous_ad_no:
            
            student_id=self.Get_Student_Id_By_Admission_No(previous_ad_no)
        else:
            student_id=self.Get_Student_Id_By_Admission_No(ad_no)
        self.Execute(query,(ad_no,name,uid,gender,dob,category,religion,caste,lang,father,mother,phone,email,ad_no))

        #print query
        
        if (not self.Div_Exists(year,class_,div)):
            self.Add_Div(year,class_,div)
        div_id=self.Get_Div_Id(year,class_,div)
        
        roll=int(roll)
        query="UPDATE T1 SET DIV_ID=?,ROLL=? WHERE STUDENT_ID=? "
        self.cur.execute(query,(div_id,roll,student_id,))
        
        query="UPDATE T2 SET DIV_ID=?, ROLL=?WHERE STUDENT_ID=? "
        self.cur.execute(query,(div_id,roll,student_id))
        
        query="UPDATE T3 SET DIV_ID=?, ROLL=? WHERE STUDENT_ID=?"
        self.cur.execute(query,(div_id,roll,student_id))
        if commit:
            self.con.commit()
    def Get_Profile(self,admission_no):
        # returns information for student profile
        fields=" NAME,UID, GENDER, DOB, CATEGORY, RELIGION, CASTE, FIRST_LANGUAGE,FATHER,MOTHER,PHONE,EMAIL "
        query="SELECT "+fields+" FROM STUDENT WHERE ADMISSION_NO=?"
        result1=self.cur.execute(query,(admission_no,))
        list1= result1.fetchone()
        
        query2="SELECT ROLL FROM T1 WHERE STUDENT_ID=?"
        student_id=self.Get_Student_Id_By_Admission_No(admission_no)
        result2=self.cur.execute(query2,(student_id,))
        list2=result2.fetchone()
        
       
        result=[]
        if list1:
            result+=list(list1)
        if list2:
            result+=list(list2)
            
       
        return result
       
       
        
        
    def DeleteDuplicates(self):
        
        query="SELECT COUNT (ID) FROM T1"
        
        result=self.ExecuteSql(query)
        count=result.fetchone()[0]
        for i in range(1,count+1,1):
            
            query="SELECT STUDENT_ID FROM T1 WHERE ID=?"
            self.cur.execute(query,(i,))
            rows=self.cur.fetchall()
            for row in rows:
                
                row[0]
                query2="SELECT ID FROM T1 WHERE STUDENT_ID=?"
                self.cur.execute(query2,(row[0],))
                count=1
                for item in self.cur.fetchall():
                    if count==1:
                        count+=1
                        continue
                    else:
                        
                        #print "more than one"
                        query3="DELETE FROM T1 WHERE ID=?"
                        
                        self.cur.execute(query3,(item[0],))
                        
                        
                        
        # Removes from Suer table
        query="SELECT COUNT (ID) FROM STUDENT"
        
        result=self.ExecuteSql(query)
        count=result.fetchone()[0]
        for i in range(1,count+1,1):
            
            query="SELECT ID, ADMISSION_NO FROM STUDENT WHERE ID=?"
            self.cur.execute(query,(i,))
            rows=self.cur.fetchall()
            count=1
            for row in rows:
                
                if count==1:
                    count+=1
                    continue
                
                query2="DELETE FROM STUDENT WHERE ID=?"
                        
                self.cur.execute(query2,(row[0],))
                #print "deleting"

                
                     
        self.con.commit()
        
    def export(self,path):
        
        #from encrypt import encrypt_file
        #encr=encrypt_file()
        
        with open(path, 'w') as f:
        
            for line in self.con.iterdump():
                f.write('%s\n' % line)
                    
                    
        #encr.encrypt_file(path)
        f.close()
    def import_ (self,path):
        
        
        #try:
        # variable name 'oroginal' is generaly assigned to the values of DB residing in the disk
        #  variable name 'new' is generally assigned to values of the DB to be imported
        
        
        
        
        self.con2=mysql.connect(":memory:")
       
        
        self.cur2 = self.con2.cursor()
        
        
        
        #encr.decrypt_file(path)
        f=open(path)
        sql = f.read() # watch out for built-in `str`
        f.close()
        #encr.encrypt_file(path)
        self.cur2.executescript(sql)
        self.con2.commit()
        #self.import_div()
        #self.con.commit()
        self.import_ce()
        self.import_working_days()
        self.import_student()
        self.import_score()
        
        self.cur2.execute("DROP TABLE STUDENT")
        self.cur2.execute("DROP TABLE DIV")
        self.cur2.execute("DROP TABLE T1")
        self.cur2.execute("DROP TABLE T2")
        self.cur2.execute("DROP TABLE T3")
        self.cur2.execute("DROP TABLE CE_TE")
        self.cur2.execute("DROP TABLE USER")
        self.cur2.execute("DROP TABLE INSTITUTION")
        self.cur2.execute("DROP TABLE WORKING_DAYS")
        self.con2.commit()
        
        self.con2.close()
        
        
            
    def  import_student(self):
        
        #print "importin sdnts"
        #try:
        #Begin check if already exists/needs updation
        query="SELECT * FROM STUDENT"        
        self.cur2.execute(query)
        
        for new_row in self.cur2.fetchall():
            #print "in for"
            new_ad_no=new_row[1]
            new_name=new_row[2]
            
            query="SELECT * FROM STUDENT WHERE ADMISSION_NO=?"
            self.cur.execute(query,(new_ad_no,))
            original_rows=self.cur.fetchone()
            #print "orogonal rows",original_rows
            if original_rows==None:# Does not exists; add new
                
                #print "not exixt, addin",new_name
                
                query="INSERT INTO  STUDENT (ADMISSION_NO,NAME) VALUES(?,?)"
                self.cur.execute(query,(new_ad_no,new_name))
                
                
            else:#  exixts,checks if has to update
                
                
                original_ad_no=original_rows[1]
                original_name=original_rows[2]
            
                if new_name==original_name: # Name same , no need to upadte
                    pass
                else: # Updates
                    query="UPDATE STUDENT SET NAME=? WHERE ADMISSION_NO=?"
                    self.cur.execute(query,(new_name,new_ad_no,))
                
                    
                    
        self.con.commit()
        
                        
    def import_score(self):
        
        
        
        for term in ("T1 ","T2 ","T3 "):
            
            query="SELECT * FROM "+term
            
            self.cur2.execute(query)
            new_score=self.cur2.fetchall()
            for new_row in new_score:
                
                new_student_id=new_row[1]
                new_div_id=new_row[2]
                
                
                
                #Begin. This block finds corresponding origina l-table div id for the division found in the new table
                query="SELECT YEAR,CLASS,DIV FROM DIV WHERE ID=?"
                self.cur2.execute(query,(new_div_id,))
                new_div_row=self.cur2.fetchone()
                
                #print "div row",new_div_row
                
                new_div_year=new_div_row[0]
                new_div_class=new_div_row[1]
                new_div_div=new_div_row[2]
                
                
                
                query="SELECT ID FROM DIV WHERE YEAR=? AND CLASS=? AND DIV=?"
                self.cur.execute(query,(new_div_year,new_div_class,new_div_div,))
                result=self.cur.fetchone()
                
                if result==None:# div does not exists; add new div to original db
                    # this can b removed if div import implimented
                    query="INSERT INTO DIV(YEAR,CLASS,DIV) VALUES(?,?,?)"
                    self.cur.execute(query,(new_div_year,new_div_class,new_div_div))
                    original_div_id=self.cur.lastrowid
                    
                else:
                    original_div_id=result[0]
                # end
                
                #This block finds corresponding original-table student_id 
                
                query="SELECT ADMISSION_NO FROM STUDENT WHERE ID=?"
                self.cur2.execute(query,(new_student_id,))
                new_student_ad_no=self.cur2.fetchone()[0]
                
                query="SELECT ID FROM STUDENT WHERE ADMISSION_NO=?"
                self.cur.execute(query,(new_student_ad_no,))
                original_student_id=self.cur.fetchone()[0]
                
                #end
                
                # IMPORTING HERE
                # IMPORTING HERE
                
                query="SELECT * FROM "+term+ " WHERE STUDENT_ID=? AND DIV_ID=?"
                self.cur.execute(query,(original_student_id,original_div_id,))
                original_score_row=self.cur.fetchall()
                
                if original_score_row==None or len(original_score_row)==0: # if no record, just add that row   changing ids  ,
                    #Then following code updates it  
                    
                    
                    query="INSERT INTO "+term+" (STUDENT_ID,DIV_ID) VALUES(?,?)"
                    self.cur.execute(query,(original_student_id,original_div_id,))
                    
                args=()
                SUBJ=["LANG","MAL","ENGLISH","HINDI","SS","PHYSICS","CHEMISTRY","BIOLOGY","MATHEMATICS","IT","ATTENDANCE"]
                SUFX=["_CE","_MAX_CE","_TE","_MAX_TE"]
                new_roll=new_row[3]
                query_last_part= "WHERE STUDENT_ID=? AND DIV_ID=? "
                args_last_part=(original_student_id,original_div_id,)
                flag1,flag2=False,False
                if new_roll!=None:
                    query_part1="UPDATE "+term+" SET ROLL=? "
                    args=(new_roll,)
                    flag1=True
                else:
                    query_part1="UPDATE "+term
                    
                for i in range(4,46,1):
                    
                    if new_row[i]!=None and new_row[i]!='':
                        
                        subj_index=(i/4)-1
                        sufx_index=i%4
                        
                        if flag1==True and flag2==False:
                            
                            query_part1+=","
                        elif flag2:
                            query_part1+=","
                            
                        if subj_index==10: #Attennadance
                            if sufx_index==0:# first time
                                query_part1+="ATTENDANCE=?"
                                args+=(new_row[i],)
                                
                            elif sufx_index==1:# 2nd time
                                query_part1+="MAX_ATTENDANCE=?"
                                args+=(new_row[i],)
                                
                        else:
                            query_part1+=SUBJ[subj_index]+SUFX[sufx_index]+"=? "
                            args+=(new_row[i],)
                        
                        
                        flag2=True
                        
                promo=new_row[46]#Col Promoted
                
                args+=(promo,)
                args+=args_last_part
                query=query_part1+',PROMOTED=? '+query_last_part
                
                if query_part1=='':
                    
                    pass
                else:
                    
                    self.cur.execute(query,args)
                    
        self.con.commit()   
              
    def import_div(self):
        query="SELECT * FROM DIV"        
        self.cur2.execute(query)
        for new_row in self.cur2.fetchall():
            
            new_year=new_row[1]
            new_class=new_row[2]
            new_div=new_row[3]
            query='SELECT ID FROM DIV WHERE YEAR=? AND CLASS=? AND DIV=?'
            self.cur.execute(query,(new_year,new_class,new_div))
            result=self.cur.fetchone()
            if result!=None:# div does not exists
                query='INSERT INTO DIV (YEAR,CLASS,DIV) VALUES(?,?,?)'
                self.cur.execute(query,(new_year,new_class,new_div))
        self.con.commit()
           
    def import_ce(self):
        query='SELECT * FROM CE_TE'
        
        self.cur2.execute(query)
        
        for new_row in self.cur2.fetchall():
            
            new_std=new_row[1]
            new_sub=new_row[2]
            new_ce=new_row[3]
            new_te=new_row[4]
            new_year=new_row[5]
            
            query="SELECT * FROM CE_TE WHERE STD=? AND SUBJECT=? AND YEAR=?"
            self.cur.execute(query,(new_std,new_sub,new_year))
            original_rows=self.cur.fetchone()
            
            if original_rows==None:# Does not exists; add new
                
                query="INSERT INTO  CE_TE (STD,SUBJECT,YEAR,CE,TE) VALUES(?,?,?,?,?)"
                self.cur.execute(query,(new_std,new_sub,new_year, new_ce,new_te))
                
            else:#  exixts,checks if has to update
                
                
                
                original_id=original_rows[0]
                original_std=original_rows[1]
                original_sub=original_rows[2]
                original_ce=original_rows[3]
                original_te=original_rows[4]
                original_year=original_rows[5]
            
            
                if new_std==original_std and new_sub==original_sub and new_ce==original_ce and new_te==original_te and new_year==original_year : # Name same , no need to upadte
                    pass
                else: # Updates
                    args=(new_std,new_sub)
                    query="UPDATE CE_TE SET STD=?,SUBJECT=?"
                    if new_ce!=None and new_ce!='':
                        args+=(new_ce,)
                        query+=',CE=?'
                    if new_te!=None and new_te!='':
                        
                        args+=(new_te,)
                        query+=',TE=?'
                        
                    args+=(new_year,original_id)
                    query+=',YEAR=? WHERE ID=?'
                    self.cur.execute(query,args)
                
                    
                    
        self.con.commit()
        
                       
         
    def import_working_days(self):
        query='SELECT * FROM WORKING_DAYS'
        
        self.cur2.execute(query)
        
        for new_row in self.cur2.fetchall():
            
            new_year=new_row[1]
            new_t1=new_row[2]
            new_t2=new_row[3]
            new_t3=new_row[4]
            
            
            query="SELECT * FROM WORKING_DAYS WHERE YEAR=?"
            self.cur.execute(query,(new_year,))
            original_rows=self.cur.fetchone()
            
            if original_rows==None:# Does not exists; add new
                
                query="INSERT INTO  WORKING_DAYS (YEAR,TERM1,TERM2,TERM3) VALUES(?,?,?,?)"
                self.cur.execute(query,(new_year,new_t1,new_t2,new_t3))
                
            else:#  exixts,checks if has to update
                
                
                
                original_id=original_rows[0]
                original_year=original_rows[1]
                original_t1=original_rows[2]
                original_t2=original_rows[3]
                original_t3=original_rows[4]
                
            
            
                if new_year==original_year and new_t1==original_t1 and new_t2==original_t2 and new_t3==original_t3 : # Name same , no need to upadte
                    pass
                else: # Updates
                    flag=False
                    query="UPDATE WORKING_DAYS SET "
                    args=()
                    if new_t1!=None and new_t1!='':
                        query+='TERM1=?'
                        args+=(new_t1,)
                    if new_t2!=None and new_t2!='':
                        query+=',TERM2=?'
                        args+=(new_t2,)
                    if new_t3!=None and new_t3!='':
                        query+=',TERM3=?'
                        args+=(new_t3,)
                        
                    
                    query+=' WHERE ID=?'
                    args+=(original_id,)
                    self.cur.execute(query,args)
                
                    
                    
        self.con.commit()
        
                
    def encrypt(self,text):
        return text
    def decrypt(self,text):
        return text       
            
            
            
    def reset_table_time(self):
        #deletes the table of time of upload and resets a new one to be backed up
        query='DROP TABLE IF EXISTS BACKUP_TIME;'    
        self.cur.execute(query)
        self.con.commit() 
        
        
        #creates new
        query="CREATE TABLE BACKUP_TIME(ID INTEGER PRIMARY KEY   AUTOINCREMENT,YEAR TEX NOT NULL,MONTH TEXT NOT NULL,DAY TEXT NOT NULL, HOUR TEXT NOT NULL,MINUTE TEXT NOT NULL )"       
        self.cur.execute(query)
        self.con.commit() 
        
        import datetime

        now = datetime.datetime.now()
        year=now.year
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute
        
        query="INSERT INTO  BACKUP_TIME (YEAR,MONTH,DAY,HOUR,MINUTE) VALUES(?,?,?,?,?)"                
        self.cur.execute(query,(year,month,day,hour,minute,))
        self.con.commit() 

