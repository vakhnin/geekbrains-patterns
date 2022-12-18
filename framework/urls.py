from framework.views import IndexView, AboutView, ContactsView, CategoryView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/category/': CategoryView(),
    '/contacts/': ContactsView(),
}
