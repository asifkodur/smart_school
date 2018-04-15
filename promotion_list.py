from __future__ import division
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Spacer,Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4,A3,landscape
from reportlab.lib.units import inch,cm
from reportlab.platypus import PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY,TA_LEFT,TA_RIGHT

import wx

from reportlab.platypus.flowables import Flowable,Image

from reportlab.lib import pdfencrypt

from dboperations import db_operations
from reportlab.lib.units import inch, mm

#Test  encrp
def encrpytmypdf(passwd=''):
    
    return pdfencrypt.StandardEncryption(passwd,canPrint=0)

# Test Encr

class verticaltext(Flowable):


    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text

    def draw(self):
        canvas = self.canv
        canvas.rotate(90)
        
        fs = canvas._fontsize
        
        
        canvas.translate(1, -fs)  # canvas._leading?
        canvas.drawString(0, 0, self.text)

    def wrap(self, aW, aH):
        canv = self.canv
        
        fn, fs = canv._fontname, canv._fontsize
        
        return canv._leading, 1 + canv.stringWidth(self.text, fn, fs)
class verticaltext_small(Flowable):
    
    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text
        

    def draw(self):
        canvas = self.canv
        #canvas.hAlign='RIGHT'
        canvas.setFont("Times-Roman", 7)
        
        canvas.rotate(90)
        
        fs = canvas._fontsize
        
        text_len=len(self.text)
        canvas.translate(text_len-1, -fs)  # canvas._leading?
        canvas.drawString(0, 0, self.text)

    def wrap(self, aW, aH):
        canv = self.canv
        
        fn, fs = canv._fontname, canv._fontsize
        
        return canv._leading, 1 + canv.stringWidth(self.text, fn, fs)
       
        
        
        
class RotatedPara(Paragraph):


    def draw(self):
        self.canv.saveState()
        self.canv.translate(0,0)# 23,-10
        self.canv.rotate(360)
        Paragraph.draw(self)

        self.canv.restoreState()

class RotatedPara_2(Paragraph):
    
        
    def draw(self):
        self.canv.saveState()
        self.canv.translate(0,0)# 23,-10
        self.canv.rotate(0)
        Paragraph.draw(self)

        self.canv.restoreState()

class RotatedPara_3(Paragraph):


    def draw(self):
        self.canv.saveState()
        self.canv.translate(17,-5)# 23,-10
        self.canv.rotate(90)
        Paragraph.draw(self)

        self.canv.restoreState()
        
class RotatedPara_4(Paragraph):
    
        
    def draw(self):
        self.canv.saveState()
        self.canv.translate(30,-15)# 23,-10
        self.canv.rotate(90)
        Paragraph.draw(self)
            
        self.canv.restoreState()




styleSheet = getSampleStyleSheet()



