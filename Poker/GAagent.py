import numpy as np
from numpy.random import choice

position = 1
update = 1

cards = {


    'Rosu': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Negru': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Romb': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Trefla': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

}

culori = ['Rosu', 'Negru', 'Romb', 'Trefla']

def pereche(carti_pereche):
    duplicates = {}
    a = []
    contor = 0
    for item in carti_pereche:
        duplicates[item] = duplicates.get(item, 0) + 1
    for item in duplicates:
        if duplicates[item] == 2:
            contor += 1
            a.append(item)
    if a and contor == 1:
        return contor, a, 'Pereche'
    elif a and contor == 2:
        return contor, a, 'Doua Perechi'
    else:
        return 0, a, 'Carte Mare'

def three_of_a_kind(carti_toak):
    duplicates = {}
    a = []
    contor = 0
    for item in carti_toak:
        duplicates[item] = duplicates.get(item, 0) + 1
    for item in duplicates:
        if duplicates[item] == 3:
            contor += 1
            a.append(item)
    if a:
        return 3, a, 'Trei Asemenea'
    else:
        return 0, a, 'Carte Mare'


def straight(carti_straight):
    carti_straight = np.sort(carti_straight)
    if isinstance(carti_straight[5], str):
        carti_straight = np.delete(carti_straight, 5)
        carti_straight = np.delete(carti_straight, 5)
    elif isinstance(carti_straight[6], str):
        carti_straight = np.delete(carti_straight, 6)
    contor = 0
    chinta = []

    if carti_straight[0] == 10 and carti_straight[1] == 12 and carti_straight[2] == 13 and carti_straight[3] == 14 and carti_straight[4] == 15:
        chinta.append(int(carti_straight[0]))
        chinta.append(int(carti_straight[1]))
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
        return 4, chinta, 'Chinta'
    elif carti_straight[1] == 10 and carti_straight[2] == 12 and carti_straight[3] == 13 and carti_straight[4] == 14 and carti_straight[5] == 15:
        chinta.append(int(carti_straight[1]))
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
        chinta.append(int(carti_straight[5]))
        return 4, chinta, 'Chinta'
    elif carti_straight[2] == 10 and carti_straight[3] == 12 and carti_straight[4] == 13 and carti_straight[5] == 14 and carti_straight[6] == 15:
        chinta.append(int(carti_straight[1]))
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
        chinta.append(int(carti_straight[5]))
        return 4, chinta, 'Chinta'

    if int(carti_straight[4]) - int(carti_straight[0]) == 5:
        chinta.append(int(carti_straight[0]))
        chinta.append(int(carti_straight[1]))
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
    if len(carti_straight) == 6:
        if int(carti_straight[5]) - int(carti_straight[1]) == 5:
            chinta.append(int(carti_straight[1]))
            chinta.append(int(carti_straight[2]))
            chinta.append(int(carti_straight[3]))
            chinta.append(int(carti_straight[4]))
            chinta.append(int(carti_straight[5]))
    elif len(carti_straight) == 7:
        if int(carti_straight[6]) - int(carti_straight[2]) == 5:
            chinta.append(int(carti_straight[2]))
            chinta.append(int(carti_straight[3]))
            chinta.append(int(carti_straight[4]))
            chinta.append(int(carti_straight[5]))
            chinta.append(int(carti_straight[6]))


    if chinta:
        return 4, chinta, 'Chinta'
    else:
        return 0, chinta, 'Carte Mare'



def flush(carti_flush, culori_flush):
    contor = 0
    c = []
    mana = 'Culoare'
    nothing = 'Carte Mare'
    for j in culori:
        for i in range(len(culori_flush)):
            if culori_flush[i] == j:
                contor += 1
                c.append(carti_flush[i])
        if contor == 5:
            c.sort()
        else:
            contor = 0
            c.clear()
    if contor == 5:
        return 5, c, mana
    else:
        return 0, c, nothing

