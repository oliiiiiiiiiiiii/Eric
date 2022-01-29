import re

class Command:
    """Command class"""

    def __init__(self, text: str):
        self.text = text
        self.command = self.returncommand()
    
    def returncommand(self):
        """Finds what the inputted command wants (for example if i said "tell me a joke" this will return "joke")"""

        if bool(re.match("(?:please |)(?:could you |)tell me (?:a |)joke"), self.command, flags = re.IGNORECASE):
            return "joke"
