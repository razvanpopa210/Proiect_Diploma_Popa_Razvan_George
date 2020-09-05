import numpy as np
from numpy.random import choice
import QAgent as q
import GAagent as ga
import time

f = open("ga.txt", "w")
p = open('qtable.txt', 'w')

varix = 0
smallB_global = 20
bigB_global = 40

cards = {

    'Rosu': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Negru': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Romb': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Trefla': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

}
new_cards = {}

# score de la 0 la 10
score_matrix = [
    # 2, 3, 4, 5, 6, 7, 8, 9,10,12,13,14,15
    [3, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 2],  # 2
    [1, 3, 2, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2],  # 3
    [1, 1, 3, 2, 2, 2, 1, 0, 1, 1, 1, 2, 2],  # 4
    [1, 1, 2, 3, 2, 2, 1, 1, 0, 1, 1, 2, 2],  # 5
    [1, 1, 2, 2, 4, 2, 1, 1, 1, 1, 1, 2, 2],  # 6
    [0, 1, 2, 2, 2, 4, 2, 2, 2, 2, 1, 2, 2],  # 7
    [1, 0, 1, 1, 1, 2, 4, 2, 2, 2, 2, 2, 2],  # 8
    [1, 1, 0, 1, 1, 2, 2, 5, 4, 3, 3, 3, 2],  # 9
    [1, 1, 1, 0, 1, 2, 2, 4, 6, 3, 3, 3, 3],  # 10
    [1, 1, 2, 0, 1, 2, 2, 4, 6, 7, 4, 4, 4],  # 12
    [1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 8, 5, 5],  # 13
    [2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5, 9, 8],  # 14
    [2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 8, 10],  # 15

]
culori = ['Rosu', 'Negru', 'Romb', 'Trefla']

states = ['Check', 'Call', 'Raise', 'Fold']

possible_hands = ['Carte Mare', 'Pereche', 'Doua Perechi', 'Trei Asemenea', 'Chinta', 'Culoare', 'Full House', 'Careu',
                  'Chinta de culoare', 'Chinta Royala']

def print_or_not(training_rounds, jocuriDiferite, flag):
    if flag == 1 and training_rounds == jocuriDiferite - 1:
        return 1
    elif flag == 0:
        return 0

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
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
        chinta.append(int(carti_straight[5]))
        chinta.append(int(carti_straight[6]))
        return 4, chinta, 'Chinta'

    if isinstance(carti_straight[5], str):
        carti_straight = np.delete(carti_straight, 5)
        carti_straight = np.delete(carti_straight, 5)
    elif isinstance(carti_straight[6], str):
        carti_straight = np.delete(carti_straight, 6)
    contor = 0
    chinta = []



    if int(carti_straight[4]) - int(carti_straight[0]) == 4:
        chinta.append(int(carti_straight[0]))
        chinta.append(int(carti_straight[1]))
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
    if len(carti_straight) == 6:
        if int(carti_straight[5]) - int(carti_straight[1]) == 4:
            chinta = []
            chinta.append(int(carti_straight[1]))
            chinta.append(int(carti_straight[2]))
            chinta.append(int(carti_straight[3]))
            chinta.append(int(carti_straight[4]))
            chinta.append(int(carti_straight[5]))
    elif len(carti_straight) == 7:
        if int(carti_straight[6]) - int(carti_straight[2]) == 4:
            chinta = []
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
                if full[item2] == 3:
                    full_array.append(item)
                    full_array.append(item2)

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
        else:
            return ok, nCards, mana

    else:
        return 0, nCards, 'Carte Mare'


def to_str_harcoded(word):
    if word == 'Rosu':
        word = 'Rosu'
    elif word == 'Negru':
        word = 'Negru'
    elif word == 'Romb':
        word = 'Romb'
    else:
        word = 'Trefla'
    return word


def modify_by_state(state, points, call_bet, raise_bet):
    if state == 'Check' or state == 'Fold':
        points -= 0
    elif state == 'Call':
        points -= call_bet
    elif state == 'Raise':
        points -= raise_bet

class kPlayer:
    def __init__(self, points, position):
        self.score = 0
        self.points = points
        self.action = ''
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.best_of_five = [None] * 5
        self.mana = ''
        self.position = position

        self.win_counter = 0

        self.bet = 0

        self.play = 0

        self.playable_actions = ['a'] * 6

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
        print('scorul tau este: ', score)
        return int(score)

    def define_playable_actions(self, moment, enemy_action):
        if moment == 'Preflop':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                # elif enemy_action == 'Call' or enemy_action == 'Fold' or enemy_action == 'Check':
                #     self.playable_actions = [None]
            elif self.position == 0:
                if enemy_action == 'Call':
                    self.playable_actions = ['Raise', 'Check', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', '', 'All-In']
                elif enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]  # MEMENTO
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
        elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]
            if self.position == 0:
                if enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]

    def take_decision(self, moment, enemy_action, enemy_points):
        self.define_playable_actions(moment,enemy_action)
        if moment == 'Preflop':
            print('cartile din mana sunt: ', self.carti[0], self.carti[1])
            print('culorile din mana sunt: ', self.culori[0], self.culori[1])
            print('punctele dumneavoastra sunt: ', self.points)
        elif moment == 'Flop':
            print('cartile din mana sunt: ', self.carti[0], self.carti[1], self.carti[2], self.carti[3], self.carti[4])
            print('culorile din mana sunt: ', self.culori[0], self.culori[1], self.culori[2], self.culori[3], self.culori[4])
            print('punctele dumneavoastra sunt: ', self.points)
        elif moment == 'Turn':
            print('cartile din mana sunt: ', self.carti[0], self.carti[1], self.carti[2], self.carti[3], self.carti[4], self.carti[5])
            print('culorile din mana sunt: ', self.culori[0], self.culori[1], self.culori[2], self.culori[3], self.culori[4], self.culori[5])
            print('punctele dumneavoastra sunt: ', self.points)
        elif moment == 'River':
            print('cartile din mana sunt: ', self.carti[0], self.carti[1], self.carti[2], self.carti[3], self.carti[4], self.carti[5], self.carti[6])
            print('culorile din mana sunt: ', self.culori[0], self.culori[1], self.culori[2], self.culori[3], self.culori[4], self.culori[5], self.culori[6])
            print('punctele dumneavoastra sunt: ', self.points)
        if None in self.playable_actions:
            print('nu puteti alege decat actiunea None')
            self.action = None
        else:
            print('alegeti o actiune: ')
            self.action = str(input())
            if self.action not in self.playable_actions:
                print('actiunea nu este permisa, va rugam alegeti alta actiune')
                print(self.playable_actions)
                self.action = str(input())

    def calculate_a_bet(self, enemy_bet, smallB, bigB, enemy_action, moment):
        if self.action == 'Call' and self.position == 1 and moment == 'Preflop' and (enemy_action == '' or enemy_action is None):
            self.bet = bigB - smallB
            if self.points > self.bet:
                # self.bet = enemy_bet
                print('ati platit big blind')
                self.points -= self.bet
            elif self.points <= self.bet:
                print('nu aveti suficiente fonduri pentru pariu, sunteti all-in')
                self.bet = self.points
                self.points = 0
                # self.action = 'All-In'
        elif self.action == 'Call':
            self.bet = enemy_bet
            if self.points > enemy_bet:
                print('ati platit opariul adversarului')
                self.points -= enemy_bet
            else:
                print('nu aveti suficiente fonduri pentru pariu, sunteti all-in')
                self.bet = self.points
                self.points = 0
        elif self.action == 'Check' or self.action == 'Fold' or self.action == '' or self.action is None:
            self.bet = 0
            self.points -= self.bet
        elif self.action == 'Raise' and enemy_action == 'Raise':
            if self.points > enemy_bet:
                print('plasati un pariu peste al adversarului')
                self.bet = int(input())
                self.bet += enemy_bet
                if self.bet >= self.points:
                    print('ati depasit punctele, sunteti all in')
                    self.bet = self.points
                    self.points = 0
                else:
                    self.points -= self.bet
            elif self.points < enemy_bet:
                print('pariul adversarului depaseste punctele dumneavoastra, sunteti all-in')
                self.bet = self.points
                self.action = None
                self.points = 0
        elif self.action == 'Raise':
            print('plasati un pariu ')
            self.bet = int(input())

            if self.bet >= self.points:
                print('ati depasit punctele, sunteti all in')
                self.bet = self.points
                self.points = 0
            else:
                self.points -= self.bet
    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        for i in range(len(self.carti)):
            carti.append(self.carti[i])

        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = full_house(carti)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana


class looseAgressivePlayer:

    def __init__(self, points, position):

        self.score = 0
        self.points = points
        self.action = ''
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.best_of_five = [None] * 5
        self.mana = ''
        self.position = position

        self.bet = 0

        self.procent = 0.28

        self.play = 0

        self.playable_actions = ['a'] *6

    def odd_calculator_for_two_cards(self,culoare, carte1, carte2):
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


    def take_decision(self, moment, enemy_action):
        x = np.random.random()

        if (x <= self.procent):
            self.play = 1
        else:
            self.action = 'Fold'
            self.play = 0
        if self.play == 1:
            if moment == 'Preflop':
                if position == 1:
                    if enemy_action is None or enemy_action == '':
                        self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                    elif enemy_action == 'All-In':
                        self.playable_actions = ['Call', 'Fold', 'Check', 'All-In']
                    elif enemy_action == 'Raise':
                        self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif position == 0:
                    if enemy_action == 'Call':
                        self.playable_actions = ['Raise', 'Check', 'All-In']
                    elif enemy_action == 'Raise':
                        self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                    elif enemy_action == 'All-In':
                        self.playable_actions = ['Call', 'Fold', '', 'All-In']
                    elif enemy_action is None or enemy_action == '':
                        self.playable_actions = ['Raise', 'Fold', 'All-In']
                    elif enemy_action == 'Fold':
                        self.playable_actions = [None]  # MEMENTO
            elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
                if position == 1:
                    if enemy_action is None or enemy_action == '':
                        self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                    elif enemy_action == 'Check':
                        self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                    elif enemy_action == 'Call':
                        self.playable_actions = [None]
                    elif enemy_action == 'Raise':
                        self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                    elif enemy_action == 'All-In':
                        self.playable_actions = ['Call', 'Fold', 'All-In']
                    elif enemy_action == 'Fold':
                        self.playable_actions = [None]
                if position == 0:
                    if enemy_action == 'Check':
                        self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                    elif enemy_action == 'Call':
                        self.playable_actions = [None]
                    elif enemy_action == 'Raise':
                        self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                    elif enemy_action == 'All-In':
                        self.playable_actions = ['Call', 'Fold', 'All-In']
                    elif enemy_action == 'Fold':
                        self.playable_actions = [None]
        if 'Raise' in self.playable_actions:
            if self.score >= 3 and self.score <=10:
                self.action = 'Raise'
            elif self.score >10:
                self.action = 'All-In'
            elif self.score < 3 and 'Call' in self.playable_actions:
                self.action = 'Call'
        elif 'Call' in self.playable_actions:
            if self.score >=1:
                self.action = 'Call'
            else:
                self.action = 'Fold'
        elif 'Check' in self.playable_actions:
            if self.score <1:
                self.action = 'Check'
        else:
            self.action = 'Fold'



    def calculate_a_bet(self, enemy_bet, bigB):
        if self.action == 'Raise':
            if enemy_bet < 2*bigB and self.points >= 2*bigB :
                self.bet = 2*bigB
                if self.bet >= self.points:
                    self.action = 'All-In'
                    self.points = 0
                else:
                    self.points -= self.bet
            elif self.points >= enemy_bet + 2*bigB:
                self.bet = enemy_bet + 2*bigB
                self.points -= self.bet
            else:
                self.bet = self.points
                self.action = 'All-In'
                self.points = 0
        elif self.action == 'Check' or self.action == 'Fold':
            self.bet = 0
        elif self.action == 'Call' and self.points > enemy_bet:
            self.bet = enemy_bet
            self.points -= self.bet
        elif self.action == 'Call' or self.action == 'All-In' and self.points <= enemy_bet:
            self.bet = self.points
            self.action = 'All-In'
            self.points = 0
        elif self.action is None:
            self.bet = 0


    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        for i in range(len(self.carti)):
            carti.append(self.carti[i])

        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = full_house(carti)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)           #DE MODIFICAT PENTRU CA DACA ARE SI PERECHE SI CULOARE ALEGE PERECHEA
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana

