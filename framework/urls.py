from framework.views import IndexView, AboutView, ContactsView, CategoryView, CourseView, StudentView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/category/': CategoryView(),
    '/course/': CourseView(),
    '/students/': StudentView(),
    '/contacts/': ContactsView(),
}
