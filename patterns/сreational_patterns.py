class User:
    def __init__(self, name):
        super().__init__()
        self.name = name


class Teacher(User):
    def __init__(self):
        super().__init__()


class Student(User):
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


class Course:
    auto_id = 0

    def __init__(self, name, category_id):
        self.id = Course.auto_id
        Course.auto_id += 1
        self.name = name
        self.category = category_id

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
