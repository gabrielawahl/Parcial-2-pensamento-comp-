print("Olá! 👋 Bem-vindo ao conversor de tempo!")

def segundos_para_hms(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segundos_restantes = resto % 60
    return horas, minutos, segundos_restantes

def hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

seg = int(input("Digite um valor em segundos: "))
h, m, s = segundos_para_hms(seg)
print(f"{seg} segundos = {h}h {m}min {s}s")

input("Pressione ENTER para sair...")