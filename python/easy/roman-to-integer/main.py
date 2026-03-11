kromans = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
}

def debug_roman(roman):
  array_roman = list(roman)
  soma = 0
  for r in array_roman:
    v = romans[r]
    print(r, '-', v)
    soma += v    
  print(soma)

debug_roman('XXI')

# percorrer array_roman
# remover cada romano que for menor que o próximo da lista e salvar o valor do mesmo numa variavel de subtração
# fazer o valor do romano inserido pelo usuario - variavel de subtração