class Promotion_List():
 

   
    
    def __init__(self,year="",school="",class_="",div="",edu_dist="",working_days="",con=[],mypagesize=A3,path="/tmp/promotion_list.pdf",passwd=''):#(21*cm,25*cm)):
        
        #print deo,school,"printing1"
        self.path=path
        self.passwd=passwd
        self.year=year
        self.school=school
        self.class_=class_
        self.div=div
        self.edu_dist=edu_dist
        self.working_days=str(working_days)
        
        self.Failed_List=[]
        if con!=[]:
            self.con=con[0]
            self.cur=con[1]
        self.mypagesize=mypagesize
        
        self.DB=db_operations()
        styleSheet = getSampleStyleSheet()
        
        self.elements = []
        enc=self.encrpytmypdf()
        self.doc = SimpleDocTemplate(self.path, pagesize=landscape(mypagesize),title="Promotion List",topMargin=.2*inch,bottomMargin=.2*inch,author="Asif Kodur",subject="easy exam",encrypt=enc)
        
        self.passed_no=0
        self.table_count=0     
        self.page_count=0   
        #self.Set_Content()
         

        # Starts measurement
        if mypagesize==A3:

            self.cW1=.8
            self.cW2=6
            self.cW3=.55
            self.cW4=.4
            self.cW5=.9
            
            
            
            self.rH1=.35
            
            self.rH2=.8
            
            self.rH3=2
            
            self.rH4=.5
        '''
        elif mypagesize==A4:
            self.cW1=.4
            self.cW2=3
            self.cW3=.22
            self.cW4=.2
            self.cW5=.45
            
            
            
            self.rH1=.12
            
            self.rH2=.4
            
            self.rH3=1
            
            self.rH4=.25
        '''
        # This area can be uncommented to enable TE total in remark
        '''msg="Do you want to add total of TE in remarks column ?"
        dlg = wx.MessageDialog(None, msg,style=wx.YES_NO)            
        if dlg.ShowModal() == wx.ID_YES:
            
            self.REMOVE_TOTAL=False
        else:
            self.REMOVE_TOTAL=True
        '''
        self.REMOVE_TOTAL=True

        #end of measurement
    def Set_Heading(self):
        
        
        
        # Rotated Text here
        style = getSampleStyleSheet()
        normal = style["Normal"]
        style1=ParagraphStyle(name='normal',fontSize = 8,alignment = TA_CENTER)
        
        
        style = getSampleStyleSheet()
        normal = style["Normal"]
        
        style1=ParagraphStyle(name='normal',fontSize = 8,alignment = TA_CENTER)
        
        roll=verticaltext('Roll No')
        
        ad_no=verticaltext('Adm No')
        trm='Term'
        year="Year\nof\nStudy"
        ce="CE"
        total=verticaltext('Total')
        te="TE"
        grade=verticaltext('Grade')
        practical=verticaltext('Practical')
        work_exp="Work\nExp"
        art_edu="Art\nEdu"
        phy_edu="Phy&\nHlth\nEdu"
        
        
        '''
        commu=Image('Resources/promotion_list_img/communication.png')#'commu'
        commu.drawHeight=35
        commu.drawWidth=5
        '''
        commu=verticaltext_small('Communication')
        
        group=verticaltext_small('Group Activity')
        
        regularity=verticaltext_small('Regularity')
        
        leadership=verticaltext_small('Leadership')
        
        club=verticaltext_small('Club Activity')
        
        
        attndn=verticaltext_small('Attendance(%)')#<font size=7>Attendance(%)</font>')
        promotion=verticaltext_small('Promoted/Detained')#<font size=7>Promoted/Detained</font>')
        basis=verticaltext_small('Basis of Promotion')#<font size=7>Basis_of_Promotion</font>')
        remarks=verticaltext_small('Remarks')#<font size=7> Remarks</font>')
        # End of Totated Txt
        if self.class_=='8':
            
            science='Basic Science'
        else:
            science='Physics'
        name=self.Format_Name('Name of Student')
        
        row1=[roll,ad_no,name,trm,year]+['I lang \nPart I','','','']
        row1+=['I lang\nPart II','','','']+['English','','','']+['Hindi','','','']+['S.S','','','']
        row1+=[science,'','','']+['Chemistry','','','']+['Biology','','','']
        row1+=['Maths','','','']+['I.T','','','','']
        row1+=['Part II','','','','','']+['Part III','','','','']
        row1+=[attndn,promotion,basis,remarks]
        
        row2=['','','','','']+[ce,te,total,grade]*9+[ce,te,practical,total,grade]
        row2+=[work_exp,'',art_edu,'',phy_edu,''] #part II
        row2+=[commu,group, regularity,leadership,club]# part III
        row2+=['','','','']
        
        row3=['','','','','']+['s','s','','']*9+['s','s','','','']+['S','G']*3+['G']*5+['']*4
        
        
        self.HEADING=[row1,row2,row3]
        
        #print len(row1),len(row2),len(row3)
        
    def Set_Heading_Style(self):
        
        self.Heading_Style=[('BOX',(0,0),(-1,-1),1.7,colors.black),
        
                                ('GRID',(0,0),(-1,-1),1,colors.black),#
                                
                                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                
                                
                                ('SPAN',(0,0),(0,-1)), # Roll
                                ('SPAN',(1,0),(1,-1)), # Ad_no
                                ('SPAN',(2,0),(2,-1)),   # Name
                                ('SPAN',(3,0),(3,-1)),   # Year
                                ('SPAN',(4,0),(4,-1)),   # Year
                                
                                ('SPAN',(5,0),(8,0)),   # Subjects1
                                ('SPAN',(7,1),(7,2)),   # Subjects1 total
                                ('SPAN',(8,1),(8,2)),   # Subjects1grade
                                
                                ('SPAN',(9,0),(12,0)),   # Subjects 2
                                ('SPAN',(11,1),(11,2)),   # Subjects 2 tot
                                ('SPAN',(12,1),(12,2)),   # Subjects 2 grd                                
                                
                                ('SPAN',(13,0),(16,0)),   # Subjects 3
                                ('SPAN',(15,1),(15,2)),   # Subjects 3 tot
                                ('SPAN',(16,1),(16,2)),   # Subjects 3 grd
                                
                                ('SPAN',(17,0),(20,0)),   # Subjects 4
                                ('SPAN',(19,1),(19,2)),   # Subjects 4 tot
                                ('SPAN',(20,1),(20,2)),   # Subjects 4grd
                                
                                ('SPAN',(21,0),(24,0)),   # Subjects 5
                                ('SPAN',(23,1),(23,2)),   # Subjects 5
                                ('SPAN',(24,1),(24,2)),   # Subjects 5
                                
                                ('SPAN',(25,0),(28,0)),   # Subjects 6
                                ('SPAN',(27,1),(27,2)),   # Subjects 6
                                ('SPAN',(28,1),(28,2)),   # Subjects 6
                                
                                ('SPAN',(29,0),(32,0)),   # Subjects 7
                                ('SPAN',(31,1),(31,2)),   # Subjects 7
                                ('SPAN',(32,1),(32,2)),   # Subjects 7
                                
                                ('SPAN',(33,0),(36,0)),   # Subjects 8
                                ('SPAN',(35,1),(35,2)),   # Subjects 8
                                ('SPAN',(36,1),(36,2)),   # Subjects 8
                                
                                ('SPAN',(37,0),(40,0)),   # Subjects 9
                                ('SPAN',(39,1),(39,2)),   # Subjects 9
                                ('SPAN',(40,1),(40,2)),   # Subjects 9
                                
                                
                                ('SPAN',(41,0),(45,0)),   # IT
                                ('SPAN',(43,1),(43,2)),   # IT prct
                                ('SPAN',(44,1),(44,2)),   # IT tot
                                ('SPAN',(45,1),(45,2)),   # IT grd
                                
                                ('SPAN',(46,0),(51,0)),   # Part2
                                ('SPAN',(46,1),(47,1)),   # Part2 row2
                                ('SPAN',(48,1),(49,1)),   # Part2 row2
                                ('SPAN',(50,1),(51,1)),   # Part2 row2
                                
                                
                                ('SPAN',(52,0),(56,0)),   # Part3
                                ('VALIGN',(52,0),(56,0),'TOP'),
                                ('ALIGN',(52,0),(56,0),'RIGHT'),
                                
                                ('SPAN',(57,0),(57,-1)),   # attnd
                                ('SPAN',(58,0),(58,-1)),   # promo
                                ('SPAN',(59,0),(59,-1)),   # Basis
                                ('SPAN',(60,0),(60,-1)) ,  # Remark
                                
                                
                                ('BOX',(0,0),(4,3),1.5,colors.black), # Subject Blocks
                                ('BOX',(5,0),(8,3),1.5,colors.black),
                                ('BOX',(9,0),(12,3),1.5,colors.black),
                                ('BOX',(13,0),(16,3),1.5,colors.black),
                                ('BOX',(17,0),(20,3),1.5,colors.black),
                                ('BOX',(21,0),(24,3),1.5,colors.black),
                                ('BOX',(25,0),(28,3),1.5,colors.black),
                                ('BOX',(29,0),(32,3),1.5,colors.black),
                                ('BOX',(33,0),(36,3),1.5,colors.black),
                                ('BOX',(37,0),(40,3),1.5,colors.black),
                                ('BOX',(41,0),(45,3),1.5,colors.black), # IT with practical
                                ('BOX',(46,0),(51,3),1.5,colors.black),
                                ('BOX',(52,0),(56,3),1.5,colors.black),
                                ('BOX',(53,0),(54,3),1.2,colors.black),# % and all
                                ('BOX',(55,0),(56,3),1.2,colors.black),
                                ('BOX',(57,0),(58,3),1.2,colors.black),
                                ('BOX',(59,0),(60,3),1.2,colors.black)
                                
                                ]
                                
                                
                                
                                
                                
    def Set_Consolidation(self):
        
        style1=ParagraphStyle(name='normal',fontSize = 8,alignment = TA_CENTER)
        
       
        t1=Paragraph('<font size=6 >Boys</font>',style1)
        t2=Paragraph('<font size=6>Girls</font>',style1)
        t3=Paragraph('<font size=6>Total</font>',style1)
        t4=Paragraph('<font size= 7>Total No of Students</font>',style1)
        t5=Paragraph('<font size= 7>No of Students Promoted</font>',style1)
        t6=Paragraph('<font size= 7>No of Students Detained</font>',style1)
        t7=Paragraph('<font size=7 >Percetage of Promotion</font>',style1)
        
        t8=Paragraph('<font size=8 >Place :</font>',style1)
        t9=Paragraph('<font size=8 >Date :</font>',style1)
        t10=Paragraph('<font size=8 >School Seal</font>',style1)
        t11=Paragraph('<font size=8 >Name and Signature of Class Teacher</font>',style1)
        t12=Paragraph('<font size=8 >Signature of Head of the School</font>',style1)
        
        pass_percentage='0'
        try:
            pass_percentage=round((self.passed_no*100)/self.total_no,2)
            pass_percentage=str(pass_percentage)
            splt=pass_percentage.split('.')
        except:
            print 'nopass percnt'
        if len(splt)==2:
            pass_percentage=splt[0]+"."+splt[1][:2]         
        
        self.total_no=Paragraph('<font size=7 >'+str(self.total_no)+'</font>',style1)
        self.passed_no=Paragraph('<font size=7 >'+str(self.passed_no)+'</font>',style1)
        self.failed_no=Paragraph('<font size=7 >'+str(self.failed_no)+'</font>',style1)
        pass_percentage=Paragraph('<font size=7 >'+str(pass_percentage)+'</font>',style1)
        
        row1=['','',t1,t2,t3,'','','']
        row2=[t8,t4,'  ','',self.total_no,'','','']
        row3=['',t5,'  ','',self.passed_no,'','','']
        row4=[t9,t6,'  ','',self.failed_no,t10,t11,t12]
        row5=['',t7,'  ','',pass_percentage,'','','']
        
        self.CONSOLIDATION=[row1,row2,row3,row4,row5]
                               
                
    def Set_Consolidation_Style(self):
        
        self.Consolidation_Style=[('BOX',(1,0),(4,-1),1,colors.black),
        
                                ('GRID',(1,0),(4,-1),1,colors.black),#
                                
                                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                                ('ALIGN',(0,0),(-1,-1),'CENTER')]
        
    
    def Set_Content(self):
        
        #global year,class_,name,roll_no,admission_no
        
        #SCORE TABLE CONTENT STARTS
        
        
        
        
        
        #tEMPORARILY DISCONNECTED BELOW
        """    
        self.NAME=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=14><i>Performance Card of : %s</i>
            
           </font> </b>
            </para>'''%(self.name),
            styleSheet["BodyText"])
            
            
        self.ADMISSION_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Admission No : %s</i>
            
           </font> </b>
            </para>'''%(self.admission_no),
            styleSheet["BodyText"])
            
            
        self.ROLL_NO=Paragraph('''
            <para align=left spaceb=3><b>
            <font size=11><i>Roll No : %s</i>
            
           </font> </b>
            </para>'''%(self.roll_no),
            styleSheet["BodyText"])
           
            
        #SCORE TABLE CONTENT ENDS


        """
        #Test values
        
        
        # Test Values end
        self.Set_Heading()
        self.Populate()
        
    def Format_Part_3(self):
        
        commu=verticaltext('communication skill')
        group=verticaltext('Group Activity Skill')
        regularity=verticaltext('Regularity')
        leadership=verticaltext('Leadership/n Quality')
        club=verticaltext('Club Activity')
        
    def Format_Adm_No(self,ad_no):
                
        style = getSampleStyleSheet()
        normal = style["Normal"]
        
        style1=ParagraphStyle(name='normal',fontSize = 8,alignment = TA_CENTER)
        
       
        ad_text= Paragraph('<font size=6>'+str(ad_no)+'</font>',style1)
        return verticaltext(str(ad_no))
        
    def Format_Title(self):
        
        
        title_text1="<b>PROMOTION RECORD OF PUPILS FOR THE YEAR "
        title_text1+=self.year+"-"+str(int(self.year)+1)
        title_text1+="..(STD VIII AND IX)</b>"
        
        title_text2="School: "+self.school+".   Class: "+self.class_+".   Div: "+self.div
        title_text2+=".   Education District: "+self.edu_dist+".   Total No of working days :"+self.working_days
        
        title_style1=ParagraphStyle(name='fancy',fontSize = 20,alignment = TA_CENTER)
        
       
        self.TITLE1=Paragraph(title_text1,title_style1)
        
        
        title_style2=ParagraphStyle(name='fancy2',fontSize = 14)
       
        
        self.TITLE2=Paragraph(title_text2,title_style2)
        
        #title_style.leading = 15
        
        self.TITLE2=Paragraph('''
            <para align=center spaceb=0><b>
            <font size=10><i>%s</i>
            
           </font> </b>
            </para>'''%(title_text2),
            styleSheet["BodyText"])
        
        
        
        
        
    def Format_Name(self,name):
        
        text=name        
        max_letters=40 # If <40 it will overflow the line
        
        if len(text)>40: # for 3 lines
            line=""
          
            split=text.split(' ')
            new_text=""
            for each_word in split:
                
                if len(line)+len(each_word)<=40:
                    
                    if line=="":
                        
                        line=line+each_word
                    else:
                        
                        line=line+" "+each_word
                        
                else:
                    new_text=new_text+"<br/>"
                    line=each_word
            new_text+=line
        else:
            new_text=text
        
                
        return Paragraph('''
            <para align=left spaceb=0><b>
            <font size=7><i>%s</i>
            
           </font> </b>
            </para>'''%(text),
            styleSheet["BodyText"])
            
    def CalculateGrade(self,ce,te,max_score):
        
        
        
        if ce!='' and te!='':
                                
            total=int(ce)+int(te)
            
        else:
            
            return '',''
        
        if self.class_=='8':
            
            if int(total)>=(max_score)*75/100:
                return  total, "A"
            elif int(total)>=(max_score)*60/100:
               return  total, "B"
            elif int(total)>=(max_score)*45/100:
                return  total, "C"
                
            elif int(total)>=(max_score)*33/100:
                return  total, "D"
            else:
                return total,'E'
            
        else:
            if int(total)>=(max_score)*90/100:
                return  total, "A+"
            elif int(total)>=(max_score)*80/100:
               return  total, "A"
            elif int(total)>=(max_score)*70/100:
                return  total, "B+"
                
            elif int(total)>=(max_score)*60/100:
                return  total, "B"
            elif int(total)>=(max_score)*50/100:
                return  total, "C+"
            elif int(total)>=(max_score)*40/100:
                return  total, "C"
            elif int(total)>=(max_score)*30/100:
                return  total, "D+"
            elif int(total)>=(max_score)*20/100:
                return  total, "D"
            else:
                return  total, "E"
        
        
    def SetTable_Style(self):
        
        #Starts Score Table
        self.Each_Pupil_Style=[('BOX',(0,0),(-1,-1),1.7,colors.black),
        
                                ('GRID',(0,0),(-1,-1),1,colors.black),#
                                
                                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                ('FONTSIZE',(0,0),(-1,-1),8),
                                
                                ('SPAN',(0,0),(0,-1)), # Roll
                                ('SPAN',(1,0),(1,-1)), # Ad_no
                                ('SPAN',(2,0),(2,-1)),   # Name
                                
                                ('SPAN',(57,0),(57,-1)),   # Attendance
                                ('SPAN',(58,0),(58,-1)),   # promo
                                ('SPAN',(59,0),(59,-1)),   # Basis
                                ('SPAN',(60,0),(60,-1)) ,  # Remark
                                ('SPAN',(4,0),(4,-1)) ,  # Remark
                                
                                ('BOX',(0,0),(4,3),1.5,colors.black), # Subject Blocks
                                ('BOX',(5,0),(8,3),1.5,colors.black),
                                ('BOX',(9,0),(12,3),1.5,colors.black),
                                ('BOX',(13,0),(16,3),1.5,colors.black),
                                ('BOX',(17,0),(20,3),1.5,colors.black),
                                ('BOX',(21,0),(24,3),1.5,colors.black),
                                ('BOX',(25,0),(28,3),1.5,colors.black),
                                ('BOX',(29,0),(32,3),1.5,colors.black),
                                ('BOX',(33,0),(36,3),1.5,colors.black),
                                ('BOX',(37,0),(40,3),1.5,colors.black),
                                ('BOX',(41,0),(45,3),1.5,colors.black), # IT with practical
                                ('BOX',(46,0),(51,3),1.5,colors.black),
                                ('BOX',(52,0),(56,3),1.5,colors.black),
                                ('BOX',(53,0),(54,3),1.2,colors.black),# % and all
                                ('BOX',(55,0),(56,3),1.2,colors.black),
                                ('BOX',(57,0),(58,3),1.2,colors.black),
                                ('BOX',(59,0),(60,3),1.2,colors.black),
                                ]
                                
    
    
    def Populate_School_Basic_Info(self):
        
        pass
    def Populate_T1(self,div_id,student_id):
        
        SCORES1=[]                
        total_te_t1=0
        
        for subj_index in range(10):
            
            if self.class_=='8' and (subj_index>=5 and subj_index<8):
                
                if subj_index==6 or subj_index==7: #skips if chem/bio
                    continue
                
                BS_SCORES1,te1=self.Manage_BasicScince(1,div_id,student_id)
                
                SCORES1+=BS_SCORES1
                if te1!='':total_te_t1+=te1
                
                continue
                               
            
            
            
            
            max_ce,max_te=self.DB.Get_CE_TE(self.year,self.class_,subj_index)
            
            try:
                max_total=int(max_ce)+int(max_te)
                score_n_roll=self.DB.Score_and_Roll('1',div_id,subj_index,student_id)[1]
            except:
                pass
            
            roll=score_n_roll[5]
            
            
            
            ce1=score_n_roll[6]
            te1=score_n_roll[8]   
             
            if ce1==None:
                ce1=""
            if te1==None:
                te1=''    
                        
            if te1!='':total_te_t1+=te1
            
            total,grade=self.CalculateGrade(ce1,te1,max_total)
            
          
            
            SCORES1+=[ce1,te1,total,grade]
            
            
        # Addin an mty item to IT
        SCORES1.insert(len(SCORES1)-2,'')
        return SCORES1,roll,total_te_t1
            
                    
                    
    def Populate_T2(self,div_id,student_id):
        
        SCORES2=[]                
        total_te_t2=0
        
        for subj_index in range(10):
            
            if self.class_=='8' and (subj_index>=5 and subj_index<8):
                
                if subj_index==6 or subj_index==7: #skips if chem/bio
                    continue
                
                BS_SCORES2,te2=self.Manage_BasicScince(2,div_id,student_id)
                
                SCORES2+=BS_SCORES2
                if te2!='':total_te_t2+=te2
                
                continue
            
            
            
            max_ce,max_te=self.DB.Get_CE_TE(self.year,self.class_,subj_index)
            max_total=int(max_ce)+int(max_te)
            
            score_n_roll=self.DB.Score_and_Roll('2',div_id,subj_index,student_id)[1]   
                             
            ce2=score_n_roll[6]
            te2=score_n_roll[8]      
            if ce2==None:
                ce2=""
            if te2==None:
                te2=''    
                    
            if te2!='':total_te_t2+=te2
                    
            total,grade=self.CalculateGrade(ce2,te2,max_total)
            
            
            SCORES2+=[ce2,te2,total,grade]
            
        # Addin an mty item to IT
        SCORES2.insert(len(SCORES2)-2,'')
        return SCORES2,total_te_t2
            
    def Populate_T3(self,div_id,student_id):
        
        SCORES3=[]     
        SCORES4=[]           
        total_te_t3=0
        grade=''
        promoted=''#hav to check
        base='' #have to check
        for subj_index in range(10):
            
            if self.class_=='8' and (subj_index>=5 and subj_index<8):
                
                if subj_index==6 or subj_index==7: #skips if chem/bio
                    
                    continue
               
                
                BS_SCORES3,SCORES4_nw,te3,promoted,base=self.Manage_BasicScince(3,div_id,student_id)
                
                SCORES3+=BS_SCORES3
                SCORES4+=SCORES4_nw
                
                if te3!='':total_te_t3+=te3
                
                continue
            
            
            max_ce,max_te=self.DB.Get_CE_TE(self.year,self.class_,subj_index)
            max_total=int(max_ce)+int(max_te)
            
            score_n_roll=self.DB.Score_and_Roll('3',div_id,subj_index,student_id)[1]
            
            ce3=score_n_roll[6]
            te3=score_n_roll[8]  
            
            if ce3==None:
                ce3=""
                print "ce=None"
            if te3==None:
                te3=''    
                
            if te3!='': total_te_t3+=te3    
            
            if ce3==0 or te3==0:
                print "ce or te is zero"
                total=0
                grade=''
            elif ce3=='' or te3=='':
                print "ce=''"
                total=''
                grade=''
            else:
                total,grade=self.CalculateGrade(ce3,te3,max_total)
            
            if grade=='' or grade=='E' or (  self.class_!='8' and grade=='D'):# D grade fails only for 9,10 std
                pass3=False
                
                SCORES4_nw,promoted,base=self.Find_Average(div_id,student_id,subj_index)
                SCORES4+=SCORES4_nw
                
            else:
                pass3=True
                SCORES4+=['','','','']
            SCORES3+=[ce3,te3,total,grade]
            
                    
        if promoted=='D':
            self.Failed_List.append(score_n_roll[3])
        
        
        # Addin an mty item to IT
        SCORES3.insert(len(SCORES3)-2,'')    
        SCORES4.insert(len(SCORES4)-2,'')   
         
        
        
        return SCORES3,total_te_t3,SCORES4,promoted,base
        
    def Find_Average(self,div_id,student_id,subj_index):
        print "in avrg"
        
        promoted,base='',''
        SCORES4=['','','','']
        
        max_ce,max_te=self.DB.Get_CE_TE(self.year,self.class_,subj_index)
        max_total=int(max_ce)+int(max_te)
        
        #Get T1    
        score_n_roll=self.DB.Score_and_Roll('1',div_id,subj_index,student_id)[1]   
        
        ce1=score_n_roll[6]
        te1=score_n_roll[8]  
        #Get T2    
        score_n_roll=self.DB.Score_and_Roll('2',div_id,subj_index,student_id)[1]   
        
        ce2=score_n_roll[6]
        te2=score_n_roll[8]      
        
               
        #Get T3    
        score_n_roll=self.DB.Score_and_Roll('3',div_id,subj_index,student_id)[1]   
        
        ce3=score_n_roll[6]
        te3=score_n_roll[8]  
        
        if ce1 =='' or ce1 ==None:
            ce1=0                            
        if te1=='' or te1== None:
            te1=0
       
        if ce2 =='' or ce2 ==None:
            ce2=0                            
        if te2=='' or te2== None:
            te2=0
        if ce3=='' or ce3== None:
            ce3=0
        if te3=='' or te3== None:
            te3=0
        
        
        if (ce2==0 and te2==0 and ce3==0 and te3==0):
            
            
            avrg_ce,avrg_te,total,grade='','','',''
            promoted='D'
        else:                        
            
            denominator=0   # if absent for one exam denominator iis adjusted accordingly
            if (ce1+te1)!=0:denominator+=1
            if (ce2+te2)!=0:denominator+=1
            if (ce3+te3)!=0:denominator+=1
            
            
            avrg_ce=(int(ce1)+int(ce2)+int(ce3))/denominator
            avrg_te=(int(te1)+int(te2)+int(te3))/denominator
            avrg_ce=int(round(avrg_ce,0))
            avrg_te=int(round(avrg_te,0))
            total,grade=self.CalculateGrade(avrg_ce,avrg_te,int(max_total))
        
        
                        
            SCORES4=[avrg_ce,avrg_te,total,grade]
       
                
            if grade=='' or grade=='E' or (  self.class_!='8' and grade=='D'):# D grade fails only for 9,10 std#Faild in Avrg
                
                promoted='D'
                #SCORES4+=[avrg_ce,avrg_te,total,grade]
                
            else: #Passed in avrg
                
                
                base='B2'

        #SCORES4.insert(len(SCORES3)-2,'')
        return SCORES4,promoted,base
    def Attendance(self,div_id,student_id) :
        
        attnd=self.DB.Score_and_Roll('3',div_id,10,student_id)[1][6]
        
    
        if attnd==None or attnd=='':
            return '' # zero %
        
        if self.working_days.isdigit():
            
            max=int(self.working_days)
            perc=attnd*100/max
            perc=str(int(round(perc,0)))
            
            style1=ParagraphStyle(name='normal',fontSize = 8,alignment = TA_RIGHT)        
       
            perc=Paragraph('<font size=7>'+perc+'</font>',style1)
            #perc=RotatedPara(perc,style1)
            return  perc
            
        return 0    
        
    def Populate(self):
        
        self.Failed_List=[]
        div_id=self.DB.Get_Div_Id(self.year,self.class_,self.div)
        if div_id!=-1:
            
            student_ids=self.DB.Get_Student_Id(div_id)
            #print "no of students",len(student_ids)
            count=0
            
            
            for each_student_id in student_ids:
                
                count+=1
                
                ad_no,name=self.DB.Get_Student_Info(each_student_id)
                
                ad_no=self.Format_Adm_No(ad_no)        
                name=self.Format_Name(name)
                
                total_te_t1=0
                total_te_t2=0
                total_te_t3=0
                
                SCORES1,roll,total_te_t1=self.Populate_T1(div_id,each_student_id)
                SCORES2,total_te_t2=self.Populate_T2(div_id,each_student_id)
                SCORES3,total_te_t3,SCORES4,promoted,base=self.Populate_T3(div_id,each_student_id)            
                
                """        
               
                    
                if self.class_=='8' and (subj_index>=5 and subj_index<8): 
                    print "BS"
                    # this function returns 
                    #SCORES1,SCORES2,SCORES3,SCORES4,basis,promoted
                    
                    '''has to manage base and promotion'''
                    SCORES1,SCORES2,SCORES3,SCORES4,base,promoted=self.Manage_BasicScince(div_id,each_student_id)
                #End BS mngmnt
                """
                    # Addin an mty item to IT
                
                
                
                if base!='B2':base='B1'
                if promoted=='':promoted='P'     
                else:base=''               
                
                #if promoted=='D':
                    
                #    self.Failed_List.append(score_n_roll[4])  
                    
                
                attendance=self.Attendance(div_id,each_student_id)    
                row1=[roll,ad_no,name,'Qly','']+SCORES1+[""]*11+[attendance,promoted,base,total_te_t1]
                row2=['','','','Half','']+SCORES2+[""]*14+[total_te_t2]
                row3=['','','','Ann','']+SCORES3+[""]*14+[total_te_t3]
                row4= ['','','','Ave','']+SCORES4+[""]*15                
                self.Each_Pupil=[row1,row2,row3,row4]
                
                
                
                if  self.REMOVE_TOTAL:
                    self.Remove_Total()
                
                self.Split_IT_Practical()
                
                self.AddPage()
                
                
                
                
                
            
        else:
            
            print "No Student in this div"
        
        
        self.passed_no=count-len(self.Failed_List)
        self.total_no=count
        self.failed_no=self.total_no-self.passed_no
        
       
    def Add_Consolidation(self):
        
        
        fill=16-self.table_count
        self.elements.append(Spacer(1, fill*15))
        self.Consolidation_Table=Table(self.CONSOLIDATION,[9*cm]+[4*cm]+[1*cm]*3+[9*cm]*3,[.3*cm]+[.3*cm]*4)
        
        self.Consolidation_Table.setStyle(TableStyle(self.Consolidation_Style))
        self.elements.append(Spacer(1, 10))
        
        self.elements.append(self.Consolidation_Table)
    def Remove_Total(self):
        
            self.Each_Pupil[0][60]=""
            self.Each_Pupil[1][60]=""
            self.Each_Pupil[2][60]=""
       
        # if te_total need not be added it's removed
    def Split_IT_Practical(self):
       
        it_te1=self.Each_Pupil[1][42]
        it_te1=self.Random_Score(it_te1)
        self.Each_Pupil[1][42]=it_te1[0]
        self.Each_Pupil[1][43]=it_te1[1]
        
        
        it_te2=self.Each_Pupil[2][42]
        it_te2=self.Random_Score(it_te2)
        self.Each_Pupil[2][42]=it_te2[0]
        self.Each_Pupil[2][43]=it_te2[1]
        
        
        it_te3=self.Each_Pupil[3][42]
        it_te3=self.Random_Score(it_te3)
        self.Each_Pupil[3][42]=it_te3[0]
        self.Each_Pupil[3][43]=it_te3[1]
        
        
        
       
    def Random_Score(self,te,max=40):
        
        from random import randint
        
        if te=='' or te==None or te==0:
            return "",""
        
        if te==max:
            return 10,30
        
        dif=max-int(te)
        
        ran_theory=randint(0,dif)
        ran_practical=dif-ran_theory
        
        ran_theory=10- ran_theory
        ran_practical=30-ran_practical
        while(True):
            flag1=False
            flag2=False
            
            if ran_theory>10:
                ran=randint(1,ran_theory-10)
                ran_theory=ran_theory-ran
                ran_practical+=ran
                
            else:
                flag1=True
            
                
            if ran_theory<4 and ran_practical>15:
                ran=randint(1,3)
                ran_theory+=ran
                ran_practical=ran_practical-ran
                
            else:
                flag2=True
                
            if flag1==True and flag2==True:
                break
                
                
        return  str(ran_theory),str(ran_practical)
            
        
        
    def Manage_BasicScince(self,term,div_id,student_id):
        
        
        
        
        promoted=''
        base=''
        p_max_ce,p_max_te=self.DB.Get_CE_TE(self.year,self.class_,5)#phy
        c_max_ce,c_max_te=self.DB.Get_CE_TE(self.year,self.class_,6)#Chem
        b_max_ce,b_max_te=self.DB.Get_CE_TE(self.year,self.class_,7)#BioBS
        
        BS_max_ce=p_max_ce+c_max_ce+b_max_ce
        BS_max_te=p_max_te+c_max_te+b_max_te
        
        if term==1:
            
            #Phy
            score_n_roll=self.DB.Score_and_Roll('1',div_id,5,student_id)[1]  
            p_ce1=score_n_roll[6]
            p_te1=score_n_roll[8]           
            
            #Chem
            score_n_roll=self.DB.Score_and_Roll('1',div_id,6,student_id)[1]  
            c_ce1=score_n_roll[6]
            c_te1=score_n_roll[8] 
            
            #Bio
            score_n_roll=self.DB.Score_and_Roll('1',div_id,7,student_id)[1]  
            b_ce1=score_n_roll[6]
            b_te1=score_n_roll[8]   

            if (p_ce1==None or p_ce1==''):p_ce1=0
            if (p_te1==None or p_te1==''):p_te1=0
            if (c_ce1==None or c_ce1==''):c_ce1=0
            if (c_te1==None or c_te1==''):c_te1=0
            if (b_ce1==None or b_ce1==''):b_ce1=0
            if (b_te1==None or b_te1==''):b_te1=0
            
            
            t1_ce_tot=p_ce1+c_ce1+b_ce1
            t1_te_tot=p_te1+c_te1+b_te1
            
            total,grade=self.CalculateGrade(t1_ce_tot,t1_te_tot,BS_max_ce+BS_max_te)
            if total==0:
                t1_ce_tot=t1_te_tot=total=grade=''
            SCORES1=[t1_ce_tot,t1_te_tot,total,grade]+['','','','']*2
            return SCORES1,t1_te_tot
            
        elif term==2 or term==3: # n case of finding avaeg  ,needs t2 score
            
            #phy
            score_n_roll=self.DB.Score_and_Roll('2',div_id,5,student_id)[1] 
            p_ce2=score_n_roll[6]
            p_te2=score_n_roll[8]
            
            #chem
            score_n_roll=self.DB.Score_and_Roll('2',div_id,6,student_id)[1] 
            c_ce2=score_n_roll[6]
            c_te2=score_n_roll[8] 
            
            #bio
            score_n_roll=self.DB.Score_and_Roll('2',div_id,7,student_id)[1] 
            b_ce2=score_n_roll[6]
            b_te2=score_n_roll[8]             
            
              
            if (p_ce2==None or p_ce2==''):p_ce2=0
            if (p_te2==None or p_te2==''):p_te2=0
            if (c_ce2==None or c_ce2==''):c_ce2=0
            if (c_te2==None or c_te2==''):c_te2=0
            if (b_ce2==None or b_ce2==''):b_ce2=0
            if (b_te2==None or b_te2==''):b_te2=0
            
            
            t2_ce_tot=p_ce2+c_ce2+b_ce2
            t2_te_tot=p_te2+c_te2+b_te2
            
            if term==2:
            
                total,grade=self.CalculateGrade(t2_ce_tot,t2_te_tot,BS_max_ce+BS_max_te)
                if total==0:
                    t2_ce_tot=t2_te_tot=total=grade=''

                SCORES2=[t2_ce_tot,t2_te_tot,total,grade]+['','','','']*2
                return SCORES2,t2_te_tot
        
        
        
            
        if term==3:
            
            #phy
            score_n_roll=self.DB.Score_and_Roll('3',div_id,5,student_id)[1] 
            p_ce3=score_n_roll[6]
            p_te3=score_n_roll[8] 
            
            #chem
            score_n_roll=self.DB.Score_and_Roll('3',div_id,6,student_id)[1] 
            c_ce3=score_n_roll[6]
            c_te3=score_n_roll[8] 
            
            #bio
            score_n_roll=self.DB.Score_and_Roll('3',div_id,7,student_id)[1] 
            b_ce3=score_n_roll[6]
            b_te3=score_n_roll[8] 
            
            #print "ce,te",p_ce3,p_te3,c_ce3,c_te3,b_ce3, b_te3
                
            if (p_ce3==None or p_ce3==''):p_ce3=0
            if (p_te3==None or p_te3==''):p_te3=0
            if (c_ce3==None or c_ce3==''):c_ce3=0
            if (c_te3==None or c_te3==''):c_te3=0
            if (b_ce3==None or b_ce3==''):b_ce3=0
            if (b_te3==None or b_te3==''):b_te3=0
            
            
            t3_ce_tot=p_ce3+c_ce3+b_ce3
            t3_te_tot=p_te3+c_te3+b_te3
            
            
            total,grade=self.CalculateGrade(t3_ce_tot,t3_te_tot,BS_max_ce+BS_max_te)
            if total==0:
                t3_ce_tot=t3_te_tot=total=grade=''

            SCORES3=[t3_ce_tot,t3_te_tot,total,grade]+['','','','']*2
            
            if grade !='' and grade!='E' :# passed
                 
                SCORES4=['','','','']*3
                
                pass_t3=True
                            
                
            else:# Failed ;
                
                pass_t3=False
           
                #finding average
                #if (t1_ce_tot==None or t1_ce_tot==''):t1_ce_tot=0
                if (t2_ce_tot==None or t2_ce_tot==''):t2_ce_tot=0
                if (t3_ce_tot==None or t3_ce_tot==''):t3_ce_tot=0
                
                #if (t1_te_tot==None or t1_te_tot==''):t1_te_tot=0
                if (t2_te_tot==None or t2_te_tot==''):t2_te_tot=0
                if (t3_te_tot==None or t3_te_tot==''):t3_te_tot=0
                
                
                if t2_ce_tot!=0 and t2_te_tot!=0:
                    
                    denom=1
                    if t3_ce_tot!=0 and t3_te_tot!=0:
                        denom+=1
                    
                    #try:    
                    avrg_ce=(t2_ce_tot+t3_ce_tot)/denom
                    avrg_te=(t2_te_tot+t3_te_tot)/denom
                    avrg_total,avrg_grade=self.CalculateGrade(avrg_ce,avrg_te,BS_max_ce+BS_max_te)
                    if avrg_total==0:
                        avrg_ce=avrg_te=avrg_total=avrg_grade=''
                    SCORES4=[avrg_ce,avrg_te,avrg_total,avrg_grade]+['','','','']*2
                    
                    if avrg_grade=='' or avrg_grade=='E' or avrg_grade=='D':# Failed evn in avrg
                        
                        promoted='D'
                    else: #promoted in averg
                        base='B2'
                    #except:
                    #    print "ce_tot",t2_ce_tot,"t3_tot",t3_ce_tot
                    #    print "ce,te",p_ce3,p_te3,c_ce3,c_te3,b_ce3, b_te3
                else:
                    promoted='D'
                    SCORES4=['','','','']*3
           
            # Return of Term 3 Only
            
            return SCORES3,SCORES4,t3_te_tot,promoted,base#,t1_te_tot,t2_te_tot,t3_te_tot
           
        
            
                
    def AddPage(self):

        #self.Score_Table=Table(self.Score_Data,[self.cW1*cm]+8*[self.cW*cm], [self.rH1*cm]+[self.rH2*cm]+14*[self.rH*cm])          
        #self.Attendance_Table=Table(self.Attendance_Data,[self.cW*2.2*cm]+4*[self.cW*2*cm],5*[self.rH*cm])
        
        #self.Score_Table.setStyle(TableStyle(self.Score_T_Style))
        #self.Attendance_Table.setStyle(TableStyle(self.Attendance_T_Style))
        
        """self.Format_Title()
        self.Set_Consolidation()
        self.Set_Consolidation_Style()
        """
        
        
        self.Each_Pupil_Table=Table(self.Each_Pupil,[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*41+[ self.cW4*cm]*11+[self.cW5*cm]+[self.cW3*cm]*3,[self.rH1*cm]*4)
        self.Each_Pupil_Table.setStyle(TableStyle(self.Each_Pupil_Style))
        
        
        
        
        self.table_count+=1
        
        
        
        if self.page_count==0: # the fist page
            
            
            self.elements.append(self.TITLE1)
            self.elements.append(Spacer(1, 20))
            self.elements.append(self.TITLE2)              
            self.elements.append(Spacer(1, 15))
            self.elements.append(self.Heading_Table)
        
        """if self.table_count==1:# Beginning of the page
            
            self.Heading_Table=Table(self.HEADING,[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*56,[self.rH2*cm]+[self.rH3*cm]+[self.rH4*cm])
            self.Heading_Table.setStyle(TableStyle(self.Heading_Style))            
            self.elements.append(self.Heading_Table)
        """    
        if self.page_count==0 and self.table_count==16:
            
            self.elements.append(PageBreak())
            #self.Heading_Table=Table(self.HEADING,[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*56,[self.rH2*cm]+[self.rH3*cm]+[self.rH4*cm])
            #self.Heading_Table.setStyle(TableStyle(self.Heading_Style))            
            self.elements.append(self.Heading_Table)
            self.elements.append(self.Each_Pupil_Table)
            self.table_count=0
            
        elif self.table_count==17:
            self.elements.append(PageBreak())
            #self.Heading_Table=Table(self.HEADING,[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*56,[self.rH2*cm]+[self.rH3*cm]+[self.rH4*cm])
            #self.Heading_Table.setStyle(TableStyle(self.Heading_Style))            
            self.elements.append(self.Heading_Table)
            self.elements.append(self.Each_Pupil_Table)
            self.table_count=0
        else:
                
            self.elements.append(self.Each_Pupil_Table)
                 
            
        self.page_count+=1
        
        
        
    def Save(self,open=True):
        
        

        
                
                        
        
        self.doc.build(self.elements,onFirstPage=self.footer, onLaterPages=self.footer)
        
        if open:
            import subprocess
            
           
            subprocess.call(["xdg-open",self.path])
            
            
    def encrpytmypdf(self):
        #use DOB
        return pdfencrypt.StandardEncryption(self.passwd,canPrint=0)            
                
                
    def Failed_Report(self):
        
        if len(self.Failed_List)==0:
            msg="All Students Passed"
        else:
            msg="The following Student(s) detained\n"
            no=0
            for pupil in self.Failed_List:
                no+=1
                msg+=str(no)+".  "+str(pupil)+"\n"
        
        #app = wx.PySimpleApp(0)
       
        dlg = wx.MessageDialog(None, msg,str(self.class_)+self.div,wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
            
    def run(self,open=True):
        
        self.Set_Heading()
        self.Set_Heading_Style()
        
        self.SetTable_Style()
        self.Format_Title()
        
       #[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*56 
                                                                    #[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*51+[ self.cW4*cm]*11+[self.cW5*cm]+[self.cW3*cm]*3
        self.Heading_Table=Table(self.HEADING,[self.cW1*cm]*2+[self.cW2*cm]+[1*cm]*2+[self.cW3*cm]*41+[ self.cW4*cm]*11+[self.cW5*cm]+[self.cW3*cm]*3,[self.rH2*cm]+[self.rH3*cm]+[self.rH4*cm])
        self.Heading_Table.setStyle(TableStyle(self.Heading_Style))  
        self.Populate()
        #self.AddPage()
        self.Set_Consolidation()
        self.Set_Consolidation_Style()
        self.Add_Consolidation()
        self.Failed_Report()
        self.Save(open)
        
    def footer(self,canvas, doc):
        Title = ""
        
        self.footer_text= "Generated using smart school software. For free download visit https://github.com/asifkodur/smartschool/releases/latest"
        
        
        PAGE_WIDTH,PAGE_HEIGHT=self.mypagesize

        canvas.saveState()
        canvas.setFont('Times-Bold',16)
        canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
        canvas.setFont('Times-Roman',7)
        canvas.drawString(inch, 0.25 * inch, self.footer_text)
        canvas.restoreState()
       
class promo_window(wx.Dialog):
    def __init__(self, *args, **kwds):
        # Constructor
        
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        
        
        self.label_1 = wx.StaticText(self, -1, "Year", style=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE)
        self.combo_box_1 = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)

        
        self.label_2 = wx.StaticText(self, -1, "Standard", style=wx.ALIGN_RIGHT|wx.ALIGN_CENTRE)
        
        self.combo_box_2 = wx.ComboBox(self, -1, choices=[ 'All',"8", "9"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        #self.label_3 = wx.StaticText(self, -1, "Division", style=wx.ALIGN_CENTRE)
        #self.combo_box_3 = wx.ComboBox(self, -1, choices=['All'], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        #self.label_4 = wx.StaticText(self, -1, "Term", style=wx.ALIGN_CENTRE)
        #self.button_3 = wx.Button(self, -1, "Import File")
        
        #self.combo_box_4 = wx.ComboBox(self, -1, choices=[ "Term 1", "Term 2", "Annual"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        
       
        self.button_2 = wx.Button(self, -1, "Proceed")
        self.button_1 = wx.Button(self, -1, "Close")
        
       
        #self.SetMenu()

        self.__set_properties()
        self.__do_layout()
        
        self.Bind(wx.EVT_COMBOBOX, self.on_year, self.combo_box_1)
        self.Bind(wx.EVT_COMBOBOX, self.on_class, self.combo_box_2)
        #self.Bind(wx.EVT_COMBOBOX, self.on_division, self.combo_box_3)

        self.Bind(wx.EVT_BUTTON, self.ok_clicked, self.button_2)
        self.Bind(wx.EVT_BUTTON,self.on_close, self.button_1)
        
        #self.CalcSheet=SpreadSheet(self)
        self.YEAR=''
        self.DIVS=[]
        self.DB=db_operations()
        self.load_year()
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Promotion List")
        self.SetSize((450, 350))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_1.SetSelection(0)
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_2.SetSelection(0)
              
        self.button_1.SetMinSize((90, 35))
        self.button_2.SetMinSize((90, 35))
        self.button_2.Enable(False)
        #self.label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        #self.combo_box_4.SetSelection(0)
        
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        
        grid_sizer_1.Add(self.label_1, 0, wx.LEFT|wx.TOP, 20)
        grid_sizer_1.Add(self.combo_box_1, 0, wx.TOP, 20)
        
        grid_sizer_1.Add(self.label_2, 0, wx.LEFT|wx.TOP, 20)
        grid_sizer_1.Add(self.combo_box_2, 0, wx.TOP, 20)
        
        #grid_sizer_1.Add(self.button_3, 0, wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND, 20)
        #grid_sizer_1.Add(self.combo_box_4, 0, wx.RIGHT|wx.TOP|wx.BOTTOM, 20)
        grid_sizer_1.Add(self.button_1, 0, wx.TOP|wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.LEFT, 30)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
    def load_year(self):
                    
        self.combo_box_1.Clear() #year combo
        
       
        
        years=self.DB.get_academic_year_list()
        years.insert(0,"Select Year")

        
        
        for item in years:
            self.combo_box_1.Append(str(item))
            
            
        self.combo_box_1.SetSelection(0) 
        self.combo_box_2.SetSelection(0) 
        

    def on_close(self,event):
        self.Close(True)
        event.Skip()
        
   
        
    def ok_clicked(self,event):
        self.DIVS=[]
        if self.combo_box_2.Value=='All':
            class_=['8','9']
        else:
            class_=[self.combo_box_2.Value]
        for cls in class_:
            
            for div in self.DB.Get_Div(self.YEAR,cls):
                self.DIVS.append([self.YEAR,cls,div])
        
        self.Close()
        
    def on_year(self, event):  # wxGlade: add_div.<event_handler>
        self.combo_box_2.SetSelection(0)
       
        self.YEAR=self.combo_box_1.Value.split('-')[0]
        self.combo_box_2.SetSelection(0)
        
       
        if self.combo_box_1.Value=='Select':
            self.button_2.Enable(False)
        else:
             self.button_2.Enable(True)
        event.Skip()

    def on_class(self, event):  # wxGlade: add_div.<event_handler>
        self.CLASS=self.combo_box_2.Value
        
        
    def get_div(self):
        return self.DIVS   
        
   
    
if __name__ == "__main__":
    
    app = wx.PySimpleApp(0)
    '''wx.InitAllImageHandlers()
    frame_1 =promo_window(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.ShowModal()
    frame_1.Destroy()

    app.MainLoop()
    '''
    P=Promotion_List("2016","school","8","C","deo",50) 
    P.run()