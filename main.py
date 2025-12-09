from env.squad_env import SquadTrainingEnv
from agent.q_agent import QLearningAgent
from utils.plot_results import plot_rewards

def main():
    env = SquadTrainingEnv()
    agent = QLearningAgent()

    episodes = 500   # 대학생 수준으로 무난
    reward_history = []

    for ep in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            total_reward += reward

        reward_history.append(total_reward)

        if ep % 50 == 0:
            print(f"Episode {ep}, Total Reward: {total_reward:.2f}")

    # Plot reward progression
    plot_rewards(reward_history)

    # Show optimal action sequence from initial state
    print("\nSample Optimal Actions:")
    state = env.reset()
    for _ in range(15):
        a = agent.get_action(state)
        print(a, end=" -> ")
        state, _, done = env.step(a)
        if done:
            break

if __name__ == "__main__":
    main()
