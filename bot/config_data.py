#
with open('C:/Users/silki/Documents/Dev/env.txt','r') as env:
    token_admin = env.read()

class Slot:
    def __init__(self, day,time):
        self.time = time
        self.day = day
        self.slot = {}
        self.slot[day] = time
class Calendary:
    def __init__(self):
        self.monday = {
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.tuesday = {
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.wednesday = {
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.thursday = {
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.friday = {
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.sunday = {
            '09:00': [None],
            '10:30': [None],
            '12:00': [None],
            '13:30': [None],
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.saturday = {
            '09:00': [None],
            '10:30': [None],
            '12:00': [None],
            '13:30': [None],
            '15:00': [None],
            '16:30': [None],
            '18:00': [None],
            '19:30': [None],
            '21:00': [None],
        }
        self.calendary = [self.monday,self.tuesday,self.wednesday,self.thursday,self.friday,self.sunday,self.saturday]
class Tutor:
    def __init__(self, id_tutor, last_name, first_name, token= None):
        self.id_tutor = id_tutor
        self.last_name = last_name
        self.first_name = first_name
        self.token = token
        self.calendary = {}
    
    def set_slot(self, day, time):
        if day in self.calendary:
            self.calendary[day].append(time)
        else:
            self.calendary[day] = [time]
        return self.calendary
    def remove_day(self,day):
        del self.calendary[day]
class Admin:
    id  = 0
    def __init__(self, last_name, first_name, token= None):
        self.last_name = last_name
        self.first_name = first_name
        self.token = token
        self.tutors = []
    
    def creat_tutor(self,theme,last_name, first_name, token= None):
        id_tutor = f't{theme[0]}{Admin.id}'
        Admin.id += 1
        self.tutors.append([theme, id_tutor, Tutor(id_tutor, last_name, first_name, token= None)])
        return self.tutors
    
    def desplay_calendary(self):
        return self.tutors
    
    def del_tutor(self,ID):
        for tutor in self.tutors:
            if tutor[1] == ID:
                index = self.tutors.index(tutor)
                self.tutors.pop(index)
        return self.tutors


class Student:
    def __init__(self, id_student, last_name, first_name, phone_number, token= None):
        self.id_student = id_student
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.token = token
        self.calendary = {} # кадендарь по типу "день недели" = [Предмет, Время]
admin = Admin('Силкин', 'Александр', token_admin)
#debug class
#print(admn)
#admn.creat_tutor("Математика",'Mark', 'Ggo', '3232')
#admn.creat_tutor("Литература",'Ирина', 'Маклакова', '893464724')
#print(admn.__dict__)
#for i in admn.tutors:
#    if i[2].first_name == 'Ggo':
#        i[2].set_slot('1','10:00')
#    if i[2].first_name == 'Маклакова':
#         i[2].set_slot('6','11:00')
#        print(i[2].__dict__)
#
#40 550 
#80 1.2  1100 1500
#160 2.4 2200 4400