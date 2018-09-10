import time
import matplotlib.pyplot as plt


def plotter(values):
    plt.title('Tempo x Iteração')
    plt.ylabel('Tempo')
    plt.xlabel('Iteração')
    plt.plot(values, color='green')
    plt.show()


def tester(func, lst, qtd):
    times = []
    for x in range(0, qtd):
        copy = lst
        start = time.time()
        copy = func(copy)
        end = time.time()
        total = end - start
        times.append(total)
    return times
