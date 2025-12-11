<!-- PROJECT THUMBNAIL -->
<p align="center">
  <img src="assets/thumbnail.png" width="70%" alt="Project Thumbnail">
</p>

<h1 align="center">🎖️ Squad Training Optimization with Reinforcement Learning</h1>
<p align="center">Undergraduate DS/AI Portfolio Project · Q-learning · Custom RL Environment</p>

---

## 🌟 Overview

This project explores how **Reinforcement Learning (RL)** can be used to design  
an effective training schedule for a small military squad.  

The idea comes from my experience as a **delegated squad leader in Korean military bootcamp**,  
where I had to balance:

- 🏃 Physical training  
- 🎯 Shooting accuracy  
- 🧭 Tactical exercises  
- 😴 Rest & recovery  

The project demonstrates how real-world decision-making can be translated into  
a **Markov Decision Process (MDP)** and solved through **Q-learning**.

---

## 📁 Project Structure

```powershell
Squad-Training-RL/
│
├── main.py
├── env/
│ └── squad_env.py
├── agent/
│ └── q_agent.py
├── utils/
│ └── plot_results.py
└── assets/
├── thumbnail.png
├── rl_loop.png
├── project_architecture.png
└── training_curve_example.png
```

---

## 🧠 Reinforcement Learning Concept

<p align="center">
  <img src="assets/rl_loop.png" width="70%" alt="RL Loop Diagram">
  <br>
  <em>Figure 1. Basic RL Loop: Agent ↔ Environment</em>
</p>

In this project:

- **State** → `[fitness, marksmanship, fatigue]`  
- **Action** → choose one of 4 training types  
- **Reward** → performance gain − fatigue penalty  
- **Goal** → find the optimal multi-day training sequence

---

## 🏗 System Architecture

<p align="center">
  <img src="assets/project_architecture.png" width="75%" alt="Architecture Diagram">
  <br>
  <em>Figure 2. Project Architecture and Data Flow</em>
</p>

The project is intentionally modular to keep it **clean, readable, and expandable**,  
which is especially important for undergraduate DS/AI projects.

---

## 🤖 Q-Learning Agent

The agent uses:

- ε-greedy exploration  
- Q-table with state discretization  
- Learning rule:

```bash
Q(s, a) ← Q(s, a) + α [r + γ max Q(s’, a’) − Q(s, a)]
```

I chose Q-learning because it is:
- easy to interpret,
- great for educational purposes,
- stable on small environments,
- perfect for a first RL project.

---

## 📊 Training Results

<p align="center">
  <img src="assets/training_curve_example.png" width="75%" alt="Training Curve">
  <br>
  <em>Figure 3. Training Reward Progression Across Episodes</em>
</p>

As episodes progress, total reward generally increases,  
showing the agent is learning a stable policy.

---

## ▶ Running the Project

```bash
python main.py
```

The script will:

**1.** Train the Q-learning agent

**2.** Display episodic reward logs

**3.** Plot training curve

**4.** Print a sample of learned “optimal actions”

---

## 📚 What I Learned

This project helped me practice:

- Designing a custom RL environment

- Implementing Q-learning from scratch

- Creating reward/state/action abstractions

- Writing clean & modular Python code

- Visualizing RL progress

- Translating real-world tasks into an MDP

This strengthened both my **AI foundations** and my **ability to model realistic systems**.

---

## 🚀 Future Work

DQN version with neural networks

More realistic fatigue/performance dynamics

Multi-agent squad interactions

Web dashboard (Flask or Streamlit)

Parameter tuning & hyperparameter search

---

<p align="center"> <strong>📬 Thanks for reading! <br>Feel free to open issues or suggestions in the repository.</strong> </p> ```
