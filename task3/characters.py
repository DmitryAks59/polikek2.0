class Character:
    name = None
    role = None
    description = None

    def __init__(self, name=str):
        self.name = name

    def __call__(self, name=str, role=str, description=str):
        self.name = name
        self.role = role
        self.description = description
        return (self, name, role, description)      

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Роль: {self.role}\n' \
               f'Описание: {self.description}\n'

    def set_description(self, description=str):
        self.description = description

    def set_role(self, role=('main', 'supporting', 'episodic ', 'static')):
        self.role = role