import numpy as np
from numpy.random import choice
import time

Q_table = np.zeros([3,3])
f = open("average.txt", "w")
p = open("equal.txt", "w")



states = {

    'Start': 'Rock',
    'Start': 'Paper',
    'Start': 'Scissors',
    'Rock': 'Start',
    'Paper': 'Start',
    'Scissors': 'Start'

}

actions_memory = {

    'Rock': ['Rock', 'Paper', 'Scissors'],
    'Paper': ['Rock', 'Paper', 'Scissors'],
    'Scissors': ['Rock', 'Paper', 'Scissors']

}

values_memory = [
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
]

values_memory_dict = {
    'Rock Rock': 0,
    'Rock Paper': 0,
    'Rock Scissors': 0,
    'Paper Rock': 0,
    'Paper Paper': 0,
    'Paper Scissors': 0,
    'Scissors Rock': 0,
    'Scissors Paper': 0,
    'Scissors Scissors': 0
}

values_array_of_array = [

    ['Rock', 'Rock', 0],
    ['Rock', 'Paper', 0],
    ['Rock', 'Scissors', 0],
    ['Paper', 'Rock', 0],
    ['Paper', 'Paper', 0],
    ['Paper', 'Scissors', 0],
    ['Scissors', 'Rock', 0],
    ['Scissors', 'Paper', 0],
    ['Scissors', 'Scissors', 0]

]


actions_layerOne = ['Rock', 'Paper', 'Scissors']
states_memory = ['Rock', 'Paper', 'Scissors']

actions_v2 = ['Rock', 'Paper', 'Scissors', 'Start']

actions = ['Rock', 'Paper', 'Scissors']
ideal_response = {'Rock': 'Paper',
                  'Paper': 'Scissors',
                  'Scissors': 'Rock'
                  }

rewards = [[0, 99, 1],
           [1, 0, -1],
           [-1, 1, 0]]

winningMatrix = {'RockRock': 1, 'RockPaper': -1, 'RockScissors': 100, 'PaperRock': 100, 'PaperPaper': 1,
                 'PaperScissors': -1, 'ScissorsRock': -1, 'ScissorsPaper': 100, 'ScissorsScissors': 1}

def working_on_average(average_vector):
    esantion_medie = 100
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
    esantion_medie = 100
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



def space(draw1, draw2):
    return draw1+' '+draw2


def to_str_hardcoded(draw):
    if draw == 'Rock':
        return 'Rock'
    if draw == 'Paper':
        return 'Paper'
    if draw == 'Scissors':
        return 'Scissors'





def two_verify(values):
    if values[0] == 0 and values[1] == 0:
        return 0, 1
    elif values[0] == 0 and values[2] == 0:
        return 0, 2
    elif values[1] == 0 and values[2] == 0:
        return 1, 2


def maximum_in_values(mx, values, actions):
    new_values = []
    new_states = []
    for i in range(len(values)):
        if mx < values[i]:
            new_values = []
            new_states = []
            new_values.append(values[i])
            new_states.append(actions[i])
            mx = values[i]
        elif mx == values[i]:
            new_values.append(values[i])
            new_states.append(actions[i])
    draw = choice(new_states, 1)
    draw = to_str_hardcoded(draw)
    # index = new_values.index(draw)
    return draw

def search_in_memory(previous_draw, current_draw, actions):
    for i in range(len(actions)):
        if actions[i][0] == previous_draw and actions[i][1] == current_draw:
            return i

def draw_maximum(x, mx, actions):
    new_values = []
    new_states = []
    for i in range(3):
        if mx < actions[x+i][2]:
            new_values = []
            new_states = []
            new_values.append(actions[x+i][2])
            new_states.append(actions[x+i][1])
            mx = actions[i][2]
        elif mx == actions[x+i][2]:
            new_values.append(actions[x+i][2])
            new_states.append(actions[x+i][1])
    draw = choice(new_states, 1)
    draw = to_str_hardcoded(draw)
    return draw

def maximum_array_of_array(actions):
    for i in range(len(actions)):
        if actions[i][2] > maximum:
            maximum = actions[i][2]
    return maximum


class jucatorComun:

    def __init__(self, choices_for_player, percentage_for_player):
        self.choices = choices_for_player
        self.percentage = percentage_for_player

    def draw_once(self):
        draw = choice(self.choices, 1, p=self.percentage)
        draw = to_str_hardcoded(draw)
        # draw_index = self.choices.index(draw)
        return draw


