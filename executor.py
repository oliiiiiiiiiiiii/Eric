from command import Command
import requests

class Executor:
    """Executor class"""

    def __init__(self, command: Command):
        self.command = command

        # Find the suitable response
        self.response = self.findresponse()
    
    def joke(self):
        """Returns a joke from some-random-api.ml"""
        
        # Make a response
        request = requests.get("https://some-random-api.ml/joke")
        _resp = request.json()
        # Return the joke
        return _resp['joke']
    
    # More functions for more responses here

    def findresponse(self):
        """Finds suitable response for the command using RegEx"""
        
        # Check if the command is wanting a joke
        if self.command.command == "joke":

            # Return a joke
            return self.joke()
        
        elif self.command.command == "unknown":
            return "Unknown command"