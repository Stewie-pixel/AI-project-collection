# Code samples for "Neural Networks and Deep Learning"

This repository contains code exercise for this book of mnielsen on ["Neural Networks
and Deep Learning"](http://neuralnetworksanddeeplearning.com).

The program `stg/main.py` uses latest version of the mnist
library.

As the code is written to solve exercises in the book, I don't intend to add
new features. However, bug reports are welcome, and you should feel
free to fork and modify the code.

# MNIST Logistic Regression from Scratch

A simple neural network implementation using only NumPy to classify handwritten digits from the MNIST dataset.

This project implements:

- 784 → 10 neural network
- No hidden layer
- Stochastic Gradient Descent (SGD)
- Sigmoid activation
- Backpropagation with Mean Squared Error (MSE)

Because there is no hidden layer, this model is mathematically equivalent to **multi-class logistic regression**.

Expected accuracy: **~92%** on the MNIST test dataset.


# Project Structure

```txt
.
├── main.py
├── README.md
└── pyproject.toml
```


# Requirements

- Python 3.10+
- NumPy
- MNIST dataset package
- uv package manager (recommended)


# Installation

## 1. Create virtual environment

```bash
uv venv
```

## 2. Install dependencies

```bash
uv add numpy mnist
```

Or using pip:

```bash
pip install numpy mnist
```


# Running the Project

```bash
uv run python main.py
```

Or:

```bash
python main.py
```


# Example Output

```txt
Loading MNIST...
Train: 60000, Test: 10000

 Epoch     Test acc     Train acc
--------------------------------------
     1        87.31%        87.65%
     2        89.41%        89.73%
     3        90.22%        90.51%
...
    30        92.14%        92.37%

Final test accuracy: 92.14%
```


# How It Works

## Input Layer

Each MNIST image is:

- 28 × 28 grayscale
- Flattened into a vector of 784 pixels

```txt
28 × 28 = 784
```


## Output Layer

The network outputs probabilities for digits:

```txt
0 1 2 3 4 5 6 7 8 9
```

using 10 output neurons.


# Network Architecture

```txt
784 inputs  →  10 outputs
```

No hidden layers are used.

This means the network can only learn **linear decision boundaries**.


# Forward Pass

The model computes:

```txt
z = Wx + b
a = sigmoid(z)
```

Where:

- `W` = weights
- `x` = input image
- `b` = bias
- `a` = activation output


# Loss Function

Mean Squared Error (MSE):

```txt
Loss = (a - y)^2
```

where:

- `a` = predicted output
- `y` = one-hot encoded label


# Training

Training uses:

- Mini-batch SGD
- Backpropagation
- Xavier weight initialization


# Accuracy

Typical performance:

| Model | Accuracy |
|---|---|
| Logistic Regression (this project) | ~92% |
| One Hidden Layer (~30 neurons) | ~95% |
| Modern CNNs | >99% |


# Notes

- This project is educational and focuses on understanding neural networks from scratch.
- Using sigmoid + MSE is not optimal for classification.
- Softmax + Cross Entropy would generally perform better.


# Possible Improvements

- Add hidden layers
- Replace sigmoid with ReLU
- Use softmax output
- Use cross-entropy loss
- Add momentum or Adam optimizer
- Visualize predictions
- GPU acceleration with PyTorch


# References

- MNIST Dataset
- Neural Networks and Deep Learning — Michael Nielsen
- NumPy Documentation


# License

MIT License @Stewie-pixel