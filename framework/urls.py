from framework.views import IndexView, AboutView

urlpatterns = {
    '/': IndexView(),
    '/about/': AboutView(),
}
