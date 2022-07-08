#  Dumkele Osegi Psid 1894081

major_gpa = input('Enter major and GPA ') #  Prompt user for major and gpa


def isfloat(num):  #  checking if the string can be converted into a number
    try:
        float(num)
        return True
    except ValueError:
        return False


def read(major_gpa):
    with open(major_gpa, 'r') as f:
        major_fname = f.readlines()
        major_list = []
        for i in major_fname:                            #  reading the major and gpa
            i = i.strip()
            major_mane.append(i.split(','))
        return major_list


student_majors = read('StudentsMajorsList.csv')

                                                             # reading the csv file input
gpalist = read('GPAList.csv')


gdates = read('GraduationDatesList.csv')


querylist = []


tgpa = major_gpa.split()


for i in tgpa:
    if isfloat(i):

        querylist.append(float(i))                          # if statement to check if gpa is a number and within query

for i in range(len(student_majors)):        # checking if major is listed in the files
    if student_majors[0][i] == 'major':

        majorlput = i

        break

for i in range(len(gpalist)):     # checking if gpa is in same length of allowed queries

    if gpalist[0][i] == 'GPA':

        gpamist = i

        break

major_fname = []

for j in range(1, len(student_majors)):

    if student_majors[j][majorlput] in major_gpa and (gpalist[j][gpamist] in major_gpa
                                              or (str((querylist[0]*0.1)+querylist[0])) in major_gpa):
        #  if statement to check if students are within .1 gpa

        space = ''

        for i in student_majors[j]:

            space += str(i)+','

        major_fname.append(space+str(gpalist[j][gpamist]))

        break
major_mane = []

for j in range(1, len(student_majors)):
    if student_majors[j][majorlput] in major_gpa and (gpalist[j][gpamist] in major_gpa or
                                                      (str((querylist[0]*0.25) + querylist[0])) in major_gpa):
        #  if statement to check if they are within gpa for scholarship

        space = ''

        for i in student_majors[j]:

            space += str(i)+','

        major_mane.append(space + str(gpalist[j][gpamist]))
        break

nlist = []


vlist = []

for j in range(1, len(gpalist)):
    vlist.append(float(gpalist[j][gpamist]) - querylist[0])

vlist.sort()

for j in range(1, len(student_majors)):

    if student_majors[j][majorlput] in major_gpa and vlist[0] == (float(gpalist[j][gpamist])-querylist[0]):
        space = ''
        for i in student_majors[j]:
            space += str(i)+','
        nlist.append(space + str(gpalist[j][gpamist]))
        break

if len(major_fname) == 0:  # if all of the query was discarded

    print('No Such Student')

if len(major_fname) > 0:    # statement to print students after input is valid for all criteria

    print('Your Students: ')

    for i in major_fname:

        print(i)

if len(major_mane) > 0:

    print('You may, also, consider: ')

    for i in major_mane:

        print(i)

if len(major_mane) == 0 and len(major_fname) == 0:

    print('Student with closer GPA ')

    for i in nlist:

        print(i)