class alwaysCall:

    def __init__(self, points, position):
        self.score = 0
        self.points = points
        self.action = ''
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.best_of_five = [None] * 5
        self.mana = ''
        self.position = position

        self.win_counter = 0

        self.bet = 0

        self.play = 0

        self.playable_actions = ['a'] * 6

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

    def define_playable_actions(self, moment, enemy_action):
        if moment == 'Preflop':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
            elif self.position == 0:
                if enemy_action == 'Call':
                    self.playable_actions = ['Raise', 'Check', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', '', 'All-In']
                elif enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]  # MEMENTO
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
        elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]
            if self.position == 0:
                if enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]

    def take_decision(self, moment, enemy_action, enemy_points):

        self.define_playable_actions(moment, enemy_action)
        # if self.position == 1 and enemy_action == '':
        #     self.action = ''
        if 'Call' in self.playable_actions:
            self.action = 'Call'
        elif 'Check' in self.playable_actions:
            self.action  = 'Check'
        elif 'Fold' in self.playable_actions:
            self.action = 'Fold'
        elif None in self.playable_actions:
            self.action = None


    def calculate_a_bet(self, enemy_bet, smallB, bigB, enemy_action, moment):
        if self.action == 'Call' and self.position == 1 and moment == 'Preflop' and (enemy_action == '' or enemy_action is None):
            self.bet = bigB - smallB
            if self.points > self.bet:
                self.points -= self.bet
            elif self.points <= self.bet:
                self.bet = self.points
                self.points = 0
        elif self.action == 'Call':
            self.bet = enemy_bet
            if self.points > enemy_bet:
                self.points -= enemy_bet
            else:
                self.bet = self.points
                self.points = 0
        elif self.action == 'Check' or self.action == 'Fold' or self.action == '' or self.action is None:
            self.bet = 0
            self.points -= self.bet

    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        mana = ''
        for i in range(len(self.carti)):
            carti.append(self.carti[i])
        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = full_house(carti)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)           #DE MODIFICAT PENTRU CA DACA ARE SI PERECHE SI CULOARE ALEGE PERECHEA
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana

class bigScore:

    def __init__(self, points, position):
        self.score = 0
        self.points = points
        self.action = ''
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.best_of_five = [None] * 5
        self.mana = ''
        self.position = position

        self.bet = 0

        self.win_counter = 0

        self.play = 0

        self.playable_actions = ['a'] * 6

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

    def define_playable_actions(self, moment, enemy_action):
        if moment == 'Preflop':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Call','Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
            elif self.position == 0:
                if enemy_action == 'Call':
                    self.playable_actions = ['Raise', 'Check', 'All-In']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', '', 'All-In']
                elif enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]  # MEMENTO
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
        elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]
            if self.position == 0:
                if enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check', 'All-In']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold', 'All-In']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]


    def take_decision(self, moment, enemy_action, enemy_points):

        self.define_playable_actions(moment, enemy_action)
        if moment == 'Preflop':
            if self.score >= 8:
                if 'Call' in self.playable_actions:
                    self.action = 'Call'
                elif 'Check' in self.playable_actions:
                    self.action = 'Check'
                elif 'Fold' in self.playable_actions:
                    self.action = 'Fold'
            elif 'Check' in self.playable_actions:
                self.action = 'Check'
            elif 'Fold' in self.playable_actions:
                self.action = 'Fold'
            elif None in self.playable_actions:
                self.action = None
        elif moment == 'Flop':
            if self.score >= 8:
                if 'Call' in self.playable_actions:
                    self.action = 'Call'
                elif 'Check' in self.playable_actions:
                    self.action = 'Check'
                elif 'Fold' in self.playable_actions:
                    self.action = 'Fold'
                elif None in self.playable_actions:
                    self.action = None
            elif 'Check' in self.playable_actions:
                self.action = 'Check'
            elif 'Fold' in self.playable_actions:
                self.action = 'Fold'
            elif None in self.playable_actions:
                self.action = None
        elif moment == 'Turn' or moment == 'River':
            if self. score >= 8:
                if 'Call' in self.playable_actions:
                    self.action = 'Call'
                elif 'Check' in self.playable_actions:
                    self.action = 'Check'
                elif 'Fold' in self.playable_actions:
                    self.action = 'Fold'
                elif None in self.playable_actions:
                    self.action = None
            elif 'Check' in self.playable_actions:
                self.action = 'Check'
            elif 'Fold' in self.playable_actions:
                self.action = 'Fold'
            elif None in self.playable_actions:
                self.action = None


    def calculate_a_bet(self, enemy_bet, smallB, bigB, enemy_action, moment):
        if self.action == 'Call' and self.position == 1 and moment == 'Preflop' and (enemy_action == '' or enemy_action is None):
            self.bet = bigB - smallB
            if self.points > self.bet:
                # self.bet = enemy_bet
                self.points -= self.bet
            elif self.points <= self.bet:
                self.bet = self.points
                self.points = 0
                # self.action = 'All-In'
        elif self.action == 'Call':
            self.bet = enemy_bet
            if self.points > enemy_bet:
                self.points -= enemy_bet
            else:
                self.bet = self.points
                self.points = 0
        elif self.action == 'Check' or self.action == 'Fold' or self.action == '' or self.action is None:
            self.bet = 0
            self.points -= self.bet
        elif self.action is None:
            self.bet = 0
            self.points -= self.bet
        elif self.action == 'Raise' and enemy_action == 'Raise':
            if self.points > enemy_bet:
                print('plasati un pariu peste al adversarului')
                self.bet = int(input())
                self.bet += enemy_bet
                if self.bet >= self.points:
                    print('ati depasit punctele, sunteti all in')
                    self.bet = self.points
                    self.points = 0
                else:
                    self.points -= self.bet
            elif self.points < enemy_bet:
                print('pariul adversarului depaseste punctele dumneavoastra, sunteti all-in')
                self.bet = self.points
                self.action = None
                self.points = 0
        elif self.action == 'Raise':
            print('plasati un pariu ')
            self.bet = int(input())

            if self.bet >= self.points:
                print('ati depasit punctele, sunteti all in')
                self.bet = self.points
                self.points = 0
            else:
                self.points -= self.bet


    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        for i in range(len(self.carti)):
            carti.append(self.carti[i])

        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            print('full', self.carti)
            scor_mana, nCards, mana = full_house(carti)
            print(scor_mana)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana


class randomPlayer:
    def __init__(self, points, position):
        self.score = 0
        self.points = points
        self.action = ''
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.best_of_five = [None] * 5
        self.mana = ''
        self.position = position

        self.bet = 0

        self.win_counter = 0

        self.moment = 'Preflop'

        self.play = 0

        self.playable_actions = ['a'] * 6

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

    def define_playable_actions(self, moment, enemy_action):
        if moment == 'Preflop':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Call','Raise', 'Fold']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold']
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold']

                elif enemy_action == 'Call' or enemy_action == 'Fold' or enemy_action == 'Check':
                    self.playable_actions = [None]

            elif self.position == 0:
                if enemy_action == 'Call' and self.action == '':
                    self.playable_actions = ['Raise', 'Check']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold']
                elif enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]  # MEMENTO
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check']
        elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
            if self.position == 1:
                if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                    self.playable_actions = ['Raise', 'Fold', 'Check']
                elif enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold', 'All-In']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]
            if self.position == 0:
                if enemy_action == 'Check':
                    self.playable_actions = ['Raise', 'Fold', 'Check']
                elif enemy_action == 'Call':
                    self.playable_actions = [None]
                elif enemy_action == 'Raise':
                    self.playable_actions = ['Call', 'Raise', 'Fold']
                elif enemy_action == 'All-In':
                    self.playable_actions = ['Call', 'Fold']
                elif enemy_action == 'Fold':
                    self.playable_actions = [None]

    def to_str_harcoded(self, word):
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

    def take_decision(self, moment, enemy_action, enemy_points):

        x = np.random.random()
        ok = 0
        self.define_playable_actions(moment, enemy_action)
        for i in range (len(self.playable_actions)):
            if self.playable_actions[i] is not None:
                ok = 1
        if ok == 0:
            self.action = None
        elif ok == 1:
            self.action = choice(self.playable_actions, 1)
            while self.action == 'Fold' and x > 0.10:
                self.action = choice(self.playable_actions, 1)
            self.action = self.to_str_harcoded(self.action)
        if self.action == 'Raise' and enemy_points <= 0:
            self.action = None

    def calculate_a_bet(self, enemy_bet, smallB, bigB, enemy_action, moment):
        if self.action == 'Call' and self.position == 1 and enemy_action == '' and self.moment == 'Preflop':
            self.bet = bigB - smallB
            self.points -= self.bet
        elif self.action == 'Raise' and self.position == 1 and enemy_action == '' and self.moment == 'Preflop':

            self.bet = smallB + 2 * bigB
            if self.points < self.bet:
                self.bet = self.points
                self.points = 0
            else:
                self.points -= self.bet
        elif self.action == 'Check' or self.action == 'Fold':
            self.bet = 0
            self.points -= self.bet
        elif self.action == 'Call' and self.points > enemy_bet:
            self.bet = enemy_bet
            self.points -= self.bet
        elif self.action == 'Call' and self.points < enemy_bet:
            self.bet = self.points
            self.points = 0

        elif self.action == 'Call' or self.action == 'All-In' and self.points <= enemy_bet:
            self.bet = self.points
            self.points = 0
        elif self.action == 'Raise' and enemy_action == 'Raise':
            if self.points > enemy_bet + 2 * bigB:
                self.bet = enemy_bet + 2 * bigB
                self.points -= self.bet
            elif self.points > enemy_bet + bigB:
                self.bet = enemy_bet + bigB
                self.points -= self.bet
            elif self.points < enemy_bet:
                self.bet = self.points
                self.action = None
                self.points = 0
        elif self.action == 'Raise':
            if self.points > 2 * bigB:
                self.bet = 2 * bigB
                self.points -= self.bet
            elif self.points > 2 * bigB:
                self.bet = bigB
                self.points -= self.bet
            elif self.points < self.bet:
                self.bet = self.points
                self.points = 0
        elif enemy_action is None and self.position == 1 and self.action == 'Call':
            self.bet = smallB
            self.points -= self.bet
        elif self.action is None:
            self.bet = 0
            self.points -= self.bet

    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        for i in range(len(self.carti)):
            carti.append(self.carti[i])

        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            print('full', self.carti)
            scor_mana, nCards, mana = full_house(carti)
            print(scor_mana)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana


