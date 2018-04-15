#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Sun Sep  7 21:22:56 2014

import wx

from dboperations import db_operations
import THEME
# begin wxGlade: extracode
# end wxGlade









#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sat Sep 30 11:13:16 2017
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class add_academic_year(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: add_academic_year.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, ("Academic Year"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_4 = wx.StaticText(self, wx.ID_ANY, ("-"))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_close = wx.Button(self, wx.ID_ANY, ("Close"))
        self.button_add = wx.Button(self, wx.ID_ANY, ("Add"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.on_enter, self.text_ctrl_1)
        
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_close)
        self.Bind(wx.EVT_BUTTON, self.on_add, self.button_add)
       
        self.text_ctrl_1.Bind(wx.EVT_KEY_DOWN, self.handle_keypress)
        
        self.NEW_YEAR=''
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: add_academic_year.__set_properties
        self.button_add.Disable()
        self.SetTitle(("Add Academic Year"))
        self.SetSize((498, 200))
        self.text_ctrl_1.SetMinSize((88, 30))
        self.text_ctrl_2.SetMinSize((88, 30))
        self.text_ctrl_2.Enable(False)
        self.button_close.SetMinSize((90, 33))
        self.button_add.SetMinSize((90, 33))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: add_academic_year.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 1, 10, 10)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_close, 0, wx.RIGHT, 20)
        sizer_5.Add(self.button_add, 0, wx.LEFT, 20)
        sizer_4.Add(sizer_5, 1, wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(sizer_4, 1, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 30)
        sizer_2.Add(grid_sizer_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
    def handle_keypress(self, event):
        
        keycode = event.GetKeyCode()
        
        if (keycode>313 and keycode <318) or keycode==8 or keycode==127:
            
            event.Skip()            
        if keycode < 255:
            
            if len(self.text_ctrl_1.GetValue())<4 and chr(keycode).isdigit():
               
                event.Skip()

    def on_enter(self, event):  # wxGlade: add_academic_year.<event_handler>
        min_year=2016
        max_year=2025
        
        TEXT_VALUE=self.text_ctrl_1.GetValue()
        if TEXT_VALUE and len(TEXT_VALUE)==4 :
        
            if int(TEXT_VALUE)<min_year or int(TEXT_VALUE)>max_year:
                msg="Academic year should not be between  "+str(min_year) +" and "+str(max_year)
                dlg = wx.MessageDialog(self, msg, '',wx.OK | wx.ICON_ERROR)                  
                dlg.ShowModal()
                dlg.Destroy()
                self.text_ctrl_1.SetValue('')
                self.button_add.Disable()
                event.Skip()
            
            else:
                self.button_add.Enable()
        else:
            self.button_add.Disable()
        
        if len(TEXT_VALUE)==4:
            self.text_ctrl_2.SetValue(str(int(TEXT_VALUE)+1))
        else:
            self.text_ctrl_2.SetValue('')
            
        event.Skip()

  

        

    def on_close(self, event):  # wxGlade: add_academic_year.<event_handler>
        self.Close()
        event.Skip()

    def on_add(self, event):  # wxGlade: add_academic_year.<event_handler>
        self.NEW_YEAR=self.text_ctrl_1.GetValue()
            
        event.Skip()
        self.Close()
        














class add_div(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: add_div.__init__
        
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_1 = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.label_1 = wx.StaticText(self.panel_1, -1, "YEAR")
        
        
        self.combo_box_1 = wx.ComboBox(self.panel_1, -1, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT)
        self.label_2 = wx.StaticText(self.panel_1, -1, "CLASS")
        self.combo_box_2 = wx.ComboBox(self.panel_1, -1, choices=["Select","8","9","10"], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT)
        self.sizer_4_staticbox = wx.StaticBox(self.panel_1, -1, "Specify Class ")
        self.list_box_1 = wx.ListBox(self.panel_1, -1, choices=[], style=wx.LB_SINGLE | wx.LB_SORT)
        self.button_1 = wx.Button(self.panel_1, -1, "Remove Divison")
        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, -1, "")
        self.button_2 = wx.Button(self.panel_1, -1, "Add Division")
        self.sizer_9_staticbox = wx.StaticBox(self.panel_1, -1, "New Division")
        self.button_3 = wx.Button(self.panel_1, -1, "Close")
        self.hyperlink_1 = wx.HyperlinkCtrl(self.panel_1, wx.ID_ANY, "", "Add Academic Year")


        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_year, self.combo_box_1)
        self.Bind(wx.EVT_COMBOBOX, self.on_class, self.combo_box_2)
        self.Bind(wx.EVT_LISTBOX, self.on_list, self.list_box_1)
        self.Bind(wx.EVT_BUTTON, self.on_remove, self.button_1)
        self.Bind(wx.EVT_TEXT, self.on_text, self.text_ctrl_1)
        
        self.Bind(wx.EVT_BUTTON, self.on_add, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_3)
        
        self.text_ctrl_1 .Bind(wx.EVT_SET_FOCUS,self.onfocus)
        self.text_ctrl_1 .Bind(wx.EVT_KILL_FOCUS,self.offocus)
        self.text_ctrl_1.Bind(wx.EVT_KEY_DOWN, self.on_keypress)
        
        self.Bind(wx.EVT_HYPERLINK, self.on_hlink, self.hyperlink_1)
        
        self.YEAR=''
        self.CLASS=''
        
        self.DB=db_operations()
        self.load_year()
        
        # end wxGlade
    
    def __set_properties(self):
        # begin wxGlade: add_div.__set_properties
        self.SetTitle("Year & Division")
        self.SetSize((600, 500))
        #self.Enable(False)
        self.SetFocus()
        self.label_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_1.SetSelection(0)
        self.label_2.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_2.SetSelection(0)
        self.list_box_1.SetMinSize((150, 257))
        self.list_box_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.list_box_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.button_1.SetMinSize((120, 40))
        self.text_ctrl_1.SetMinSize((90, 33))
        self.text_ctrl_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_1.Value='Eg: A-K'
        self.text_ctrl_1.SetForegroundColour('#9CA998')
        self.button_2.SetMinSize((120, 40))
        self.button_1.Enable(False)
        self.button_2.Enable(False)
        self.button_3.SetMinSize((85, 35))
        self.panel_1.SetScrollRate(10, 10)
        
        
        # end wxGlade
        
    def set_theme(self):
        
        self.SetForegroundColour(THEME.WINDOW_FG_COLOR)
        self.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.panel_1.SetForegroundColour(THEME.WINDOW_FG_COLOR)
        self.panel_1.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        
        self.button_1.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_1.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        self.button_2.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_2.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        self.button_3.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_3.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        
        self.label_1.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_2.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        
        
        
        

    def __do_layout(self):
        # begin wxGlade: add_div.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_9_staticbox.Lower()
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_4_staticbox.Lower()
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.VERTICAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.label_1, 0, 0, 0)
        sizer_5.Add(self.combo_box_1, 0, 0, 0)
        sizer_4_copy.Add(sizer_5, 0, 0, 0)
        sizer_6.Add(self.label_2, 0, wx.LEFT, 85)
        sizer_6.Add(self.combo_box_2, 0, wx.LEFT, 85)
        sizer_4_copy.Add(sizer_6, 0, wx.EXPAND, 20)
        sizer_4.Add(sizer_4_copy, 0, wx.SHAPED, 0)
        sizer_3.Add(sizer_4, 0, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.BOTTOM, 20)
        sizer_7.Add(self.list_box_1, 0, 0, 0)
        sizer_8.Add(self.button_1, 0, wx.TOP, 20)
        sizer_9.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_9.Add(self.button_2, 0, wx.TOP, 10)
        sizer_8.Add(sizer_9, 1, wx.TOP | wx.EXPAND, 50)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_10.Add(self.button_3, 0, wx.LEFT, 200)
        sizer_2.Add(sizer_10, 0, wx.TOP | wx.EXPAND, 40)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.ALL | wx.EXPAND, 12)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def on_year(self, event):  # wxGlade: add_div.<event_handler>
        self.combo_box_2.SetSelection(0)
        if self.combo_box_1.Value!='Select':
            self.YEAR=self.combo_box_1.Value.split('-')[0]
        self.list_box_1.Clear()
        if self.text_ctrl_1.Value!='' and self.text_ctrl_1.Value!='Eg: A-K' and self.combo_box_1.Value!='Select' and  self.combo_box_2.Value!='Select' :
            self.button_2.Enabled=True
        else:
             self.button_2.Enabled=False
        event.Skip()
    def on_hlink(self, event):  # wxGlade: student_profie.<event_handler>
        
        new_acd_win=add_academic_year(self)
        new_acd_win.ShowModal()
        new_year=new_acd_win.NEW_YEAR
        if not new_year:
            new_acd_win.Destroy()

            return 0
        new_acd_win.Destroy()
        years=self.DB.Get_Years()
        if years.count(int(new_year)):
            msg= "Acdemic year "+str(new_year)+"-"+str(int(new_year)+1)+"already exists"
            dlg = wx.MessageDialog(self,msg, 'Error Adding',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return
        
        years.sort()
        
        msg="Do you want to add new academic year "+new_year+"-"+str(int(new_year)+1)
        
        dlg = wx.MessageDialog(self, msg,"Add Year?", wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()# == wx.ID_YES
        if result==wx.ID_NO:
            dlg.Destroy()
            

            return 0
        
        dlg.Destroy()
        self.DB.Add_Div(new_year,'8','A')
        self.DB.Add_Div(new_year,'9','A')
        self.DB.Add_Div(new_year,'10','A')
        
        self.load_year()
        

        
        event.Skip()
    def on_class(self, event):  # wxGlade: add_div.<event_handler>
        self.list_box_1.Clear()
        if self.combo_box_2.Value!='Select':
            
            self.CLASS=self.combo_box_2.Value
            self.load_div()
            
        
        
        if self.text_ctrl_1.Value!='' and self.text_ctrl_1.Value!='Eg: A-K' and self.combo_box_1.Value!='Select' and  self.combo_box_2.Value!='Select' :
            self.button_2.Enabled=True
        else:
             self.button_2.Enabled=False
        event.Skip()

    def on_list(self, event):  # wxGlade: poll.<event_handler>
        self.button_1.Enabled=True
        event.Skip()

    def on_remove(self, event):  # wxGlade: poll.<event_handler>
        sel=self.list_box_1.GetSelection()
        item=self.list_box_1.GetString(sel)
        if self.validate_removal(item):
            query='DELETE FROM DIV WHERE YEAR=? AND CLASS=? AND DIV=?'
            self.DB.cur.execute(query,(self.YEAR,self.CLASS,item))
            self.DB.con.commit()
            self.list_box_1.Delete(sel)
            self.button_1.Enable(False)
        else:
            dlg = wx.MessageDialog(self, 'Cannot delete!\nThere are students in this division. Delete student(s)before deleting division', 'Error Removing',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
        event.Skip()

    def on_text(self, event):  # wxGlade: add_div.<event_handler>
        if self.text_ctrl_1.Value!='' and self.text_ctrl_1.Value!='Eg: A-K' and self.combo_box_1.Value!='Select' and  self.combo_box_2.Value!='Select' :
            self.button_2.Enabled=True
        else:
             self.button_2.Enabled=False
        event.Skip()

    def on_add(self, event):  # wxGlade: add_div.<event_handler>
        for div in self.validate_div():
        
            query='INSERT INTO DIV(YEAR,CLASS,DIV) VALUES(?,?,?)'
            self.DB.cur.execute(query,(self.YEAR,self.CLASS,div))
            self.DB.con.commit()
            self.load_div()
            
        self.text_ctrl_1.Value=''
        
        event.Skip()

    def on_close(self, event):  # wxGlade: add_div.<event_handler>
        self.Close()
        event.Skip()
    def load_year(self):
                
        self.combo_box_1.Clear()
        self.list_box_1.Clear()
        
        years=self.DB.get_academic_year_list()
        years.insert(0,"Select")

        
        
        for item in years:
            self.combo_box_1.Append(str(item))
            
        self.combo_box_1.SetSelection(0)    
        


    def load_div(self):
        self.list_box_1.Clear()
        
        
        divs=self.DB.Get_Div(self.YEAR,self.CLASS)
        
        for item in divs:
            self.list_box_1.Append(str(item))
           
    def onfocus(self,event):

        if self.text_ctrl_1.Value=='Eg: A-K':
            self.text_ctrl_1.Value=""
            self.text_ctrl_1.SetForegroundColour('#0A0A0A')



    def offocus(self,event):

        if self.text_ctrl_1.Value=="":

            self.text_ctrl_1.Value='Eg: A-K'
            self.text_ctrl_1.SetForegroundColour('#9CA998')
            
    def validate_removal(self,item):
        #Checks if any student is bound to the particular divsion
        div_id=self.DB.Get_Div_Id(self.YEAR,self.CLASS,item)
        query='SELECT COUNT(ID) FROM T1 WHERE DIV_ID=?'
        self.DB.cur.execute(query,(div_id,))
        res=self.DB.cur.fetchone()
        if res[0]==0:
            return 1
        return 0
    def validate_div(self):
        divs=[]
        val=self.text_ctrl_1.Value
        
        
            
        if val.find('-')!=-1: 
            if len(val)==3 and val.find('-')!=0 and val.find('-')!=2:
                
                start=val.split('-')[0]
                end=val.split('-')[1]
                if ord(start)<ord(end):
                    for i in range(ord(start),ord(end)+1,1):
                        if not self.DB.Div_Exists(self.YEAR,self.CLASS,chr(i)):
                            divs.append(chr(i))
                        else:
                            txt= "Division '"+chr(i)+"' already exists"
                            dlg = wx.MessageDialog(self,txt, 'Error Adding',wx.OK | wx.ICON_ERROR)
                            dlg.ShowModal()
                            dlg.Destroy()
                else:
                    dlg = wx.MessageDialog(self, 'Division in Wrong Format', 'Error Adding',wx.OK | wx.ICON_ERROR)
                    dlg.ShowModal()
                    dlg.Destroy()
                    
            else:
                dlg = wx.MessageDialog(self, 'Division in Wrong Format', 'Error Adding',wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                    
        else:
            if not self.DB.Div_Exists(self.YEAR,self.CLASS,val):
                divs=[val]
            else:
                txt= "Division '"+val+"' already exists"
                dlg = wx.MessageDialog(self,txt, 'Error Adding',wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
        return divs    
        
    def on_keypress(self,event):
        
        keycode = event.GetKeyCode()
        
        if keycode>64 and keycode<91 and len(self.text_ctrl_1.Value)<3:
            self.text_ctrl_1.write (chr(keycode))
            

        elif keycode==8 or keycode==45 or keycode==44 or keycode==306 or keycode==312 or keycode==314 or keycode==316 or keycode==127 or keycode==310:
            event.Skip()
'''
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = add_div(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
'''