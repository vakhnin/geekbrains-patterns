class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category


class Engine:
    def __init__(self):
        self.categories = []

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)
