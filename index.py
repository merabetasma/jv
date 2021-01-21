#import library
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import sqlite3
import datetime
from xlrd import *
from xlsxwriter import *

ui,_ = loadUiType('jv.ui')


class MainApp(QMainWindow,ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db_connect()
        self.ui_change()
        self.handel_button()
        self.category_name()
        self.login_tab()
        self.category_user()
        self.category_code()
    #change of ui
    def  ui_change(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_4.resizeColumnsToContents()
    #connect sqlite3 with python code
    def db_connect(self):
        self.con = sqlite3.connect('jvb.db')
        self.cur = self.con.cursor()
        print('db connected')

    def handel_button(self):
        self.pushButton.clicked.connect(self.volunt_tab)
        self.pushButton_2.clicked.connect(self.family_tab)
        self.pushButton_3.clicked.connect(self.child_tab)
        self.pushButton_4.clicked.connect(self.donation_tab)
        self.pushButton_14.clicked.connect(self.dashbaord_tab)
        self.pushButton_5.clicked.connect(self.setting_tab)
        self.pushButton_7.clicked.connect(self.add_volunteers)
        self.pushButton_18.clicked.connect(self.search_volunteers)
        self.pushButton_8.clicked.connect(self.save_volunteers)
        self.pushButton_9.clicked.connect(self.delete_volunteers)
        self.pushButton_6.clicked.connect(self.show_volunteers)
        self.pushButton_11.clicked.connect(self.add_family)
        self.pushButton_19.clicked.connect(self.search_family)
        self.pushButton_12.clicked.connect(self.save_family)
        self.pushButton_13.clicked.connect(self.delete_family)
        self.pushButton_10.clicked.connect(self.show_family)
        self.pushButton_16.clicked.connect(self.export_volunteer)
        self.pushButton_20.clicked.connect(self.export_family)
        self.pushButton_25.clicked.connect(self.add_child)
        self.pushButton_26.clicked.connect(self.search_child)
        self.pushButton_28.clicked.connect(self.save_child)
        self.pushButton_27.clicked.connect(self.delete_child)
        self.pushButton_23.clicked.connect(self.show_child)
        self.pushButton_29.clicked.connect(self.export_donation)
        self.pushButton_24.clicked.connect(self.export_child)
        self.pushButton_34.clicked.connect(self.user)
        self.pushButton_37.clicked.connect(self.permission)
        self.pushButton_32.clicked.connect(self.handel_login)
        self.pushButton_15.clicked.connect(self.add_donation_import)
        self.pushButton_35.clicked.connect(self.add_donation_export)
        self.pushButton_30.clicked.connect(self.show_donation)
    #code for the part of login to the system
    def handel_login(self):
        user_name = self.lineEdit_34.text()
        user_password = self.lineEdit_33.text()

        self.cur.execute('''SELECT id,name,password FROM user
                       ''')
        data = self.cur.fetchall()

        #if user_name== None and user_password== None:
            #QMessageBox.warning(self, "Data Error", " Please  Provide a valid  username or password")

        for row in data:
            print(row)
            if row[1] == user_name and row[2] == user_password:
                self.groupBox.setEnabled(True)
                self.cur.execute(''' SELECT * FROM permession WHERE name=?
                                                            ''', (user_name,))
                user = self.cur.fetchone()
                print(user)

                if user[2] == 1:
                    self.pushButton.setEnabled(True)
                if user[3] == 1:
                    self.pushButton_2.setEnabled(True)
                if user[4] == 1:
                    self.pushButton_3.setEnabled(True)
                if user[5] == 1:
                    self.pushButton_4.setEnabled(True)
                if user[6] == 1:
                    self.pushButton_14.setEnabled(True)

                if user[7] == 1:
                    self.pushButton_5.setEnabled(True)
                if user[8] == 1:
                    self.pushButton_7.setEnabled(True)
                if user[9] == 1:
                    self.pushButton_8.setEnabled(True)
                if user[10] == 1:
                    self.pushButton_9.setEnabled(True)
                if user[11] == 1:
                    self.pushButton_16.setEnabled(True)
                if user[12] == 1:
                    self.pushButton_17.setEnabled(True)
                if user[13] == 1:
                    self.pushButton_6.setEnabled(True)
                if user[14] == 1:
                    self.pushButton_11.setEnabled(True)
                if user[15] == 1:
                    self.pushButton_12.setEnabled(True)
                if user[16] == 1:
                    self.pushButton_13.setEnabled(True)
                if user[17] == 1:
                    self.pushButton_20.setEnabled(True)
                if user[18] == 1:
                    self.pushButton_21.setEnabled(True)
                if user[19] == 1:
                    self.pushButton_10.setEnabled(True)
                if user[20] == 1:
                    self.pushButton_25.setEnabled(True)
                if user[21] == 1:
                    self.pushButton_28.setEnabled(True)
                if user[22] == 1:
                    self.pushButton_27.setEnabled(True)
                if user[23] == 1:
                    self.pushButton_24.setEnabled(True)
                if user[29] == 1:
                    self.pushButton_22.setEnabled(True)
                if user[24] == 1:
                    self.pushButton_23.setEnabled(True)
                if user[25] == 1:
                    self.pushButton_15.setEnabled(True)
                if user[26] == 1:
                    self.pushButton_29.setEnabled(True)
                if user[27] == 1:
                    self.pushButton_31.setEnabled(True)
                if user[28] == 1:
                    self.pushButton_30.setEnabled(True)

            if row[1] != user_name or row[2] != user_password:
                sql = (''' SELECT name,password FROM user WHERE name=? and password=?
                                           ''')
                self.cur.execute(sql, [(user_name),(user_password)])
                data = self.cur.fetchone()
                print(data)

                if data == None:

                  QMessageBox.warning(self, "Data Error",  " Please  Provide a valid  username or password")

      #volunteers or members part############################################
    def show_volunteers(self):
        data_search=self.lineEdit.text()
        self.tableWidget.insertRow(0)
        if self.comboBox.currentIndex() == 0:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            self.cur.execute(''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers ''')
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position+=1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

        if self.comboBox.currentIndex() == 1:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql =(''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers WHERE name=? 
                                                 ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))


        if self.comboBox.currentIndex() == 2:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql = (''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers  WHERE addrese=? 
                                                 ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

        if self.comboBox.currentIndex() == 3:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql = (''' SELECT * FROM volunteers  WHERE job=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

        if self.comboBox.currentIndex() == 4:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql = (''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers  WHERE etude=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

        if self.comboBox.currentIndex() == 5:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql = (''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers  WHERE phone=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

        if self.comboBox.currentIndex() == 6:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            sql = (''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers  WHERE national_id=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position=0
            for row, form in enumerate(data):
              for col, item in enumerate(form):
               self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
               col += 1
              row_position += 1
              self.tableWidget.insertRow(row_position)

            self.tableWidget.removeRow((len(data)))

    def add_volunteers(self):
        name=self.lineEdit_2.text()
        date_broth=self.lineEdit_3.text()
        addrese=self.lineEdit_4.text()
        phone=self.lineEdit_5.text()
        level=self.lineEdit_6.text()
        job=self.lineEdit_7.text()
        national_id=self.lineEdit_8.text()
        date= datetime.datetime.now()
        self.cur.execute('''INSERT INTO volunteers(name,date_brith,addrese,phone,etude,job,national_id,date)
        VALUES(?,?,?,?,?,?,?,?)''',(name,date_broth,addrese,phone,level,job,national_id,date))

        self.con.commit()
        print('done')
        self.lineEdit_2.setText(' ')
        self.lineEdit_3.setText(' ')
        self.lineEdit_4.setText(' ')
        self.lineEdit_5.setText(' ')
        self.lineEdit_6.setText(' ')
        self.lineEdit_7.setText(' ')
        self.lineEdit_8.setText(' ')
    def save_volunteers(self):
        name = self.lineEdit_20.text()
        addrese = self.lineEdit_11.text()
        phone = self.lineEdit_12.text()
        job = self.lineEdit_9.text()
        national_id = self.lineEdit_10.text()
        date = datetime.datetime.now()
        self.cur.execute(''' UPDATE volunteers SET name=?,addrese=?,phone=?,job=?, national_id=?
                              ''', (name, addrese, phone,job, national_id))
        self.con.commit()
        print('done')
        self.lineEdit_20.setText(' ')
        self.lineEdit_11.setText(' ')
        self.lineEdit_12.setText(' ')
        self.lineEdit_9.setText(' ')
        self.lineEdit_10.setText(' ')

    def search_volunteers(self):
       data_search=self.lineEdit_26.text()


       if self.comboBox_10.currentIndex()==0:

             sql = (''' SELECT * FROM volunteers WHERE name=?
                                   ''')
             self.cur.execute(sql, [(data_search)])
             data = self.cur.fetchone()
             print(data)

             if data==None:

                 self.lineEdit_20.setText('')
                 self.lineEdit_11.setText('')
                 self.lineEdit_12.setText('')
                 self.lineEdit_9.setText('')
                 self.lineEdit_10.setText('')
                 QMessageBox.warning(self, "Data Error",  " No Result Provide a valid data")

             elif data!= None:
              self.lineEdit_20.setText(str(data[1]))
              self.lineEdit_11.setText(str(data[3]))
              self.lineEdit_12.setText(str(data[4]))
              self.lineEdit_9.setText(str(data[6]))
              self.lineEdit_10.setText(str(data[7]))
       if self.comboBox_10.currentIndex() == 1:
           sql = (''' SELECT * FROM volunteers WHERE etude=?
                                        ''')
           self.cur.execute(sql, [(data_search)])
           data1 = self.cur.fetchone()
           print(data1)
           if data1 == None:

               self.lineEdit_20.setText('')
               self.lineEdit_11.setText('')
               self.lineEdit_12.setText('')
               self.lineEdit_9.setText('')
               self.lineEdit_10.setText('')
               QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

           elif data1 != None:
               self.lineEdit_20.setText(str(data1[1]))
               self.lineEdit_11.setText(str(data1[3]))
               self.lineEdit_12.setText(str(data1[4]))
               self.lineEdit_9.setText(str(data1[6]))
               self.lineEdit_10.setText(str(data1[7]))
       if self.comboBox_10.currentIndex() == 2:
           sql = (''' SELECT * FROM volunteers WHERE addrese=?
                                        ''')
           self.cur.execute(sql, [(data_search)])
           data2 = self.cur.fetchone()

           print(data2)
           if data2 == None:

               self.lineEdit_20.setText('')
               self.lineEdit_11.setText('')
               self.lineEdit_12.setText('')
               self.lineEdit_9.setText('')
               self.lineEdit_10.setText('')
               QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

           elif data2 != None:
               self.lineEdit_20.setText(str(data2[1]))
               self.lineEdit_11.setText(str(data2[3]))
               self.lineEdit_12.setText(str(data2[4]))
               self.lineEdit_9.setText(str(data2[6]))
               self.lineEdit_10.setText(str(data2[7]))
       if self.comboBox_10.currentIndex() == 3:
           sql = (''' SELECT * FROM volunteers WHERE job=?
                                              ''')
           self.cur.execute(sql, [(data_search)])
           data3 = self.cur.fetchone()
           print(data3)
           if data3 == None:

               self.lineEdit_20.setText('')
               self.lineEdit_11.setText('')
               self.lineEdit_12.setText('')
               self.lineEdit_9.setText('')
               self.lineEdit_10.setText('')
               QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

           elif data3 != None:
               self.lineEdit_20.setText(str(data3[1]))
               self.lineEdit_11.setText(str(data3[3]))
               self.lineEdit_12.setText(str(data3[4]))
               self.lineEdit_9.setText(str(data3[6]))
               self.lineEdit_10.setText(str(data3[7]))
       if self.comboBox_10.currentIndex() == 4:
           sql = (''' SELECT * FROM volunteers WHERE national_id=?
                                              ''')
           self.cur.execute(sql, [(data_search)])
           data4 = self.cur.fetchone()
           print(data4)
           if data4 == None:

               self.lineEdit_20.setText('')
               self.lineEdit_11.setText('')
               self.lineEdit_12.setText('')
               self.lineEdit_9.setText('')
               self.lineEdit_10.setText('')
               QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

           elif data4!= None:
               self.lineEdit_20.setText(str(data4[1]))
               self.lineEdit_11.setText(str(data4[3]))
               self.lineEdit_12.setText(str(data4[4]))
               self.lineEdit_9.setText(str(data4[6]))
               self.lineEdit_10.setText(str(data4[7]))


       self.lineEdit_26.setText(' ')


    def delete_volunteers(self):
        data_search = self.lineEdit_26.text()
        date = datetime.datetime.now()
        delete_message = QMessageBox.warning(self, 'delete information', 'are you sure do you want to delete the information?',
                                             QMessageBox.Yes | QMessageBox.No)
        if delete_message == QMessageBox.Yes:
            if self.comboBox_10.currentIndex() == 0:
                sql = (''' DELETE  FROM volunteers WHERE name=?
                             ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_10.currentIndex() == 1:
                sql = (''' DELETE  FROM volunteers WHERE level=?
                                      ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_10.currentIndex() == 2:
                sql = (''' DELETE  FROM volunteers WHERE addrese=?
                                      ''')
                self.cur.execute(sql, [(data_search)])
            if self.comboBox_10.currentIndex() == 3:
                sql = (''' DELETE  FROM volunteers WHERE job=?
                    ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_10.currentIndex() == 4:
                sql = (''' DELETE  FROM volunteers WHERE national_id=?
                                      ''')
                self.cur.execute(sql, [(data_search)])
            self.con.commit()
            self.statusBar().showMessage('the delete is done successful')
            print('done')
        self.lineEdit_20.setText(' ')
        self.lineEdit_11.setText(' ')
        self.lineEdit_12.setText(' ')
        self.lineEdit_9.setText(' ')
        self.lineEdit_10.setText(' ')
    def export_volunteer(self):
        self.cur.execute(''' SELECT name,date_brith,addrese,phone,etude,job,national_id,date FROM volunteers ''')
        data = self.cur.fetchall()
        excel_file=Workbook('volunteers_report.xlsx')
        sheet1=excel_file.add_worksheet()
        sheet1.write(0, 0, 'name')
        sheet1.write(0, 1, 'broth_date')
        sheet1.write(0, 2, 'addrese')
        sheet1.write(0, 3, 'phone')
        sheet1.write(0, 4, 'level')
        sheet1.write(0, 5, 'job')
        sheet1.write(0, 6, 'national_id')
        sheet1.write(0, 7, 'date')

        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        excel_file.close()

    #####################################################familly needed part###################################################
    def show_family(self):
        data_search = self.lineEdit_13.text()
        self.tableWidget.insertRow(0)
        if self.comboBox_2.currentIndex() == 0:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            self.cur.execute(''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family ''')
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)

            self.tableWidget_2.removeRow((len(data)))

        if self.comboBox_2.currentIndex() == 1:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            sql=(''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family  WHERE name=?''')
            self.cur.execute (sql,[(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)

            self.tableWidget_2.removeRow((len(data)))
        if self.comboBox_2.currentIndex() == 2:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            sql = (''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family  WHERE addrese=?''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)

            self.tableWidget_2.removeRow((len(data)))
        if self.comboBox_2.currentIndex() == 3:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            sql = (''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family  WHERE phone=?''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)

            self.tableWidget_2.removeRow((len(data)))

        if self.comboBox_2.currentIndex() == 4:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            sql = (''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family  WHERE num_child=?''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)

            self.tableWidget_2.removeRow((len(data)))

        if self.comboBox_2.currentIndex() == 5:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)

            sql = (''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family  WHERE sitution=?''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_2.insertRow(row_position)
            self.tableWidget_2.removeRow((len(data)))

    def add_family(self):
        family_name=self.lineEdit_14.text()
        addrese=self.lineEdit_16.text()
        phone=self.lineEdit_17.text()
        nb_children=self.lineEdit_15.text()
        sitution=self.comboBox_3.currentIndex()
        describe_famaliy=self.textEdit.toPlainText()
        date = datetime.datetime.now()
        self.cur.execute('''INSERT INTO  family(name,addrese,phone,num_child,sitution,description,date)
        VALUES(?,?,?,?,?,?,?)''',(family_name,addrese,phone,nb_children,sitution,describe_famaliy,date))
        self.con.commit()
        print('add done')
        self.lineEdit_14.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_17.setText('')
        self.lineEdit_15.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.textEdit.setText('')
    def search_family(self):
        date_search=self.lineEdit_27.text()

        if self.comboBox_11.currentIndex()==0:
            sql= ('''SELECT * FROM family WHERE name=?
                                    ''')
            self.cur.execute(sql,[(date_search)])
            data=self.cur.fetchone()
            print(data)
            if data == None:

                self.lineEdit_21.setText('')
                self.lineEdit_18.setText('')
                self.lineEdit_19.setText('')
                self.lineEdit_23.setText('')
                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data != None:
                self.lineEdit_21.setText(str(data[2]))
                self.lineEdit_18.setText(str(data[3]))
                self.lineEdit_19.setText(str(data[4]))
                self.lineEdit_23.setText(str(data[1]))
        if self.comboBox_11.currentIndex() == 1:

            sql= ('''SELECT * FROM family WHERE addrese=?
                                           ''')
            self.cur.execute(sql, [(date_search)])
            data1 = self.cur.fetchone()
            print(data1)
            if data1 == None:

                self.lineEdit_21.setText('')
                self.lineEdit_18.setText('')
                self.lineEdit_19.setText('')
                self.lineEdit_23.setText('')
                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data1 != None:
                self.lineEdit_21.setText(str(data1[2]))
                self.lineEdit_18.setText(str(data1[3]))
                self.lineEdit_19.setText(str(data1[4]))
                self.lineEdit_23.setText(str(data1[1]))


        if  self.comboBox_11.currentIndex() == 2:

            sql= ('''SELECT * FROM family WHERE phone=?
                                                  ''')
            self.cur.execute(sql, [(date_search)])
            data2 = self.cur.fetchone()
            print(data2)
            if data2 == None:

                self.lineEdit_21.setText('')
                self.lineEdit_18.setText('')
                self.lineEdit_19.setText('')
                self.lineEdit_23.setText('')
                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data2 != None:
                self.lineEdit_21.setText(str(data2[2]))
                self.lineEdit_18.setText(str(data2[3]))
                self.lineEdit_19.setText(str(data2[4]))
                self.lineEdit_23.setText(str(data2[1]))

        if self.comboBox_11.currentIndex() == 3:
            sql = ('''SELECT * FROM family WHERE num_child=?
                                                  ''')
            self.cur.execute(sql, [(date_search)])
            data3 = self.cur.fetchone()
            print(data3)
            if data3 == None:

                self.lineEdit_21.setText('')
                self.lineEdit_18.setText('')
                self.lineEdit_19.setText('')
                self.lineEdit_23.setText('')
                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data3 != None:
                self.lineEdit_21.setText(str(data3[2]))
                self.lineEdit_18.setText(str(data3[3]))
                self.lineEdit_19.setText(str(data3[4]))
                self.lineEdit_23.setText(str(data3[1]))

        print('done')
        self.lineEdit_27.setText('')
    def save_family(self):
        name=self.lineEdit_23.text()
        addrese = self.lineEdit_21.text()
        phone = self.lineEdit_18.text()
        numchild = self.lineEdit_19.text()
        self.cur.execute('''UPDATE family SET name=?, addrese=?,phone=?,num_child=?''',(name,addrese,phone,numchild))
        self.con.commit()
        print('update done')
        self.lineEdit_21.setText('')
        self.lineEdit_18.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_23.setText('')
        self.lineEdit_27.setText('')
        self.comboBox_11.setCurrentIndex(0)

    def delete_family(self):
        data_search = self.lineEdit_27.text()
        date = datetime.datetime.now()
        delete_message = QMessageBox.warning(self, 'delete information',
                                             'are you sure do you want to delete the information?',
                                             QMessageBox.Yes | QMessageBox.No)
        if delete_message == QMessageBox.Yes:
            if self.comboBox_11.currentIndex() == 0:
                sql = (''' DELETE  FROM family WHERE name=?
                                    ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_11.currentIndex() == 1:
                sql = (''' DELETE  FROM family WHERE addrese=?
                                             ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_11.currentIndex() == 2:
                sql = (''' DELETE  FROM family WHERE phone=?
                                             ''')
                self.cur.execute(sql, [(data_search)])
            if self.comboBox_11.currentIndex() == 3:
                sql = (''' DELETE  FROM family WHERE num_child=?
                           ''')
                self.cur.execute(sql, [(data_search)])
            self.con.commit()
            self.statusBar().showMessage('the delete is done successful')
            print('done')
            self.lineEdit_21.setText('')
            self.lineEdit_18.setText('')
            self.lineEdit_19.setText('')
            self.lineEdit_23.setText('')
            self.lineEdit_27.setText('')
            self.comboBox_11.setCurrentIndex(0)

    def export_family(self):
        self.cur.execute(''' SELECT name,addrese,phone,num_child,sitution,description,date FROM family ''')
        data = self.cur.fetchall()
        excel_file = Workbook('family_report.xlsx')
        sheet1 = excel_file.add_worksheet()
        sheet1.write(0, 0, 'name')
        sheet1.write(0, 1, 'addrese')
        sheet1.write(0, 2, 'phone')
        sheet1.write(0, 3, 'num_child')
        sheet1.write(0, 4, 'social_sitution')
        sheet1.write(0, 5, 'description')
        sheet1.write(0, 6, 'date')

        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        excel_file.close()

    ######################################children of family needed#########################################################
    def category_name(self):
        self.comboBox_11.clear()
        self.cur.execute('''
                          SELECT name FROM family  ''')
        categories = self.cur.fetchall()
        print(categories)
        for category in categories:
            self.comboBox_6.addItem(str(category[0]))
    def add_child(self):
        name_family=self.comboBox_6.currentText()
        age_child=self.lineEdit_29.text()
        sitution_child=self.lineEdit_28.text()
        description=self.textEdit_3.toPlainText()
        date = datetime.datetime.now()
        self.cur.execute('''INSERT INTO  Children (name,age,sitution,description,date)
        VALUES(?,?,?,?,?)''',(name_family,age_child,sitution_child,description,date))
        self.con.commit()
        print('done')
        self.lineEdit_29.setText('')
        self.lineEdit_28.setText('')
        self.comboBox_6.setCurrentIndex(0)
        self.textEdit_3.setText('')

    def search_child(self):
        data_search = self.lineEdit_32.text()

        if self.comboBox_12.currentIndex() == 0:
            sql = (''' SELECT * FROM Children WHERE name=?
                                           ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchone()
            print(data)
            if data == None:

                self.lineEdit_30.setText('')
                self.lineEdit_30.setText('')

                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data != None:
                self.lineEdit_30.setText(str(data[2]))
                self.lineEdit_31.setText(str(data[3]))

        if self.comboBox_12.currentIndex() == 1:
            sql = (''' SELECT * FROM Children WHERE age=?
                                                ''')
            self.cur.execute(sql, [(data_search)])
            data1 = self.cur.fetchone()
            print(data1)
            if data1 == None:

                self.lineEdit_30.setText('')
                self.lineEdit_30.setText('')

                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data1 != None:
                self.lineEdit_30.setText(str(data1[2]))
                self.lineEdit_31.setText(str(data1[3]))
        if self.comboBox_12.currentIndex() == 2:
            sql = (''' SELECT * FROM Children WHERE sitution=?
                                                ''')
            self.cur.execute(sql, [(data_search)])
            data2 = self.cur.fetchone()
            print(data2)
            if data2 == None:

                self.lineEdit_30.setText('')
                self.lineEdit_30.setText('')

                QMessageBox.warning(self, "Data Error", " No Result Provide a valid data")

            elif data2 != None:
                self.lineEdit_30.setText(str(data2[2]))
                self.lineEdit_31.setText(str(data2[3]))
        print('done')
        self.lineEdit_32.setText('')
    def save_child(self):
        age_child = self.lineEdit_30.text()
        sitution_child = self.lineEdit_31.text()

        self.cur.execute('''UPDATE Children SET age=?, sitution=?''',
                         (age_child, sitution_child,))
        self.con.commit()
        print('update done')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
    def delete_child(self):

        data_search = self.lineEdit_32.text()
        delete_message = QMessageBox.warning(self, 'delete information',
                                             'are you sure do you want to delete the information?',
                                             QMessageBox.Yes | QMessageBox.No)
        if delete_message == QMessageBox.Yes:
            if self.comboBox_12.currentIndex() == 0:
                sql = (''' DELETE  FROM Children WHERE name=?
                                    ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_12.currentIndex() == 1:
                sql = (''' DELETE  FROM Children WHERE age=?
                                             ''')
                self.cur.execute(sql, [(data_search)])

            if self.comboBox_12.currentIndex() == 2:
                sql = (''' DELETE  FROM Children WHERE sitution=?
                                             ''')
                self.cur.execute(sql, [(data_search)])
            self.con.commit()
            self.statusBar().showMessage('the delete is done successful')
            print('done')
        self.lineEdit_30.setText('')
        self.lineEdit_31.setText('')
        self.comboBox_12.setCurrentIndex(0)
    def show_child(self):
        data_search = self.lineEdit_25.text()
        #self.tableWidget_4.insertRow(0)
        if self.comboBox_5.currentIndex() == 0:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            self.cur.execute(''' SELECT name,age,sitution,description,date FROM  Children ''')
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_4.insertRow(row_position)

            self.tableWidget_4.removeRow((len(data)))


        if self.comboBox_5.currentIndex() == 1:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            sql = (''' SELECT name,age,sitution,description,date FROM Children WHERE name=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_4.insertRow(row_position)

            self.tableWidget_4.removeRow((len(data)))

        if self.comboBox_5.currentIndex() == 2:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            sql =  (''' SELECT name,age,sitution,description,date FROM Children WHERE age=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_4.insertRow(row_position)
        if self.comboBox_5.currentIndex() == 3:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            sql =  (''' SELECT name,age,sitution,description,date FROM Children WHERE sitution=? 
                                                       ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_4.insertRow(row_position)
    def export_child(self):
        self.cur.execute('''SELECT name,age,sitution,description,date FROM Children ''')
        data = self.cur.fetchall()
        excel_file = Workbook('children_report.xlsx')
        sheet1 = excel_file.add_worksheet()
        sheet1.write(0, 0, 'name')
        sheet1.write(0, 1, 'age')
        sheet1.write(0, 2, 'sitution')
        sheet1.write(0, 3, 'description')
        sheet1.write(0, 4, 'date')
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        excel_file.close()

    ###################################################donation############################################################


    def show_donation(self):
        data_search = self.lineEdit_24.text()
        # self.tableWidget_4.insertRow(0)
        if self.comboBox_7.currentIndex() == 0:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            self.cur.execute(''' SELECT I.code,I.type,I.amountimpo,I.joined_dateimp,I.description, e.amountex,e.date_ex
                              FROM donationimport I
                              LEFT JOIN donationexport e
                              ON I.code= e.code   ''')

            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_3.insertRow(row_position)

            self.tableWidget_3.removeRow((len(data)))

        if self.comboBox_7.currentIndex() == 1:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            sql = (''' SELECT I.code,I.type,I.amountimpo,I.joined_dateimp,I.description, e.amountex,e.date_ex
                              FROM donationimport I
                              LEFT JOIN donationexport e
                              ON I.code= e.code
                               WHERE I.code=?   ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_3.insertRow(row_position)

            self.tableWidget_3.removeRow((len(data)))

        if self.comboBox_7.currentIndex() == 2:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            sql = ('''  SELECT I.code,I.type,I.amountimpo,I.joined_dateimp,I.description, e.amountex,e.date_ex
                              FROM donationimport I
                              LEFT JOIN donationexport e
                              ON I.code= e.code  WHERE  I.type=?  ''')
            self.cur.execute(sql, [(data_search)])
            data = self.cur.fetchall()
            print(data)
            row_position = 0
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position += 1
                self.tableWidget_3.insertRow(row_position)

            self.tableWidget_3.removeRow((len(data)))

    def add_donation_import(self):
        code_donation=self.lineEdit_35.text()
        type_donation=self.comboBox_4.currentText()
        amount_import = self.lineEdit_22.text()
        joind_dateimp = self.dateEdit.text()
        description_donation=self.textEdit_2.toPlainText()
        date=datetime.datetime.now()
        self.cur.execute(''' INSERT INTO  donationimport (type,amountimpo,joined_dateimp,description,date,code)
        VALUES(?,?,?,?,?,?)''',(type_donation,amount_import,joind_dateimp,description_donation,date,code_donation))
        self.con.commit()
        print('done')
        self.lineEdit_35.setText('')
        self.comboBox_4.setCurrentIndex(0)
        self.lineEdit_22.setText('')
        #self.dateEdit.setText('')
        self.textEdit_2.setText('')

    def add_donation_export(self):
        code_donation = self.comboBox_8.currentText()
        amount_export = self.lineEdit_37.text()
        joind_dateex = self.dateEdit_2.text()
        date = datetime.datetime.now()
        self.cur.execute(''' INSERT INTO  donationexport (code,amountex,date_ex,date)
               VALUES(?,?,?,?)''',
                         (code_donation, amount_export, joind_dateex, date))
        self.con.commit()
        print('done')
        self.comboBox_8.setCurrentIndex(0)
        self.lineEdit_37.setText('')
        #self.dateEdit_2.setText('')

    def category_code(self):
        self.comboBox_8.clear()
        # user=self.comboBox_16.currentText()
        self.cur.execute('''SELECT code FROM donationimport''')
        categories = self.cur.fetchall()
        for data in categories:
            self.comboBox_8.addItem(str(data[0]))


    def export_donation(self):
        self.cur.execute(''' SELECT I.code,I.type,I.amountimpo,I.joined_dateimp,I.description, e.amountex,e.date_ex
                              FROM donationimport I
                              LEFT JOIN donationexport e
                              ON I.code= e.code   ''')
        data = self.cur.fetchall()
        excel_file = Workbook('donation_report.xlsx')
        sheet1 = excel_file.add_worksheet()
        sheet1.write(0, 0, 'code')
        sheet1.write(0, 1, 'type')
        sheet1.write(0, 2, 'import amount')
        sheet1.write(0, 3, 'import_joined_date')
        sheet1.write(0, 4, 'description')
        sheet1.write(0, 5, 'export amount')
        sheet1.write(0, 6, 'export_joined_date')
        row_number = 1
        for row in data:
            col_number = 0
            for item in row:
                sheet1.write(row_number, col_number, str(item))
                col_number += 1
            row_number += 1
        excel_file.close()
    ##########################################dashboard#########################################
    def show_dashboard(self):
      pass

    ##########################################setting user#######################################
    def user(self):
        user_name = self.lineEdit_49.text()
        password = self.lineEdit_41.text()
        password2 = self.lineEdit_39.text()

        if password == password2:
            self.cur.execute(''' INSERT INTO user( name,password)
                     VALUES(?, ?)''', (user_name, password))
            self.con.commit()
            self.lineEdit_49.setText('')
            self.lineEdit_41.setText('')
            self.lineEdit_39.setText('')
        else:

            QMessageBox.warning(self, "Data Error", " Wrong password provide a valid password" )
            self.lineEdit_39.setText('')
        print('done')
    def category_user(self):
        self.comboBox_16.clear()
        #user=self.comboBox_16.currentText()
        self.cur.execute('''SELECT name FROM user''')
        categories=self.cur.fetchall()
        for data in categories:
            self.comboBox_16.addItem(str(data[0]))

    def permission(self):
        user_name = self.comboBox_16.currentText()
        date=datetime.datetime.now()
        if self.checkBox_23.isChecked() == True:
            self.cur.execute('''INSERT INTO permession(name,volunteers,family, children,donation,dashboard,setting,addv,editv,deletev,exportv,importv,searchv,addf,editf,deletef,exportf,importf,searchf,addch,editch,deletech,exportch,searchch,adddon,editdon,deletedon,exportdon,importdon,searchdon,importch,date)
                                         VALUES(?,?,?,?,?,? ,?,?,?,?,?,?,?,?,?,?,?,? ,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
             (user_name, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1,1 ,1,1,date))
            self.con.commit()
            self.statusBar().showMessage('the input of information is done successful')
            print('done')
        if self.checkBox_23.isChecked() == False:
                tab_volunteers = 0
                tab_family= 0
                tab_children = 0
                tab_donation = 0
                tab_dashboard = 0
                tab_setting = 0
                #############################################
                # volunteers
                add_v = 0
                edit_v = 0
                delete_v = 0
                import_v = 0
                export_v = 0
                search_v=0
                ################################################
                # family
                add_f = 0
                edit_f = 0
                delete_f = 0
                import_f = 0
                export_f = 0
                search_f = 0
                ################################################
                # children
                add_ch = 0
                edit_ch = 0
                delete_ch = 0
                import_ch = 0
                export_ch = 0
                search_ch = 0
                # donation
                add_don = 0
                edit_don = 0
                delete_don = 0
                import_don = 0
                export_don = 0
                search_don = 0
                if self.checkBox_7.isChecked() == True:
                    tab_volunteers = 1
                if self.checkBox_8.isChecked() == True:
                    tab_family = 1
                if self.checkBox_11.isChecked() == True:
                    tab_dashboard = 1
                if self.checkBox_10.isChecked() == True:
                    tab_children = 1
                if self.checkBox_12.isChecked() == True:
                    tab_setting = 1
                if self.checkBox_9.isChecked() == True:
                    tab_donation = 1
                if self.checkBox_3.isChecked() == True:
                    add_v = 1
                if self.checkBox_5.isChecked() == True:
                    edit_v = 1
                if self.checkBox_6.isChecked() == True:
                    delete_v = 1
                if self.checkBox_16.isChecked() == True:
                    import_v = 1
                if self.checkBox_24.isChecked() == True:
                    export_v = 1
                if self.checkBox_22.isChecked() == True:
                    search_v=1
                if self.checkBox_4.isChecked() == True:
                    add_f = 1
                if self.checkBox_13.isChecked() == True:
                    edit_f = 1
                if self.checkBox_14.isChecked() == True:
                    delete_f = 1
                if self.checkBox_26.isChecked() == True:
                    import_f = 1
                if self.checkBox_27.isChecked() == True:
                    export_f = 1
                if self.checkBox_25.isChecked() == True:
                    search_f=1
                if self.checkBox_15.isChecked() == True:
                    add_ch = 1
                if self.checkBox_17.isChecked() == True:
                    edit_ch = 1
                if self.checkBox_18.isChecked() == True:
                    delete_ch = 1
                if self.checkBox_28.isChecked() == True:
                    import_ch = 1
                if self.checkBox_29.isChecked() == True:
                    export_ch = 1
                if self.checkBox_32.isChecked() == True:
                    search_ch = 1
                if self.checkBox_19.isChecked() == True:
                    add_don = 1
                if self.checkBox_20.isChecked() == True:
                    edit_don = 1
                if self.checkBox_21.isChecked() == True:
                    delete_don = 1
                if self.checkBox_30.isChecked() == True:
                    import_don = 1
                if self.checkBox_31.isChecked() == True:
                    export_don = 1
                if self.checkBox_33.isChecked() == True:
                    search_don = 1
                self.cur.execute('''INSERT INTO permession(name,volunteers,family,children,donation,dashboard,setting,addv,editv,deletev,exportv,importv,searchv,addf,editf,deletef,exportf,importf,searchf,addch,editch,deletech,exportch,searchch,adddon,editdon,deletedon,exportdon,importdon,searchdon,importch)
                                                    
                VALUES(?,?,?,?,?,? ,?,?,?,?,?,?,?,?,?,?,?,? ,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(user_name,tab_volunteers,tab_family,tab_children,tab_donation,tab_dashboard,tab_setting,add_v,edit_v,delete_v,export_v,import_v,search_v,add_f,edit_f,delete_f,export_f,import_f,search_f,add_ch,edit_ch,delete_ch,export_ch,search_ch,add_don,edit_don,delete_don,export_don,import_don,search_don,import_ch))
                self.con.commit()
                self.statusBar().showMessage('the input of information is done successful')
                print('done')
    ###########################################current tabwidget##############################################

    def login_tab(self):
        self.tabWidget.setCurrentIndex(0)
        #images=self.tabWidget.currentIndex(0)


    def volunt_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
    def family_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)
    def child_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_5.setCurrentIndex(0)
    def donation_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_4.setCurrentIndex(0)
    def dashbaord_tab(self):
        self.tabWidget.setCurrentIndex(5)
    def setting_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_6.setCurrentIndex(0)


def main():
        app = QApplication(sys.argv)
        window = MainApp()
        window.show()
        app.exec_()

if __name__ == '__main__':
        main()
