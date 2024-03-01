
import random
classes ={'aiml':[['sub1','sub2','sub3','sub4'],['lab_sub3','lab_sub2']],
          'cse':[['sub1','sub2','sub5','sub4'],['lab_sub2','lab_sub5']],
          'ece':[['sub1','sub5','sub6'],['lab_sub0']]
        }

teachers = {'teacher1':[['sub1','aiml',3],['sub1','cse',3],['sub5','ece',3]],
          'teacher2':[['sub2','aiml',3],['sub2','cse',3],['sub1','ece',3],['lab_sub2','aiml',1],['lab_sub2','cse',1]],
          'teacher3':[['sub3','aiml',2],['lab_sub3','aiml',1],['lab_sub0','ece',1]],
          'teacher4':[['sub4','aiml',4],['sub4','cse',2]],
          'teacher5':[['sub5','cse',4,],['sub6','ece',3],['lab_sub5','cse',1]]	
        }

labs =['lab1','lab2','lab3','lab4']
class_tt={'aiml':[],'cse':[],'ece':[]}
teachers_tt={'teacher1':[],'teacher2':[],'teacher3':[],'teacher4':[],'teacher5':[]}
labs_tt={'lab1':[],'lab2':[],'lab3':[],'lab4':[]}

# Time Table Generator 
def T_T_G(classes_list):
    for clas in classes_list:
        # teachers_of_class = get_teachers(clas)
        assign_labs(clas)
        assign_lectures(clas)

# Making list of techers for a particular class
def get_teachers(clas):
    t=[]
    for teacher in teachers.keys():
        for lol in teachers[teacher]: #lol = list of list
            if(lol[1]==clas):
                t.append(teacher)
                break
    return t

# Scheduling labs for a class
def assign_labs(cls):
    # print("labs alloted "+cls)
    lab_sub= get_lab_sub(cls)
    lab_and_teachers =get_lab_and_teachers(cls)
    lec_for_labs=[[(1,56),(1,34)],[(2,34),(2,67)],[(4,56),(4,34)],[(5,34),(5,67)]]
    for selected_sub in lab_sub:
        num_of_labsub=len(lec_for_labs)
        for l in range(num_of_labsub):
            lecl = random.choice(lec_for_labs)
            lec=random.choice(lecl)
            teacher=lab_and_teachers[selected_sub]
            if(is_teacher_free(teacher,lec)):
                lab=get_lab(lec)
                update_tt('teachers_tt',teacher,lec)
                update_tt('labs_tt',lab,lec)
                update_tt('classes_tt',cls,lec)
                lec_for_labs.remove(lecl)
                print(lab+" "+selected_sub+
                    " alloted to ",lec , 
                    " for " + cls +
                    ' teacher '+teacher)
                break

# Getting list of labs for a class
def get_lab_sub(cls):
    return classes[cls][1]

def get_lab_and_teachers(cls):
    t={}
    for teacher in teachers.keys():
        for lol in teachers[teacher]: #lol = list of list
            if(lol[1]==cls and lol[0][:3]=='lab'):
                t[lol[0]]= teacher
                break
    return t

def is_teacher_free(teacher,lec):
    if(lec not in teachers_tt[teacher]):
        return True
    else:
        return False

def get_lab(lec):
    temp=labs
    for l in labs:
        lab=random.choice(temp)
        if (lec not in labs_tt[lab]):
            return lab
        else:
            temp.remove(lab)

def update_tt(tt,key,lec):
    if(tt=='teachers_tt'):
        teachers_tt[key].append(lec)
    elif(tt=='labs_tt'):
        labs_tt[key].append(lec)
    else:
        class_tt[key].append(lec)

def assign_lectures(cls):
    print("lectures alloted to "+cls)

# Calling the time table genrator with list of all class names
T_T_G(classes.keys())
print(teachers_tt)
print(labs_tt)
print(class_tt)