def full_house(carti_full):
    full = {}
    contor = 0
    full_array = []
    for item in carti_full:
        full[item] = full.get(item, 0) + 1
    for item in full:
        if full[item] == 2:
            for item2 in full:
                if full[item] == 3:
                    full_array.append(item)
                    full_array.append(item2)
                    # print('a fost gasit full de: ', item2, ' cu ', item)

    if full_array:
        return 6, full_array, 'Full House'
    else:
        return 0, full_array, 'Carte Mare'

def four_of_a_kind(carti_careu):
    careu = {}
    contor = 0
    careu_array = []
    for item in carti_careu:
        careu[item] = careu.get(item, 0) + 1
    for item in careu:
        if careu[item] == 4:
            careu_array.append(item)
            # print('a fost gasit careu de: ', item)
    if careu_array:
        return 7, careu_array, 'Careu'
    else:
        return 0, careu_array, 'Carte Mare'


def straight_flush(carti, culori):
    ok, nCards, mana = straight(carti)
    if ok != 0:
        ok, nCards, mana = flush(carti,culori)
        if ok != 0:
            return 8, nCards, 'Chinta de culoare'
    return 0, nCards, 'Carte Mare'

def to_str_harcoded(word):
    if word == 'Call':
        word = 'Call'
    elif word == 'Raise':
        word = 'Raise'
    elif word == 'Fold':
        word = 'Fold'
    elif word == 'Check':
        word = 'Check'
    elif word == 'All-In':
        word = 'All-In'
    elif word is None:
        word = None
    return word


def determine_actions (position, moment, enemy_action):
    if moment == 'Preflop':
        if position == 1:
            if enemy_action is None or enemy_action == '':
                return ['Call', 'Raise', 'Fold', None, None, None]
            # elif enemy_action == None:
            #     return ['Call', None, 'Fold', 'Check', None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None, None]
            elif enemy_action == 'All-In':
                return [None, 'Raise', 'Fold', 'All-In', None, None]
        elif position == 0:
            if enemy_action == 'Call':
                return [None, 'Raise', None, 'Check', None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None, None]
            elif enemy_action == None:
                return ['Call', None, 'Fold', None, None,None]
            elif enemy_action is None or enemy_action == None:
                return [None, 'Raise', 'Fold', 'Check', None, None]
            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None] #MEMENTO
            elif enemy_action == 'Check':
                return [None, None, None, None, None, None]
    elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
        if position == 1:
            if enemy_action is None or enemy_action == '':
                return [None, 'Raise', 'Fold', 'Check', None, None]
            elif enemy_action == 'Check':
                return [None, 'Raise', None, 'Check', None, None]
            elif enemy_action == 'Call':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None,None]
            elif enemy_action == None:
                return ['Call', None, 'Fold', None, None,None]
            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None]
        if position == 0:
            if enemy_action == 'Check':
                return [None, 'Raise', None, 'Check', None,None]
            elif enemy_action == 'Call':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None,None]
            elif enemy_action == None:
                return ['Call', None, 'Fold', None, 'All-In',None]
            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None]

def reset_win_counter(population):
    for individ in range(len(population)):
        population[individ].win_counter_games = 0
    return population

def select_individ(population, k):

    aspirants = [None] * k
    fitness = [None] * k
    for i in range(k):
        aspirants[i] = choice(population,1)
        fitness[i] = aspirants[i][0].fitness
    index = fitness.index(max(fitness))
    return aspirants[index]

def starting_pop(numar_indivizi):
    population = [None] * numar_indivizi
    for i in range(numar_indivizi):
        individ = GAagent(update, position, 4000)
        individ.initialize_genes()
        population[i] = individ
    return population

def worst_fitness(population):

    fitness = [None] * len(population)

    for i in range(len(population)):
        fitness[i] = population[i].fitness
    index = fitness.index(min(fitness))
    return population[index]

def crossover(parent1, parent2, position):

    child1 = GAagent(1, position, 4000)
    # child2 = GAagent(1, position, 4000)

    for i in range(4):
        for j in range(15):
            child1.genes[i][j] = (parent1[0].genes[i][j] + parent2[0].genes[i][j])/2
            child1.raise_genes[j] = (parent1[0].raise_genes[j] + parent2[0].raise_genes[j])/2
            if child1.genes[i][j] > 5:
                child1.genes[i][j] = 5
            elif child1.genes[i][j] < 0:
                child1.genes[i][j] = 0
            if child1.raise_genes[j] > 5:
                child1.raise_genes[j] = 5
            elif child1.raise_genes[j] < 0:
                child1.raise_genes[j] = 0
    return child1

