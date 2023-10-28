import agent
import util
import rgb
N_RANDOM = 8
DEFAULT_STATE = 'rgrb|grbr|b gr|gbbr'

if __name__ == '__main__':
    cmd = util.get_arg(1)
    if cmd:
        state = rgb.State(util.get_arg(2))
        agent = agent.Agent(state)
        if cmd == 'random':
            agent.random_walk(state, N_RANDOM)
        elif cmd == "bfs":
            agent.bfs()
        elif cmd == "dfs":
            agent.dfs()
        elif cmd == "astar":
            agent.astar()
            