class Player:
    def __init__(self, score, points, states, action, culori, carti, best_of_five, mana, position, bet):
        self.score = score
        self.points = points
        self.states = states
        self.action = action
        self.culori = culori
        self.carti = carti
        self.best_of_five = best_of_five
        self.mana = mana
        self.position = position
        self.bet = bet

    def draw_pre_flop(self, d):
        culoare = choice(culori, 2)
        culoare[0] = to_str_harcoded(culoare[0])
        culoare[1] = to_str_harcoded(culoare[1])
        carte1 = choice(d[culoare[0]], 1)
        d[culoare[0]].remove(carte1)
        carte2 = choice(d[culoare[1]], 1)
        # print('Jucatorul a tras cartea ', carte1, ' de ', culoare[0], 'si ', carte2, 'de culoare', culoare[1])
        return culoare, carte1, carte2

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

    def how_to_play(self, position, score):
        if position == 0:
            if score >= 0 and score <= 4:
                action1 = self.states[0]
            elif score >= 5:
                action1 = self.states[2]
        if position == 1:
            if score == 0:
                action2 = self.states[3]
            elif 1 <= score <= 4:
                action2 = self.states[1]
            elif score >= 5:
                action2 = self.states[2]

    def take_decision(self, score_actual_player, moment):
        if moment == 'Preflop':
            if score_actual_player == 0:
                actionP1 = 'Fold'
            elif 1 <= score_actual_player <= 4:
                actionP1 = 'Call'
            elif score_actual_player >= 5:
                actionP1 = 'Raise'
        elif moment == 'Flop':
            if score_actual_player <= 7:
                actionP1 = 'Check'
            elif score_actual_player <= 10:
                actionP1 = 'Raise'
            else:
                actionP1 = 'All-In'

        elif moment == 'Turn':
            if score_actual_player <= 8:
                actionP1 = 'Check'
            elif score_actual_player <= 11:
                actionP1 = 'Raise'
            else:
                actionP1 = 'All-In'

        elif moment == 'River':
            if score_actual_player <= 9:
                actionP1 = 'Check'
            elif score_actual_player <= 12:
                actionP1 = 'Raise'
            else:
                actionP1 = 'All-In'


        return actionP1

    def take_decision_vs_enemy(self, score_actual_player, action_enemy, moment):
        if moment == 'Preflop':
            if action_enemy == 'Call' or action_enemy == 'Check':
                if 0 <= score_actual_player <= 4:
                    return 'Check'
                elif score_actual_player >= 5:
                    return 'Raise'
            elif action_enemy == 'Raise':
                if score_actual_player <= 5:
                    return 'Fold'
                elif 5 < score_actual_player <= 6:
                    return 'Call'
                elif score_actual_player >= 7:
                    return 'Raise'
                elif score_actual_player >=8:
                    return 'All-In'
            elif action_enemy == 'Fold':
                # print('The other player folds')
                return None
            elif action_enemy == 'All-In':
                if score_actual_player >= 7:
                    return 'All-In'
                else:
                    return 'Fold'


        elif moment == 'Flop':
            if action_enemy == 'Check':
                if 0 <= score_actual_player <= 7:
                    return 'Check'
                elif 7 < score_actual_player <= 10:
                    return 'Raise'
                elif 10 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Raise':
                if 0 <= score_actual_player <= 7:
                    return 'Fold'
                elif 7 < score_actual_player <= 10:
                    return 'Call'
                elif 10 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Fold':
                return None
            elif action_enemy == 'All-In':
                if score_actual_player >=11:
                    return 'Call'
                else:
                    return 'Fold'
        elif moment == 'Turn':
            if action_enemy == 'Check':
                if 0 <= score_actual_player <= 8:
                    return 'Check'
                elif 8 < score_actual_player <= 11:
                    return 'Raise'
                elif 11 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Raise':
                if 0 <= score_actual_player <= 8:
                    return 'Fold'
                elif 8 < score_actual_player <= 11:
                    return 'Call'
                elif 11 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Fold':
                # print('The other player folds')
                return None
            elif action_enemy == 'All-In':
                if score_actual_player >=11:
                    return 'Call'
                else:
                    return 'Fold'
        elif moment == 'River':
            if action_enemy == 'Check':
                if 0 <= score_actual_player <= 9:
                    return 'Check'
                elif 9 < score_actual_player <= 13:
                    return 'Raise'
                elif 13 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Raise':
                if 0 <= score_actual_player <= 9:
                    return 'Fold'
                elif 9 < score_actual_player <= 13:
                    return 'Call'
                elif 13 < score_actual_player:
                    return 'All-In'
            elif action_enemy == 'Fold':
                # print('The other player folds')
                return None
            elif action_enemy == 'All-In':
                if score_actual_player >=14:
                    return 'Call'
                else:
                    return 'Fold'

    def calculate_a_bet(self, score, player_action, enemy_action, enemy_bet, pot, points, moment, smallB, bigB):
        reraise = enemy_bet + score * 7
        if moment == 'Preflop':
            if enemy_action == 'Raise':
                if player_action == 'Raise':
                    if reraise < points:
                        return reraise
                    else:
                        self.action = 'All-In'
                        return points
                elif player_action == 'Call':
                    return enemy_bet
                elif player_action == 'Fold':
                    return 0
            elif enemy_action == '' and player_action == 'Raise':
                return pot
            elif enemy_action == 'Call' and player_action == 'Raise':
                return bigB
            elif enemy_action == 'Call' and player_action == 'Check':
                return 0
            elif player_action == 'Call':
                return smallB
            elif player_action == 'Fold' or player_action == None or enemy_action == 'Fold':
                return 0
            elif player_action == 'Check':
                return bigB
            elif enemy_action == 'All-In' and player_action == 'Call' or player_action == 'All-In':
                return points
            elif enemy_action == 'Check' and player_action == 'Raise':
                return 2*bigB
        elif moment == 'Flop':
            if enemy_action == 'Raise' and player_action == 'Raise':
                if reraise < points:
                    return reraise
                else:

                    return points
            elif enemy_action == 'Raise' and player_action == 'Call':
                return enemy_bet
            elif enemy_action == 'Raise' and player_action == 'Fold':
                return 0
            elif enemy_action == 'Check' and player_action == 'Check':
                return 0
            elif enemy_action == 'Check' and player_action == 'Raise':
                return 0.25*pot
            elif enemy_action == '' and player_action == 'Check':
                return 0
            elif enemy_action == '' and player_action == 'Raise':
                return 0.5*pot
            elif player_action == 'Fold' or player_action == None or enemy_action == 'Fold':
                return 0
            elif enemy_action == 'All-In' and player_action == 'Call' or player_action == 'All-In':
                return points
            elif enemy_action == 'All-In' and player_action == 'Fold':
                return 0
            elif player_action == 'All-In':
                return points

        elif moment == 'Turn':
            if enemy_action == 'Raise' and player_action == 'Raise':
                if reraise < points:
                    return reraise
                else:
                    return points
            elif enemy_action == 'Raise' and player_action == 'Call':
                return enemy_bet
            elif enemy_action == 'Raise' and player_action == 'Fold':
                return 0
            elif enemy_action == 'Check' and player_action == 'Check':
                return 0
            elif enemy_action == 'Check' and player_action == 'Raise':
                return 0.5*pot
            elif enemy_action == '' and player_action == 'Check':
                return 0
            elif enemy_action == '' and player_action == 'Raise':
                return pot
            elif player_action == 'Fold' or player_action == None or enemy_action == 'Fold':
                return 0
            elif enemy_action == 'All-In' and player_action == 'Call' or player_action == 'All-In':
                return points
            elif enemy_action == 'All-In' and player_action == 'Fold':
                return 0
            elif player_action == 'All-In':
                return points

        elif moment == 'River':
            if enemy_action == 'Raise' and player_action == 'Raise':
                if reraise < points:
                    return reraise
                else:
                    return points
            elif enemy_action == 'Raise' and player_action == 'Call':
                return enemy_bet
            elif enemy_action == 'Raise' and player_action == 'Fold':
                return 0
            elif enemy_action == 'Check' and player_action == 'Check':
                return 0
            elif enemy_action == 'Check' and player_action == 'Raise':
                return  pot
            elif enemy_action == '' and player_action == 'Check':
                return 0
            elif enemy_action == '' and player_action == 'Raise':
                return 2*pot
            elif player_action == 'Fold' or player_action == None or enemy_action == 'Fold':
                return 0
            elif enemy_action == 'All-In' and player_action == 'Call' or player_action == 'All-In':
                return points
            elif player_action == 'All-In':
                return points

    def check_hand(self):
        scor_mana = 0
        nCards = []
        carti = []
        for i in range(len(self.carti)):
            carti.append(self.carti[i])

        if scor_mana == 0:
            scor_mana, nCards, mana = straight_flush(carti, self.culori)
        if scor_mana == 0:
            scor_mana, nCards, mana = four_of_a_kind(carti)
        if scor_mana == 0:
            print('full', self.carti)
            scor_mana, nCards, mana = full_house(carti)
            print(scor_mana)
        if scor_mana == 0:
            scor_manaa, nCards, mana = flush(carti, self.culori)
        if scor_mana== 0:
            scor_mana, nCards, mana = straight(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = three_of_a_kind(carti)
        if scor_mana == 0:
            scor_mana, nCards, mana = pereche(carti)
        if scor_mana == 0:
            return scor_mana, carti, 'Carte Mare'
        else:
            return scor_mana, nCards, mana



class Dealer:

    def __init__(self, new_deck):
        self.new_deck = new_deck

    def make_the_new_deck(self, culoare_p1, carte1_p1, carte2_p1):
        self.new_deck[culoare_p1[0]].remove(carte1_p1[0])
        self.new_deck[culoare_p1[1]].remove(carte2_p1[0])
        return self.new_deck

    def draw_for_player(self, player):
        shuffle_deck = self.new_deck.copy()
        culoare_p, carte1_p, carte2_p = player.draw_pre_flop(shuffle_deck)
        self.new_deck = self.make_the_new_deck(culoare_p, carte1_p, carte2_p)
        return culoare_p, carte1_p, carte2_p

    def draw_for_player_v2(self):
        culoare = choice(culori, 2)
        culoare[0] = to_str_harcoded(culoare[0])
        culoare[1] = to_str_harcoded(culoare[1])
        carte1 = choice(self.new_deck[culoare[0]], 1)
        self.new_deck[culoare[0]].remove(carte1)
        carte2 = choice(self.new_deck[culoare[1]], 1)
        self.new_deck[culoare[1]].remove(carte2)
        # print('Jucatorul a tras cartea ', carte1, ' de ', culoare[0], 'si ', carte2, 'de culoare', culoare[1])
        return culoare[0], culoare[1], carte1[0], carte2[0]

    def draw_flop(self):
        culoare = choice(culori, 3)
        culoare[0] = to_str_harcoded(culoare[0])
        culoare[1] = to_str_harcoded(culoare[1])
        culoare[2] = to_str_harcoded(culoare[2])
        carte1 = choice(self.new_deck[culoare[0]], 1)
        self.new_deck[culoare[0]].remove(carte1)
        carte2 = choice(self.new_deck[culoare[1]], 1)
        self.new_deck[culoare[1]].remove(carte2)
        carte3 = choice(self.new_deck[culoare[2]], 1)
        self.new_deck[culoare[2]].remove(carte3)
        # print('Flop-ul a adus in joc cartile: ', carte1, ' de ', culoare[0], ' ', carte2, ' de ', culoare[1], ' ', carte3, ' de ', culoare[2])
        return culoare, carte1, carte2, carte3

    def draw_turn_river(self):
        culoare = choice(culori,1)
        culoare[0] = to_str_harcoded(culoare[0])
        carte = choice(self.new_deck[culoare[0]],1)
        self.new_deck[culoare[0]].remove(carte)
        # print('Urmatorul nivel a adus in joc cartea: ', carte, 'de: ', culoare[0])
        return culoare, carte

class Poker:

    def __init__(self, cards, new_deck):

        self.cards = cards
        self.new_deck = new_deck
        self.pot = 0
        self.rounds = 0
        self.split_rounds = 0
        self.flop_rounds = 0
        self.turn_rounds = 0
        self.river_rounds = 0

    def big_blind(self, position, p1Score, p2Score, smallB, bigB):
        if position == 0:
            p1Score -= bigB
            p2Score -= smallB
        else:
            p1Score -= smallB
            p2Score -= bigB
        return p1Score, p2Score

    def make_the_new_deck(self, culoare_p1, carte1_p1, carte2_p1, culoare_p2, carte1_p2, carte2_p2):
        new_deck = self.cards.copy()
        new_deck[culoare_p1[0]].remove(carte1_p1[0])
        new_deck[culoare_p1[1]].remove(carte2_p1[0])
        new_deck[culoare_p2[0]].remove(carte1_p2[0])
        new_deck[culoare_p2[1]].remove(carte2_p2[0])
        return new_deck


    def conducting_the_round(self, p1, p2, moment):
        flag = 1
        # print('conducting_the_round')
        p1.action = ''
        p2.action = ''
        p1.moment = moment
        if type(p2) == q.QAgent:
            p2.moment = moment
        if p1.position == 1:
            # print('Q este small blind')
            while p2.action != 'Check' and p2.action != 'Fold' and p1.action != 'Fold' and p2.action != 'Call':# and p1.action != 'Call':

                if p1.action is None and p2.action == 'Call':
                    break
                if p2.action is None and p1.action == 'Call':
                    break

                if p2.action == 'Raise' or p2.action == 'All-In':
                    p1.determine_state(self.pot, bigB_global)
                    p1.select_actions(self.rounds, p2.action)
                    if print_or_not(training_rounds, generation, flag = 1):
                        print('p1 action: ', p1.action)
                        print('p1 bet: ', p1.bet)
                        print('p1 points', p1.points)
                    p1.calculate_bet(p2.action, p2.bet, bigB_global, smallB_global)
                    self.pot += p1.bet
                    if p2.action != 'All-In':
                        if type(p2) != q.QAgent:
                            p2.take_decision(moment, p1.action, p1.points)
                            p2.calculate_a_bet(p1.bet, smallB_global, bigB_global, p1.action, moment)
                            self.pot += p2.bet
                            if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                                print('noob action: ', p2.action)
                                print('noob action bet: ', p2.bet)
                                print('noob action points: ', p2.points)
                        elif type(p2) == q.QAgent:
                            p2.determine_state(self.pot, bigB_global)
                            p2.select_actions(self.rounds, p1.action)
                            p2.calculate_bet(p1.action, p1.bet, bigB_global, smallB_global)
                            self.pot += p2.bet
                            if print_or_not(training_rounds, jocuriDiferite, flag):
                                print('noob action: ', p2.action)
                                print('noob action bet: ', p2.bet)
                                print('noob action points: ', p2.points)

                else:
                    p1.determine_state(self.pot, bigB_global)
                    p1.select_actions(self.rounds, p2.action)
                    p1.calculate_bet(p2.action, p2.bet, bigB_global, smallB_global)
                    self.pot += p1.bet
                    if print_or_not(training_rounds, jocuriDiferite, flag = 1):
                        print('p1 action: ', p1.action)
                        print('p1 bet: ', p1.bet)
                        print('p1 points', p1.points)
                    if type(p2) != q.QAgent:
                        p2.take_decision(moment, p1.action, p1.points)
                        p2.calculate_a_bet(p1.bet, smallB_global, bigB_global, p1.action, moment)
                        self.pot += p2.bet
                        if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                            print('noob action: ', p2.action)
                            print('noob Player bet: ', p2.bet)
                            print('noob player points: ', p2.points)
                    elif type(p2) == q.QAgent:
                        p2.determine_state(self.pot, bigB_global)
                        p2.select_actions(self.rounds, p1.action)
                        p2.calculate_bet(p1.action, p1.bet, bigB_global, smallB_global)
                        self.pot += p2.bet
                        if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                            print('noob action: ', p2.action)
                            print('noob Player bet: ', p2.bet)
                            print('noob player points: ', p2.points)
                if p1.action == 'All-In' and p2.action == 'All-In':
                    break
        elif p2.position == 1:
            while p1.action != 'Check' and p1.action != 'Fold' and p2.action != 'Fold' and p1.action != 'Call': #and p2.action != 'Call':
                if p1.action is None and p2.action == 'Call':
                    break
                if p2.action is None and p1.action == 'Call':
                    break
                if p1.action == 'Raise' or p1.action == 'All-In':
                    if type(p2) != q.QAgent:
                        p2.take_decision(moment, p1.action, p1.points)
                        p2.calculate_a_bet(p1.bet, smallB_global, bigB_global, p1.action, moment)
                        self.pot += p2.bet
                        if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                            print('noob action: ', p2.action)
                            print('noob Player bet: ', p2.bet)
                            print('noob player points: ', p2.points)
                    elif type(p2) == q.QAgent:
                        p2.determine_state(self.pot, bigB_global)
                        p2.select_actions(self.rounds, p1.action)
                        p2.calculate_bet(p1.action, p1.bet, bigB_global, smallB_global)
                        self.pot += p2.bet
                        if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                            print('noob action: ', p2.action)
                            print('noob Player bet: ', p2.bet)
                            print('noob player points: ', p2.points)
                    if p1.action != 'All-In':
                        p1.determine_state(self.pot, bigB_global)
                        p1.select_actions(self.rounds, p2.action)
                        p1.calculate_bet(p2.action, p2.bet, bigB_global, smallB_global)
                        self.pot += p1.bet
                        if print_or_not(training_rounds, jocuriDiferite, flag = 1):
                            print('p1 action: ', p1.action)
                            print('p1 bet: ', p1.bet)
                            print('p1 points', p1.points)

                else:
                    if type(p2) != q.QAgent:
                        p2.take_decision(moment, p1.action, p1.points)
                        p2.calculate_a_bet(p1.bet, smallB_global, bigB_global, p1.action, moment)
                    elif type(p2) == q.QAgent:
                        p2.determine_state(self.pot, bigB_global)
                        p2.select_actions(self.rounds, p1.action)
                        p2.calculate_bet(p1.action, p1.bet, bigB_global, smallB_global)
                    self.pot += p2.bet
                    if print_or_not(training_rounds, jocuriDiferite, flag = 0):
                        print('noob action: ', p2.action)
                        print('noob Player bet: ', p2.bet)
                        print('noob player points: ', p2.points)
                    p1.determine_state(self.pot, bigB_global)
                    p1.select_actions(self.rounds, p2.action)
                    p1.calculate_bet(p2.action, p2.bet, bigB_global, smallB_global)
                    self.pot += p1.bet
                    if print_or_not(training_rounds, jocuriDiferite, flag = 1):
                        print('p1 action: ', p1.action)
                        print('p1 bet: ', p1.bet)
                        print('p1 points', p1.points)
                if p1.action == 'All-In' and p2.action == 'All-In':
                    break

        return p1.points, p2.points


    def verify_winner_simple(self, p1, p2): # p1 devine Qplayer in viitor ( trebuie doar modificat pe aici )
        #
        index_manaP1 = possible_hands.index(p1.mana)
        index_manaP2 = possible_hands.index(p2.mana)

        if index_manaP1 > index_manaP2:
            winner =  1
        elif index_manaP2 > index_manaP1:
            winner =  2
        elif index_manaP1 == index_manaP2:
            if p1.mana == 'Pereche':
                if max(p1.best_of_five) > max(p2.best_of_five):
                    winner =  1
                elif max(p2.best_of_five) > max(p1.best_of_five):
                    winner =  2
                else:
                    carti_sortedP1 = p1.carti.copy()
                    carti_sortedP1.sort()
                    carti_sortedP2 = p2.carti.copy()
                    carti_sortedP2.sort()
                    if carti_sortedP1[len(carti_sortedP1) - 1] == max(p1.best_of_five):
                        kickerP1 = carti_sortedP1[len(carti_sortedP1) - 3]
                    else:
                        kickerP1 = carti_sortedP1[len(carti_sortedP1) - 1]
                    if carti_sortedP2[len(carti_sortedP2) - 1] == max(p2.best_of_five):
                        kickerP2 = carti_sortedP2[len(carti_sortedP2) - 3]
                    else:
                        kickerP2 = carti_sortedP2[len(carti_sortedP2) - 1]
                    if kickerP1 > kickerP2:
                        winner =  1
                    elif kickerP2 > kickerP1:
                        winner =  2
                    else:
                        winner =  0
            elif p1.mana == 'Doua Perechi':
                if max(p1.best_of_five) > max(p2.best_of_five):
                    winner =  1
                elif max(p2.best_of_five) > max(p1.best_of_five):
                    winner =  2
                else:
                    cartiCopyP1 = p1.carti.copy()
                    cartiCopyP2 = p2.carti.copy()
                    cartiCopyP1 = set(cartiCopyP1) - set(p1.best_of_five)
                    cartiCopyP2 = set(cartiCopyP2) - set(p2.best_of_five)
                    kickerP1 = max(cartiCopyP1)
                    kickerP2 = max(cartiCopyP2)
                    if kickerP1 > kickerP2:
                        winner =  1
                    elif kickerP2 > kickerP1:
                        winner =  2
                    else:
                        winner =  0
            elif p1.mana == 'Trei Asemenea':
                if max(p1.best_of_five) == max(p1.carti):
                    p1.carti.remove(max(p1.best_of_five))
                if max(p2.best_of_five) == max(p2.carti):
                    p2.carti.remove(max(p2.best_of_five))
                if max(p1.carti) > max(p2.carti):
                    winner =  1
                elif max(p2.carti) > max(p1.carti):
                    winner =  2
                else:
                    carti_sorted1 = p1.carti
                    carti_sorted1.sort()
                    carti_sorted2 = p2.carti
                    carti_sorted2.sort()
                    if carti_sorted1[len(carti_sorted1)-1] > carti_sorted2[len(carti_sorted2)-1]:
                        winner = 1
                    elif carti_sorted2[len(carti_sorted2)-1] > carti_sorted1[len(carti_sorted1)-1]:
                        winner = 2
                    elif carti_sorted1[len(carti_sorted1)-2] > carti_sorted2[len(carti_sorted2)-2]:
                        winner = 1
                    elif carti_sorted2[len(carti_sorted2)-2] > carti_sorted1[len(carti_sorted1)-2]:
                        winner = 2
                    else:
                        winner = 0
            elif p1.mana == 'Chinta' or p1.mana == 'Chinta de culoare':
                if max(p1.best_of_five) > max(p2.best_of_five):
                    winner =  1
                elif max(p2.best_of_five) > max(p1.best_of_five):
                    winner =  2
                else:
                    winner = 0
            elif p1.mana == 'Culoare':
                if max(p1.best_of_five) > max(p2.best_of_five):
                    winner =  1
                elif max(p2.best_of_five) > max(p1.best_of_five):
                    winner =  2
            elif p1.mana == 'Careu':
                if max(p1.best_of_five) == max(p1.carti):
                    p1.carti.remove(max(p1.best_of_five))
                if max(p2.best_of_five) == max(p2.carti):
                    p2.carti.remove(max(p2.best_of_five))
                if max(p1.carti) > max(p2.carti):
                    winner =  1
                elif max(p2.carti) > max(p1.carti):
                    winner =  2
                else:
                    carti_sorted1 = p1.carti
                    carti_sorted1.sort()
                    carti_sorted2 = p2.carti
                    carti_sorted2.sort()
                    if carti_sorted1[len(carti_sorted1)-1] > carti_sorted2[len(carti_sorted2)-1]:
                        winner = 1
                    elif carti_sorted2[len(carti_sorted2)-1] > carti_sorted1[len(carti_sorted1)-1]:
                        winner = 2
                    elif carti_sorted1[len(carti_sorted1)-2] > carti_sorted2[len(carti_sorted2)-2]:
                        winner = 1
                    elif carti_sorted2[len(carti_sorted2)-2] > carti_sorted1[len(carti_sorted1)-2]:
                        winner = 2
                    else:
                        winner = 0
            elif p1.mana == 'Full House':
                if p1.best_of_five[1] > p2.best_of_five[1]:
                    winner =  1
                elif p2.best_of_five[1] > p1.best_of_five[1]:
                    winner =  2
                elif p1.best_of_five[0] > p2.best_of_five[0]:
                    winner = 1
                elif p2.best_of_five[0] > p1.best_of_five[0]:
                    winner = 2
                else:
                    winner = 0
            elif p1.mana == 'Carte Mare':
                if max(p1.best_of_five) > max(p2.best_of_five):
                    winner =  1
                elif max(p2.best_of_five) > max(p1.best_of_five):
                    winner =  2
                else:
                    p1.best_of_five.sort()
                    p2.best_of_five.sort()
                    if (p1.best_of_five[1] > p2.best_of_five[1]):
                        winner = 1
                    elif (p2.best_of_five[1] > p1.best_of_five[1]):
                        winner = 2
                    elif (p1.best_of_five[2] > p2.best_of_five[2]):
                        winner = 1
                    elif (p2.best_of_five[2] > p1.best_of_five[2]):
                        winner = 2
                    elif (p1.best_of_five[3] > p2.best_of_five[3]):
                        winner = 1
                    elif (p2.best_of_five[3] > p1.best_of_five[3]):
                        winner = 2
                    elif (p1.best_of_five[4] > p2.best_of_five[4]):
                        winner = 1
                    elif (p2.best_of_five[4] > p1.best_of_five[4]):
                        winner = 2
                    else:
                        winner = 0

        if print_or_not(generation, jocuriDiferite, flag=1):
            if winner == 1:
                print ('ati pierdut')
                print('player 1 a castigat cu: ', possible_hands[index_manaP1], 'impotriva: ', possible_hands[index_manaP2])
            elif winner == 2:
                print ('ati castigat cu:', possible_hands[index_manaP2], 'impotriva: ', possible_hands[index_manaP1])
            elif winner == 0:
                print('este split')

        return winner


    def recalculate_score(self,p1,p2, indexPrecedentP1, indexPrecedentP2):

        index_manaP1 = possible_hands.index(p1.mana)
        index_manaP2 = possible_hands.index(p2.mana)

        p1.score += index_manaP1 - indexPrecedentP1
        p2.score += index_manaP2 - indexPrecedentP1

        return p1.score, p2.score




    def preflop(self, p1, p2, dealer, smallB, bigB): #si aici p1 va fi QPlayer
        flag = 1
        if print_or_not(training_rounds, jocuriDiferite, flag):
            print('este preflop')
        self.pot = smallB + bigB
        culori = [None]*2
        carti = [None]*2
        p1.action = ''
        p2.action = ''
        p1.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        p1.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        p2.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        p2.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        culori[0], culori[1], carti[0], carti[1] = dealer.draw_for_player_v2()
        p1.culori[0] = culori[0]
        p1.culori[1] = culori[1]
        p1.carti[0] = carti[0]
        p1.carti[1] = carti[1]
        culori[0], culori[1], carti[0], carti[1] = dealer.draw_for_player_v2()
        p2.culori[0] = culori[0]
        p2.culori[1] = culori[1]
        p2.carti[0] = carti[0]
        p2.carti[1] = carti[1]
        # print('preflop', p1.carti[0], p1.carti[1])
        # print('preflop', p2.carti[0], p2.carti[1])
        p1.points, p2.points = self.big_blind(p1.position, p1.points, p2.points, smallB, bigB)
        p1.score = p1.odd_calculator_for_two_cards(p1.culori, p1.carti[0], p1.carti[1])
        p2.score = p2.odd_calculator_for_two_cards(p2.culori, p2.carti[0], p2.carti[1])
        p1.moment = 'Preflop'
        p1.points, p2.points = self.conducting_the_round(p1, p2, 'Preflop')
        # # print('FINAL: ')
        # # print('p1.action: ', p1.action)
        # # print('p2.action: ', p2.action)
        # # print('p1.points: ', p1.points)
        # # print('p2.points: ', p2.points)
        # print('pot: ', self.pot)

        if p1.action != 'Fold' and p2.action != 'Fold':
            return 1
        elif p1.action == 'Fold':
            winner = 2
            p2.points += self.pot
            # print('Player 2 WIN')
            # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward) #de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)

          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)

            p2.win_counter += 1
            return 0
        elif p2.action == 'Fold':
            winner = 1
            p1.points += self.pot
            p1.bigblinds = self.pot / bigB
            # print('Player 1 WIN')
            # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            p1.preflop_win += 1
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p1.win_counter += 1
            return 0


    def flop(self, p1, p2, dealer,smallB, bigB):
        flag = 1
        if print_or_not(training_rounds, jocuriDiferite, flag):
            print('este flop')
        self.flop_rounds += 1
        culoriFlop, carte_Flop1, carte_Flop2, carte_Flop3 = dealer.draw_flop()
        p1.carti[2] = carte_Flop1[0]
        p1.carti[3] = carte_Flop2[0]
        p1.carti[4] = carte_Flop3[0]
        p1.culori[2] = culoriFlop[0]
        p1.culori[3] = culoriFlop[1]
        p1.culori[4] = culoriFlop[2]
        p2.carti[2] = carte_Flop1[0]
        p2.carti[3] = carte_Flop2[0]
        p2.carti[4] = carte_Flop3[0]
        p2.culori[2] = culoriFlop[0]
        p2.culori[3] = culoriFlop[1]
        p2.culori[4] = culoriFlop[2]

        flopScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
        flopScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

        p1.score += flopScoreP1
        p2.score += flopScoreP2
        p1.moment = 'Flop'
        p1.points, p2.points = self.conducting_the_round(p1, p2, 'Flop')
        # print ('p1 p: ', p1.points)
        # print ('p2 p: ', p2.points)
        # print('pot: ', self.pot)

        if p1.action != 'Fold' and p2.action != 'Fold':
            return 1
        elif p1.action == 'Fold':
            winner = 2
            p2.points += self.pot
            # print('Player 2 WIN')
            # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p2.win_counter += 1
            return 0
        elif p2.action == 'Fold':
            winner = 1
            p1.points += self.pot
            p1.bigblinds = self.pot / bigB

            # print('Player 1 WIN')
            # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            p1.flop_win += 1
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p1.win_counter += 1
            return 0

    def turn (self, p1, p2, dealer, smallB, bigB):
        flag = 1
        if print_or_not(training_rounds, jocuriDiferite, flag):
            print('este turn')
        self.turn_rounds += 1
        culoareTurn, carteTurn = dealer.draw_turn_river()
        p1.culori[5] = culoareTurn[0]
        p1.carti[5] = carteTurn[0]
        p2.culori[5] = culoareTurn[0]
        p2.carti[5] = carteTurn[0]
        indexPrecedentP1 = possible_hands.index(p1.mana)
        indexPrecedentP2 = possible_hands.index(p2.mana)
        turnScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
        turnScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

        p1.score, p2.score = self.recalculate_score(p1,p2,indexPrecedentP1,indexPrecedentP2)
        p1.moment = 'Turn'
        p1.points, p2.points = self.conducting_the_round(p1, p2, 'Turn')
        if p1.action != 'Fold' and p2.action != 'Fold':
            return 1
        elif p1.action == 'Fold':
            winner = 2
            p2.points += self.pot
            # print('Player 2 WIN')
            # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p2.win_counter += 1
            return 0
        elif p2.action == 'Fold':
            winner = 1
            p1.points += self.pot
            p1.bigblinds = self.pot / bigB

            # print('Player 1 WIN')
            # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
            p1.turn_win += 1
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p1.win_counter += 1
            return 0


    def river (self, p1, p2, dealer, smallB, bigB):
        flag = 1
        if print_or_not(training_rounds, jocuriDiferite, flag):
            print('este river')
        self.river_rounds += 1
        culoareRiver, carteRiver = dealer.draw_turn_river()

        p1.culori[6] = culoareRiver[0]
        p1.carti[6] = carteRiver[0]
        p2.culori[6] = culoareRiver[0]
        p2.carti[6] = carteRiver[0]
        indexPrecedentP1 = possible_hands.index(p1.mana)
        indexPrecedentP2 = possible_hands.index(p2.mana)
        riverScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
        riverScoreP2, p2.best_of_five, p2.mana = p2.check_hand()
        p1.score, p2.score = self.recalculate_score(p1,p2,indexPrecedentP1,indexPrecedentP2)
        # p1.score += riverScoreP1
        # p2.score += riverScoreP2
        p1.moment = 'River'
        p1.points, p2.points = self.conducting_the_round(p1, p2, 'River')

        if p1.action != 'Fold' and p2.action != 'Fold':
            winner = self.verify_winner_simple(p1, p2)
            if winner == 1:
                p1.points += self.pot
                p1.river_win += 1
                p1.bigblinds = self.pot / bigB

                # print ('Player 1 WIN')
                # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
                reward = p1.calculate_reward(self.pot, bigB_global, winner)
                if type(p1) == q.QAgent:
                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                if type(p2) == q.QAgent:
                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                    p2.updateQ(reward)
              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                p1.win_counter += 1
            elif winner == 2:
                p2.points += self.pot
                # print('Player 2 WIN')
                # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
                reward = p1.calculate_reward(self.pot, bigB_global, winner)
                if type(p1) == q.QAgent:
                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                if type(p2) == q.QAgent:
                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                    p2.updateQ(reward)
              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                p2.win_counter += 1
            else:
                p1.points += self.pot/2
                p2.points += self.pot/2
                # print('Split')
                # print('Split intre : ', p1.mana, ' si ', p2.mana)
                reward = p1.calculate_reward(self.pot, bigB_global, winner)
                if type(p1) == q.QAgent:
                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                if type(p2) == q.QAgent:
                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                    p2.updateQ(reward)
              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                self.split_rounds += 1


        elif p1.action == 'Fold':
            winner = 2
            p2.points += self.pot
            # print('Player 2 WIN')
            # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p2.win_counter += 1
            return 0
        elif p2.action == 'Fold':
            winner = 1
            p1.river_win += 1
            p1.points += self.pot
            p1.bigblinds = self.pot / bigB

            # print('Player 1 WIN')
            # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
            reward = p1.calculate_reward(self.pot, bigB_global, winner)
            if type(p1) == q.QAgent:
                p1.updateQ(reward)  # de rezolvat treaba cu state si new state
            if type(p2) == q.QAgent:
                reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                p2.updateQ(reward)
          #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
            p1.win_counter += 1
            return 0

    def all_in_situation(self, p1, p2, dealer, moment):
        game.flop_rounds += 1
        game.turn_rounds += 1
        game.river_rounds += 1
        if moment == 'Preflop':
            culoriFlop, carte_Flop1, carte_Flop2, carte_Flop3 = dealer.draw_flop()
            p1.carti[2] = carte_Flop1[0]
            p1.carti[3] = carte_Flop2[0]
            p1.carti[4] = carte_Flop3[0]
            p1.culori[2] = culoriFlop[0]
            p1.culori[3] = culoriFlop[1]
            p1.culori[4] = culoriFlop[2]
            p2.carti[2] = carte_Flop1[0]
            p2.carti[3] = carte_Flop2[0]
            p2.carti[4] = carte_Flop3[0]
            p2.culori[2] = culoriFlop[0]
            p2.culori[3] = culoriFlop[1]
            p2.culori[4] = culoriFlop[2]

            flopScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            flopScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += flopScoreP1
            p2.score += flopScoreP2

            culoareTurn, carteTurn = dealer.draw_turn_river()
            p1.culori[5] = culoareTurn[0]
            p1.carti[5] = carteTurn[0]
            p2.culori[5] = culoareTurn[0]
            p2.carti[5] = carteTurn[0]

            turnScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            turnScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += turnScoreP1
            p2.score += turnScoreP2

            culoareRiver, carteRiver = dealer.draw_turn_river()

            p1.culori[6] = culoareRiver[0]
            p1.carti[6] = carteRiver[0]
            p2.culori[6] = culoareRiver[0]
            p2.carti[6] = carteRiver[0]

            riverScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            riverScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += riverScoreP1
            p2.score += riverScoreP2

        elif moment == 'Flop':
            culoareTurn, carteTurn = dealer.draw_turn_river()
            p1.culori[5] = culoareTurn[0]
            p1.carti[5] = carteTurn[0]
            p2.culori[5] = culoareTurn[0]
            p2.carti[5] = carteTurn[0]

            turnScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            turnScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += turnScoreP1
            p2.score += turnScoreP2

            culoareRiver, carteRiver = dealer.draw_turn_river()

            p1.culori[6] = culoareRiver[0]
            p1.carti[6] = carteRiver[0]
            p2.culori[6] = culoareRiver[0]
            p2.carti[6] = carteRiver[0]

            riverScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            riverScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += riverScoreP1
            p2.score += riverScoreP2


        elif moment == 'Turn':

            culoareRiver, carteRiver = dealer.draw_turn_river()

            p1.culori[6] = culoareRiver[0]
            p1.carti[6] = carteRiver[0]
            p2.culori[6] = culoareRiver[0]
            p2.carti[6] = carteRiver[0]

            riverScoreP1, p1.best_of_five, p1.mana = p1.check_hand()
            riverScoreP2, p2.best_of_five, p2.mana = p2.check_hand()

            p1.score += riverScoreP1
            p2.score += riverScoreP2


    def play_more_games(self, p1, p2, number_of_rounds, smallB, bigB):
        dealer = Dealer(cards)

        p1.points = 4000
        p2.points = 4000
        while p1.points > 0 and p2.points > 0:
            # if self.rounds >= 50 and type(p1) == ga.GAagent:
            #     break
            ok = 0
            dealer.new_deck = {

    'Rosu': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Negru': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Romb': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Trefla': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

}
            self.rounds += 1
            self.pot = 0
            ok_all_in = 1
            ok = self.preflop(p1, p2, dealer,smallB, bigB)
            if ok == 1:
                if p1.points <= 0 or p2.points <= 0:
                    # print('p1 points: ', p1.points)
                    # print('p2 points: ', p2.points)
                    # print('pot: ', self.pot)
                    self.all_in_situation(p1, p2, dealer, 'Preflop')
                    winner = self.verify_winner_simple(p1, p2)
                    if winner == 1:
                        p1.points += self.pot
                        p1.river_win += 1
                        p1.bigblinds = self.pot/bigB

                        # print('Player 1 WIN')
                        # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
                        reward = p1.calculate_reward(self.pot, bigB, winner)
                        if type(p1) == q.QAgent:
                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                        if type(p2) == q.QAgent:
                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                            p2.updateQ(reward)
                      #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                        p1.win_counter += 1
                        break
                    elif winner == 2:
                        p2.points += self.pot
                        # print('Player 2 WIN')
                        # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
                        reward = p1.calculate_reward(self.pot, bigB, winner)
                        if type(p1) == q.QAgent:
                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                        if type(p2) == q.QAgent:
                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                            p2.updateQ(reward)
                       # elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                        p2.win_counter += 1
                        break
                    else:
                        p1.points += self.pot / 2
                        p2.points += self.pot / 2
                        # print('Split')
                        # print('Split intre : ', p1.mana, ' si ', p2.mana)
                        reward = p1.calculate_reward(self.pot, bigB, winner)
                        if type(p1) == q.QAgent:
                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                        if type(p2) == q.QAgent:
                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                            p2.updateQ(reward)
                      #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                    ok_all_in = 0

                if ok_all_in == 1:
                    ok = self.flop(p1,p2,dealer, smallB, bigB)
                    if ok == 1:
                        if p1.points <= 0 or p2.points <= 0:
                            # print('p1 points: ', p1.points)
                            # print('p2 points: ', p2.points)
                            # print(' jocul s-a terminat')
                            self.all_in_situation(p1, p2, dealer, 'Flop')
                            winner = self.verify_winner_simple(p1,p2)
                            if winner == 1:
                                p1.points += self.pot
                                p1.river_win += 1
                                p1.bigblinds = self.pot / bigB

                                # print('Player 1 WIN')
                                # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
                                reward = p1.calculate_reward(self.pot, bigB, winner)
                                if type(p1) == q.QAgent:
                                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                if type(p2) == q.QAgent:
                                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                    p2.updateQ(reward)
                              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                                p1.win_counter += 1
                                break
                            elif winner == 2:
                                p2.points += self.pot
                                # print('Player 2 WIN')
                                # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
                                reward = p1.calculate_reward(self.pot, bigB, winner)
                                if type(p1) == q.QAgent:
                                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                if type(p2) == q.QAgent:
                                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                    p2.updateQ(reward)
                              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                                p2.win_counter += 1
                                break
                            else:
                                p1.points += self.pot / 2
                                p2.points += self.pot / 2
                                # print('Split')
                                # print('Split intre : ', p1.mana, ' si ', p2.mana)
                                reward = p1.calculate_reward(self.pot, bigB, winner)
                                if type(p1) == q.QAgent:
                                    p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                if type(p2) == q.QAgent:
                                    reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                    p2.updateQ(reward)
                              #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                            ok_all_in = 0

                        if ok_all_in == 1:
                            ok = self.turn(p1, p2, dealer, smallB, bigB)
                            if ok == 1:
                                if p1.points <= 0 or p2.points <= 0:
                                    # print('p1 points: ', p1.points)
                                    # print('p2 points: ', p2.points)
                                    self.all_in_situation(p1, p2, dealer, 'Turn')
                                    winner = self.verify_winner_simple(p1, p2)
                                    if winner == 1:
                                        p1.points += self.pot
                                        p1.river_win += 1
                                        p1.bigblinds = self.pot / bigB

                                        # print('Player 1 WIN')
                                        # print('A castigat cu: ', p1.mana, ' impotriva ', p2.mana)
                                        reward = p1.calculate_reward(self.pot, bigB, winner)
                                        if type(p1) == q.QAgent:
                                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                        if type(p2) == q.QAgent:
                                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                            p2.updateQ(reward)
                                      #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                                        p1.win_counter += 1
                                        break
                                    elif winner == 2:
                                        p2.points += self.pot
                                        # print('Player 2 WIN')
                                        # print('A castigat cu: ', p2.mana, ' impotriva ', p1.mana)
                                        reward = p1.calculate_reward(self.pot, bigB, winner)
                                        if type(p1) == q.QAgent:
                                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                        if type(p2) == q.QAgent:
                                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                            p2.updateQ(reward)
                                      #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                                        p2.win_counter += 1
                                        break
                                    else:
                                        p1.points += self.pot / 2
                                        p2.points += self.pot / 2
                                        # print('Split')
                                        # print('Split intre : ', p1.mana, ' si ', p2.mana)
                                        reward = p1.calculate_reward(self.pot, bigB, winner)
                                        if type(p1) == q.QAgent:
                                            p1.updateQ(reward)  # de rezolvat treaba cu state si new state
                                        if type(p2) == q.QAgent:
                                            reward = p2.calculate_reward_p2(self.pot, bigB_global, winner)
                                            p2.updateQ(reward)
                                      #  elif type(p1) == ga.GAagent:
            #    p1.calculate_fitness(winner)
                                    ok_all_in = 0
                                if ok_all_in == 1:
                                    self.river(p1, p2, dealer, smallB, bigB)
            #                 else:
            #                     # print('Jocul s a oprit la turn')
            #         else:
            #             # print('Jocul s a oprit la flop')
            # else:
            #     # print('Jocul s a oprit la preflop')

            p1.position = 1 - p1.position
            p2.position = 1 - p2.position

            # if self.rounds % 10 == 0:
            #     smallB = smallB + 5
            #     bigB = smallB*2



            if p1.points <= 0 or p2.points <= 0:
                # print ('p1 points: ', p1.points)
                # print ('p2 points: ', p2.points)
                # print(' jocul s-a terminat')
                # if p1.points <= 0:
                #     print('castigator jucator 2')
                #     print(p1.points)
                #     print(p2.points)
                # elif p2.points <= 0:
                #     print('castigator jucator 1')
                #     print(p1.points)
                #     print(p2.points)
                break

