import databasetesting as db
import pandas as pd

def classesui():
    cnxn=db.connect()
    crsr=cnxn.cursor()
    names=pd.read_sql("select name from classes;",cnxn)
    print("list of classes")
    for name in names['name']:
        print(name)
    print("1. Add class")
    print("2. Delete class")
    print("0 . Back")
    i=int(input("Enter choice: "))
    if i==1:
        newclass=input("Enter name: ")
        crsr.execute("insert into classes values('{}');".format(newclass))
        cnxn.commit()
        print("Class added")
    elif i==2:
        name=input("Enter name: ")
        crsr.execute("delete from classes where name='{}';".format(name))
        cnxn.commit()
        print("Class deleted")
    cnxn.close()
    return
def teachersui():
    cnxn=db.connect()
    crsr=cnxn.cursor()
    names=pd.read_sql("select name from teachers;",cnxn)
    print("list of teachers")
    for name in names['name']:
        print(name)
    print("1. Add teacher")
    print("2. Delete teacher")
    print("0 . Back")
    i=int(input("Enter choice: "))
    if i==1:
        newteacher=input("Enter name: ")
        crsr.execute("insert into teachers values ('{}');".format(newteacher))
        cnxn.commit()
        print("Teacher added")
    elif i==2:
        name=input("Enter name: ")
        crsr.execute("delete from teachers where name='{}';".format(name))
        cnxn.commit()
        print("Teacher deleted")
    cnxn.close()
    return
def labsui():
    cnxn=db.connect()
    crsr=cnxn.cursor()
    names=pd.read_sql("select name from labs;",cnxn)
    print("list of labs")
    for name in names['name']:
        print(name)
    print("1. Add lab")
    print("2. Delete lab")
    print("0 . Back")
    i=int(input("Enter choice: "))
    if i==1:
        newlab=input("Enter name: ")
        crsr.execute("insert into labs values ('{}');".format(newlab))
        cnxn.commit()
        print("Lab added")
    elif i==2:
        name=input("Enter name: ")
        crsr.execute("delete from labs where name='{}';".format(name))
        cnxn.commit()
        print("Lab deleted")
    cnxn.close()
    return
start=1
while(start):
    print("ACEM Scheduling System")
    print("1. Classes")
    print("2. Teachers")
    print("3. Labs")
    act=int(input("Enter action: "))
    if act==1:
        classesui()
    elif act==2:
        teachersui()
    elif act==3:
        labsui()
    else:
        start=0