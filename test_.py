from Other.ClassFuncDb import dbFunctions

db = dbFunctions

def testCreateDb():
    assert db.createDb() == True

def testFillDb():
    assert db.fillDb() == True

def testClientsCount():
    assert db.showClientsDb() >= 10

def testOrdersCount():
    assert db.showOrdersDb() >= 10