initialStatus = ''
initialAction = ''
initialHandP1 = ''
initialHandP2 = ''
best_of_fiveP1 = [None] * 5
best_of_fiveP2 = [None] * 5
best_of_fiveQPLayer = [None] * 5

a = [None, None, None, None, None, 'a', 'b']

epsilon = 0.005

position = 1


game = Poker(cards, new_cards)
dealer = Dealer(cards)

points_q_vector = []
points_p2_vector = []


save_matrix = q.Q_table_river.copy()



print('introduceti modalitatea de joc dorita')
print('Q player vs Jucatori simplii: 1')
print('GA player vs Jucatpri simplii: 2')
print ('Qplayer antrenat cu el insusi vs Jucator de la Tastatura')
print('mod: ')
mod = int(input())

if mod == 1:


    wins = 0
    wins_noob = 0
    wins_counter = 0
    wins_counter_noob = 0
    split_counter = 0
    rounds_counter = 0
    split_counter = 0

    update = 1

    stats_vector = []

    # # print('numarul de jocuri diferite')
    # jocuriDiferite = int(input())
    game_win_counter_q = 0

    ################################# QPLAYER ####################################


    Q_table_preflop = np.zeros([31, 3, 3, 6])
    Q_table_flop = np.zeros([31, 3, 3, 6])
    Q_table_turn = np.zeros([31, 3, 3, 6])
    Q_table_river = np.zeros([31, 3, 3, 6])
    Q_table_raise = np.zeros([31, 3, 3, 5])


    jocuriDiferite_vector = [10,20,30,40,50,60,70,80,90,100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000]

    for jocuriDiferite in jocuriDiferite_vector:
        wins = 0
        wins_noob = 0
        wins_counter = 0
        wins_counter_noob = 0
        split_counter = 0
        rounds_counter = 0
        split_counter = 0

        update = 1
        save_epsilon = 1
        stats_vector = []

        # # print('numarul de jocuri diferite')
        # jocuriDiferite = int(input())
        game_win_counter_q = 0

        start_time = time.time()
        print(jocuriDiferite)


        save_matrix_preflop = Q_table_preflop.copy()
        save_matrix_flop = Q_table_flop.copy()
        save_matrix_turn = Q_table_turn.copy()
        save_matrix_river = Q_table_river.copy()

        game_win_counter_q = 0
        save_matrix_raise = Q_table_raise.copy()

        stats_vector = []
        game.split_rounds = split_counter
        training_rounds = 0
        for training_rounds in range (jocuriDiferite):
            # print(training_rounds)
            # print('INCEPE UN NOU JOC')
            playerQ = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, position, 4000, epsilon)
            playerQ.epsilon = save_epsilon
            playerQ.win_counter = wins
            playerQ2 = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, 1-position, 4000, epsilon)
            # playerQ.state_new_state = save_vector.copy()
            playerQ.Q = save_matrix.copy()

            playerQ.Q_preflop = save_matrix_preflop.copy()
            playerQ.Q_flop = save_matrix_flop.copy()
            playerQ.Q_turn = save_matrix_turn.copy()
            playerQ.Q_river = save_matrix_river.copy()
            playerQ.Q_raise = save_matrix_raise.copy()

            # noobPlayer = alwaysCall(4000, 1 - position)
            noobPlayer = bigScore(4000, 1 - position)
            # noobPlayer = randomPlayer(4000, 1 - position) # sa il oblig la niste probabilitati -: mai spre call, dar si cateva folduri

            noobPlayer.win_counter = wins_noob
            game.play_more_games(playerQ, noobPlayer, 0, smallB_global, bigB_global)
            ######### self train ############

            # game.play_more_games(playerQ, playerQ2, 0, smallB_global, bigB_global)



        #MEMENTO - adaugare numar de jocuriDiferite castigate ( la finalul unui game cine castiga )

            if playerQ.points > playerQ2.points:
                game_win_counter_q += 1

            save_matrix = playerQ.Q.copy()

            save_matrix_preflop = playerQ.Q_preflop.copy() + playerQ2.Q_preflop.copy()
            save_matrix_flop = playerQ.Q_flop.copy() + playerQ2.Q_flop.copy()
            save_matrix_turn = playerQ.Q_turn.copy() + playerQ2.Q_turn.copy()
            save_matrix_river = playerQ.Q_river.copy() + playerQ2.Q_river.copy()
            save_matrix_raise = playerQ.Q_raise.copy() + playerQ2.Q_raise.copy()

            # points_q_vector.append(playerQ.points)
            # points_p2_vector.append(noobPlayer.points)
            # wins_counter += playerQ.win_counter
            # wins_counter_noob += noobPlayer.win_counter
            # rounds_counter = game.rounds
            # split_counter += game.split_rounds

            river_win = playerQ.river_win
            turn_win = playerQ.turn_win
            flop_win = playerQ.flop_win
            preflop_win = playerQ.preflop_win
            save_epsilon = playerQ.epsilon
            # print(playerQ.epsilon)

        # print ('epsilon:', playerQ.epsilon)
        # print('q: ', points_q_vector)
        # print ('suma q este: ', sum(points_q_vector))
        #
        # print('p2: ', points_p2_vector)
        # print(' suma player este: ', sum(points_p2_vector))
        #
        # print('rounds counter: ', rounds_counter)
        # print('Qplayer wins counter: ', wins_counter)
        # print('noob player wins counter:  ', wins_counter_noob)
        # print('split: ', split_counter)
        # print(playerQ.epsilon)
        # stats_vector.append(game.rounds)
        # stats_vector.append(wins_counter)
        # stats_vector.append(wins_counter_noob)
        # stats_vector.append(split_counter)
        # stats_vector.append(sum(points_q_vector))
        # stats_vector.append(sum(points_p2_vector))
        # stats_vector.append(game_win_counter_q)

        # save_matrix = playerQ.Q

        stats_vector_no_training = []

        update = 0

        wins = 0
        wins_noob = 0
        wins_counter = 0
        wins_counter_noob = 0
        split_counter = 0
        rounds_counter = 0
        split_counter = 0

        game_win_counter_q = 0
        game.rounds = 0
        game.river_rounds = 0
        game.turn_rounds = 0
        game.flop_rounds = 0
        f.write(str(jocuriDiferite))
        f.write(' timpul: ')
        f.write(str((time.time() - start_time)))

        # playerQ.Q_preflop = save_matrix_preflop.copy()
        # playerQ.Q_flop = save_matrix_flop.copy()
        # playerQ.Q_turn = save_matrix_turn.copy()
        # playerQ.Q_river = save_matrix_river.copy()
        # playerQ.Q_raise = save_matrix_raise.copy()

        # print (' ---- %s seconds ---- ' % (time.time() - start_time))
        river_win = 0
        turn_win = 0
        flop_win = 0
        preflop_win = 0
        jocuriTest = 500
        game.split_rounds = 0
        varix = 0
        points_q_vector.clear()
        points_p2_vector.clear()
        after_training_rounds = 0
        for after_training_rounds in range (jocuriTest):
            # print('INCEPE UN NOU JOC FARA ANTRENARE')
            playerQ = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, position, 4000, epsilon)

            playerQ.update = 0

            playerQ.Q = save_matrix.copy()

            playerQ.Q_preflop = save_matrix_preflop.copy()
            playerQ.Q_flop = save_matrix_flop.copy()
            playerQ.Q_turn = save_matrix_turn.copy()
            playerQ.Q_river = save_matrix_river.copy()
            playerQ.Q_raise = save_matrix_raise.copy()

            playerQ.river_win =  river_win
            playerQ.turn_win = turn_win
            playerQ.flop_win = flop_win
            playerQ.preflop_win = preflop_win


            # noobPlayer = alwaysCall(4000, 1 - position)
            noobPlayer = bigScore(4000, 1 - position)
            # noobPlayer = randomPlayer(4000, 1 - position)


            game.play_more_games(playerQ, noobPlayer, 0, smallB_global, bigB_global)



            if playerQ.points > noobPlayer.points:
                game_win_counter_q += 1

            points_q_vector.append(playerQ.points)
            points_p2_vector.append(noobPlayer.points)

            wins_counter += playerQ.win_counter
            wins_counter_noob += noobPlayer.win_counter
            # rounds_counter = game.rounds
            # split_counter += game.split_rounds

            river_win = playerQ.river_win
            turn_win = playerQ.turn_win
            flop_win = playerQ.flop_win
            preflop_win = playerQ.preflop_win


        # # print('rounds counter: ', rounds_counter)
        # # print('Qplayer wins counter: ', wins_counter)
        # # print('noob player wins counter:  ', wins_counter_noob)
        # # print('split: ', split_counter)


        stats_vector_no_training.append(game.rounds)
        stats_vector_no_training.append(wins_counter)
        stats_vector_no_training.append(wins_counter_noob)
        stats_vector_no_training.append(game.split_rounds)
        stats_vector_no_training.append((sum(points_q_vector)/bigB_global)/game.rounds)
        stats_vector_no_training.append(sum(points_q_vector)/jocuriTest)
        stats_vector_no_training.append((sum(points_p2_vector)/bigB_global)/game.rounds)
        stats_vector_no_training.append(sum(points_p2_vector)/jocuriTest)
        stats_vector_no_training.append(game_win_counter_q / jocuriTest)
        stats_vector_no_training.append(preflop_win)
        stats_vector_no_training.append(flop_win)
        stats_vector_no_training.append(turn_win)
        stats_vector_no_training.append(river_win)
        f.write(' ')
        f.write(str(game.rounds))
        f.write(' ')
        f.write(str(wins_counter))
        f.write(' ')
        f.write(str(wins_counter_noob))
        f.write(' ')
        f.write(str(game.split_rounds))
        f.write(' ')
        f.write(str((sum(points_q_vector)/bigB_global)/game.rounds))
        f.write(' ')
        f.write(str(sum(points_q_vector)/jocuriTest))
        f.write(' ')
        f.write(str((sum(points_p2_vector)/bigB_global)/game.rounds))
        f.write(' ')
        f.write(str(sum(points_p2_vector)/jocuriTest))
        f.write(' ')
        f.write(str(game_win_counter_q / jocuriTest))
        f.write(' ')
        f.write(str(preflop_win))
        f.write(' ')
        f.write(str(flop_win))
        f.write(' ')
        f.write(str(turn_win))
        f.write(' ')
        f.write(str(river_win))
        f.write(' \n')
        # print(stats_vector_no_training)



        print('Stats vector: ', stats_vector)
        print('stats vector no training: ', stats_vector_no_training)
        print('flop rounds: ', game.flop_rounds)
        print('turn rounds: ', game.turn_rounds)
        print('river rounds: ', game.river_rounds)
    p.write(' ')
    p.write(str(playerQ.Q_preflop))
    p.write('\n')
    p.write(str(playerQ.Q_raise))


