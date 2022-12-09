from urls import urlpatterns


class Framework:

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # проверяем наличие слеша в конце URL
        if not path.endswith('/'):
            path += '/'

        code = '200 Ok'
        if path in urlpatterns.keys():
            answer = urlpatterns[path]()
        else:
            code = '404 Not found'
            answer = '404 Not found'

        start_response(code, [('Content-Type', 'text/html')])
        return [answer.encode('utf-8')]
