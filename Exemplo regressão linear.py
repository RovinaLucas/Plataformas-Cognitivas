def previsao():
  ano = int(input("Digite o ano para a previsão: "))
  glen = (ano - 2010)*91 + 723
  print(f"A previsão para o ano de {ano} é: ", glen)
  return glen
while True:
  previsao()