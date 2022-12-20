from framework.views import IndexView, AboutView, ContactsView, CategoryView, CourseView, StudentView, EnrollmentView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/category/': CategoryView(),
    '/course/': CourseView(),
    '/students/': StudentView(),
    '/enrollments/': EnrollmentView(),
    '/contacts/': ContactsView(),
}
