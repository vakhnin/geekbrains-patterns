from framework.views import IndexView, AboutView, ContactsView, CategoryView, CourseView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/category/': CategoryView(),
    '/course/': CourseView(),
    '/contacts/': ContactsView(),
}
