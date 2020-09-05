import random
import numpy as np
from numpy.random import choice
from datetime import datetime
import time

f = open('average2.txt', 'w')
p = open('text1.txt', 'w')

optiuni_global = ['Piatra', 'Hartie', 'Foarfece']

initialscor = 0

winningMatrix = {'PiatraPiatra': 0, 'PiatraHartie': -1, 'PiatraFoarfece': 1, 'HartiePiatra': 1, 'HartieHartie': 0,
                 'HartieFoarfece': -1, 'FoarfecePiatra': -1, 'FoarfeceHartie': 1, 'FoarfeceFoarfece': 0}


def generate_random_procentages():

    procentajes = [None] * 3
    x = 1
    y = 1
    z = 1
    while x + y + z != 1.0:
        x = round(random.uniform(0.0, 1.0), 2)
        y = round(random.uniform(0.0, 1.0), 2)
        z = round(random.uniform(0.0, 1.0), 2)
    procentajes[0] = x
    procentajes[1] = y
    procentajes[2] = z

    return procentajes


def reset_scor (population):
    for i in range(len(population)):
        population[i].scor = 0
    return population





def choice_against_enemy(index):
    normal_optiuni = ['Piatra', 'Hartie', 'Foarfece']
    new_optiuni = [None] * len(normal_optiuni)
    new_optiuni[0] = normal_optiuni[index]
    if new_optiuni[0] == 'Piatra':
        new_optiuni[1] = 'Hartie'
        new_optiuni[2] = 'Foarfece'
    elif new_optiuni[0] == 'Hartie':
        new_optiuni[1] = 'Foarfece'
        new_optiuni[2] = 'Piatra'
    elif new_optiuni[0] == 'Foarfece':
        new_optiuni[1] = 'Piatra'
        new_optiuni[2] = 'Hartie'
    return new_optiuni





class jucatorComun:


    def __init__(self, procentaje):
        self.scor = 0
        self.optiuni = ['Piatra', 'Hartie', 'Foarfece']
        self.procentaje = procentaje
        self.win_counter = 0
        self.equal_counter = 0
        self.rounds_vector = []
        self.average_vector = []
        self.equal_average_vector = []


    def alege(self):
        draw = choice(self.optiuni, 1, p=self.procentaje)
        draw_index = self.optiuni.index(draw)
        return draw, draw_index


def starting_pop(numar_indivizi):
    population = [None] * numar_indivizi
    for i in range(numar_indivizi):
        procentajes = generate_random_procentages()
        individ = Chromosome(procentajes)
        population[i] = individ
    return population


def best_fitness(population):
    fitness = [None] * len(population)

    for i in range(len(population)):
        fitness[i] = population[i].scor
    index = fitness.index(max(fitness))
    return population[index]


def worst_fitness(population):

    fitness = [None] * len(population)

    for i in range(len(population)):
        fitness[i] = population[i].scor
    index = fitness.index(min(fitness))
    return population[index]


def select_individ(population, k):

    aspirants = [None] * k
    fitness = [None] * k
    for i in range(k):
        aspirants[i] = random.choice(population)
        fitness[i] = aspirants[i].scor
    index = fitness.index(max(fitness))
    return aspirants[index]


def crossover(parent1, parent2):

    child = Chromosome([0, 0, 0])
    child.procentaje[0] = (parent1.procentaje[0]+parent2.procentaje[0])/2
    child.procentaje[1] = (parent1.procentaje[1]+parent2.procentaje[1])/2
    child.procentaje[2] = (parent1.procentaje[2]+parent2.procentaje[2])/2

    return child



def mutation ( population, mutation_prob ):
    for individual in range(len(population)):
        positions = random.sample(range(0,3),2)
        pzero = positions[0]
        pone = positions[1]
        mutate = random.uniform(0, 0.1)
        x = random.uniform(0,0.1)
        if x < mutation_prob:
            if population[individual].procentaje[pzero] > mutate:
                population[individual].procentaje[pzero] = population[individual].procentaje[pzero] - mutate
                population[individual].procentaje[pone] = population[individual].procentaje[pone] + mutate
            elif population[individual].procentaje[pone] > mutate:
                population[individual].procentaje[pone] = population[individual].procentaje[pone] - mutate
                population[individual].procentaje[pzero] = population[individual].procentaje[pzero] + mutate

    return population


def reset_win_counter(population):
    for individ in range(len(population)):
        population[individ].win_counter = 0
        population[individ].split_counter = 0
    return population

