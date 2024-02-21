#!/usr/bin/python3
'''
Скрипт получает на вход файл name.csv установленного формата (является выгрузкой из 1С),
берет из файла необходимые данные и подготовливает к SQL запросу.
На выходе получаем .txt файл, в который необходимо добавить служебное слово VALUES и заменить в последней строке запятую на точку с запятой.
'''

import pandas as pd
import pathlib

class File_path:
    #получение адреса файла
    path1 = pathlib.Path(__file__)
    path2 = path1.parents[0]
    path3 = path2.joinpath('name.csv')
    print('Файл со списком лежит по адресу:', path3, '\n')
    csv_file = pd.read_csv(path3, encoding='windows-1251', sep=';')
    
class Processing(File_path):
    def list_processing():
        
        #создаем датафрейм
        csv_file = File_path.csv_file
        df = pd.DataFrame(csv_file)

        #Работаем рационами
        df.fillna({'name1': 0}, inplace=True)
        df = df.loc[df['name1'] != 0]
        df['name1'] = df['name1'].astype(int)
        
        #Работаем с ценой рационов
        df.fillna({'name3': 0}, inplace=True)
        df['name3'] = df['name3'] * 100
        df['name3'] = df['name3'].astype(int) 

        #сортируем по дате и рационам
        df = df.sort_values(by=['name4', 'name1'])
        
        #работаем с датой
        df['name4'] = pd.to_datetime(df['name4'], dayfirst=True)

        #добавляем служебные символы
        df['name2'] = df['name2'].astype(str)
        df['name4'] = df['name4'].astype(str)
        df['name1'] = df['name1'].astype(str)
        df['name3'] = df['name3'].astype(str)
        
        df['name2'] = ('(' + '\'' + df['name2'] + '\'' + ',').astype(str)
        df['name4'] = ('\'' + df['name4'] + '\'' + ',').astype(str)
        df['name1'] = ('\'' + df['name1'] + '\'' + ',').astype(str)
        df['name3'] = ('\'' + df['name3'] + '\'' + '),').astype(str)
        
        #Формируем итоговый датафрейм
        #Создаем датафрейм с запросом SQL
        request = pd.DataFrame({'result': ['INSERT INTO (SCHOOL,DATE,HOT_GOODS_ID,PRICE)']})
        df['result'] = df['name2'].astype(str) + df['name4'].astype(str) + df['name1'].astype(str) + df['name3'].astype(str)
        df = df[['result']]
        #объединяем датафреймы 
        res = pd.concat([request, df])
        
        
        #print(result.columns)
        print(res)

        #сохранение в файл
        print('Введите название/номер:')
        id_school = input()
        res = res.to_csv ('insert_' + id_school +'.txt', sep=';', encoding='windows-1251', header=False, index=False)
        
        
def print_menu():
    print('1. Start script')
    print('2. Print menu')
    print('0. Exit')
    
def __main__():
    print_menu()
    
    enter_num = input('Enter num menu: ')

    if enter_num == '1': Processing.list_processing()
    elif enter_num == '2': print_menu()
    elif enter_num == '0': exit()
    else: print('error input!')

if __name__ == "__main__":
    __main__()