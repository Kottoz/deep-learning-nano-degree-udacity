# Deep Learning with PyTorch

This repo contains notebooks and related code for Udacity's Deep Learning with PyTorch lesson. This lesson appears in our [AI Programming with Python Nanodegree program](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089).

* **Part 1:** Introduction to PyTorch and using tensors
* **Part 2:** Building fully-connected neural networks with PyTorch
* **Part 3:** How to train a fully-connected network with backpropagation on MNIST
* **Part 4:** Exercise - train a neural network on Fashion-MNIST
* **Part 5:** Using a trained network for making predictions and validating networks
* **Part 6:** How to save and load trained models
* **Part 7:** Load image data with torchvision, also data augmentation
* **Part 8:** Use transfer learning to train a state-of-the-art image classifier for dogs and cats

* **Notes:** 
- In part 2 trainloader use a Stochastic(Mini batch approache) each iteration(Epoch) loader load number of exambles = 64 
    and our data is image which equal 28x28 pixels and one channel so we need to flatten data(image) 28x28x1 = 784
    so minibatch = (64, 784) 