class Joc:

    winningMatrix ={'PiatraPiatra': 0, 'PiatraHartie': -1, 'PiatraFoarfece': 1, 'HartiePiatra': 1, 'HartieHartie': 0,
                     'HartieFoarfece': -1, 'FoarfecePiatra': -1, 'FoarfeceHartie': 1, 'FoarfeceFoarfece': 0}

    def __init__(self, numarDeRunde):
        
        self.n = numarDeRunde
        self.wins_vector = [0] * 50
        self.i = 0
        self.moving_average_vector = []

    procentaje = []

    def winner(self, draw1, draw2):
        z_winner = draw1 + draw2
        if winningMatrix[z_winner] == 0:
            result = 'draw'
        elif winningMatrix[z_winner] == 1:
            result = 'win'
        elif winningMatrix[z_winner] == -1:
            result = 'lose'
        return result

    def calculare_scor(self, result):

        if result == 'draw':
            scor = 0
        if result == 'win':
            scor = 1
        if result == 'lose':
            scor = -1
        return scor

    def play_a_round(self, player1, player2, precedent_win_p2, precendent_index_p2):

        # if self.i % 2 == 0:
        #     player1.procentaje = [1, 0, 0]
        #     draw_p1, index_p1 = player1.alege()
        # else:
        #     player1.procentaje = [0, 1, 0]
        #     draw_p1, index_p1 = player1.alege()
        if self.i == 0:
            draw_p1, index_p1 = player1.alege()
        else:
            draw_p1 = precedent_win_p2
            index_p1 = precendent_index_p2
        draw_p2, index_p2 = player2.alege()
        # print ('index_p1: ', index_p1, 'index_p2', index_p2)
        # print('drawOne: ', draw_p1, 'drawTwo', draw_p2)
        result = self.winner(draw_p2[0], draw_p1[0])
        # print ('procentaje player 2: ', player2.procentaje)
        # if result == 'draw':
        #     print('Player 1 and Player 2 are EQUAL')
        # elif result == 'win':
        #     print('PLayer 1 LOSE, PLayer 2 WIN')
        # elif result == 'lose':
        #     print('Player 1 WIN, Player 2 LOSE')
        if result == 'win':
            player2.win_counter += 1
            player2.rounds_vector.append(1)
            player2.average_vector.append(1)
            player2.equal_average_vector.append(0)
            if self.i < 50:
                self.wins_vector[self.i] = 1
            else:
                self.wins_vector[int(self.i / 50)] = 1
        # if result == 'lose' or result == 'draw':
        #     if self.i >=50:
        #         self.wins_vector[int(self.i / 50)] = 0
        if result == 'lose':
            player2.average_vector.append(0)
            player2.equal_average_vector.append(0)
        elif result == 'draw':
            player2.average_vector.append(0)
            player2.equal_average_vector.append(1)

        # else:
        #     if self.i < 50:
        #         self.wins_vector[self.i] = 0
        #     else:
        #         self.wins_vector[int(self.i / 50)] = 0
        if result == 'draw':
            player2.split_counter += 1
            player2.rounds_vector.append(0)
        if result == 'lose':
            player2.rounds_vector.append(-1)
        player2.scor += self.calculare_scor(result)
        # self.scor += calculare_scor(result)
        # return last_round_index
        return draw_p2, index_p2

    def play_n_rounds(self, player1, player2):
        self.i = 0
        moving_average = 0
        precedent_win_p2 = ''
        precedent_index_p2 = ''
        # print('Se vor juca ', self.n, ' runde')
        for self.i in range(self.n):

            # print('Runda ', i + 1)
            precedent_win_p2, precedent_index_p2 = self.play_a_round(player1, player2, precedent_win_p2, precedent_index_p2)
            # if self.i >= 50 :
            #     moving_average = sum(self.wins_vector) / 50
            #     self.moving_average_vector.append(moving_average)
            # if player2.scor >= 100:
            #     # print(player2.procentaje)
            #     # print(i-1)
            #     break
            # print('Sfarsitul rundei ', i + 1)

def working_on_average(average_vector):
    esantion_medie = 50
    aux = esantion_medie
    S = 0
    medie = 0
    j = 0
    i = 0
    vector_pt_egal = []
    while i < len(average_vector):
        while i < esantion_medie:
            if average_vector[i] == 1:
                S += average_vector[i]
            i += 1
        if i == esantion_medie:
            medie = S / aux
            # f.write('')
            f.write(str(medie))
            f.write(' ')
            vector_pt_egal.append(medie)
            # f.write(' \n')
        esantion_medie = esantion_medie+1
        S = 0
        medie = 0
        j += 1
        i = j
        if esantion_medie > len(average_vector):
            break
    return vector_pt_egal

def working_on_average_equal(average_equal_vector, vector_pt_egal):
    esantion_medie = 50
    aux = esantion_medie
    S = 0
    medie = 0
    j = 0
    i = 0
    v = []
    while i < len(average_equal_vector):
        while i < esantion_medie:
            if average_equal_vector[i] == 1:
                S += average_equal_vector[i]
            i += 1
        if i == esantion_medie:
            medie = S / aux
            v.append(medie)
            # f.write('')
            # f.write(str(medie))
            # f.write(' ')
            # f.write(' \n')
        esantion_medie = esantion_medie+1
        S = 0
        medie = 0
        j += 1
        i = j
        if esantion_medie > len(average_equal_vector):
            break
    i = 0

    output = []
    for i in range(len(vector_pt_egal)):
        output.append(vector_pt_egal[i] + v[i])
    i = 0
    for i in range(len(output)):
        p.write(str(output[i]))
        p.write(' ')