epsilon = 1

class jucatorR:

    def __init__(self, actions, values, mx, mx_score, percentages):
        self.actions = actions
        self.values = values
        self.mx = mx
        self.percentages = percentages
        self.mx_score = mx_score
        self.Q = Q_table
        self.action_vector = [None]*2
        self.eps_min = 0.001
        self.eps_dec = 0.001

    def draw_r_v2(self):
        return maximum_in_values(self.mx, self.values, self.actions)

    def draw_w_percentages(self):
        draw = choice(self.actions, 1, self.percentages)
        draw = to_str_hardcoded(draw)
        return draw

    def modify_percentages(self, score, draw):

        if score >= self.mx_score:
            index = self.actions.index(draw)
            self.mx_score = score
            self.percentages[index] = self.percentages[index] + 0.05
        for k in range(3):
            if k != self.actions.index(draw):
                self.percentages[k] = self.percentages[k] - 0.025
        if sum(self.percentages) > 1:
            for i in range(len(self.percentages)):
                self.percentages[i] = self.percentages[i] / sum(self.percentages)
        for i in range(len(self.percentages)):
            if self.percentages[i] > 1:
                for j in range(len(self.percentages)):
                    if i == j:
                        self.percentages[j] = 1
                    else:
                        self.percentages[j] = 0
            elif self.percentages[i] < 0:
                self.percentages[i] = 0







class jucatorCuMemorie:

    def __init__(self, mx, actions_layerOne, values):
        self.mx = mx
        self.actions_layerOne = actions_layerOne
        self.values = values
        self.Q = Q_table
        self.action_vector = [None]*2
        self.action = None
        self.alpha = 0.05
        self.gamma = 0.90
        self.win_counter = 0
        self.equal_counter = 0
        self.train = 0
        self.save_vector = []
        self.average_vector = []
        self.lose_counter = 0
        self.equal_average_vector = []
        self.epsilon = 1
        self.eps_dec = 0.0001
        self.eps_min = 0.0

        self.my_actions = [None]*2

    def draw(self, previous_draw):
        if previous_draw is None:
            return self.draw_first_round()
        else:
            for i in range(len(self.values)):
                if previous_draw == self.values[i][0]:
                    self.action =  draw_maximum(i, self.mx, self.values)
                    return self.action

    def draw_q(self):
        actions = ['Rock', 'Paper', 'Scissors']
        new_values = []
        new_states = []
        if self.action_vector[0] is None:
            return self.draw_first_round()
        elif self.action_vector[1] is None:
            previous_action = self.action_vector[0]
        else:
            previous_action = self.action_vector[1]
        indexPrevious = self.determineIndex(previous_action)
        mx = -999999999


        x = np.random.random()
        if (x <= self.epsilon):
            self.action = np.random.choice(['Rock', 'Paper', 'Scissors'], 1)
            self.action = to_str_hardcoded(self.action)
            if self.epsilon > self.eps_min:
                self.epsilon -= self.eps_dec
            return self.action
        else:
            if self.epsilon > self.eps_min:
                self.epsilon -= self.eps_dec


            for i in range(len(self.Q[indexPrevious])):
                if mx < self.Q[indexPrevious][i]:
                    new_values = []
                    new_states = []
                    new_values.append(self.Q[indexPrevious][i])
                    new_states.append(actions[i])
                    mx = self.Q[indexPrevious][i]
                elif mx == self.Q[indexPrevious][i]:
                    new_values.append(self.Q[indexPrevious][i])
                    new_states.append(actions[i])
            self.action = choice(new_states, 1)
            self.action = to_str_hardcoded(self.action)
            return self.action

    def draw_q_prob(self):
        actions = ['Rock', 'Paper', 'Scissors']
        new_values = []
        new_states = []
        if self.action_vector[0] is None:
            return self.draw_first_round()
        elif self.action_vector[1] is None:
            previous_action = self.action_vector[0]
        else:
            previous_action = self.action_vector[1]

        indexPrevious = self.determineIndex(previous_action)
        mn = 99999999

        x = np.random.random()
        if (x <= self.epsilon):
            self.action = choice(actions, 1)
            self.action = to_str_hardcoded(self.action)
            if self.epsilon > self.eps_min:
                self.epsilon -= self.eps_dec
            return self.action
        else:
            if self.epsilon > self.eps_min:
                self.epsilon -= self.eps_dec
            for i in range(len(self.Q[indexPrevious])):
                if self.Q[indexPrevious][i] < mn:
                    mn = self.Q[indexPrevious][i]
            S = 0
            if mn < 0:
                mn = -mn
                for i in range(len(self.Q[indexPrevious])):
                    x = self.Q[indexPrevious][i] + mn
                    new_values.append(x)
                    S += x
                if S == 0:
                    self.action = choice(actions, 1)
                    self.action = to_str_hardcoded(self.action)
                    return self.action

            elif mn >= 0:
                for i in range(len(self.Q[indexPrevious])):

                    S += self.Q[indexPrevious][i]
                    new_values.append(self.Q[indexPrevious][i])
                if S == 0:
                    self.action = choice(actions, 1)
                    self.action = to_str_hardcoded(self.action)
                    return self.action
            for i in range(len(new_values)):
                new_values[i] = new_values[i] / S
            self.action = choice(actions, 1, p=new_values)

            self.action = to_str_hardcoded(self.action)
            return self.action

    def draw_first_round(self):
        draw = choice(actions_layerOne, 1)
        draw = to_str_hardcoded(draw)
        self.my_actions[0] = draw
        return draw

    def determine_action_vector(self, draw_p2):
        if self.action_vector[0] is None:
            self.action_vector[0] = draw_p2
            self.my_actions[0] = self.action
        elif self.action_vector[1] is None:
            self.action_vector[1] = draw_p2
            self.my_actions[1] = self.action
        else:
            self.action_vector[0] = self.action_vector[1]
            self.action_vector[1] = draw_p2
            self.my_actions[0] = self.my_actions[1]
            self.my_actions[1] = self.action

    def determineIndex(self, action):
        if action == 'Rock':
            return 0
        elif action == 'Paper':
            return 1
        elif action == 'Scissors':
            return 2

    def updateQ(self, reward, draw_p2):
        if self.train == 1:
            state = [None]*2
            new_state = [None]*2
            state_action = [None]*2
            new_state_action = [None]*2
            if self.action_vector[0] is not None and self.action_vector[1] is not None:
                state[0] = self.determineIndex(self.action_vector[0]) #rock
                state[1] = self.determineIndex(self.action_vector[1]) #paper
                state_action[0] = self.determineIndex(self.my_actions[0])
                state_action[1] = self.determineIndex(self.my_actions[1])
                self.determine_action_vector(draw_p2)
                new_state[0] = self.determineIndex(self.action_vector[0]) #paper
                new_state[1] = self.determineIndex(self.action_vector[1]) #rock
                new_state_action[0] = self.determineIndex(self.my_actions[0])
                new_state_action[1] = self.determineIndex(self.my_actions[1])

                self.Q[state[0]][state_action[1]] += self.alpha * (reward + self.gamma * max( self.Q[new_state[0]]) - self.Q[state[0]][state_action[1]])



