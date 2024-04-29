import random
classes ={'aiml':[['sub1','sub2','sub3','sub4'],['lab_sub3','lab_sub2']],
          'cse':[['sub1','sub2','sub5','sub4'],['lab_sub2','lab_sub5']],
          'ece':[['sub1','sub5','sub6'],['lab_sub0']]
        }

teachers = {'teacher1':[['sub1','aiml',3],['sub1','cse',3],['sub5','ece',3]],
          'teacher2':[['sub2','aiml',3],['sub2','cse',2],['sub1','ece',3],['lab_sub2','aiml',1],['lab_sub2','cse',1]],
          'teacher3':[['sub3','aiml',2],['lab_sub3','aiml',1],['lab_sub0','ece',1]],
          'teacher4':[['sub4','aiml',4],['sub4','cse',2]],
          'teacher5':[['sub5','cse',4,],['sub6','ece',3],['lab_sub5','cse',1]]  
        }
def basic_structure():
    tt=[["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
    return tt
ctt={'aiml':[x for x in basic_structure()],'cse':[x for x in basic_structure()],'ece':[x for x in basic_structure()]}
ttt={'teacher1':[x for x in basic_structure()],'teacher2':[x for x in basic_structure()],'teacher3':[x for x in basic_structure()],'teacher4':[x for x in basic_structure()],
     'teacher5':[x for x in basic_structure()]}

labs =['lab1','lab2','lab3','lab4']
class_tt={'aiml':[],'cse':[],'ece':[]}
teachers_tt={'teacher1':[],'teacher2':[],'teacher3':[],'teacher4':[],'teacher5':[]}
labs_tt={'lab1':[],'lab2':[],'lab3':[],'lab4':[]}

# Time Table Generator 
def T_T_G(classes_list):
    for clas in classes_list:
        # teachers_of_class = get_teachers(clas)
        print(clas)
        assign_labs(clas)
        assign_lectures(clas)
        print("")

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
    lab_sub= get_sub(cls,1)
    lab_and_teachers =get_data(cls,1)
    lec_for_labs=[(1,5,6),(1,3,4),(2,3,4),(2,6,7),(4,5,6),(4,3,4),(5,3,4),(5,6,7)]#(day,lec1,lec2)
    for selected_sub in lab_sub:
        lecs=[x for x in lec_for_labs]
        num_of_lec=len(lec_for_labs)
        for l in range(num_of_lec):
            lec = random.choice(lecs)
            teacher=lab_and_teachers[selected_sub]
            if(is_teacher_free(teacher,lec,1)):
                lab=get_lab(lec)
                for i in range(2):
                    ttt[teacher][lec[0]-1][lec[i+1]-1]=(cls,selected_sub)
                    update_tt('teachers_tt',teacher,(lec[0],lec[i+1]))
                    update_tt('labs_tt',lab,(lec[0],lec[i+1]))
                    ctt[cls][lec[0]-1][lec[i+1]-1]=(selected_sub,teacher)
                    update_tt('classes_tt',cls,(lec[0],lec[i+1]))
                lec_for_labs.remove(lec)
                print((lec[0],lec[1])," and ",(lec[0],lec[2])," ",selected_sub," ",teacher," ",lab)
                break
            else:
                lecs.remove(lec)

# Getting list of labs for a class
def get_sub(cls,lab):
    cc=[i for i in classes[cls][lab]]
    return cc

def get_data(cls,lab):
    t={}
    if(lab):
        for teacher in teachers.keys():
            for lol in teachers[teacher]: #lol = list of list
                if(lol[1]==cls and lol[0][:3]=='lab'):
                    t[lol[0]]= teacher
                    break
    else:
        for teacher in teachers.keys():
            for lol in teachers[teacher]:
                if(lol[1]==cls and lol[0][:3]!='lab'):
                    t[lol[0]]=[teacher,lol[2]]
    return t

def is_teacher_free(teacher,lec,lab):
    if(lab):
        if((lec[0],lec[1]) not in teachers_tt[teacher] and (lec[0],lec[2]) not in teachers_tt[teacher]):
            return True
        else:
            return False
    else:
        if(lec not in teachers_tt[teacher]):
            if(lec[1]==1 or lec[1]==2):
                return True
            elif((lec[0],lec[1]-1) not in teachers_tt[teacher] and (lec[0],lec[1]-2) not in teachers_tt[teacher]):
                return True
            else:
                return False
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
  
  cls_sub= get_sub(cls,0)   # get subjects data of class
  sub_data=get_data(cls,0)
  days=[1,2,3,4,5]# make list of weekdays
  sub_left=get_sub(cls,0) #prepare list of subjects to be scheduled
  while(len(sub_left)):# while(sum of lectures needed in subjects dat )
    day=random.choice(days)#     choose any day from weekdays 
    for lec in range(1,8):#         for each lecture
        if( (day,lec) not in class_tt[cls]):#             if lecure free:
            subjects= [i for i in sub_left]#                 make copy of subject list
            num=len(subjects)
            for n in range(num):#                 for range(num of subjects):
                subject=random.choice(subjects)#                     select random subject from copy list
                if(is_teacher_free(sub_data[subject][0],(day,lec),0)):# if (teacher available for lecture):
                    ttt[sub_data[subject][0]][day-1][lec-1]=(cls,subject)
                    update_tt('teachers_tt',sub_data[subject][0],(day,lec))#   update teacher tt 
                    ctt[cls][day-1][lec-1]=(subject,sub_data[subject][0])
                    update_tt('classes_tt',cls,(day,lec))#                         update clas tt
                    sub_data[subject][1]-=1#                         dec num of lec for subject in subject data 
                    sub_left.remove(subject)#                         remove subject from list of subjects for today
                    print((day,lec)," ",subject," ",sub_data[subject][0]," ")
                    break#                         break
                else:#                     else:
                    subjects.remove(subject)#                         remove subject from copy
    sub_left=[s for s in cls_sub if sub_data[s][1]>0] #update list of subjects left
    days.remove(day)#     remove day from weekdays
    if( len(days)==0 and len(sub_left)!=0): # insufficient space
        print("Exhausted !!!!!! no space left with \n",sub_left)
        break
# Calling the time table genrator with list of all class names
T_T_G(classes.keys())
for cls in classes.keys():
    print(cls)
    for r in ctt[cls]:
        print(r)
for cls in teachers.keys():
    print(cls)
    for r in ttt[cls]:
        print(r)
# for cls in classes.keys():
#     print(r for r in ctt[cls])
# for teacher in teachers.keys():
#     for r in ttt[teacher]:
#         print(r)
# print(ttt['teacher1'])