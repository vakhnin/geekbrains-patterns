from sqlite3 import connect

from patterns.architectural_system_pattern_unit_of_work import DomainObject
from patterns.behavioral_patterns import Subject


class User:
    def __init__(self, name):
        super().__init__()
        self.name = name


class Teacher(User):
    def __init__(self):
        super().__init__()


class Student(User, DomainObject):
    auto_id = 0

    def __init__(self, name):
        super().__init__(name)
        self.id = Student.auto_id
        Student.auto_id += 1
        self.courses = []

    def __repr__(self):
        return f'<Student: {self.id} - id, "{self.name}" - name>'


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class Category:
    auto_id = 0

    def __init__(self, name):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name

    def __repr__(self):
        return f'<Category: {self.id} - id, "{self.name}" - name>'


class Course(Subject):
    auto_id = 0

    def __init__(self, name, category_id):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.name = name
        self.category = category_id
        self.students = []
        super().__init__()

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)
        self.notify()

    def __repr__(self):
        return f'<Course: {self.id} - id, "{self.name}" - name, ' \
               f'{self.category} - category_id>'


class Engine:
    def __init__(self):
        self.categories = []
        self.courses = []
        self.students = []

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create(type_, name)

    @staticmethod
    def create_category(name):
        return Category(name)

    @staticmethod
    def create_course(name, category_id):
        return Course(name, category_id)

    def category_by_id(self, id):
        for item in self.categories:
            if int(item.id) == int(id):
                return item
        return None

    def course_by_id(self, id):
        for item in self.courses:
            if int(item.id) == int(id):
                return item
        return None

    def student_by_id(self, id):
        for item in self.students:
            if int(item.id) == int(id):
                return item
        return None

    def get_students_enrollments(self):
        enrollments = []
        for student in self.students:
            for course in student.courses:
                enrollments.append({
                    'student_name': student.name,
                    'course_name': course.name,
                })
        return enrollments


class SingletonByName(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('Log:', text)


class StudentMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tablename = 'student'

    def all(self):
        statement = f'SELECT * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            student = Student(name)
            student.id = id
            result.append(student)
        return result

    def insert(self, obj):
        statement = f"INSERT INTO {self.tablename} (name) VALUES (?)"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)


connection = connect('patterns.sqlite')


class MapperRegistry:
    mappers = {
        'student': StudentMapper,
    }

    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Student):
            return StudentMapper(connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')
