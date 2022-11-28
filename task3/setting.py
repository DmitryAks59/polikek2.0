class Setting:
    description = None

    def __init__(self, name=str):
        self.name = name

    def set_description(self, description=str):
        self.description = description


class Nature(Setting):
    type = 'Nature'
    pass


class Location(Setting):
    type = 'Location'
    pass


class Race(Setting):
    type = 'Race'
    pass


class Magic(Setting):
    type = 'Magic'
    pass