class jocV2:

    def __init__(self, rounds):
        self.rounds = rounds

    def score_and_result(self, draw1, draw2):

        x = draw1 + draw2
        if winningMatrix[x] == 0:
            result = 'draw'
            score = winningMatrix[x]
        elif winningMatrix[x] > 0:
            result = 'win'
            score = winningMatrix[x]
        elif winningMatrix[x] < 0:
            result = 'lose'
            score = winningMatrix[x]
        return score, result

    def play_a_round(self, p1, p2):
        # draw_p1 = p1.draw_w_percentages()
        draw_p1 = p1.draw_q()

        draw_p2 = p2.draw_once()
        if p1.action_vector[0] is None or p1.action_vector[1] is None:
            p1.determine_action_vector(draw_p2)
        score, result = self.score_and_result(draw_p1, draw_p2)
        p1.values[p1.actions.index(draw_p1)] += score
        p1.updateQ(score)
        print("p1 values: ", p1.values)
        print('p1 percentages: ', p1.percentages)
        p1.modify_percentages(score, draw_p1)

    def play_n_rounds (self, p1, p2):
        for i in range(self.rounds):
            self.play_a_round(p1, p2)


class jocCuMemorie:

    def __init__(self, rounds):
        self.rounds = rounds
        self.contor = 0

    first_round = 1
    previous_draw = ''
    result = ''
    score = 0

    def score_and_result(self, draw1, draw2):

        x = draw1 + draw2
        if winningMatrix[x] == 0:
            result = 'draw'
            score = winningMatrix[x]
        elif winningMatrix[x] > 0:
            result = 'win'
            score = winningMatrix[x]
        elif winningMatrix[x] < 0:
            result = 'lose'
            score = winningMatrix[x]
        return score, result

    def play_a_round(self, p1, p2, i):
        self.contor += 1
        # draw_p1 = p1.draw_w_percentages()
        if p1.action_vector[0] is None:
            draw_p1 = p1.draw_first_round()
            draw_p2 = p2.draw_once()
            p1.action_vector[0] = draw_p2
            p1.my_actions[0] = draw_p1
            score, result = self.score_and_result(draw_p1, draw_p2)
            if result == 'win':
                p1.win_counter += 1
                p1.average_vector.append(1)
                p1.equal_average_vector.append(0)
            elif result == 'draw':
                p1.equal_counter += 1
                p1.average_vector.append(0)
                p1.equal_average_vector.append(0)

            elif result == 'lose':
                p1.lose_counter += 1
                p1.average_vector.append(0)
                p1.equal_average_vector.append(1)



            p1.save_vector.append(draw_p1)

        else:
            draw_p1 = p1.draw_q()

            draw_p2 = p2.draw_once()
            if p1.action_vector[0] is None or p1.action_vector[1] is None:
                p1.determine_action_vector(draw_p2)

            score, result = self.score_and_result(draw_p1, draw_p2)
            if self.contor > 1:
                p1.updateQ(score,draw_p2)
            if result == 'win':
                p1.win_counter += 1
                p1.average_vector.append(1)
                p1.equal_average_vector.append(0)

            elif result == 'draw':
                p1.equal_counter += 1
                p1.average_vector.append(0)
                p1.equal_average_vector.append(1)

            elif result == 'lose':
                p1.lose_counter += 1
                p1.average_vector.append(0)
                p1.equal_average_vector.append(0)

            p1.save_vector.append(draw_p1)



    def play_n_rounds (self, p1, p2):
        for i in range(self.rounds):
            if i % 2 == 0:
                p2.percentage = [1, 0, 0]
            elif i % 2 == 1:
                p2.percentage = [0, 1, 0]
            self.play_a_round(p1, p2, i)