elif mod == 2:


    ######################################## GAPLYER #################################################
    #
    numar_indivizi = 20
    print('Numar indivizi din populatie: ', numar_indivizi)

    # print ('Numar de generatii ')

    # generatii = 10


    print ('Numar aspiranti turneu selectie ')
    jocuriDiferite = 50
    numar_aspiranti = 5
    generatii_vector = [100]
    jocuriDiferite_vector = [50]
    stats_vector_ga = []
    for generatii in generatii_vector:
        ganaratii = 100
        start_time = time.time()
        f.write(str(generatii))
        f.write('\n')
        training_rounds = jocuriDiferite
        best_individs_win_per = []
        wins = 0
        wins_noob = 0
        wins_counter = 0
        wins_counter_noob = 0
        split_counter = 0
        rounds_counter = 0
        split_counter = 0

        population_win_per = []
        best_individs = []

        win_rate_generatie = []
        generatii_vector = []
        stats_vector_ga.clear()
        populatie = ga.starting_pop(numar_indivizi)
        for i in range(len(populatie)):
            populatie[i].initialize_genes()
        # noobPlayer = alwaysCall(4000, 1 - position)
        # game.play_more_games(populatie[0], noobPlayer, 0, smallB_global, bigB_global)
        individs_vector_wins = [len(populatie)] * 0
        start_time = time.time()
        wincounterunooblist = []

        for generation in range(generatii):
            print('generatia ', generation)

            # print(generation)
            training_rounds = generation
            noobPlayer = alwaysCall(4000, 1 - position)
            # noobPlayer = bigScore(4000, 1 - position)
            # noobPlayer = randomPlayer(4000, 1 - position)

            win_rate_generatie.clear()
            win_counter_ga = 0
            win_counter_ga_part = 0
            contor_populatie = 0
            individ_wins = 0
            populatie = ga.reset_win_counter(populatie)

            for individ in range(len(populatie)):
                populatie[individ].win_counter_games = 0
                populatie[individ].win_counter_part = 0
                populatie[individ].split_rounds = 0
                populatie[individ].rounds = 0
                populatie[individ].win_counter_noob_games = 0
                populatie[individ].total_points = 0
                populatie[individ].total_points_noob = 0
                populatie[individ].points = 4000
                populatie[individ].bigblinds = 0
                populatie[individ].preflop_win = 0
                populatie[individ].flop_win = 0
                populatie[individ].turn_win = 0
                populatie[individ].river_win = 0
                noobPlayer.points = 4000
                win_counter_ga = 0
                populatie[individ].points_vector.clear()
                contor_noob_populatie = 0
                for i in range(jocuriDiferite):
                    # training_rounds = i
                    # win_counter_ga = 0
                    populatie[individ].points = 4000
                    populatie[individ].action = ''
                    populatie[individ].position = 1
                    # noobPlayer = bigScore(4000, 1 - position)
                    noobPlayer = alwaysCall(4000, 1 - populatie[individ].position)
                    # noobPlayer = randomPlayer(4000, 1 - populatie[individ].position)
                    noobPlayer.points = 4000
                    game = Poker(cards, new_cards)
                    game.play_more_games(populatie[individ], noobPlayer, 0, smallB_global, bigB_global)
                    populatie[individ].split_rounds += game.split_rounds
                    populatie[individ].rounds += game.rounds
                    populatie[individ].total_points += populatie[individ].points
                    populatie[individ].total_points_noob += noobPlayer.points
                    # print (game.rounds)
                    populatie[individ].points_vector.append(populatie[individ].points)
                    if populatie[individ].points > noobPlayer.points:
                        if populatie[individ].points >= 7900:
                            populatie[individ].fitness += 3
                            populatie[individ].win_counter_games += 1
                            win_counter_ga += 1

                        else:
                            populatie[individ].fitness += 1
                            populatie[individ].win_counter_part += 1
                            win_counter_ga_part += 1
                    elif populatie[individ].points < noobPlayer.points:
                        populatie[individ].fitness -= 1
                        populatie[individ].win_counter_noob_games += 1


                    contor_populatie = contor_populatie + win_counter_ga + win_counter_ga_part
                    contor_noob_populatie = contor_noob_populatie + populatie[individ].win_counter_noob_games
                # win_rate_generatie.append(win_counter_ga/jocuriDiferite)
                # print(contor_populatie)
                win_rate_generatie.append(populatie[individ].win_counter_games/jocuriDiferite)
                # print('contor pop: ', populatie[individ].win_counter_games/(jocuriDiferite))
                # print('contor noob: ', populatie[individ].win_counter_noob_games/(jocuriDiferite))
                wincounterunooblist.append(populatie[individ].win_counter_noob_games)
            generatii_vector.append(sum(win_rate_generatie) / numar_indivizi)
            the_best_individ = ga.best_fitness(populatie)
            best_individs.append(the_best_individ)
            best_individs_win_per.append(the_best_individ.win_counter_games / jocuriDiferite)
            population_win_per.append(contor_populatie / (jocuriDiferite*numar_indivizi))
            # best_individs.append(ga.best_fitness(populatie))

            parent1 = ga.select_individ(populatie, numar_aspiranti)
            parent2 = ga.select_individ(populatie, numar_aspiranti)

            child1 = ga.crossover(parent1, parent2, position)

            celMaiSlab = ga.worst_fitness(populatie)

            populatie.remove(celMaiSlab)

            populatie.append(child1)

            mutation_rate = 0.05

            populatie = ga.mutatie(populatie, mutation_rate)

            populatie = ga.reset_fitness(populatie)

            stats_vector_ga.clear()
            print('time: ', (time.time() - start_time))

            if generation == 1 or generation == 5 or generation == 10 or generation == 20 or generation == 30 or generation == 40 or generation == 50 or generation == 60 or generation == 70 or generation == 80 or generation == 90 or generation == 100:
                stats_vector_ga.append(the_best_individ.rounds)
                stats_vector_ga.append(the_best_individ.win_counter_games)
                stats_vector_ga.append(the_best_individ.win_counter_part)
                stats_vector_ga.append(the_best_individ.win_counter_noob_games)
                stats_vector_ga.append(the_best_individ.split_rounds)
                stats_vector_ga.append((the_best_individ.total_points / bigB_global) / the_best_individ.rounds)
                stats_vector_ga.append(the_best_individ.total_points / jocuriDiferite)
                stats_vector_ga.append((the_best_individ.total_points_noob / bigB_global) / the_best_individ.rounds)
                stats_vector_ga.append((the_best_individ.total_points_noob / jocuriDiferite))
                stats_vector_ga.append(the_best_individ.win_counter_games / jocuriDiferite)
                stats_vector_ga.append(the_best_individ.win_counter_part / jocuriDiferite)
                stats_vector_ga.append(the_best_individ.preflop_win)
                stats_vector_ga.append(the_best_individ.flop_win)
                stats_vector_ga.append(the_best_individ.turn_win)
                stats_vector_ga.append(the_best_individ.river_win)
                stats_vector_ga.append(the_best_individ.bigblinds)
                f.write('Pentru generatia: ')
                f.write(str(generation))
                f.write('\n')
                f.write('time: ')
                f.write (str((time.time() - start_time)))
                print('time: ', (time.time()- start_time))
                f.write('\n')
                f.write(str(generatii_vector))
                f.write('\n')
                f.write(str(stats_vector_ga))
                f.write('\n')
                print ('pt gen: ', generation)
                print(generatii_vector)
                print(stats_vector_ga)


            # f.write(' ')
            # f.write(str(the_best_individ.rounds))
            # f.write(' ')
            # f.write(str(the_best_individ.win_counter_games))
            # f.write(' ')
            # f.write(str(the_best_individ.win_counter_part))
            # f.write(' ')
            # f.write(str(the_best_individ.win_counter_noob_games))
            # f.write(' ')
            # f.write(str(the_best_individ.split_rounds))
            # f.write(' ')
            # f.write(str((the_best_individ.total_points / bigB_global) / the_best_individ.rounds))
            # f.write(' ')
            # f.write(str(the_best_individ.total_points / jocuriDiferite))
            # f.write(' ')
            # f.write(str((the_best_individ.total_points_noob / bigB_global) / the_best_individ.rounds))
            # f.write(' ')
            # f.write(str(the_best_individ.total_points_noob / jocuriDiferite))
            # f.write(' ')
            # f.write(str(the_best_individ.win_counter_games / jocuriDiferite))
            # f.write(' ')
            # f.write(str(the_best_individ.win_counter_part / jocuriDiferite))
            # f.write(' ')
            # f.write(str(the_best_individ.preflop_win))
            # f.write(' ')
            # f.write(str(the_best_individ.flop_win))
            # f.write(' ')
            # f.write(str(the_best_individ.turn_win))
            # f.write(' ')
            # f.write(str(the_best_individ.river_win))
            # f.write('\n')
            # f.write('Pentru generatie')
            # f.write('\n')
            # f.write(str(generatii_vector[generation]))
            # f.write(' ')

        print('sfarsit de generatie: ', generatii_vector)

        for i in range(len(populatie)):
            print('individul ', i, ' ', populatie[i].win_counter_games, ' ',populatie[i].win_counter_part )
        print (' ---- %s seconds ---- ' % (time.time() - start_time))
        f.write(str((time.time() - start_time)))
        f.write('\n')

        print(generatii_vector)
        print(win_rate_generatie)
        print(the_best_individ.points_vector)
        stats_vector_ga.append(the_best_individ.rounds)
        stats_vector_ga.append(the_best_individ.win_counter_games)
        stats_vector_ga.append(the_best_individ.win_counter_part)
        stats_vector_ga.append(the_best_individ.win_counter_noob_games)
        stats_vector_ga.append(the_best_individ.split_rounds)
        stats_vector_ga.append((the_best_individ.total_points/bigB_global)/the_best_individ.rounds)
        stats_vector_ga.append(the_best_individ.total_points/jocuriDiferite)
        stats_vector_ga.append((the_best_individ.total_points_noob/bigB_global)/the_best_individ.rounds)
        stats_vector_ga.append((the_best_individ.total_points_noob/jocuriDiferite))
        stats_vector_ga.append(the_best_individ.win_counter_games / jocuriDiferite)
        stats_vector_ga.append(the_best_individ.win_counter_part / jocuriDiferite)
        stats_vector_ga.append(the_best_individ.preflop_win)
        stats_vector_ga.append(the_best_individ.flop_win)
        stats_vector_ga.append(the_best_individ.turn_win)
        stats_vector_ga.append(the_best_individ.river_win)
        stats_vector_ga.append(the_best_individ.bigblinds)
        print(stats_vector_ga)
        f.write('\n')
        f.write(str(generatii_vector))
        f.write('\n')
        f.write(str(stats_vector_ga))
        f.write('\n')
        # f.write(' ')
        # f.write(str(the_best_individ.rounds))
        # f.write(' ')
        # f.write(str(the_best_individ.win_counter_games))
        # f.write(' ')
        # f.write(str(the_best_individ.win_counter_part))
        # f.write(' ')
        # f.write(str(the_best_individ.win_counter_noob_games))
        # f.write(' ')
        # f.write(str(the_best_individ.split_rounds))
        # f.write(' ')
        # f.write(str((the_best_individ.total_points/bigB_global)/the_best_individ.rounds))
        # f.write(' ')
        # f.write(str(the_best_individ.total_points/jocuriDiferite))
        # f.write(' ')
        # f.write(str((the_best_individ.total_points_noob/bigB_global)/the_best_individ.rounds))
        # f.write(' ')
        # f.write(str(the_best_individ.total_points_noob/jocuriDiferite))
        # f.write(' ')
        # f.write(str(the_best_individ.win_counter_games / jocuriDiferite))
        # f.write(' ')
        # f.write(str(the_best_individ.win_counter_part / jocuriDiferite))
        # f.write(' ')
        # f.write(str(the_best_individ.preflop_win))
        # f.write(' ')
        # f.write(str(the_best_individ.flop_win))
        # f.write(' ')
        # f.write(str(the_best_individ.turn_win))
        # f.write(' ')
        # f.write(str(the_best_individ.river_win))
        # f.write(' \n')
        print(best_individs_win_per)
        print(population_win_per)
        S = 0
        for individ in range (len(populatie)):
            # print(populatie[individ].win_counter_games)
            S += populatie[individ].win_counter_games
        # print (S)
        # print(wincounterunooblist)
        print (' ---- %s seconds ---- ' % (time.time() - start_time))
         # implementare in cate maini ajunge la flop turn river.
