from framework.urls import urlpatterns
from framework.views import Page404View


class Framework:
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # проверяем наличие слеша в конце URL
        if not path.endswith('/'):
            path += '/'

        if path in urlpatterns.keys():
            view = urlpatterns[path]
        else:
            view = Page404View()
        code, answer = view()

        start_response(code, [('Content-Type', 'text/html')])
        return [answer.encode('utf-8')]
