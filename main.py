n1 = 5
tentativas = 0
mxTentativas = 3

while tentativas < mxTentativas:
  resp = int(input("Adivinhe o número: (entre 1 e 10) "))

  if resp == n1:
    print("Você acertou, Parabéns!")
  else:
    tentativas += 1
    print(f"Você errou! tente novamente! {mxTentativas - tentativas}")

else:
  print(f"Suas tntativas acabara!")