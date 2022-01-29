from .command import Command
from .executor import Executor

if __name__ == "__main__":
    # The below is just an example, there will be voice interaction instead soon

    cmd = input("What would you like to do?")
    print(Executor(Command(cmd)))