print('nr runde')
# n = int(input())
n = 50000
start_time = time.time()

only_rock = [1, 0, 0]
only_paper = [0, 1, 0]
only_scissors = [0, 0, 1]

# player1 = jucatorR(actions, [0, 0, 0], -100, -100, [1/3, 1/3, 1/3])
player2 = jucatorComun(actions, [0.40, 0.40, 0.20])


# # game = jocV2(n)
# game.play_n_rounds(player1, player2)

player1 = jucatorCuMemorie(-100,actions_layerOne,values_array_of_array)


game = jocCuMemorie(n)
suma = 0
ok = 0
runde = 0
player1.train = 1
m = 1
nvector = []
####################################### NON ADAPTIV ######################################################
for i in range (m):
    player1.Q = np.zeros([3,3])
    player1.train = 1
    player1.win_counter = 0
    player1.equal_counter = 0
    player1.epsilon = 1
    game.play_n_rounds(player1, player2)
    # while ok == 0:
    #     game.play_a_round(player1, player2)
    #     suma = 0
    #     for i in range (len(player1.values)):
    #         suma += player1.values[i][2]
    #     if suma >= 100:
    #         ok = 1
    #     runde += 1
    # print (runde)



    player1.train = 0

    player1.win_counter = 0
    player1.equal_counter = 0

    game.play_n_rounds(player1, player2)

    print('equal rate', player1.equal_counter/n)
    print('win rate', player1.win_counter/n)

    if i == 0:
        a = player1.win_counter/n

    print(player1.Q)

    nvector.append(player1.win_counter/n)

# #################################################### ADAPTIVE ##########################################################
#
# game.play_n_rounds(player1,player2)
# v = working_on_average(player1.average_vector)
# working_on_average_equal(player1.equal_average_vector, v)
#
#
#
#
print(player1.action_vector)
print(player1.my_actions)
print(player1.action)
print ('win rate one time', a)
print (player1.Q)
print(' ---- %s seconds ---- ' % (time.time() - start_time))
print(nvector)
print(sum(nvector)/len(nvector))
#
# # print(player1.save_vector)
# # print(len(player1.save_vector))
# f.close()