from framework.templator import render
from patterns.behavioral_patterns import EmailNotifier, SmsNotifier
from patterns.structural_patterns import AppRoute
from patterns.сreational_patterns import Engine, Logger

site = Engine()
logger = Logger('views')

email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()

routes = {}


class Page404View:
    def __call__(self, request):
        logger.log('Страница не найдена')
        return '404 Not found', '404 Not found'


@AppRoute(routes=routes, url='/')
class IndexView:
    template = 'index.html'

    def __call__(self, request):
        logger.log('Главная страница')
        return '200 OK', render(self.template)


@AppRoute(routes=routes, url='/category/')
class CategoryView:
    template = 'category.html'

    def __call__(self, request):
        logger.log('Категории')
        if request['method'] == 'POST':
            data = request['data']
            if 'name' in data.keys():
                name = data['name'][0]

                new_category = site.create_category(name)
                site.categories.append(new_category)
        return '200 OK', render(self.template, categories=site.categories)


@AppRoute(routes=routes, url='/course/')
class CourseView:
    template = 'course.html'

    def __call__(self, request):
        logger.log('Курсы')
        if request['method'] == 'POST':
            data = request['data']
            if 'name' in data.keys() \
                    and 'category_id' in data.keys():
                name = data['name'][0]
                category_id = data['category_id'][0]

                new_course = site.create_course(name, category_id)
                site.courses.append(new_course)

                new_course.observers.append(email_notifier)
                new_course.observers.append(sms_notifier)

        courses = site.courses
        for course in courses:
            category = site.category_by_id(course.category)
            if category:
                course.category_name = category.name
        return '200 OK', render(self.template,
                                categories=site.categories, courses=courses)


@AppRoute(routes=routes, url='/students/')
class StudentView:
    template = 'students.html'

    def __call__(self, request):
        logger.log('Студенты')
        if request['method'] == 'POST':
            data = request['data']
            if 'name' in data.keys():
                name = data['name'][0]

                new_student = site.create_user('student', name)
                site.students.append(new_student)
        return '200 OK', render(self.template, students=site.students)


@AppRoute(routes=routes, url='/enrollments/')
class EnrollmentView:
    template = 'enrollment.html'

    def __call__(self, request):
        logger.log('Записи на курс')
        if request['method'] == 'POST':
            data = request['data']
            if 'student_id' in data.keys() and 'course_id' in data.keys():
                student_id = data['student_id'][0]
                course_id = data['course_id'][0]

                student = site.student_by_id(student_id)
                course = site.course_by_id(course_id)
                course.add_student(student)
        return '200 OK', render(self.template, students=site.students,
                                courses=site.courses,
                                enrollments=site.get_students_enrollments())


@AppRoute(routes=routes, url='/about/')
class AboutView:
    template = 'about.html'

    def __call__(self, request):
        logger.log('Страница About')
        return '200 OK', render(self.template)


@AppRoute(routes=routes, url='/contacts/')
class ContactsView:
    template = 'contacts.html'

    def __call__(self, request):
        logger.log('Страница контакты')
        return '200 OK', render(self.template)
