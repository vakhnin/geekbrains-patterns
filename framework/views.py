class Page404View:
    def __call__(self):
        return '404 Not found', '404 Not found'


class IndexView:
    def __call__(self):
        return '200 OK', 'Index page'


class AboutView:
    def __call__(self):
        return '200 OK', 'About page'
