from .command import Command


class Executor:
    """Executor class"""

    def __init__(self, command: Command):
        self.command = command
        self.response = self.findresponse()
    
    def joke(self):
        """Returns a joke from some-random-api.ml"""

        request = requests.get("https://some-random-api.ml/joke")
        _resp = request.json()
        return _resp['joke']

    def findresponse(self):
        """Finds suitable response for the command using RegEx"""
        
        if self.command.command == "joke":
            return self.joke()