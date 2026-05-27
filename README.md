# Machine Learning Models Collection

A collection of machine learning and deep learning models implemented from scratch and with minimal dependencies for educational purposes.

This repository focuses on understanding the mathematics, algorithms, and implementation details behind modern AI systems.

---

# Goals

This project is designed to:

- Learn machine learning fundamentals deeply
- Implement algorithms from scratch
- Understand neural network mathematics
- Explore optimization and training techniques
- Build intuition for AI systems
- Compare classical ML vs deep learning approaches

---

# Repository Structure

```txt
machine-learning-models/
│
├── models/
│   ├── machine_learning/
│   │   ├── linear_regression/
│   │   ├── logistic_regression/
│   │   ├── decision_trees/
│   │   ├── svm/
│   │   └── clustering/
│   │
│   └── deep_learning/
│       ├── neural_networks/
│       ├── cnn/
│       ├── rnn/
│       ├── transformers/
│       └── autoencoders/
│
├── datasets/
├── notebooks/
├── docs/
└── README.md
```

---

# What is Machine Learning?

Machine Learning (ML) is a field of artificial intelligence where computers learn patterns from data instead of being explicitly programmed.

Traditional programming:

```txt
Rules + Data → Answers
```

Machine learning:

```txt
Data + Answers → Rules
```

ML systems improve performance by learning from examples.

---

# Main Types of Machine Learning

## Supervised Learning

The model learns using labeled data.

Examples:

- Image classification
- Spam detection
- Price prediction
- Sentiment analysis

Algorithms:

- Linear Regression
- Logistic Regression
- Support Vector Machines
- Neural Networks

---

## Unsupervised Learning

The model finds hidden patterns without labels.

Examples:

- Clustering
- Dimensionality reduction
- Anomaly detection

Algorithms:

- K-Means
- PCA
- DBSCAN

---

## Reinforcement Learning

An agent learns by interacting with an environment using rewards and penalties.

Examples:

- Game AI
- Robotics
- Self-driving systems

---

# What is Deep Learning?

Deep Learning is a subset of machine learning based on artificial neural networks with multiple layers.

Instead of manually designing features, deep learning models automatically learn representations directly from data.

Deep learning excels at:

- Computer vision
- Natural language processing
- Speech recognition
- Generative AI
- Robotics

---

# Neural Networks

Artificial neural networks are inspired by biological neurons.

Basic structure:

```txt
Input Layer → Hidden Layers → Output Layer
```

Each neuron performs:

```txt
z = Wx + b
a = activation(z)
```

Where:

- `x` = inputs
- `W` = weights
- `b` = bias
- `a` = output activation

---

# Deep Learning Architectures

## Feedforward Neural Networks

Basic fully connected networks used for classification and regression.

---

## Convolutional Neural Networks (CNNs)

Specialized for image processing.

Used in:

- Object detection
- Image classification
- Medical imaging

---

## Recurrent Neural Networks (RNNs)

Designed for sequential data.

Used in:

- Text generation
- Language modeling
- Time-series forecasting

---

## Transformers

Modern architecture powering large language models.

Used in:

- ChatGPT
- Translation systems
- Code generation
- Multimodal AI

---

# Mathematical Foundations

This repository explores the mathematics behind AI, including:

- Linear algebra
- Calculus
- Probability
- Optimization
- Gradient descent
- Backpropagation
- Information theory

---

# Current Models

| Category | Model | Status |
|---|---|---|
| Deep Learning | MNIST Logistic Regression | Complete |
| Deep Learning | Fully Connected Neural Network | In Progress |
| Machine Learning | Linear Regression | Planned |
| Machine Learning | Decision Tree | Planned |
| Deep Learning | CNN | Planned |
| Deep Learning | Transformer | Planned |

---

# Technologies Used

- Python
- NumPy
- Matplotlib
- Jupyter Notebook
- PyTorch (future)
- TensorFlow (future)

---

# Running Projects

Each project folder contains its own README with setup instructions.

Example:

```bash
cd models/deep_learning/neural_networks/stg
uv run python main.py
```

---

# Educational Philosophy

This repository prioritizes:

- Simplicity
- Mathematical understanding
- Clean implementations
- Minimal abstractions
- Learning-by-building

Many implementations intentionally avoid high-level frameworks initially to expose the underlying mechanics.

---

# Future Goals

- Implement CNNs from scratch
- Build transformers from scratch
- Explore diffusion models
- Add reinforcement learning agents
- Compare optimizers mathematically
- Create visual training tools
- Benchmark models

---

# Recommended Learning Path

1. Linear Algebra
2. Calculus
3. Probability & Statistics
4. Classical Machine Learning
5. Neural Networks
6. Deep Learning
7. Transformers
8. Generative AI

---

# References

Books:

- Deep Learning — Ian Goodfellow
- Neural Networks and Deep Learning — Michael Nielsen
- Pattern Recognition and Machine Learning — Christopher Bishop

Courses:

- Andrew Ng Machine Learning
- CS231n Stanford
- fast.ai

---

# License

MIT License @Stewie-pixel