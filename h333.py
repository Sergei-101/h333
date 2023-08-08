# Урок 12. ООП. Финал
#
# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
class ExaminationName:
    """Проверка правильности ввода ФИО. Имена должны быть только буквами и начинаться с заглавных."""

    def __set_name__(self, owner, name):
        """Установить имя проверяемого атрибута."""
        self.param_name = name

    def __get__(self, instance, owner):
        """Вернуть значение атрибута."""
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        """Установить значение атрибута."""
        if not value.isalpha() or not value.istitle():
            raise ValueError("Неверные данные для ФИО!")
        instance.__dict__[self.param_name] = value

class CheckingTheMarks:
    """Класс-дескриптор для проверки выставленных оценок."""

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        """Сохранить имя параметра."""
        self.param_name = name

    def __set__(self, instance, value):
        """Установка значения атрибута."""
        self._validate(value)
        instance.__dict__[self.param_name] = value
        # setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        """Получить значение атрибута"""
        return instance.__dict__[self.param_name]
        # getattr(instance, self.param_name)

    def _validate(self, value):
        """Валидация полученного значения."""
        if not isinstance(value, int):
            raise TypeError("Неверный тип для оценки!")
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{value} вне диапазона [{self.min_value}, {self.max_value}]")

class Student:
    """Класс студент."""

    VALUATION_LIMIT_SUBJECT_MIN = 2
    VALUATION_LIMIT_SUBJECT_MAX = 5
    VALUATION_LIMIT_TEST_MIN = 0
    VALUATION_LIMIT_TEST_MAX = 100
    family = ExaminationName()
    name = ExaminationName()
    second_name = ExaminationName()
    subject_grade = CheckingTheMarks(VALUATION_LIMIT_SUBJECT_MIN, VALUATION_LIMIT_SUBJECT_MAX)
    test_grade = CheckingTheMarks(VALUATION_LIMIT_TEST_MIN, VALUATION_LIMIT_TEST_MAX)

    def __init__(self, family: str, name: str, second_name: str):
        """Инициализация экземпляра."""
        self.family = family
        self.name = name
        self.second_name = second_name
        self.progress_student = {}


    def __str__(self):
        """Вывод информации для пользователя"""
        return f"{self.family} {self.name} {self.second_name}"

    def __repr__(self):
        """Вывод информации для программиста"""
        return f"{self.family} {self.name} {self.second_name}"

    def give_marks(self, subject:str, subject_grade:int, test_grade:int, file:str="work.csv"):
        """Вводим предмет и оценки"""
        with open(file, "r", encoding="UTF 8") as f:
            names = f.readlines()
            for i in names:
               test = i.split(",")
            for j in test:
                if subject in j:
                    self.progress_student[subject] = subject_grade, test_grade


    def сheck_progress(self):
        """Выводим прогресс обуения"""
        average_score_subject = []
        average_score_test = []
        for i in self.progress_student.values():
            average_score_subject.append(i[0])
            average_score_test.append(i[1])
        if len(average_score_test) >= 1 and len(average_score_subject) >= 1:
            average_score_subject = sum(average_score_subject)/len(average_score_subject)
            average_score_test = sum(average_score_test) / len(average_score_test)
            print(f"{self.family} {self.name} {self.second_name} Средняя оценка по предметам {average_score_subject}"
                  f", Средняя оценка по тестам {average_score_test}")
        else:
            print(f"У {self.family} {self.name} {self.second_name}а Нет оценок по предметам")

    def сheck_progress_subject(self):
        print(f"{self.family} {self.name} {self.second_name}")

        for key, value in self.progress_student.items():
            print(f"{key}, предм. - {value[0]}, тест - {value[1]}")




student_1 = Student('Сидоров', 'Андрей', 'Михайлович')
student_2 = Student('Петров', 'Иван', 'Михайлович')
student_3 = Student('Соболяко', 'Мария', 'Михайловна')
student_4 = Student('Сивец', 'Катерина', 'Петровна')
student_5 = Student('Кровоногова', 'Александра', 'Петровна')



student_1.give_marks("Математика", 7, 90)
student_1.give_marks("Физика", 3, 60)
student_1.give_marks("Химия", 5, 80)
student_1.give_marks("Английский", 8, 90)
student_1.give_marks("Физкультура", 5, 80)

student_1.сheck_progress()
student_2.сheck_progress()
student_1.сheck_progress_subject()