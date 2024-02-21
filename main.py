from openpyxl import Workbook
wb = Workbook()  # Create a new workbook
ws = wb.active  # Select the active worksheet

def get_initial_info():
    num_of_teachers=int(input("Enter No. of Teachers: "))
    teachers={}
    for i in range(num_of_teachers):
        lst=[]
        name=input("Teacher Name: ").capitalize()
        lst.append(int(input("No. of Lectures: ")))
        lst.append(input("Subjects:"))
        teachers[name]=lst
    return teachers

def create_teachers_xls(teachers_name,tt_stucture):
    for name in teachers_name:
        file_name = name+".xlsx"
        wb.create_sheet(file_name)  
        for row in tt_stucture:
            ws.append(row)
        wb.save(file_name)

def create_class_xls():
    print(" class working")

tt_stucture=[["","1st","2nd","3rd","4th","5th","6th","7th"],["Mon"],["Tues"],["Wed"],["Thurs"],["Fri"]]
# tc=get_initial_info()
# tc={'a':[6,'s1'],'b':[4,'s2']}
create_teachers_xls(tc.keys(),tt_stucture)
create_class_xls()

# generate_time_table(tc)