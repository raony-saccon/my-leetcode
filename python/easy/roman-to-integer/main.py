from constants import romans, no_repeat, valid_subtracts
from functions.int_to_roman import int_to_roman

# tasks
def roman_to_integer():
  print("\n== Roman to integer by RaonyDev ==")

  while True:
    roman_input = input("Insira o número romano aqui: ").upper()
    roman_array = list(roman_input)
    to_sum = 0
    to_subtract = 0
    counter = 0 
    repeat_sequence = 1

    print("\n=== Romano:", roman_input, '===')
    # search for non-roman chars
    for char in roman_array:
      if char not in romans:
        raise ValueError(f"{char} não é um número romano!")

    for roman in roman_array:
      roman_value = romans[roman]
      if (counter + 1 < len(roman_array)):
        next_roman = roman_array[counter + 1]
        next_roman_value = romans[next_roman]

        # tratamento de erros
        if (roman in no_repeat and roman == next_roman):
          print("Não pode repetir o romano: ", roman)
          return

        if (roman_value < next_roman_value and repeat_sequence > 1):
          print("Subtração em grupo não é permitido!")
          return

        if (roman == next_roman):
          repeat_sequence += 1
        else:
          repeat_sequence = 1

        if (repeat_sequence > 3):
          print(roman, 'repetiu mais que o permitido (3x)!')
          return

        if (romans[roman] < romans[next_roman]):
          if roman not in valid_subtracts:
            print("oxi")
            return
          if not (next_roman == valid_subtracts[roman][0] or next_roman == valid_subtracts[roman][1]):
            print('Subtração invalida!')
            return
          print(f"{roman}({roman_value}) é menor que {next_roman}({next_roman_value})")
          to_subtract += roman_value
        else:
          print(f"{roman}({roman_value}) é maior ou igual à {next_roman}({next_roman_value})")
          to_sum += roman_value
      counter += 1
    to_sum += romans[roman_array[-1]]
    result = to_sum - to_subtract


    int_converted_to_roman = int_to_roman(result)


    if (int_converted_to_roman != roman_input):
      print("Inválido (não passou no conversor int to roman)")
      return
    print("Resultado:", result)


roman_to_integer()


