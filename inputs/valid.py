from commands import get_commands
class ValidInput:
    def __init__(self):
        self.valid_commands = get_commands()
    def valid(self, input):
        return input in self.valid_commands
Validinput = ValidInput()
def get_inputs():
        inputs = input()
        try:
            if Validinput.valid(inputs):
                command = Validinput.valid_commands.get(inputs)
                try:
                    command()
                except Exception as e:
                    print(f"Erro ao tentar executar o comando: {e}")
            else:
                print("Comando inválido")
        except Exception as e:
            print(f"Erro ao tentar executar o comando: {e}")