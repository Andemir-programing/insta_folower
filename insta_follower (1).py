# -*- coding: utf-8 -*-
"""insta_follower.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17mLlHKua6qU9gHnpx7SwOhWHIO_ynzVX
"""

from google.colab import drive# мы импортируем из google colab модуль drive: #import drive module
drive.mount('/content/gdrive', force_remount=True)#мы вызываем функцию drive.mount чтобы подключить колаб к диску #connect the colab to the drive
path777 = "/content/gdrive/My Drive/COLAB_Andemir/homeworks/insta_follower.csv"#записываем путь к файлу #path to the file

with open(path777, "r") as f: #открываем файл для чтения #open the file for reading
  segments = f.readlines() #получаем список строк: #list of strings

dict_inst = {}#создаем новый словарь #create a new dictionary
for i in range(len(segments[0].split(","))): #для каждого элемента первого списка строк, который отделен на элементы по запятым #for each element of the first list of strings, which is separated into elements by commas
  dict_inst[i] = [] #создаем для каждого подписчика Elan в качестве значения в словаре пустой список #for each Elan subscriber, write an empty list as a value in the dictionary

for line in segments[1:]: #для каждого элемента списка строк подписок #for each item in the list of subscription strings
  for i in dict_inst: #для каждого аккаунта в словаре #for each account in the dictionary
    a = line.split(",")[i] #отделяем по запятым каждую подписку подписчиков Elan  #Separate each Elan subscription by commas
    if a != "" and a != "\n" and a != "\t" and a != " ": #исключаем пустые строки, переносы и отступы #exclude blank lines, line breaks and indents
      dict_inst[i].append(a) #записываем в словарь в качестве значений подписки каждого подписчика Elan # write to the dictionary as values the subscription of each Elan subscriber

names = [] #создаем пустой список #create new list
for i in range(len(dict_inst.values())): #для каждого списка, состоящего из подписок подписчиков Elan #for each list of subscriptions of Elan subscribers
  names += dict_inst[i] #добавляем в список всех подписчиков Elan #add all Elan subscribers to the list
names_set = set(names) #избавляемся от повторов аккаунтов #remove duplicate accounts
dict_followers = {name:names.count(name) for name in names_set} #считаем подписчиков каждого аккаунта среди подписок подписчиков elan: #count the subscribers of each account among the subscriptions of elan subscribers
common_names = sorted(dict_followers, key = dict_followers.get, reverse = True) #записываем в порядке уменьшения популярности #write in order of decreasing popularity
top_accounts = common_names[2:22] #иключаем из списка акаунты Elan: #keep the account Elan and elan_coding

d = {} #создаем новый словарь #create a new dictionary
for i in top_accounts: #проходимя по топу аккаунтов #for top accounts
    d[i] = dict_followers[i] #записываем в словарь парами аккаунт и количество его подписчиков среди подписчиков elan #write in the dictionary in pairs the account and the number of its subscribers among the subscribers of elan
print(d) #печатаем словарь #print dictionary

text = '' #создаем новую строку #create new string
for i,j in d.items(): #для значений и ключей #for values and keys
  text += i + ' - ' + str(j) + '\n' #записываем в строку в формате "аккаунт - количество подписчиков " #write to a string in the format "account - number of subscribers"

path = "/content/gdrive/My Drive/COLAB_Andemir/classworks/report_insta.txt" #создаем новый файл #create new file
with open(path, "w") as f: #открываем файл для записи #open file for writing
  f.write(text) #записываем строку в новый файл #write the line to a new file









