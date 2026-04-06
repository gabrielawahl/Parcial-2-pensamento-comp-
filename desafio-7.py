print("Bom dia!")

nome = input("Qual é o seu nome? ")
capital = float(input("Digite o valor do capital (R$): "))
taxa = float(input("Digite a taxa de juros (% ao período): "))
tempo = float(input("Digite o tempo (número de períodos): "))

juros = capital * (taxa / 100) * tempo
montante = capital + juros

print("\n--- RESULTADO ---")
print(f"Prazer em te conhecer, {nome}!")
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa de juros: {taxa}% ao período")
print(f"Tempo: {tempo} períodos")
print(f"Juros simples: R$ {juros:.2f}")
print(f"Montante final: R$ {montante:.2f}")

input("\nPressione ENTER para sair...")