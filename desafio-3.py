print("Bom dia!")

# Entrada (pergunta)
ver = input("Você quer ver a lista de nomes? (s/n): ")

# Dados
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Processamento
if ver.lower() == "s":
    resultado = "\n".join(nomes)
else:
    resultado = "Lista não exibida."

# Saída (tudo no final)
print("\n--- RESULTADO ---")
print(resultado)

input("\nPressione ENTER para sair...")