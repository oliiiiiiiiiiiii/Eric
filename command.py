import re

class Command:
    """Command class"""

    def __init__(self, text: str):
        self.text = text
        self.command = self.returncommand()
        self.addToList = re.match("(?:(could you |can you )|)(?:please |)add (?P<item>\w.+) to (?P<listname>\w.+) list(?: please|)", self.text, flags = re.IGNORECASE)
        self.getListMatch = re.match("(what does (?:the |)list (?P<listname>\w.+) (have|contain)|what does (?P<listname2>\w.+) list (have|contain))", self.text, flags = re.IGNORECASE)
        self.jokeMatch = re.match("((?:((?:please |)|(?:(could you |can you )|))(send|tell)(?:(?: me|) a|) |)joke(?:\?|)|make me laugh|i want (?:a |)joke(?: please|))", self.text, flags = re.IGNORECASE)
    
    def returncommand(self):
        """Finds what the inputted command wants (for example if i said "tell me a joke" this will return "joke")"""
        
        # Check if the command matches the joke regex
        # We use regex so that we can use as much probabilities as possible, for example here if i say "Please could you tell me a joke" this will match, or if i say "Could you tell me a joke" it will also match, or if i say "Tell me a joke" it would also match, this is better than putting many ifs and elifs
        if bool(self.jokeMatch):
            return "joke"
        elif bool(self.getListMatch):
            # Returns <getlist <listname>>
            # Will return list elements
            return f"getlist {self.getListMatch.groupdict()['listname'] or self.getListMatch.groupdict()['listname2']}"
        elif bool(self.addToList):
            # Returns <addToList <item> <listname>>
            # Will append to a list
            return f"addtolist {self.addToList.groupdict()['item']} {self.addToList.groupdict()['listname']}"
        else:
            return "unknown"
