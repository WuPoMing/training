class Student(object):
    def __init__(self, name):
        self.name, self.grades = name, []
    def append_grade(self, grade):
        self.grades.append(grade)
    def average(self):
        return sum(self.grades) / len(self.grades)
    def letter_grade(self):
        average = self.average()
        for value, grade in (90, "A"), (80, "B"), (70, "C"), (60, "D"):
            if average >= value:
                return grade
        else:
            return "F"

def print_report(a_class):
    print()
    print('班級清單')
    print()
    for student in sorted(a_class, key=lambda s: s.name):
        print('學生: {:10s} 成績:{} 平均成績: {:3.2f}  等第: {}'.format(
            student.name, student.grades, student.average(), student.letter_grade()))
    print()
    print('班級平均成績 {:.2f}'.format(class_average(a_class)))

def class_average(a_class):
    return sum(student.average() for student in a_class) / len(a_class)

print('班上學生考試資訊:')
a_class = []  
while True:
    print()
    print('學生人數{}人'.format(len(a_class)))
    another_student = input('輸入新的學生資料 (y/n) ? ')
    if another_student[0].lower() != 'y':
        break
    print()
    student_name = input('輸入學生姓名: ')
    a_class.append(Student(student_name))
    print()
    print('學生:', student_name)
    print('-------------------')
    number_of_tests = int(input('考試科目有幾科? : '))
    for test_num in range(1, number_of_tests+1):
        print('科目 {} 分數'.format(test_num), end='')
        score = float(input(' : '))
        if score < 0:
            break
        a_class[-1].append_grade(score) 
print_report(a_class)