def mutatie(populatie, mutation_rate):
    for individ in range(len(populatie)):
        x = np.random.uniform(0,0.1)
        if x < mutation_rate:
            for i in range (4):
                for j in range(15):
                    if (j + 1)  % 5 != 0:
                        if (j % 2 ) == 0:
                            populatie[individ].genes[i][j] = populatie[individ].genes[i][j] * 0.85
                            populatie[individ].raise_genes[j] = populatie[individ].raise_genes[j] * 0.85
                        else:
                            populatie[individ].genes[i][j] = populatie[individ].genes[i][j] * 1.15
                            populatie[individ].raise_genes[j] = populatie[individ].raise_genes[j] * 1.15
                        if populatie[individ].genes[i][j] > 5:
                            populatie[individ].genes[i][j] = 5
                        elif populatie[individ].genes[i][j] < 0:
                            populatie[individ].genes[i][j] = 0
                        if populatie[individ].raise_genes[j] > 5:
                            populatie[individ].raise_genes[j] = 5
                        elif populatie[individ].raise_genes[j] < 0:
                            populatie[individ].raise_genes[j] = 0
                    else:
                        if ( j % 2) == 0:
                            populatie[individ].raise_genes[j] = populatie[individ].raise_genes[j] * 0.15
                        else:
                            populatie[individ].raise_genes[j] = populatie[individ].raise_genes[j] * 1.15
                        if populatie[individ].raise_genes[j] > 5:
                            populatie[individ].raise_genes[j] = 5
                        elif populatie[individ].raise_genes[j] < 0:
                            populatie[individ].raise_genes[j] = 0
                        populatie[individ].genes[i][j] = 0
    return populatie

def reset_fitness(population):
    for i in range(len(population)):
        population[i].fitness = 0
    return population

def best_fitness(population):
    fitness = [None] * len(population)

    for i in range(len(population)):
        fitness[i] = population[i].fitness
    index = fitness.index(max(fitness))
    return population[index]


