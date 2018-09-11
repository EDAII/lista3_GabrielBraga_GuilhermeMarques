import random
import os
import time
from sorters import Sorter
from plotter import plotter, tester


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Ordenação por Quicksort')
  print('3 - Ordenação por MergeSort')
  print('4 - Ordenação por BucketSort')
  print('5 - Ordenação por ShellSort')
  print('6 - Gráfico de desempenho Quicksort')
  print('7 - Gráfico de desempenho MergeSort')
  print('8 - Gráfico de desempenho BucketSort')
  print('9 - Gráfico de desempenho ShellSort')
  print('10 - Printar lista')
  print('0 - Sair')
  option = input()
  return option


if __name__ == '__main__':
  lst = []
  lst2 = []
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
      lst2 = lst
      print('Lista criada com sucesso')
    elif option == '2':
      clear()
      lst = lst2
      result = sorter.timer(sorter.quicksort, lst, 0, len(lst) - 1)
      print('Tempo gasto: ' + str(result[0]))
      print('Lista: ' + str(lst))
    elif option == '3':
      clear()
      lst = lst2
      #result = sorter.timer(sorter.mergeSort, lst, 0, len(lst) - 1)
      #print('Tempo gasto: ' + str(result[0]))
      #print('Lista: ' + str(lst))
    elif option == '4':
      clear()
      lst = lst2
      #result = sorter.timer(sorter.bucketSort, lst, 0, len(lst) - 1)
      #print('Tempo gasto: ' + str(result[0]))
      #print('Lista: ' + str(lst))
    elif option == '5':
      clear()
      lst = lst2
      #result = sorter.timer(sorter.shellSort, lst, 0, len(lst) - 1)
      #print('Tempo gasto: ' + str(result[0]))
      #print('Lista: ' + str(lst))
    elif option == '6':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(qtdTeste, sorter.quicksort, lst, 0, len(lst) - 1)
      plotter(times)
    elif option == '7':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(qtdTeste, sorter.mergeSort, lst, 0, len(lst) - 1)
      plotter(times)
    elif option == '8':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(qtdTeste, sorter.bucketSort, lst, 0, len(lst) - 1)
      plotter(times)
    elif option == '9':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(qtdTeste, sorter.shellSort, lst, 0, len(lst) - 1)
      plotter(times)
    elif option == '10':
      clear()
      print('\n\n')
      print(lst)
      print('\n\n')
    else:
      pass
