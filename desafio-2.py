print("Bom dia!")

nome = input("Qual é o seu nome? ")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

print("\n--- RESULTADO ---")
print(f"Prazer em te conhecer, {nome}!")
print(f"O número {numero} é {resultado}.")

input("\nPressione ENTER para sair...")