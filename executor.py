from command import Command
import os
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
    
    def add2list(self, item, listname):
        """Adds an item to list"""

        lists = os.listdir()
        listslist = []
        for i in lists:
            if i.endswith("_list.txt"):
                listslist.append(i.strip("_list.txt"))
        with open(f"{listname}_list.txt", "a+") as f:
            f.write(f"{item}, ")
        return f"Added {item} to {listname} list"

    def getlist(self, listname):

        print(listname)
        lists = os.listdir()
        listslist = []
        for i in lists:
            if i.endswith("_list.txt"):
                listslist.append(i.split("_list.txt"))
        print(listslist)
        if listname not in listslist[0]:
            return "List not found"
        with open(f"{listname}_list.txt", "r") as f:
            lines = f.read()
            return lines

    # More functions for more responses here

    def findresponse(self):
        """Finds suitable response for the command using RegEx"""
        
        # Check if the command is wanting a joke
        if self.command.command == "joke":

            # Return a joke
            return self.joke()
        
        elif self.command.command.startswith("getlist"):
            
            lname = self.command.command.split()[1]
            return f"The {self.command.command.split()[1]} list contains:\n" + self.getlist(lname)
        
        elif self.command.command.startswith("addtolist"):
            
            item = self.command.command.split()[1]
            lname = self.command.command.split()[2]
            return self.add2list(item, lname)


        elif self.command.command == "unknown":
            return "Unknown command"