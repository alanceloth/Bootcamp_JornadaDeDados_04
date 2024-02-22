# 1) Solicita ao usuário que digite seu nome
def recebe_nome():
    """
    This function prompts the user to input their name and returns the input as a string.
    """
    nome: str = None
    while nome is None or len(nome) == 0 or any(char.isdigit() for char in nome) or len(nome) < 3 or len(nome) > 30 or not nome.isalpha():
        try:
            nome = input("Qual seu nome? ")
            
            if nome is None or len(nome) == 0:
                raise Exception("O nome deve ser informado.")
            elif any(char.isdigit() for char in nome):
                raise Exception("O nome deve conter apenas letras.")
            elif len(nome) < 3:
                raise Exception("O nome deve conter pelo menos 3 letras.")
            elif len(nome) > 30:
                raise Exception("O nome deve conter no maximo 30 letras.")
            elif not nome.isalpha():
                raise Exception("O nome deve conter apenas letras.")
            else:
                print("Nome valido.", nome)
            
        except Exception as e:
            print(e)
    return nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
def recebe_salario():
    """
    Function to receive and return the user's salary as a float.
    """
    salario: float = None
    while salario is None or salario < 0:
        try:
            salario = float(input("Qual seu salário? "))
            if salario < 0:
                raise ValueError("O valor do seu salário deve ser positivo.")
        except ValueError as e:
            print(e)
    return salario

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
def recebe_bonus():
    """
    A function that prompts the user to input the value of a bonus and returns it as a float.
    """
    bonus: float = None
    while bonus is None or bonus < 0:
        try:
            bonus = float(input("Qual o valor do bônus? "))
            if bonus < 0:
                raise ValueError("O valor do bônus deve ser positivo.")
        except ValueError as e:
            print(e)
    return bonus

# 4) Calcule o valor do bônus final
def calcula_bonus(salario, bonus):
    """
    Calculate the bonus based on the given salary and bonus multiplier.

    Parameters:
    salario (int): The base salary.
    bonus (float): The bonus multiplier.

    Returns:
    int: The calculated bonus.
    """
    return (1000 + salario * bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
def imprime_mensagem():
    """
    This function prints a message with the name, bonus, and final bonus amount.
    """
    print("Ola ", recebe_nome(), ", o seu bônus final é: ", (f"R$ {calcula_bonus(recebe_salario(), recebe_bonus()):.2f}"))


def main():
    """
    This function calls the imprime_mensagem function.
    """
    imprime_mensagem()


if __name__ == "__main__":
    main()

# Exemplo de uso:
# Qual seu nome? Luciano
# Qual seu salário? 10000
# Qual o valor do bônus? 1.5
# Ola  Luciano , o seu bônus final e:  16000.0