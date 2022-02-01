from command import Command
from executor import Executor
import re
import threading
import utils

if __name__ == "__main__":
    # The below is just an example, there will be voice interaction instead soon
    _x = input("Would you like voice interaction or text interaction?\n")
    while True:

      if bool(re.match("text(?: interaction|)(?: please|)", _x, flags = re.IGNORECASE)):

        cmd = input()
        print("\n" + Executor(Command(cmd)).response)

      else:
        # Coming soon
        print("test")
        pass