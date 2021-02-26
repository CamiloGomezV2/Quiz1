class Command:
    def __init__(self):
        self.list_commands = []

    def execute(self, command):
        if command not in self.list_commands:
            print("Don't support")
        else:
            print(f"Command execute: {command}")

    def register(self, commands):
        for q in range(len(commands)):
            self.list_commands.append(commands[q])
        print('Successful register')


class Bot(Command):

    def __init__(self, commands):
        super().__init__()
        Command.register(self, commands)

    def action(self, command):
        Command.execute(self, command)


robot = Bot(['Encender','Apagar','Hablar','Dormir'])
robot.execute('Dormir')
robot.execute('comer')