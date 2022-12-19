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
        self.id = Category.auto_id
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
