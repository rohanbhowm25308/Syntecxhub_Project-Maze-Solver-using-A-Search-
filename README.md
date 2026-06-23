# Syntecxhub_Project-Maze-Solver-using-A*-Search
Maze Solver using A* Search Algorithm in Python with Manhattan heuristic to find the shortest path in a grid-based maze.

# 🧩 Maze Solver using A* Search Algorithm

## 🚀 Overview

Maze Solver using A* Search Algorithm is an intelligent pathfinding project developed in Python. The system navigates through a grid-based maze and efficiently discovers the shortest route from a starting point to a destination while avoiding obstacles.

By combining actual travel cost with a heuristic estimate, the A* algorithm delivers fast and optimal pathfinding, making it one of the most widely used algorithms in Artificial Intelligence, Robotics, and Navigation Systems.

---

## ✨ Features

- Implementation of the A* Search Algorithm
- Grid-based maze representation
- Obstacle and wall handling
- Manhattan Distance heuristic
- Optimal shortest-path discovery
- Clean and beginner-friendly Python code
- Fast and efficient pathfinding

---

## 🛠️ Technologies Used

- Python
- Priority Queue
- Artificial Intelligence Concepts
- A* Search Algorithm

---

## 🧠 How It Works

The maze consists of:

- `0` → Free path
- `1` → Obstacle/Wall

The A* algorithm evaluates each possible move using:

f(n) = g(n) + h(n)

Where:

- `g(n)` = Cost from start node to current node
- `h(n)` = Estimated cost to reach the goal
- `f(n)` = Total estimated cost

The algorithm always chooses the path with the lowest estimated cost, ensuring efficient navigation.

---

## ▶️ Running the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/maze-solver-a-star.git
