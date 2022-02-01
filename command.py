import re

class Command:
    """Command class"""

    def __init__(self, text: str):
        self.text = text
        self.command = self.returncommand()
    
    def returncommand(self):
        """Finds what the inputted command wants (for example if i said "tell me a joke" this will return "joke")"""
        
        # Check if the command matches any regex

        addToList = re.match("((?:please |)(?:(could you |can you )|)add (?P<item>(\w\s?)+) to (?:my |)(?P<listname>\w+) list(?: please|)(?:\?|)|what( is|(?:'|)s) inside(?: (the|my)|) (?P<listname2>\w+) list)", self.text, flags = re.IGNORECASE)

        getListMatch = re.match("(what does (?:the |)list (?P<listname>\w+) (have|contain)(?:\?|)|what does (?:the |)(?P<listname2>\w.+) list (have|contain)(?:\?|))", self.text, flags = re.IGNORECASE)

        jokeMatch = re.match("((?:((?:please |)|(?:(could you |can you )|))(send|tell)(?:(?: me|) a|) |)joke(?:\?|)|make me laugh|i want (?:a |)joke(?: please|))", self.text, flags = re.IGNORECASE)
        
        removeFromList = re.match("(?:please |)(?:(could you |can you )|)(?:please |)remove (?P<item>(\w+\s?)+) from (list (?P<listname>(\w\s?)+)|(?P<listname2>\w+))(?: please|)(?:\?|)", self.text, flags = re.IGNORECASE)
        if bool(jokeMatch):
            return "joke"
        elif bool(getListMatch):
            # Returns <getlist <listname>>
            # Will return list elements

            return f"getlist {getListMatch.groupdict()['listname'] or getListMatch.groupdict()['listname2']}"
        elif bool(addToList):
            # Returns <addToList <item> <listname>>
            # Will append to a list
            
            return f"addtolist item: {addToList.groupdict()['item']} list: {addToList.groupdict()['listname']}"
        elif bool(removeFromList):
          a=f"removefromlist item: {removeFromList.groupdict()['item']} list: {removeFromList.groupdict()['listname'] or removeFromList.groupdict()['listname2']}"
          return a
        else:
            return "AI"
