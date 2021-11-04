from utils import clear_value
from constants import VarType

def get_var_type():
    while True:
        try:
            var_type = int(
                input("Informe o tipo de variável: '1' qualitativa ou '2' quantitativa\n-> ")
            )
            if var_type == 1:
                return VarType.QUALITATIVE
            elif var_type == 2:
                return VarType.QUANTITATIVE
            else:
                raise KeyError
        except Exception:
            print('O valor informado é inválido!')


def get_entry_method():
    while True:
        try:
            var_type = int(
                input("Digite '1' para cadastrar manualmente ou '2' para informar o nome de um arquivo\n-> ")
            )
            if var_type in [1, 2]:
                return var_type
            else:
                raise KeyError
        except Exception:
            print('O valor informado é inválido!')


def get_data(var_type, entry_method):
    if entry_method == 1:
        data = []
        print("Cadastre os valores")
        print("Para finalizar digite 0")

        while True:
            try:
                value = input("Digite um valor:\n-> ")
                if value == '0':
                    raise KeyError
                else:
                    if var_type == VarType.QUANTITATIVE:
                        value = clear_value(value)
                    if value:
                        data.append(value)
                    else:
                        print('O valor informado é inválido')
            except Exception:
                break

        return data

    if entry_method == 2:
        data = []

        while(True):
            file_name = input('Digite o nome do arquivo:\n-> ')
            try:
                file = open(file_name, 'r')
                break
            except Exception:
                print('Arquivo não encontrado')

        lines = file.readlines()

        for value in lines:
            value = value.replace('\n', '').replace(' ', '')
            if var_type == VarType.QUANTITATIVE:
                value = clear_value(value)
            if value:
                data.append(value)

        return data
