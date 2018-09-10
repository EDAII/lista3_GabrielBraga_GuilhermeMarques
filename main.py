import random
import os
import time
from sorters import Sorter
from plotter import plotter, tester


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def mainMenu():
  print('1 - Criar lista aleatória')
  print('8 - Printar lista')
  print('0 - Sair')
  option = input()
  return option


if __name__ == '__main__':
  lst = []
  sorter = Sorter()
  exit = False

  while(not exit):
    option = mainMenu()
    if option == '0':
      exit = True
      clear()
    elif option == '1':
      clear()
      entry = int(input('Insira o tamanho da lista: '))
      lst = random.sample(range(0, 3*entry), entry)
      print('Lista criada com sucesso')
    elif option == '7':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      # times = tester(bubble_sort, lst, qtdTeste)
      # plotter(times)
    elif option == '8':
      clear()
      print('\n\n')
      print(lst)
      print('\n\n')
    else:
      pass
