# Efficient Parallel Reinforcement Learning Framework Using the Reactor Model

This repository contains the code and benchmarks for the paper "Efficient Parallel Reinforcement Learning Framework Using the Reactor Model". The paper proposes a solution implementing the reactor model, which enforces a set of actors to have a fixed communication pattern, allowing for efficient orchestration of training, serving, and simulation workloads in Reinforcement Learning tasks.

## Contents

The repository includes the following folders and files:

1. `Number_of_Actors`: Benchmarks for evaluating the performance with varying number of actors.
2. `Object_Size`: Benchmarks for evaluating the performance with different object sizes.
3. `Gym_Environments`: Benchmarks for OpenAI Gym environments.
4. `Atari_Environments`: Benchmarks for Atari environments.
5. `Parallel_Q_learning`: Benchmarks for synchronized parallel Q-learning.
6. `Multi_Agent_Inference`: Benchmarks for multi-agent RL inference.
7. `Dataflow_Graph`: Template for generating dataflow graph.
8. `.gitignore`: Git ignore file.
9. `Dockerfile`: Dockerfile for running the benchmarks.

## Install

You can simplify reproduction using an OS virtualization environment with Docker.

### Build the Docker image

```
docker build -t parallel_rl_benchmarks`
```

## Running the Benchmarks

```
docker run parallel_rl_benchmarks
```
