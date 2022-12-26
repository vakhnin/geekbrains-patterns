class Observer:
    def update(self, subject):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        for item in self.observers:
            item.update(self)


class SmsNotifier(Observer):
    def update(self, subject):
        print(f'SMS: к нам присоединился {subject.students[-1].name}')


class EmailNotifier(Observer):
    def update(self, subject):
        print(f'EMAIL: к нам присоединился {subject.students[-1].name}')
