"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
"""

import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not all(map(lambda val: val.istitle(), value.split())):
            raise ValueError(f"ФИО должно начинаться с заглавной буквы!")
        if not all(map(lambda val: val.isalpha(), value.split())):
            raise ValueError(f"ФИО не должно содержать символы, кроме букв")
        setattr(instance, self.param_name, value)


class Student:
    name = NameValidator()

    def __init__(self, name):
        self.name = name
        self.subject_grades = {}
        self.subject_tests = {}
        self.subj = []

        with open('subject.csv', 'r', encoding='utf8') as csv_file:
            subjects = csv.reader(csv_file, delimiter="\n")
            for item in subjects:
                self.subject_grades[item[0]] = []
                self.subject_tests[item[0]] = []
                self.subj.append(''.join(item))

    def add_score(self, score, subject):
        if subject not in self.subj:
            raise ValueError("Такого предмета нет в списке")
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subject_grades[subject].append(score)

    def add_test_result(self, result, subject):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subject_tests[subject].append(result)

    def average_score_student(self):
        subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        if not subject_scores:
            return 0
        return sum(subject_scores) / len(subject_scores)

    def subject_test_average(self, subject):
        if not len(self.subject_tests[subject]):
            res = 0
        else:
            res = sum(self.subject_tests[subject]) / len(self.subject_tests[subject])
        return f'Ученик: {self.name}, Предмет: {subject}, Средний балл по тестам: {res:.2f}'

    def subject_score_average(self, subject):
        if not len(self.subject_grades[subject]):
            res = 0
        else:
            res = sum(self.subject_grades[subject]) / len(self.subject_grades[subject])
        return f'Ученик: {self.name}, Предмет: {subject}, Средний балл: {res:.2f}'

    def all_score_average(self):
        subject_scores = []
        count = 0
        # subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        # subject_scores.append([score for score in self.subject_grades.values() if score != []])
        for score in self.subject_grades.values():
            if score:
                for el in score:
                    subject_scores.append(el)
                    count += 1
        if not subject_scores:
            return 0
        return f'Ученик: {self.name}, Общий средний балл по предметам: {sum(subject_scores) / count:.2f}'

    def all_test_average(self):
        tests_scores = []
        count = 0
        for score in self.subject_tests.values():
            if score:
                for el in score:
                    tests_scores.append(el)
                    count += 1
        if not tests_scores:
            return 0
        return f'Ученик: {self.name}, Общий средний балл тестов: {sum(tests_scores) / count:.2f}'

    def save_data_student(self):
        dct = {}
        for subject in self.subj:
            grades = self.subject_grades[subject]
            test = self.subject_tests[subject]
            dct[subject] = f'grades:{grades}', f'test:{test}'
        with open(f'{self.name}.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(dct.keys())
            writer.writerow(dct.values())


# student = Student("Захаров Игорь П1235")    # невалидные ФИО - цифры
# student = Student("Захаров игорь Петрович")   # невалидные ФИО - строчная буква

student1 = Student("Иванов Иван Петрович")
# student1.add_score(7, 'Математика')   # невалидные баллы по предмету
# student1.add_score(5, 'Ботаника')   # невалидный предмет
student1.add_score(5, 'Математика')
student1.add_score(4, 'Математика')
student1.add_score(5, 'Математика')
student1.add_score(5, 'Руcский язык')
student1.add_score(5, 'Руcский язык')
student1.add_score(3, 'Руcский язык')
student1.add_score(5, 'Английский язык')
student1.add_score(4, 'Химия')
student1.add_test_result(80, 'Математика')
student1.add_test_result(90, 'Руcский язык')
student1.add_test_result(50, 'Руcский язык')
student1.add_test_result(70, 'Английский язык')
student1.add_test_result(85, 'Химия')
# student1.add_test_result(105, 'Химия')  # невалидные баллы по тесту


print(student1.subject_score_average('Математика'))
print(student1.subject_test_average('Руcский язык'))
print(student1.all_score_average())
print(student1.all_test_average())

student2 = Student("Сидоров Петр Иванович")

student2.add_score(4, 'Химия')
student2.add_score(5, 'Руcский язык')
student2.add_score(5, 'Химия')
student2.add_score(4, 'Математика')
student2.add_score(5, 'Математика')
student2.add_score(5, 'Физика')
student2.add_score(5, 'Физика')
student2.add_score(3, 'Руcский язык')
student2.add_score(4, 'Химия')
student2.add_score(4, 'Английский язык')
student2.add_test_result(80, 'Химия')
student2.add_test_result(90, 'Физика')
student2.add_test_result(85, 'Руcский язык')
student2.add_test_result(75, 'Физика')
student2.add_test_result(85, 'Математика')
student2.add_test_result(95, 'Химия')

print(student2.subject_score_average('Химия'))
print(student2.subject_test_average('Английский язык'))
print(student2.all_score_average())
print(student2.all_test_average())

student2.save_data_student()  # сохранение данных по студенту
