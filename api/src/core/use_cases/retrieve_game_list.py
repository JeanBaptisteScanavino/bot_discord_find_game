class RetrieveGameList():
    def __init__(self,dependencies):
        self.game_repository= dependencies
    
    def exec(self):
        return self.game_repository.retrieveAll()

