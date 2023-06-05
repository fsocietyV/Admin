import datetime
import os
import random
from Other.ClassDb import *
from Other.ClassFileData import *

class dbFunctions:

    def createDb():
        sqliteDbFile = os.path.isfile(DATABASE)
        if (sqliteDbFile == True):
            os.remove(DATABASE)
            with sqlite_db:
                sqlite_db.create_tables([Clients, Orders])
        else:
            with sqlite_db:
                sqlite_db.create_tables([Clients, Orders])
            sqliteDbFile = True
        return sqliteDbFile

    def fillDb():
        sqliteDbFile = os.path.isfile(DATABASE)
        File = FileData
        File.city = File.importDateFromFileCity()
        File.name = File.importDateFromFileName()
        if (sqliteDbFile == True):
            with sqlite_db:
                clients = [
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'30 years Victory 12'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Twerskaya 13'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Mayskaya 2'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'30 years Victory 35'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Sovetskaya 19'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Primorskaya 65'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Mirnaya 27'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Lipkaya 15'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Montaznikov 25'},
                    {'name':random.choice(File.name),'city':random.choice(File.city),'address':'Privokzalnaya 47'}
                ]
                Clients.insert_many(clients).execute()
                ClientsTable = Clients.select()
                orders = [
                    {'client_id':ClientsTable[len(ClientsTable)-10],'date':datetime.date(2022,2,15),'amount':1.0,'description':'Table'},
                    {'client_id':ClientsTable[len(ClientsTable)-9],'date':datetime.date(2023,1,17),'amount':4.0,'description':'Board'},
                    {'client_id':ClientsTable[len(ClientsTable)-8],'date':datetime.date(2021,7,22),'amount':7.0,'description':'Cup'},
                    {'client_id':ClientsTable[len(ClientsTable)-7],'date':datetime.date(2022,10,21),'amount':10.0,'description':'Hammer'},
                    {'client_id':ClientsTable[len(ClientsTable)-6],'date':datetime.date(2022,6,9),'amount':14.0,'description':'Nails'},
                    {'client_id':ClientsTable[len(ClientsTable)-5],'date':datetime.date(2023,2,19),'amount':6.0,'description':'Chair'},
                    {'client_id':ClientsTable[len(ClientsTable)-4],'date':datetime.date(2023,2,10),'amount':9.0,'description':'Fastener'},
                    {'client_id':ClientsTable[len(ClientsTable)-3],'date':datetime.date(2022,12,5),'amount':1.0,'description':'Lamp'},
                    {'client_id':ClientsTable[len(ClientsTable)-2],'date':datetime.date(2022,2,17),'amount':16.0,'description':'Screw'},
                    {'client_id':ClientsTable[len(ClientsTable)-1],'date':datetime.date(2023,1,1),'amount':22.0,'description':'Board'}
                ]
                Orders.insert_many(orders).execute()
            CheckForTable = True
        else:
            print("Database not found")
        return CheckForTable

    def showClientsDb():
        sqliteDbFile = os.path.isfile(DATABASE)
        if (sqliteDbFile == True):
            print(f"{'id' : <15}{'name' : <15}{'city' : <20}{'address' : <15}")
            for i in Clients.select():
                print(f"{i.id : <15}{i.name : <15}{i.city : <20}{i.address : <15}")
        else:
            print("Database not found")
        return Clients.select().count()

    def showOrdersDb():
        sqliteDbFile = os.path.isfile(DATABASE)
        if (sqliteDbFile == True):
            print(f"{'id' : <15}{'client_id' : <15}{'date' : <15}{'amount' : <15}{'description' : <15}")
            for i in Orders.select():
                print(f"{i.id : <15}{i.client_id}\t\t{i.date}\t{i.amount : <15}{i.description : <15}")
        else:
            print("Database not found")
        return Orders.select().count()