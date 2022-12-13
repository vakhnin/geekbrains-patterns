from framework.views import IndexView, AboutView, ContactsView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contacts/': ContactsView(),
}