class GAagent():

    def __init__(self, update, position, points):
        self.update = update

        self.moment = 'Preflop'
        self.position = position

        self.callEcuation = 0
        self.raiseEcuation = 0
        self.foldEcuation = 0
        self.checkEcuation = 0
        self.noneEcuation = 0

        self.gaRasieEcuationOne = 0
        self.gaRasieEcuationTwo = 0
        self.gaRasieEcuationThree = 0
        self.gaRasieEcuationFour = 0
        self.gaRasieEcuationFive = 0

        self.game_rounds = 0

        self.result = None

        self.genes = [
            [None]*15, #preflop
            [None]*15, #flop
            [None]*15, #turn
            [None]*15  #river
        ]

        self.raise_genes = [None] * 15

        self.action = ''
        self.state = [None] * 3

        self.points = points
        self.score = 0
        self.bet = 0

        self.points_vector = []

        self.ecuation_vector = [None]*5
        self.raise_vector = [None]*5

        self.fitness = 0

        self.playable_actions = ['a'] * 6

        self.counter = 0

        self.mana = ''
        self.best_of_five = [None] * 5
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']

        self.state_new_state = [None] * 2


        self.win_counter = 0
        self.win_counter_games = 0
        self.win_counter_noob_games = 0
        self.split_rounds = 0
        self.total_points = 0
        self.total_points_noob = 0
        self.win_counter_part = 0


        self.bigblinds = 0
        self.preflop_win = 0
        self.flop_win = 0
        self.turn_win = 0
        self.river_win = 0

    def determine_actions(self, enemy_action):
        if self.moment == 'Preflop':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Call', 'Raise', 'Fold', None, None, None]

                elif enemy_action == 'Raise':
                    self.playable_actions =  ['Call', 'Raise', 'Fold', None, None, None]
                elif enemy_action == 'All-In':
                    self.playable_actions =  ['Call', None, 'Fold', None, None, None]
                elif enemy_action == 'Call' or enemy_action == 'Fold' or enemy_action == 'Check':
                    self.playable_actions =  [None, None, None, None, None, None]
            elif self.position == 0:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions =  [None, 'Raise', 'Fold', 'Check', None, None]
                elif enemy_action == 'Call' and self.action == 'Raise':
                    self.playable_actions =  [None, None, None, None, None, None]
                elif enemy_action == 'Call':
                    self.playable_actions =  [None, 'Raise', None, 'Check', None, None]
                elif enemy_action == 'Raise':
                    self.playable_actions =  ['Call', 'Raise', 'Fold', None, None, None]
                elif enemy_action == 'Fold':
                    self.playable_actions =  [None, None, None, None, None, None]  # MEMENTO
                elif enemy_action == 'Check':
                    self.playable_actions =  [None, None, None, None, None, None]
        elif self.moment == 'Flop' or self.moment == 'Turn' or self.moment == 'River':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions =  [None, 'Raise', 'Fold', 'Check', None, None]
                elif enemy_action == 'Check':
                    self.playable_actions =  [None, 'Raise', None, 'Check', None, None]
                elif enemy_action == 'Call' and self.action == 'Raise':
                    self.playable_actions =  [None, None, None, None, None, None]
                elif enemy_action == 'Call':
                    self.playable_actions =  [None, None, None, None, None, None]
                elif enemy_action == 'Raise':
                    self.playable_actions =  ['Call', 'Raise', 'Fold', None, None, None]
                elif enemy_action == None:
                    self.playable_actions =  [None, 'Raise', 'Fold', 'Check', None, None]
                elif enemy_action == 'Fold':
                    self.playable_actions =  [None, None, None, None, None, None]
            if self.position == 0:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions =  ['Call', None, 'Fold', None, None, None]
                elif enemy_action == 'Check':
                    self.playable_actions =  [None, 'Raise', None, 'Check', None, None]
                elif enemy_action == 'Call':
                    self.playable_actions =  [None, None, None, None, None, None]
                elif enemy_action == 'Raise':
                    self.playable_actions =  ['Call', 'Raise', 'Fold', None, None, None]

                elif enemy_action == 'Fold':
                    self.playable_actions =  [None, None, None, None, None, None]

    def odd_calculator_for_two_cards(self, culoare, carte1, carte2):
        score = 0
        if carte1 == 15:
            score += 10
        elif carte1 == 14:
            score += 8
        elif carte1 == 13:
            score += 7
        elif carte1 == 12:
            score += 6
        elif carte1 % 2 == 0:
            score += carte1 / 2
        elif carte1 % 2 == 1:
            score += carte1 / 2 + 0.5
        if carte2 == 15:
            score += 10
        elif carte2 == 14:
            score += 8
        elif carte2 == 13:
            score += 7
        elif carte2 == 12:
            score += 6
        elif carte2 % 2 == 0:
            score += carte2 / 2
        elif carte2 % 2 == 1:
            score += carte2 / 2 + 0.5

        if culoare[0] == culoare[1]:
            score += 2

        if abs(carte1 - carte2) == 1:
            score -= 1
        elif abs(carte1 - carte2) == 2:
            score -= 2
        elif abs(carte1 - carte2) == 3:
            score -= 4
        elif abs(carte1 - carte2) >= 4:
            score -= 5

        if carte1 < 13 and carte2 < 13 and abs(carte1 - carte2) <= 1:
            score += 1
        if score < 0:
            score = 0
        return int(score)

    def calculate_reward(self, pot, bigB, winner):
        reward = 0
        if winner == 1:
            reward += 1

        elif winner == 2:
            reward -= 1

        elif winner == 0:
            reward = 0

    def check_hand(self):
        scor_mana = 0
        nCards = []
        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(self.carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(self.carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = full_house(self.carti)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(self.carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(self.carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(self.carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(self.carti)
        if scor_mana == 0:
            return scor_mana, self.carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana

    def calculate_bet(self, opponent_action, opponent_bet, bigB, smallB):

        if self.action == 'Call' and self.position == 1 and opponent_action == '' and self.moment == 'Preflop':
            self.bet = bigB - smallB
            self.points -= self.bet
        elif self.action == 'Raise':
            index = self.index_raise()
            self.determine_raise(index, bigB, opponent_action, opponent_bet)
            # self.bet = smallB + 2*bigB
            # self.points -= self.bet
        elif self.action == 'Check' or self.action == 'Fold':
            self.bet = 0
            self.points -= self.bet
        elif self.action == 'Call' and self.points > opponent_bet:
            self.bet = opponent_bet
            self.points -= self.bet

        elif self.action == 'Call' or self.action == 'All-In' and self.points <= opponent_bet:
            # self.action = 'All-In'
            self.bet = self.points
            self.points = 0
        elif self.action == 'Raise':
            index = self.index_raise()
            self.determine_raise(index, bigB, opponent_action, opponent_bet)
        elif self.action == 'Raise':
            index = self.index_raise()
            self.determine_raise(index, bigB, opponent_action, opponent_bet)

        elif opponent_action is None and self.position == 1 and self.action == 'Call':
            self.bet = smallB
            self.points -= self.bet
        elif self.action is None:
            self.bet = 0
            self.points -= self.bet


    def determine_state(self, pot, bigB):

        self.state[0] = self.score
        if pot / bigB <= 6:
            self.state[1] = 0
        elif pot / bigB <= 12:
            self.state[1] = 1
        else:
            self.state[2] = 2
        if self.points / bigB <= 50:
            self.state[2] = 0
        elif self.points / bigB <= 100:
            self.state[2] = 1
        else:
            self.state[2] = 2

    def initialize_genes(self):
        for i in range(4):
            for j in range(15):
                if (j+1) % 5 != 0:
                    self.genes[i][j] = np.random.uniform(0,5,1)
                else:
                    self.genes[i][j] = 0 # pentru none
                self.raise_genes[j] = np.random.uniform(0, 5, 1)





    def determine_ecuation(self):
        if self.moment == 'Preflop':
            i = 0
        elif self.moment == 'Flop':
            i = 1
        elif self.moment == 'Turn':
            i = 2
        elif self.moment == 'River':
            i = 3
        self.callEcuation = (self.state[0]+1)*self.genes[i][0] + (self.state[1]+1)*self.genes[i][5] + (self.state[2]+1)*self.genes[i][10]
        self.raiseEcuation = (self.state[0]+1)*self.genes[i][1] + (self.state[1]+1)*self.genes[i][6] + (self.state[2]+1)*self.genes[i][11]
        self.foldEcuation = (self.state[0]+1)*self.genes[i][2] + (self.state[1]+1)*self.genes[i][7] + (self.state[2]+1)*self.genes[i][12]
        self.checkEcuation = (self.state[0]+1)*self.genes[i][3] +(self.state[1]+1)*self.genes[i][8] + (self.state[2]+1)*self.genes[i][13]
        # self.noneEcuation = (self.state[0]+1)*self.genes[i][4] + (self.state[1]+1)*self.genes[i][9] + (self.state[2]+1)*self.genes[i][14]
        self.noneEcuation = 0
        # # print('none',self.noneEcuation)
        S = self.callEcuation + self.raiseEcuation + self.foldEcuation + self.checkEcuation

        self.callEcuation = self.callEcuation / S
        self.raiseEcuation = self.raiseEcuation / S
        self.foldEcuation = self.foldEcuation / S
        self.checkEcuation = self.checkEcuation / S

        self.ecuation_vector[0] = self.callEcuation
        self.ecuation_vector[1] = self.raiseEcuation
        self.ecuation_vector[2] = self.foldEcuation
        self.ecuation_vector[3] = self.checkEcuation
        self.ecuation_vector[4] = self.noneEcuation


    def determine_ecuation_for_raise(self):

        self.raiseEcuationOne = (self.state[0]+1)*self.raise_genes[0] + (self.state[1]+1)*self.raise_genes[5] + (self.state[2]+1)*self.raise_genes[10]
        self.raiseEcuationTwo = (self.state[0]+1)*self.raise_genes[1] + (self.state[1]+1)*self.raise_genes[6] + (self.state[2]+1)*self.raise_genes[11]
        self.raiseEcuationThree = (self.state[0]+1)*self.raise_genes[2] + (self.state[1]+1)*self.raise_genes[7] + (self.state[2]+1)*self.raise_genes[12]
        self.raiseEcuationFour = (self.state[0]+1)*self.raise_genes[3] +(self.state[1]+1)*self.raise_genes[8] + (self.state[2]+1)*self.raise_genes[13]
        self.raiseEcuationFive = (self.state[0]+1)*self.raise_genes[4] + (self.state[1]+1)*self.raise_genes[9] + (self.state[2]+1)*self.raise_genes[14]

        S = self.raiseEcuationOne + self.raiseEcuationTwo + self.raiseEcuationThree + self.raiseEcuationFour + self.raiseEcuationFive

        self.raiseEcuationOne = self.raiseEcuationOne / S
        self.raiseEcuationTwo = self.raiseEcuationTwo / S
        self.raiseEcuationThree = self.raiseEcuationThree / S
        self.raiseEcuationFour = self.raiseEcuationFour / S
        self.raiseEcuationFive = self.raiseEcuationFive / S

        self.raise_vector[0] = self.raiseEcuationOne
        self.raise_vector[1] = self.raiseEcuationTwo
        self.raise_vector[2] = self.raiseEcuationThree
        self.raise_vector[3] = self.raiseEcuationFour
        self.raise_vector[4] = self.raiseEcuationFive




    def calculate_fitness(self, winner):
        if winner == 1:
            self.fitness += 1
        elif winner == 2:
            self.fitness -= 1
        elif winner == 0:
            self.fitness += 0

    def select_actions(self, rounds, enemy_action):

        self.determine_actions(enemy_action)
        self.determine_ecuation()


        dim = 0
        ok_none = 1
        for i in range(len(self.playable_actions)):
            if self.playable_actions[i] is not None:
                ok_none = 0
                dim += 1
        acVector = [0]*dim
        probVector = [0]*dim

        if ok_none == 1:

            self.action = None
            return

        j = 0
        for i in range (len(self.playable_actions)):
            if self.playable_actions[i] is not None:
                acVector[j] = self.playable_actions[i]
                probVector[j] = self.ecuation_vector[i][0]
                # posVector[j] = i
                j += 1
        S = sum(probVector)
        if S < 1:
            for i in range(len(probVector)):
                probVector[i] = probVector[i] / S
        draw = choice(acVector, 1, p=probVector)
        draw = to_str_harcoded(draw)
        self.action = draw

    def index_raise(self):
        self.determine_ecuation_for_raise()
        index_list = [0,1,2,3,4]
        probVector = [None]*5
        for i in range(5):
            probVector[i] = self.raise_vector[i][0]
        x = choice(index_list, 1, p=probVector)
        return x

    def determine_raise(self,index, bigB, enemy_action, enemy_bet):
        if enemy_action != 'Raise':
            if index == 0:
                self.bet = bigB
            elif index == 1:
                self.bet = 2*bigB
            elif index == 2:
                self.bet = 4*bigB
            elif index == 3:
                self.bet = 6*bigB
            elif index == 4:
                self.bet = 8*bigB
            if self.bet >= self.points:
                self.bet = self.points
                self.points = 0
            elif self.bet < self.points:
                self.points -= self.bet
        elif enemy_action == 'Raise':
            if index == 0:
                self.bet = bigB + enemy_bet
            elif index == 1:
                self.bet = 2 * bigB + enemy_bet
            elif index == 2:
                self.bet = 4 * bigB + enemy_bet
            elif index == 3:
                self.bet = 6 * bigB + enemy_bet
            elif index == 4:
                self.bet = 8 * bigB + enemy_bet
            if self.bet >= self.points:
                self.bet = self.points
                self.points = 0
            elif self.bet < self.points:
                self.points -= self.bet