def reset_vector(population):
    for i in range(len(population)):
        population[i].average_vector = []
        population[i].equal_average_vector = []
    return population

class Chromosome(jucatorComun):


    def fitness_scor(self):
        return self.scor


print('Numarul de indivizi din populatie ')
# pop_size = int(input())
pop_size = 50

numar_generatii = 250
population = starting_pop(pop_size)

print('Pentru selectia "parintilor" specificati numarul de aspiranti')
# number_of_aspirants = int(input())
number_of_aspirants = 1
print('Introduceti numarul de runde pe care fiecare individ sa le joace contra jucatorului stabilit')
best_fitness_vector_population = []
most_wins_vector_population = []

# n = int(input())
n = 500
start_time = time.time()
ok_individ = 0
ok_populatie = 0
joc = Joc(n)
numar_runde_pentru_medie = 50
vector = np.zeros((numar_generatii,int( n / numar_runde_pentru_medie)))
adaptive_generation = int(numar_generatii*(2/5))

vector_medii_generatii = np.zeros([numar_generatii, n])

for generation in range(numar_generatii):
    medie_the_best_one = 0

    ok = 1
    idealscor = n * max(winningMatrix.values())
    random_procentajes = generate_random_procentages()


    contor_populatie = 0
    population = reset_win_counter(population)
    # if generation >= 50:
    #     new_player1 = jucatorComun(only_paper)
    # else:
    #     new_player1 = jucatorComun(only_rock)
    for individ in range(len(population)):
        # if generation + 1 <= adaptive_generation:
        #     new_player1 = jucatorComun([0.70, 0.15, 0.15])
        # else:
        #     new_player1 = jucatorComun([0.15, 0.15, 0.70])
        piatra_hartie = jucatorComun([1/3,1/3,1/3])
        joc.play_n_rounds(piatra_hartie, population[individ])

        # if population[individ].scor >= 100:
        #     print('Scorul individului cu numarul ', individ, 'este ', population[individ].scor,
        #           ' iar scorul maxim este ', idealscor)
        #     print(population[individ].procentaje)
        #     print(generation)
        #     ok = 0
        #     break
        contor_populatie += population[individ].win_counter
        contor_populatie += population[individ].split_counter

    the_best_one = best_fitness(population)

    v = []
    if generation == numar_generatii - 1 or generation == 0 or generation == int(numar_generatii/5) or generation == int(numar_generatii*(2/5)) or generation == int(numar_generatii*(3/5)) or generation == int(numar_generatii*(4/5)) or generation == int(numar_generatii) or generation == adaptive_generation or generation == adaptive_generation + 1:
        f.write('\n')
        f.write(str(generation))
        f.write('\n')
        v = working_on_average(the_best_one.average_vector)
        p.write('\n')
        p.write(str(generation))
        p.write('\n')
        working_on_average_equal(the_best_one.equal_average_vector, v)
    if generation + 1 == adaptive_generation:
        print(the_best_one.procentaje)
    # x = 0
    # suma = 0
    # media = 0
    # contor_medii = int( n / numar_runde_pentru_medie )
    # for i in range(contor_medii):
    #     suma = 0
    #     j = numar_runde_pentru_medie*i
    #
    #     while j < numar_runde_pentru_medie*(i+1):
    #         if the_best_one.rounds_vector[j] == 1:
    #             suma += 1
    #         j += 1
    #     media = suma / numar_runde_pentru_medie
    #     vector[generation][i] = media
        # print (media)



    if ok == 0:
        break
    parent_1 = select_individ(population, number_of_aspirants)
    parent_2 = select_individ(population, number_of_aspirants)

    child = crossover(parent_1, parent_2)

    the_worst_one = worst_fitness(population)

    population.remove(the_worst_one)
    population.append(child)

    mutation_rate = 0.01

    population = mutation(population, mutation_rate)
    if generation  != numar_generatii - 1:
        population = reset_scor(population)
        population = reset_vector(population)


print (' ---- %s seconds ---- ' % (time.time() - start_time))
# print('za vector', vector)
# print (new_player1.procentaje)
the_best_one = best_fitness(population)
# print(the_best_one.rounds_vector)
# print(joc.moving_average_vector)

print(the_best_one.procentaje)
print('dupa ', numar_generatii, ' generatii cel mai bun individ are un procentaj de ', the_best_one.win_counter / n)
print('dupa', numar_generatii, 'generatii cel mai bun individ are split rate de ', the_best_one.split_counter/n)
print(' populatia are un procentaj de ', contor_populatie / (n*pop_size) )



