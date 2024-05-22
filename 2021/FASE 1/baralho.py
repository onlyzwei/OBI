cartasSTR = input()
cartas = []
qntdTipoCarta = {
   'C': 13,
   'E': 13,
   'U': 13,
   'P': 13
}
for i in range(0, len(cartasSTR), 3):
   carta = cartasSTR[i:i+3]
   tipoCarta = carta[2]
   if qntdTipoCarta[tipoCarta] == "erro":
      continue
   if carta in cartas:
      qntdTipoCarta[tipoCarta] = "erro"
      continue
   qntdTipoCarta[tipoCarta] -= 1
   cartas += [carta]

for tipoCarta in qntdTipoCarta:
   print(qntdTipoCarta[tipoCarta])
    