from framework.templator import render


class Page404View:
    def __call__(self, request):
        return '404 Not found', '404 Not found'


class IndexView:
    template = 'index.html'

    def __call__(self, request):
        return '200 OK', render(self.template)


class CategoryView:
    template = 'category.html'

    def __call__(self, request):
        return '200 OK', render(self.template)


class AboutView:
    template = 'about.html'

    def __call__(self, request):
        return '200 OK', render(self.template)


class ContactsView:
    template = 'contacts.html'

    def __call__(self, request):
        return '200 OK', render(self.template)
