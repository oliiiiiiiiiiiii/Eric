import re

class Command:
    """Command class"""

    def __init__(self, text: str):
        self.text = text
        self.command = self.returncommand()
        
    
    def returncommand(self):
        """Finds what the inputted command wants (for example if i said "tell me a joke" this will return "joke")"""
        
        # Check if the command matches the joke regex
        # We use regex so that we can use as much probabilities as possible, for example here if i say "Please could you tell me a joke" this will match, or if i say "Could you tell me a joke" it will also match, or if i say "Tell me a joke" it would also match, this is better than putting many ifs and elifs
        if bool(re.match("((?:((?:please |)|(?:(could you |can you )|))(send|tell)(?:(?: me|) a|) |)joke(?:\?|)|make me laugh|i want (?:a |)joke(?: please|))", self.text, flags = re.IGNORECASE)):
            return "joke"
        
        else:
            return "unknown"
