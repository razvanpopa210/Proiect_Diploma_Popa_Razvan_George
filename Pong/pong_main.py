import numpy as np
from pongV3_agent import DQNAgent
from pongV3_wrappers import make_env

env = make_env('PongNoFrameskip-v4')


gamma = 0.99
epsilon = 1
lr = 0.0001
input_dims = env.observation_space.shape
n_actions = env.action_space.n
memory_size = 10000
eps_min = 0.001
batch_size = 32
replace = 1000
eps_dec = 1e-5
chkpt_dir = 'models/'
algo = 'DQNAgent'
env_name = 'PongNoFrameskip-v4'


best_score = -np.inf
load_checkpoint = False
n_games = 300

agent = DQNAgent(gamma, epsilon, lr, n_actions, input_dims, memory_size, batch_size, eps_min,
                  eps_dec, replace, chkpt_dir='models/', algo='DQNAgent', env_name='PongNoFrameskip-v4')

if load_checkpoint:
    agent.load_models()

fname = agent.algo + '_' + agent.env_name + '_lr' + str(agent.lr) +'_' \
        + str(n_games) + 'games'
figure_file = 'plots/' + fname + '.png'

n_steps = 0
scores, eps_history, steps_array = [], [], []
print(agent.q_eval.device)
for i in range(n_games):
    done = False
    observation = env.reset()

    score = 0
    while not done:
        action = agent.choose_action(observation)
        observation_, reward, done, info = env.step(action)
        score += reward

        if not load_checkpoint:

            index = agent.memory.mem_cntr % agent.memory.mem_size
            agent.memory.state_memory[index] = observation
            agent.memory.new_state_memory[index] = observation_
            agent.memory.action_memory[index] = action
            agent.memory.reward_memory[index] = reward
            agent.memory.terminal_memory[index] = int(done)
            agent.memory.mem_cntr += 1
            agent.learn()
        observation = observation_
        n_steps += 1
    scores.append(score)
    steps_array.append(n_steps)

    avg_score = np.mean(scores[-100:])
    print('episode: ', i,'score: ', score,
         ' average score %.1f' % avg_score, 'best score %.2f' % best_score,
        'epsilon %.2f' % agent.epsilon, 'steps', n_steps)

    if avg_score > best_score:
        if not load_checkpoint:
           agent.save_models()
        best_score = avg_score

    eps_history.append(agent.epsilon)
    if load_checkpoint and n_steps >= 18000:
        break

