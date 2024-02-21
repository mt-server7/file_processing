#!/usr/bin/python3
#version 7 
#created specifically for Aksioma/launch

import pandas as pd
import pathlib

class File_path:
# в этом классе находим путь к файлу и читаем csv файл
    path1 = pathlib.Path(__file__)
    path2 = path1.parents[0]
    path3 = path2.joinpath('name.csv')
    print('Файл со списком лежит по адресу: ',path3,'\n')
    csv_file = pd.read_csv(path3, encoding='windows-1251', sep=';')

class Student(File_path):
# В этом классе обрабатываем список учеников и учителей без классного руководства
    def create_list_students():
        
        csv_file = File_path.csv_file
        df = pd.DataFrame(csv_file)
        df.insert(loc=0, column='id_aks', value=0)
        df.insert(loc=0, column='id_ext', value=0)
        df = df.rename(columns = {'Unnamed: 0': 'sur_name', 'Unnamed: 1': 'first_name', 'Unnamed: 2': 'second_name', 'Unnamed: 3': 'school', 'Unnamed: 4': 'figure', 'Unnamed: 5': 'letter', 'Unnamed: 6': 'mex', 'Unnamed: 7': 'typep', 'Unnamed: 8': 'categorical'})
        
        print('Введите название/номер школы:')
        id_school = input()
        
        df.school = id_school

        df.fillna({'mex':1, 'categorical':0}, inplace=True)
        df['typep'] = 1
        
        df['sur_name'] = df['sur_name'].str.replace(' ', '')
        df['first_name'] = df['first_name'].str.replace(' ', '')
        df['second_name'] = df['second_name'].str.replace(' ', '')
        
        df.fillna('0', inplace=True)
        
        df['letter'] = df['letter'].str.lower()
        
        df.id_aks = df.id_aks.astype(int)
        df.id_ext = df.id_ext.astype(int)
        df.mex = df.mex.astype(int)
        df.typep = df.typep.astype(int)
        df.categorical = df.categorical.astype(int)
        df.figure = df.figure.astype(int)

        df.sort_values(by= ['sur_name', 'first_name', 'second_name'], inplace=True)
        df = df.drop_duplicates()
        
        df = df.to_csv ('Список name ' + id_school + '.csv', sep=';', encoding='windows-1251', header=False, index=False) #upload csv
        print('Completed list students')


class Teachers(File_path):
# В этом классе обрабатываем список классных руководителей
    def create_list_teachers():
        csv_file = File_path.csv_file
        
        df = pd.DataFrame(csv_file)
        df = df.rename(columns = {'Unnamed: 0': 'id_aks', 'Unnamed: 1': 'id_ext', 'Unnamed: 2': 'sur_name', 'Unnamed: 3': 'first_name', 'Unnamed: 4': 'second_name', 'Unnamed: 5': 'school', 'Unnamed: 6': 'figure', 'Unnamed: 7': 'letter', 'Unnamed: 8': 'mex', 'Unnamed: 9': 'typep', 'Unnamed: 10': 'categorical'})
        
        print('Введите название/номер name:')
        id_school = input()
        
        df.school = id_school
        df['id_aks'] = 0
        df['id_ext'] = 0
        df.fillna({'mex':1, 'typep':1, 'categorical':0}, inplace=True)
        df['typep'] = 1
        df['figure'] = 100
        df['letter'] = 'у' 
        
        df['sur_name'] = df['sur_name'].str.replace(' ', '')
        df['first_name'] = df['first_name'].str.replace(' ', '')
        df['second_name'] = df['second_name'].str.replace(' ', '')
        
        df.fillna('0', inplace=True)
        df.id_aks = df.id_aks.astype(int)
        df.id_ext = df.id_ext.astype(int)
        df.mex = df.mex.astype(int)
        df.typep = df.typep.astype(int)
        
        df.categorical = df.categorical.astype(int)
        df.figure = df.figure.astype(int)
        df.sort_values(by= ['sur_name', 'first_name', 'second_name'], inplace=True)
        df = df.drop_duplicates()
        
        df.to_csv ('Список name ' + id_school + '.csv', sep=';', encoding='windows-1251', header=False, index=False) 
        print('Completed list name')

class Balance(File_path):
    def create_list_of_balance():
        csv_file = File_path.csv_file
        df = pd.DataFrame(csv_file)
        df = df.rename(columns = {'Unnamed: 0': 'id_aks', 'Unnamed: 1': 'date_pay', 'Unnamed: 2': 'hot_goods', 'Unnamed: 3': 'bar_goods', 'Unnamed: 4': 'id_external', 'Unnamed: 5': 'school', 'Unnamed: 6': 'Bank', 'Unnamed: 7': 'check'})

        df = df.drop_duplicates(subset=['id_aks'])
        
        print('Введите название или id name:')
        input_name_school = input()
        print('Введите дату платежа:')
        input_date_pay = input()
        df.date_pay = input_date_pay
        
        df.fillna(value = 0, inplace=True)

        print(df.columns)
        
        df.hot_goods = df.hot_goods.astype(float)
        df.bar_goods = df.bar_goods.astype(float)
        
        df.hot_goods *= 100
        df.bar_goods *= 100
        df['id_external'] = 0
        df['school'] = 0
        df['Bank'] = 'name1'
        df['check'] = 'name2'

        df.id_aks = df.id_aks.astype(int)
        df.hot_goods = df.hot_goods.astype(int)
        df.bar_goods = df.bar_goods.astype(int)
        df.id_external = df.id_external.astype(int)
        df.school = df.school.astype(int)

        return_name_date = input_name_school + ' за ' + input_date_pay

        df = df.to_csv ('Список name3 для ' + return_name_date + '.csv', sep=';', encoding='windows-1251', header=False, index=False) #upload csv
        print('Сформирован список name3')

def __main__():
# Главная функция программы
    print('Введите 1 если список с name и name без name')
    print('Введите 2 если список с name2')
    print('Введите 3 если список с name3')
    print('Введите 11 для выхода')
    
    while(True):
        print('Введите номер:')
        number_menu = input()
    
        if(number_menu == '1'): 
            Student.create_list_students()
        elif(number_menu == '2'):
            Teachers.create_list_teachers()
        elif(number_menu == '3'):
            Balance.create_list_of_balance()
        elif(number_menu == '11'):
            print('Хорошего дня!)')
            exit()
               
        else:
            print('Неправильно введен номер меню!\n')

# Задаем точку входа
if __name__ == '__main__':
    __main__()