from peewee import *

DATABASE = 'MyDB.sqlite'

# SQLite database using WAL journal mode and 64MB cache.
sqlite_db = SqliteDatabase(DATABASE, pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


sqlite_db = SqliteDatabase(DATABASE, pragmas={'journal_mode': 'wal'})

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class Clients(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

class Orders(BaseModel):
    client_id = ForeignKeyField(Clients, null = True)
    date = DateField()
    amount = FloatField()
    description = CharField()