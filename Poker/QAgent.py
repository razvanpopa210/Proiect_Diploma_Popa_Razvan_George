import numpy as np
from numpy.random import choice

eps = 1
eps_end = 0.001
eps_rate = 0.001


cards = {

    'Rosu': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Negru': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Romb': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Trefla': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

}

culori = ['Rosu', 'Negru', 'Romb', 'Trefla']

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
        chinta.append(int(carti_straight[2]))
        chinta.append(int(carti_straight[3]))
        chinta.append(int(carti_straight[4]))
        chinta.append(int(carti_straight[5]))
        chinta.append(int(carti_straight[6]))
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
    return 0, nCards, 'Carte Mare'

#

states = ['Call', 'Raise', 'Fold', 'Check', 'All-In']


alpha = 0.01
gamma = 0.90
Q_table_preflop = np.zeros([31,3,3,6])
Q_table_flop = np.zeros([31,3,3,6])
Q_table_turn = np.zeros([31,3,3,6])
Q_table_river = np.zeros([31,3,3,6])
Q_table_raise = np.zeros([31,3,3,5])


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




def determine_actions (position, moment, enemy_action, action):
    if moment == 'Preflop':
        if position == 1:
            if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                return ['Call', 'Raise', 'Fold', None, None, None]

            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None, None]
            elif enemy_action == 'All-In':
                return ['Call', None, 'Fold', None, None, None]
            elif enemy_action == 'Call' or enemy_action == 'Fold' or enemy_action == 'Check':
                return [None, None, None, None, None, None]
        elif position == 0:
            if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                return [None, 'Raise', 'Fold', 'Check', None, None]
            elif enemy_action == 'Call' and action == 'Raise':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Call':
                return [None, 'Raise', None, 'Check', None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None, None]

            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None] #MEMENTO
            elif enemy_action == 'Check':
                return [None, None, None, None, None, None]
    elif moment == 'Flop' or moment == 'Turn' or moment == 'River':
        if position == 1:
            if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                return [None, 'Raise', 'Fold', 'Check', None, None]
            elif enemy_action == 'Check':
                return [None, 'Raise', None, 'Check', None, None]
            elif enemy_action == 'Call' and action == 'Raise':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Call':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None,None]
            elif enemy_action == None:
                return [None, 'Raise', 'Fold', 'Check', None,None]
            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None]
        if position == 0:
            if enemy_action != 'Call' and enemy_action != 'Raise' and enemy_action != 'Fold' and enemy_action != 'Check' and enemy_action != 'All-In':
                return ['Call', None, 'Fold', None, None ,None]
            elif enemy_action == 'Check':
                return [None, 'Raise', None, 'Check', None,None]
            elif enemy_action == 'Call':
                return [None, None, None, None, None, None]
            elif enemy_action == 'Raise':
                return ['Call', 'Raise', 'Fold', None, None,None]

            elif enemy_action == 'Fold':
                return [None, None, None, None, None, None]






class QAgent():

    def __init__(self, update, alpha, gamma, Q, position, points, epsilon):
        
        self.Q_flop = Q_table_flop
        self.Q_preflop = Q_table_preflop
        self.Q_turn = Q_table_turn
        self.Q_river = Q_table_river

        self.Q_raise = Q_table_raise


        self.blinds = 0
        
        self.update = update
        self.reward_moment = 'Preflop'

        self.gamma = gamma
        self.alpha = alpha


        self.state = [None] * 3

        self.state_dict = {'Preflop' : [None]*2,
                           'Flop' : [None]*2,
                           'Turn' : [None]*2,
                           'River' : [None]*2
                           }


        self.epsilon = epsilon

        self.moment = 'Preflop'
        self.position = position


        self.state_dict = {'Preflop' : [None]*2,
                           'Flop' : [None]*2,
                           'Turn' : [None]*2,
                           'River' : [None]*2
                           }

        self.action = ''
        



        self.points = points
        self.score = 0
        self.bet = 0

        self.playable_actions = ['a']*6


        self.mana = ''
        self.best_of_five = [None] * 5
        self.culori = ['E', 'T', 'T', 'I', 'C', 'T', 'I']
        self.carti = ['E', 'T', 'T', 'I', 'C', 'T', 'I']

        self.state_new_state = [None]*2

        self.flag = 2

        self.win_counter = 0
        self.iraise = 0

        self.bigblinds = 0
        self.preflop_win = 0
        self.flop_win = 0
        self.turn_win = 0
        self.river_win = 0


