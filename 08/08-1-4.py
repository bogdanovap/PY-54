def average(lst):
    if len(lst) > 0:
        return sum(lst) / len(lst)
    return 0


def get_average_hw_grade(students, course):
    res = 0
    count = 0
    for student in students:
        grades = student.grades.get(course, [])
        if grades:
            res += sum(grades)
            count += len(grades)
            # res += average(grades)
            # count += 1
    if count > 0:
        return res/count
    return res


def get_average_lector_grade(lectors, course):
    res = 0
    count = 0
    for lector in lectors:
        grades = lector.grades.get(course, [])
        if grades:
            res += sum(grades)
            count += len(grades)
            # res += average(grades)
            # count += 1
    if count > 0:
        return res/count
    return res


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def get_avg_grade(self):
        count = len(self.grades)
        if count == 0:
            return 0
        res = 0
        for course, grades in self.grades.items():
            res += average(grades)
        res /= count
        return res

    def courses_to_string(self, courses):
        if len(courses) == 0:
            return ""
        res = courses[0]
        for course in range(1, len(courses)):
            res += f", {courses[course]}"
        return res

    def rate_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Не лектор"
        if course not in lecturer.courses_attached:
            return "Нет курса у лектора"
        if not (course in self.courses_in_progress or course in self.finished_courses):
            return "Нет курса у студента"
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
        return "Оценка добавлена"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() == other.get_avg_grade()
        print("not Student")
        return

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_avg_grade() < other.get_avg_grade()
        print("not Student")
        return

    def __str__(self):
        res = f"Имя: {self.name}" \
              f"\nФамилия: {self.surname}" \
              f"\nСредняя оценка за домашние задания: {self.get_avg_grade():.2f}" \
              f"\nКурсы в процессе изучения: {self.courses_to_string(self.courses_in_progress)}" \
              f"\nЗавершенные курсы: {self.courses_to_string(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def get_avg_grade(self):
        count = len(self.grades)
        if count == 0:
            return 0
        res = 0
        for course, grades in self.grades.items():
            res += average(grades)
        res /= count
        return res

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() == other.get_avg_grade()
        print("not Lecturer")
        return

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_avg_grade() < other.get_avg_grade()
        print("not Lecturer")
        return

    def __str__(self):
        res = f"Имя: {self.name}" \
              f"\nФамилия: {self.surname}" \
              f"\nСредняя оценка за лекции: {self.get_avg_grade():.2f}"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}" \
              f"\nФамилия: {self.surname}"
        return res




# студенты
best_student = Student('Ruoy', 'Eman', 'male')
best_student.finished_courses += ['Intro to programming']
best_student.courses_in_progress += ['Python', 'Git']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

foo_student = Student('Foo', 'Bar', 'male')
foo_student.finished_courses += ['Intro to programming']
foo_student.courses_in_progress += ['Python', 'Git']
foo_student.grades['Git'] = [6, 8, 10, 5, 9]
foo_student.grades['Python'] = [6, 8]

# лекторы
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached = ["Git"]

foo_lecturer = Lecturer('Bar', 'Foo')
foo_lecturer.courses_attached = ["Python"]

# проверяльщики
foo_reviewer = Reviewer("mr.", "Foo")
bar_reviewer = Reviewer("mr.", "Bar")

# оценка лекторов
foo_student.rate_lecturer(cool_lecturer, "Git", 10)
foo_student.rate_lecturer(foo_lecturer, "Python", 7)
best_student.rate_lecturer(cool_lecturer, "Git", 8)
best_student.rate_lecturer(foo_lecturer, "Python", 6)
# print(foo_student.rate_lecturer(cool_lecturer, "Python", 10))
# print(foo_student.rate_lecturer(best_student, "Git", 10))

# оценка домашних работ
foo_reviewer.rate_hw(best_student, "Python", 6)
foo_reviewer.rate_hw(foo_student, "Python", 10)
foo_reviewer.rate_hw(best_student, "Git", 10)
foo_reviewer.rate_hw(foo_student, "Git", 6)



# вывод инфо о проверяльшиках
print(foo_reviewer)
print(bar_reviewer)
# вывод инфо о лекторах
print(cool_lecturer)
print(foo_lecturer)
# вывод инфо о студентах
print(best_student)
print(foo_student)
# сравнение стундентов
print(foo_student < best_student)
# сравнение лекторов
print(foo_lecturer < cool_lecturer)
#средняя оценка за домашнее задание студентов по предмету Git
print(get_average_hw_grade([foo_student, best_student], "Git"))
#средняя оценка лекторов по предмету Python
print(get_average_hw_grade([cool_lecturer, foo_lecturer], "Python"))