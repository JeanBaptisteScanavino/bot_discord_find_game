class InMemoryGamesRepository():
    def __init__(self):
        self.list = ['Mario', 'Sonic', 'Alex Kidd']
    
    def retrieveAll(self):
        return self.list