elif mod == 3:

    Q_table_preflop = np.zeros([31, 3, 3, 6])
    Q_table_flop = np.zeros([31, 3, 3, 6])
    Q_table_turn = np.zeros([31, 3, 3, 6])
    Q_table_river = np.zeros([31, 3, 3, 6])
    Q_table_raise = np.zeros([31, 3, 3, 5])

    jocuriDiferite_vector = [100]

    for jocuriDiferite in jocuriDiferite_vector:
        wins = 0
        wins_noob = 0
        wins_counter = 0
        wins_counter_noob = 0
        split_counter = 0
        rounds_counter = 0
        split_counter = 0
        update = 1
        save_epsilon = 1
        stats_vector = []
        game_win_counter_q = 0
        start_time = time.time()
        print(jocuriDiferite)
        save_matrix_preflop = Q_table_preflop.copy()
        save_matrix_flop = Q_table_flop.copy()
        save_matrix_turn = Q_table_turn.copy()
        save_matrix_river = Q_table_river.copy()
        game_win_counter_q = 0
        save_matrix_raise = Q_table_raise.copy()
        stats_vector = []
        game.split_rounds = split_counter
        training_rounds = 0
        for training_rounds in range(jocuriDiferite):
            generation = training_rounds
            playerQ = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, position, 4000, epsilon)
            playerQ.epsilon = save_epsilon
            playerQ.win_counter = wins
            playerQ2 = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, 1 - position, 4000, epsilon)
            # playerQ.state_new_state = save_vector.copy()

            playerQ.Q = save_matrix.copy()
            playerQ.Q_preflop = save_matrix_preflop.copy()
            playerQ.Q_flop = save_matrix_flop.copy()
            playerQ.Q_turn = save_matrix_turn.copy()
            playerQ.Q_river = save_matrix_river.copy()
            playerQ.Q_raise = save_matrix_raise.copy()


            # noobPlayer.win_counter = wins_noob
            # game.play_more_games(playerQ, noobPlayer, 0, smallB_global, bigB_global)

            ######### self train ############

            game.play_more_games(playerQ, playerQ2, 0, smallB_global, bigB_global)

            # MEMENTO - adaugare numar de jocuriDiferite castigate ( la finalul unui game cine castiga )

            if playerQ.points > playerQ2.points:
                game_win_counter_q += 1

            save_matrix = playerQ.Q.copy()

            save_matrix_preflop = playerQ.Q_preflop.copy() + playerQ2.Q_preflop.copy()
            save_matrix_flop = playerQ.Q_flop.copy() + playerQ2.Q_flop.copy()
            save_matrix_turn = playerQ.Q_turn.copy() + playerQ2.Q_turn.copy()
            save_matrix_river = playerQ.Q_river.copy() + playerQ2.Q_river.copy()
            save_matrix_raise = playerQ.Q_raise.copy() + playerQ2.Q_raise.copy()

            # points_q_vector.append(playerQ.points)
            # points_p2_vector.append(noobPlayer.points)
            # wins_counter += playerQ.win_counter
            # wins_counter_noob += noobPlayer.win_counter
            # rounds_counter = game.rounds
            # split_counter += game.split_rounds

            river_win = playerQ.river_win
            turn_win = playerQ.turn_win
            flop_win = playerQ.flop_win
            preflop_win = playerQ.preflop_win
            save_epsilon = playerQ.epsilon
            # print(playerQ.epsilon)

        # print ('epsilon:', playerQ.epsilon)
        # print('q: ', points_q_vector)
        # print ('suma q este: ', sum(points_q_vector))
        #
        # print('p2: ', points_p2_vector)
        # print(' suma player este: ', sum(points_p2_vector))
        #
        # print('rounds counter: ', rounds_counter)
        # print('Qplayer wins counter: ', wins_counter)
        # print('noob player wins counter:  ', wins_counter_noob)
        # print('split: ', split_counter)
        # print(playerQ.epsilon)
        # stats_vector.append(game.rounds)
        # stats_vector.append(wins_counter)
        # stats_vector.append(wins_counter_noob)
        # stats_vector.append(split_counter)
        # stats_vector.append(sum(points_q_vector))
        # stats_vector.append(sum(points_p2_vector))
        # stats_vector.append(game_win_counter_q)

        # save_matrix = playerQ.Q

        stats_vector_no_training = []

        update = 0

        wins = 0
        wins_noob = 0
        wins_counter = 0
        wins_counter_noob = 0
        split_counter = 0
        rounds_counter = 0
        split_counter = 0

        game_win_counter_q = 0
        game.rounds = 0
        game.river_rounds = 0
        game.turn_rounds = 0
        game.flop_rounds = 0
        f.write(str(jocuriDiferite))
        f.write(' timpul: ')
        f.write(str((time.time() - start_time)))

        # playerQ.Q_preflop = save_matrix_preflop.copy()
        # playerQ.Q_flop = save_matrix_flop.copy()
        # playerQ.Q_turn = save_matrix_turn.copy()
        # playerQ.Q_river = save_matrix_river.copy()
        # playerQ.Q_raise = save_matrix_raise.copy()

        # print (' ---- %s seconds ---- ' % (time.time() - start_time))
        river_win = 0
        turn_win = 0
        flop_win = 0
        preflop_win = 0
        jocuriTest = 500
        game.split_rounds = 0
        varix = 0
        points_q_vector.clear()
        points_p2_vector.clear()
        after_training_rounds = 0
        for after_training_rounds in range(jocuriTest):
            # print('INCEPE UN NOU JOC FARA ANTRENARE')
            playerQ = q.QAgent(update, q.alpha, q.gamma, q.Q_table_river, position, 4000, epsilon)

            playerQ.update = 0

            playerQ.Q = save_matrix.copy()

            playerQ.Q_preflop = save_matrix_preflop.copy()
            playerQ.Q_flop = save_matrix_flop.copy()
            playerQ.Q_turn = save_matrix_turn.copy()
            playerQ.Q_river = save_matrix_river.copy()
            playerQ.Q_raise = save_matrix_raise.copy()

            playerQ.river_win = river_win
            playerQ.turn_win = turn_win
            playerQ.flop_win = flop_win
            playerQ.preflop_win = preflop_win

            keyboardPlayer = kPlayer(4000, 1-playerQ.position)

            game.play_more_games(playerQ, keyboardPlayer, 0, smallB_global, bigB_global)

            if playerQ.points > kPlayer.points:
                game_win_counter_q += 1

            points_q_vector.append(playerQ.points)
            points_p2_vector.append(noobPlayer.points)

            wins_counter += playerQ.win_counter
            wins_counter_noob += noobPlayer.win_counter
            # rounds_counter = game.rounds
            # split_counter += game.split_rounds

            river_win = playerQ.river_win
            turn_win = playerQ.turn_win
            flop_win = playerQ.flop_win
            preflop_win = playerQ.preflop_win

        # # print('rounds counter: ', rounds_counter)
        # # print('Qplayer wins counter: ', wins_counter)
        # # print('noob player wins counter:  ', wins_counter_noob)
        # # print('split: ', split_counter)

        stats_vector_no_training.append(game.rounds)
        stats_vector_no_training.append(wins_counter)
        stats_vector_no_training.append(wins_counter_noob)
        stats_vector_no_training.append(game.split_rounds)
        stats_vector_no_training.append((sum(points_q_vector) / bigB_global) / game.rounds)
        stats_vector_no_training.append(sum(points_q_vector) / jocuriTest)
        stats_vector_no_training.append((sum(points_p2_vector) / bigB_global) / game.rounds)
        stats_vector_no_training.append(sum(points_p2_vector) / jocuriTest)
        stats_vector_no_training.append(game_win_counter_q / jocuriTest)
        stats_vector_no_training.append(preflop_win)
        stats_vector_no_training.append(flop_win)
        stats_vector_no_training.append(turn_win)
        stats_vector_no_training.append(river_win)
        f.write(' ')
        f.write(str(game.rounds))
        f.write(' ')
        f.write(str(wins_counter))
        f.write(' ')
        f.write(str(wins_counter_noob))
        f.write(' ')
        f.write(str(game.split_rounds))
        f.write(' ')
        f.write(str((sum(points_q_vector) / bigB_global) / game.rounds))
        f.write(' ')
        f.write(str(sum(points_q_vector) / jocuriTest))
        f.write(' ')
        f.write(str((sum(points_p2_vector) / bigB_global) / game.rounds))
        f.write(' ')
        f.write(str(sum(points_p2_vector) / jocuriTest))
        f.write(' ')
        f.write(str(game_win_counter_q / jocuriTest))
        f.write(' ')
        f.write(str(preflop_win))
        f.write(' ')
        f.write(str(flop_win))
        f.write(' ')
        f.write(str(turn_win))
        f.write(' ')
        f.write(str(river_win))
        f.write(' \n')
        # print(stats_vector_no_training)

        print('Stats vector: ', stats_vector)
        print('stats vector no training: ', stats_vector_no_training)
        print('flop rounds: ', game.flop_rounds)
        print('turn rounds: ', game.turn_rounds)
        print('river rounds: ', game.river_rounds)
    p.write(' ')
    p.write(str(playerQ.Q_preflop))
    p.write('\n')
    p.write(str(playerQ.Q_raise))



f.close()
p.close()