#
    def index_raise(self, values, eps_end, eps_rate):
        new_values = []
        mx = values[0]
        v = [0, 1, 2, 3, 4]
        a = np.random.random()
        if (a <= self.epsilon):
            index = choice(v, 1)

        for i in range(len(values)):
            if mx < values[i]:
                new_values = []
                new_values.append(values[i])
                mx = values[i]
            elif mx == values[i]:
                new_values.append(values[i])

        x = choice(new_values,1)
        for i in range(5):
            if self.Q_raise[self.state[0]][self.state[1]][self.state[2]][i] == x:
                index = i
        if self.epsilon > eps_end:
            self.epsilon -= eps_rate
        return index

    def determine_raise(self, index, bigB, enemy_action, enemy_bet):
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
            else:
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
            else:
                self.points -= self.bet

            

    def calculate_bet(self, opponent_action, opponent_bet, bigB, smallB):

        if self.action == 'Call' and self.position == 1 and opponent_action == '' and self.moment == 'Preflop':
            self.bet = bigB - smallB
            self.points -= self.bet
        elif self.action == 'Raise':
            self.iraise = self.index_raise(self.Q_raise[self.state[0]][self.state[1]][self.state[2]], eps_end, eps_rate)
            self.determine_raise(self.iraise, bigB, opponent_action, opponent_bet)

        elif self.action == 'Check' or self.action == 'Fold':
            self.bet = 0
            self.points -= self.bet
        elif self.action == 'Call' and self.points > opponent_bet:
            self.bet = opponent_bet
            self.points -= self.bet

        elif self.action == 'Call' or self.action == 'All-In' and self.points <= opponent_bet:
            self.bet = self.points
            self.points = 0
        elif self.action == 'Raise':
            self.iraise = self.index_raise(self.Q_raise[self.state[0]][self.state[1]][self.state[2]], eps_end, eps_rate)
            self.determine_raise(self.iraise, bigB, opponent_action, opponent_bet)
        elif self.action == 'All-In':
            self.bet = self.points
            self.points = 0
        elif opponent_action is None and self.position == 1 and self.action == 'Call':
            self.bet = smallB
            self.points -= self.bet
        elif self.action is None:
            self.bet = 0
            self.points -= self.bet
        self.blinds += int(self.bet / bigB)

    def exploitation_vs_exploaration(self, values, actions, eps_end, eps_rate):
        new_values = []
        new_states = []
        mx = -99999999999999
        mn = values[0]
        for i in values:
            if i < mn:
                mn = i
        mx = mn
        x = np.random.random()
        if (x <= self.epsilon):

            ok_mai_mic = 0

            for i in range(len(actions)):
                if actions[i] is not None:
                    ok_mai_mic = 1
            if ok_mai_mic == 1:
                draw = choice(actions, 1)
                draw = to_str_harcoded(draw)
                while draw[0] is None:
                    draw = choice(actions, 1)
                    # draw = to_str_harcoded(draw)
                draw = to_str_harcoded(draw)
            elif ok_mai_mic == 0:
                # print('toate sunt nOne')
                draw = None
        else:
            ok_none = 0
            for i in range(len(actions)):
                if actions[i] is not None:
                    ok_none = 1
            if ok_none == 0:
                # print('toate sunt noNe ')
                draw = None
            elif ok_none == 1:
                for i in range(len(values)):
                    if mx < values[i] and actions[i] is not None:
                        new_values = []
                        new_states = []
                        new_values.append(values[i])
                        new_states.append(actions[i])
                        mx = values[i]
                    elif mx == values[i] and actions[i] is not None:
                        new_values.append(values[i])
                        new_states.append(actions[i])
                okok = 0
                for i in range(len(new_states)):
                    if new_states[i] is not None:
                        okok = 1
                if okok == 1:
                    draw = choice(new_states, 1)
                    # draw = to_str_harcoded(draw)
                    while draw[0] is None:
                        draw = choice(new_states, 1)
                        # draw = to_str_harcoded(draw)
                elif okok == 0:

                    draw = None

                # index = new_values.index(draw)
                draw = to_str_harcoded(draw)
        if self.epsilon > eps_end:
            self.epsilon -= eps_rate
        return draw

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


        if self.state_dict[self.moment][0] is None:
            self.state_dict[self.moment][0] = self.state
            self.flag = 0
        elif self.state_dict[self.moment][1] is None:
            self.state_dict[self.moment][1] = self.state
            self.flag = 1
        else:
            self.state_dict[self.moment][0] = self.state_dict[self.moment][1]
            self.state_dict[self.moment][1] = self.state
            self.flag = 1




    def select_actions(self, rounds, opponent_action):

        self.playable_actions = determine_actions(self.position, self.moment, opponent_action, self.action)
        if self.moment == 'Preflop':
            self.action = self.exploitation_vs_exploaration(self.Q_preflop[self.state[0]][self.state[1]][self.state[2]], self.playable_actions, eps_end, eps_rate)
        elif self.moment == 'Flop':
            self.action = self.exploitation_vs_exploaration(self.Q_flop[self.state[0]][self.state[1]][self.state[2]], self.playable_actions, eps_end, eps_rate)
        elif self.moment == 'Turn':
            self.action = self.exploitation_vs_exploaration(self.Q_turn[self.state[0]][self.state[1]][self.state[2]], self.playable_actions, eps_end, eps_rate)
        elif self.moment == 'River':
            self.action = self.exploitation_vs_exploaration(self.Q_river[self.state[0]][self.state[1]][self.state[2]], self.playable_actions, eps_end, eps_rate)



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
            # print('full', self.carti)
            scor_mana, nCards, mana = full_house(carti)
            # print(scor_mana)
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

    def calculate_reward(self, pot, bigB, winner):
        reward = 0
        if winner == 1:
            reward += 1

        elif winner == 2: #pierd
            reward -= 1

        elif winner == 0: #split
            reward = 0

        if (self.state_new_state[0] is None):
            self.state_new_state[0] = self.state
            self.flag = 0
        elif (self.state_new_state[1] is None):
            self.state_new_state[1] = self.state
            self.flag = 1
        else:
            self.state_new_state[0] = self.state_new_state[1]
            self.state_new_state[1] = self.state
            self.flag = 1

        return reward

    def calculate_reward_p2(self,pot, bigB, winner):
        reward = 0
        if winner == 2:
            reward = 1
        elif winner == 1:
            reward = -1
        elif winner == 0:
            reward = 0
        if (self.state_new_state[0] is None):
            self.state_new_state[0] = self.state
            self.flag = 0
        elif (self.state_new_state[1] is None):
            self.state_new_state[1] = self.state
            self.flag = 1
        else:
            self.state_new_state[0] = self.state_new_state[1]
            self.state_new_state[1] = self.state
            self.flag = 1
        return reward

    def notNone(self):
        if self.state_dict['Preflop'][0] is not None and self.state_dict['Preflop'][1] is not None and self.state_dict['Preflop'][0] is not None and self.state_dict['Flop'][0] is not None and  self.state_dict['Flop'][1] is not None and self.state_dict['Turn'][0] is not None and self.state_dict['Turn'][1] is not None and self.state_dict['River'][0] is not None and self.state_dict['River'][1] is not None:
            return 1
        else:
            return 0


    def updateQ (self, reward):

        if self.update == 1:
            if self.action is not None:
                # if self.flag == 1:
                if self.notNone():
                    if self.moment == 'Preflop':
                        state = self.state_dict['Preflop'][0]
                        new_state = self.state_dict['Preflop'][1]
                        index = self.playable_actions.index(self.action)
                        self.Q_preflop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_preflop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_preflop[state[0]][state[1]][state[2]][index])
                        if self.action == 'Raise':
                            self.Q_raise[state[0]][state[1]][state[2]][self.iraise] += self.alpha * (
                                        reward + self.gamma * max(
                                    self.Q_raise[new_state[0]][new_state[1]][new_state[2]]) -
                                        self.Q_raise[state[0]][state[1]][state[2]][self.iraise])
                    elif self.moment == 'Flop':
                        state = self.state_dict['Preflop'][0]
                        new_state = self.state_dict['Preflop'][1]
                        index = self.playable_actions.index(self.action)
                        self.Q_preflop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_preflop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_preflop[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['Flop'][0]
                        new_state = self.state_dict['Flop'][1]
                        self.Q_flop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_flop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_flop[state[0]][state[1]][state[2]][index])
                        if self.action == 'Raise':
                            self.Q_raise[state[0]][state[1]][state[2]][self.iraise] += self.alpha * (
                                        reward + self.gamma * max(
                                    self.Q_raise[new_state[0]][new_state[1]][new_state[2]]) -
                                        self.Q_raise[state[0]][state[1]][state[2]][self.iraise])
                    elif self.moment == 'Turn':
                        state = self.state_dict['Preflop'][0]
                        new_state = self.state_dict['Preflop'][1]
                        index = self.playable_actions.index(self.action)
                        self.Q_preflop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_preflop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_preflop[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['Flop'][0]
                        new_state = self.state_dict['Flop'][1]
                        self.Q_flop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_flop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_flop[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['Turn'][0]
                        new_state = self.state_dict['Turn'][1]
                        self.Q_turn[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_turn[new_state[0]][new_state[1]][new_state[2]]) - self.Q_turn[state[0]][state[1]][state[2]][index])
                        if self.action == 'Raise':
                            self.Q_raise[state[0]][state[1]][state[2]][self.iraise] += self.alpha * (
                                        reward + self.gamma * max(
                                    self.Q_raise[new_state[0]][new_state[1]][new_state[2]]) -
                                        self.Q_raise[state[0]][state[1]][state[2]][self.iraise])
                    elif self.moment == 'River':
                        state = self.state_dict['Preflop'][0]
                        new_state = self.state_dict['Preflop'][1]
                        index = self.playable_actions.index(self.action)
                        self.Q_preflop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_preflop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_preflop[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['Flop'][0]
                        new_state = self.state_dict['Flop'][1]
                        self.Q_flop[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_flop[new_state[0]][new_state[1]][new_state[2]]) - self.Q_flop[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['Turn'][0]
                        new_state = self.state_dict['Turn'][1]
                        self.Q_turn[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_turn[new_state[0]][new_state[1]][new_state[2]]) - self.Q_turn[state[0]][state[1]][state[2]][index])
                        state = self.state_dict['River'][0]
                        new_state = self.state_dict['River'][1]
                        self.Q_river[state[0]][state[1]][state[2]][index] += self.alpha * (reward + self.gamma * max(self.Q_river[new_state[0]][new_state[1]][new_state[2]]) - self.Q_river[state[0]][state[1]][state[2]][index])
                        if self.action == 'Raise':
                            self.Q_raise[state[0]][state[1]][state[2]][self.iraise] += self.alpha * (reward + self.gamma * max(self.Q_raise[new_state[0]][new_state[1]][new_state[2]]) - self.Q_raise[state[0]][state[1]][state[2]][self.iraise])

