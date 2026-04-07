print("Bom dia!")

ver = input("Você quer ver a lista de nomes? (s/n): ")

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

if ver.lower() == "s":
    resultado = "\n".join(nomes)
else:
    resultado = "Lista não exibida."

print("\n--- RESULTADO ---")
print(resultado)

input("\nPressione ENTER para sair...")
