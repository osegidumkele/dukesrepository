#  Dumkele Osegi PSID 1893081
import csv
# importing csv module


class Student:  # creating a class for student to hold all the data required
    def __init__(self, student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.gpa = gpa
        self.graduation_date = graduation_date
        self.disciplinary_action = disciplinary_action


class Roster:  # creating class for roster of students
    def __init__(self):
        self.students = {}

    def add_student(self, student):  # defining a function for adding students
        self.students[student.student_id] = student

    def get_student(self, student_id):  # defining a function for finding a student
        return self.students[student_id]

    def get_students_by_major(self, major):  # function to find a student by major
        students_in_major = []  # creating a list
        for student_id in self.students:
            student = self.students[student_id]  # student_id = student

            if student.major == major:
                students_in_major.append(student)
        return students_in_major

    def get_all_students(self):  # function for pulling all students in file
        all_students = []  # creating a an array to hold studentw
        for student_id in self.students:
            student = self.students[student_id]
            all_students.append(student)  # update the list of students
        return all_students

    def get_students_by_gpa(self, gpa):  # function for students by gpa
        students_with_gpa = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.gpa == gpa:
                students_with_gpa.append(student)
        return students_with_gpa

    def get_students_by_graduation_date(self, graduation_date):  # function for grad datr
        students_by_graduation_date = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.graduation_date == graduation_date:
                students_by_graduation_date.append(student)
        return students_by_graduation_date

    def get_students_by_disciplinary_action(self, disciplinary_action):  # function for disciplinary action
        students_by_disciplinary_action = []
        for student_id in self.students:
            student = self.students[student_id]
            if student.disciplinary_action == disciplinary_action:
                students_by_disciplinary_action.append(student)
        return students_by_disciplinary_action


def main():
    roster = Roster()

    with open('StudentsMajorsList.csv') as csvfile:  #  filling csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = row['student_id']
            last_name = row['last_name']
            first_name = row['first_name']
            major = row['major']
            gpa = None
            graduation_date = None
            disciplinary_action = None
            student = Student(student_id, last_name, first_name, major, gpa, graduation_date, disciplinary_action)
            roster.add_student(student)

            with open('GPAList.csv') as csvfile:  #  updating gpalist file
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student_id = row['student_id']
                    gpa = row['GPA']
                    student = roster.get_student(student_id)
                    student.gpa = gpa

            with open('GraduationDatesList.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student_id = row['student_id']
                    graduation_date = row['graduation_date']
                    student = roster.get_student(student_id)
                    student.graduation_date = graduation_date
            with open('DisciplinaryActionList.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student_id = row['student_id']
                    disciplinary_action = row['disciplinary_action']
                    student = roster.get_student(student_id)
                    student.disciplinary_action = disciplinary_action

            with open('FullRoster.csv', mode='w') as csvfile:  #  updating full roster for students
                fieldnames = ['student_id', 'last_name', 'first_name', 'major', 'gpa', 'graduation_date',
                              'disciplinary_action']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                all_students = roster.get_all_students()
                for student in all_students:
                    row = {'student_id': student.student_id,
                           'last_name': student.last_name,
                           'first_name': student.first_name,
                           'major': student.major,
                           'gpa': student.gpa,
                           'graduation_date': student.graduation_date,
                           'disciplinary_action': student.disciplinary_action}
                    writer.writerow(row)
                majors = set()
                for student_id in roster.students:
                    student = roster.students[student_id]
                    majors.add(student.major)

                for major in majors:
                    students_in_major = roster.get_students_by_major(major)

                    file_name = major.replace(" ", "") + 'Students.csv'
                    with open(file_name, mode='w') as csvfile:
                        fieldnames = ['student_id', 'last_name', 'first_name', 'graduation_date', 'disciplinary_action']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        for student in students_in_major:
                            row = {'student_id': student.student_id,
                                   'last_name': student.last_name,
                                   'first_name': student.first_name,
                                   'graduation_date': student.graduation_date,
                                   'disciplinary_action': student.disciplinary_action}
                            writer.writerow(row)
                    with open('ScholarshipCandidates.csv', mode='w') as csvfile:
                        fieldnames = ['student_id', 'last_name', 'first_name', 'major', 'gpa']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()

                        for student_id in roster.students:  #  checking is students qualify for scholarship
                            student = roster.students[student_id]
                            if student.gpa >= 3.8 and student.graduation_date is None and\
                                    student.disciplinary_action is None:
                                row = {'student_id': student.student_id,
                                       'last_name': student.last_name,
                                       'first_name': student.first_name,
                                       'major': student.major,
                                       'gpa': student.gpa}
                                writer.writerow(row)
                    with open('DisciplinedStudents.csv', mode='w') as csvfile:  #  checking if any of the students have disc action
                        fieldnames = ['student_id', 'last_name', 'first_name', 'graduation_date']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()

                        for student_id in roster.students:
                            student = roster.students[student_id]
                            if student.disciplinary_action == 'Y':
                                row = {'student_id': student.student_id,
                                       'last_name': student.last_name,
                                       'first_name': student.first_name,
                                       'graduation_date': student.graduation_date}
                                writer.writerow(row)


main()

