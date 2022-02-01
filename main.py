from command import Command
from executor import Executor
import re
import threading
import utils

if __name__ == "__main__":
    # The below is just an example, there will be voice interaction instead soon
    _x = input("Would you like voice interaction or text interaction?\n")
    print("Hello, am eric!")
    while True:
      if bool(re.match("text(?: interaction|)(?: please|)", _x, flags = re.IGNORECASE)):
        cmd = input()
        print("\n" + Executor(Command(cmd)).response)
        if cmd.lower() in ["adios", "goodbye", "bye", "cya"]:
          print("See you next time!")
          break

      else:
        # Coming soon
        pass