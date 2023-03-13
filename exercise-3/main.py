def sum(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y

def calc():
    print("#" * 30)
    print("CALCULADORA")
    print("#" * 30)

    print("Digite o primeiro número")
    x = int(input())
    print("Digite o segundo número")
    y = int(input())
    print("Digite um dos operadores (x | - | *)")
    op = input()
    result = None

    if op == "+":
        result = sum(x, y)
    elif op == "-":
        result = sub(x, y)
    elif op == "*":
        result = mult(x, y)
    elif op == "/":
        result = div(x, y)
    else:
        print("O resultado não pode ser executado!")

    print(f"O resultado é: {result}")
    yes = "yes"
    no = "no"
    print(f"Desejar Continuar ({yes.upper()} | {no.upper()}")
    conditional = input()

    if conditional != "No":
        calc()
    #     if result == None:
    #         print("O resultado é 0")
    #     print("O resultado não pode ser executado!")

    # print(f"O resultado é: {result}")
    # print("O resultado é: ", result)
    # pass
        
if __name__ == "__main__":
    calc()