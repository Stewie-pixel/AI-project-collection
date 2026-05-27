"""
Exercise: 784 → 10 network (no hidden layer) trained with SGD on MNIST.
This is equivalent to multi-class logistic regression.

Expected accuracy: ~92% on MNIST test set.
(vs ~95% with one hidden layer of 30 neurons)

Usage:
    uv pip install numpy
    python main.py
    
    MNIST data is loaded via the `mnist` package:
    uv pip install mnist
"""

import numpy as np
from sklearn.datasets import fetch_openml


def load_mnist():
    mnist_data = fetch_openml('mnist_784', version=1)

    X = mnist_data.data.to_numpy().astype(np.float64) / 255.0
    y = mnist_data.target.astype(np.int64).to_numpy()

    x_train = X[:60000]
    y_train = y[:60000]

    x_test = X[60000:]
    y_test = y[60000:]

    return x_train, y_train, x_test, y_test

def one_hot(y, n=10):
    oh = np.zeros((len(y), n))
    oh[np.arange(len(y)), y] = 1.0
    return oh


def sigmoid(z):
    """Element-wise sigmoid."""
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

def sigmoid_prime(z):
    s = sigmoid(z)
    return s * (1 - s)


class Network:
    """
    Two-layer network: input (784) → output (10).
    No hidden layer — this is exactly multi-class logistic regression.
    """

    def __init__(self, lr=3.0, mini_batch_size=10, epochs=30):
        self.lr = lr
        self.mini_batch_size = mini_batch_size
        self.epochs = epochs
        if self.epochs <= 0:
            raise ValueError("epochs must be > 0")
        rng = np.random.default_rng(42)
        # Xavier init: scale by 1/sqrt(n_in)
        self.W = rng.normal(0, 1.0 / np.sqrt(784), (10, 784))  # (10, 784)
        self.b = np.zeros((10, 1))                              # (10, 1)

    def feedforward(self, x):
        """x: (784,) → output: (10,)"""
        return sigmoid(self.W @ x.reshape(-1, 1) + self.b).flatten()

    def evaluate(self, X, y):
        """Return number of correctly classified samples."""
        Z = self.W @ X.T + self.b        # (10, n)
        preds = np.argmax(sigmoid(Z), axis=0)
        return int(np.sum(preds == y))

    def sgd(self, x_train, y_train, x_test, y_test):
        y_train_oh = one_hot(y_train)
        n = len(x_train)
        rng = np.random.default_rng(42)

        test_acc = 0.0

        print(f"\n{'Epoch':>6}  {'Test acc':>12}  {'Train acc':>12}")
        print("-" * 38)

        for epoch in range(self.epochs):
            # Shuffle
            idx = rng.permutation(n)
            Xs, Ys = x_train[idx], y_train_oh[idx]

            # Mini-batch updates
            for k in range(0, n, self.mini_batch_size):
                Xb = Xs[k : k + self.mini_batch_size]   # (mb, 784)
                Yb = Ys[k : k + self.mini_batch_size]   # (mb, 10)
                mb = len(Xb)

                # Forward pass
                Z = self.W @ Xb.T + self.b              # (10, mb)
                A = sigmoid(Z)                          # (10, mb)

                # Backprop with MSE loss
                # δ = (a − y) ⊙ σ′(z)
                delta = (A - Yb.T) * sigmoid_prime(Z)  # (10, mb)

                # Gradient descent
                self.W -= self.lr * (delta @ Xb) / mb
                self.b -= self.lr * delta.mean(axis=1, keepdims=True)

            # Evaluate
            train_acc = self.evaluate(x_train, y_train) / n * 100
            test_acc  = self.evaluate(x_test, y_test) / len(x_test) * 100
            print(f"{epoch+1:>6}  {test_acc:>11.2f}%  {train_acc:>11.2f}%")

        return test_acc


if __name__ == "__main__":
    print("Loading MNIST...")
    x_train, y_train, x_test, y_test = load_mnist()
    print(f"Train: {len(x_train)}, Test: {len(x_test)}")

    net = Network(lr=3.0, mini_batch_size=10, epochs=30)
    final_acc = net.sgd(x_train, y_train, x_test, y_test)

    print(f"\nFinal test accuracy: {final_acc:.2f}%")
    print("\nNote: without a hidden layer this network is equivalent to")
    print("multi-class logistic regression — it can only learn linear")
    print("decision boundaries in pixel space, giving ~92% accuracy.")
    print("Adding a hidden layer (e.g. 30 neurons) pushes this to ~95%.")