from framework.templator import render
from patterns.сreational_patterns import Engine, Logger

site = Engine()
logger = Logger('views')


class Page404View:
    def __call__(self, request):
        logger.log('Страница не найдена')
        return '404 Not found', '404 Not found'


class IndexView:
    template = 'index.html'

    def __call__(self, request):
        logger.log('Главная страница')
        return '200 OK', render(self.template)


class CategoryView:
    template = 'category.html'

    def __call__(self, request):
        logger.log('Категории')
        if request['method'] == 'POST':
            data = request['data']
            name = data['name'][0]

            new_category = site.create_category(name)

            site.categories.append(new_category)
        return '200 OK', render(self.template, categories=site.categories)


class AboutView:
    template = 'about.html'

    def __call__(self, request):
        logger.log('Страница About')
        return '200 OK', render(self.template)


class ContactsView:
    template = 'contacts.html'

    def __call__(self, request):
        logger.log('Страница контакты')
        return '200 OK', render(self.template)
