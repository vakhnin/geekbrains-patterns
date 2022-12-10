from framework.templator import render


class Page404View:
    def __call__(self, request):
        return '404 Not found', '404 Not found'


class IndexView:
    template = 'index.html'
    title = 'Главная'

    def __call__(self, request):
        request['title'] = self.title
        return '200 OK', render(self.template, title=self.title)


class AboutView:
    template = 'about.html'
    title = 'About'

    def __call__(self, request):
        return '200 OK', render(self.template, title=self.title)
