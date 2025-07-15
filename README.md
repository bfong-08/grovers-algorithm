# Implementing Grover's Algorithm for a 3-Qubit Unique Search Problem using Qiskit

## Table of Contents

- [Overview](#overview)
- [Key Concepts](#key-concepts)
- [How to Use](#how-to-use)
- [Next Steps](#next-steps)
- [License](#license)
- [Contact](#contact)

## Overview

Grover's Algorithm is one of the most important quantum algorithms in terms of showcasing potential advantages of quantum methods over classical solutions. It provides a *quadratic* speedup on unstructed search problems compared to classical algorithms, bringing the time complexity from $O(N)$ to $O(\sqrt{N})$.

In this project, I seek to implement Grover's Algorithm using Qiskit in order to solve a 3-Qubit unique search problem. 

## Key concepts

- **Custom Oracles** using built-in qubit operations
- **A

## How to Use

1. Clone the repository

```bash
git clone https://github.com/bfong-08/grovers-algorithm.git
cd grovers-algorithm
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python main.py
```

4. View the output
- A matplotlib bar chart will display the measurement outcomes from 100 iterations of Grover's Algorithm.

## Next Steps

My future goals are to explore how Grover's Algorithm can be utilized to solve various real world problems (crytography key search, CSPs, etc.). I intend to research advantages of Grover's Algorithm in solving meaningful problems, as well as how I can modify Grover's Algorithm to achieve different results.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for detals.

## Contact

Brandon Fong

branfong21@gmail.com

[https://github.com/bfong-08](https://github.com/bfong-08)
