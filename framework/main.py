from urllib import parse

from framework.requests import PostRequests
from framework.urls import urlpatterns
from framework.views import Page404View


class Framework:
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # проверяем наличие слеша в конце URL
        if not path.endswith('/'):
            path += '/'

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'GET':
            request_params = parse.parse_qs(environ['QUERY_STRING'])
            request['request_params'] = request_params
            print(f'GET запрос: {request_params}')
        if method == 'POST':
            data = PostRequests().get_data_from_POST_query(environ)
            request_params = parse.parse_qs(data)
            request['request_params'] = request_params
            print(f'POST запрос: {request_params}')

        if path in urlpatterns.keys():
            view = urlpatterns[path]
        else:
            view = Page404View()
        code, answer = view(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [answer.encode('utf-8')]
