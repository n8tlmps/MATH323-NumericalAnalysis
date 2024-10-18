# Numerical Analysis

## Solutions of Equations in One Variable
Solutions of equations in one variable facilitate optimization processes, such as minimizing loss functions, and help in establishing relationships between variables in regression models. They also provide theoretical foundations for various algorithms and enhance the interpretability of model results.
- [Bisection Method](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab1.ipynb)
- [Fixed-Point Iteration](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab1.ipynb)
- [Newton's Method and Its Extensions](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab2.ipynb)
  - [Secant Method](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab2.ipynb)
- [Muller's Method](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab3.ipynb)

## Interpolation and Polynomial Approximation
Interpolation and polynomial approximation estimate unknown values from known data points, allowing for more accurate predictions and data analysis. These techniques help in modeling complex relationships and handling noisy data, thereby improving the robustness and performance of machine learning models.
- [Langrange Interpolating Polynomial](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab4.ipynb)
- [Newton's Divided-Difference Formula](https://github.com/n8tmps/MATH323-NumericalAnalysis/blob/main/Lab4.ipynb)
- Hermite Polynomials Using Divided Differences
- Hermite Interpolation
- Natural Cubic Spline Interpolation

## Numerical Differentiation and Integration
Numerical differentiation and integration can be used to estimate gradients and optimize functions, which are essential for training models through techniques like gradient descent. Additionally, these methods help in approximating areas under curves for probability distributions, enabling better understanding and modeling of uncertainty in predictions.

### 1D
- Composite Simpson's Rule
- Gaussian Quadrature
### 2D
- Composite Simpson's Rule
- Gaussian Quadrature

## Initial-Value Problems for Ordinary Differential Equations
Initial-value problems for ordinary differential equations (ODEs) are used to model dynamic systems where the future state depends on both the current state and its rate of change, enabling the simulation of complex behaviors over time. These problems are particularly relevant in areas such as reinforcement learning and neural network training, where they can help optimize trajectories and improve model performance by capturing temporal dependencies.
- Euler's Method
- Runge-Kutta Method (Order Four)
- Adams Fourth-Order Predictor-Corrector
- Runge-Kutta Method for Systems of Differential Equations
- Implicit Trapezoidal with Newton Iteration

## Direct Methods for Solving Linear Systems
Direct methods for solving linear systems, such as Gaussian elimination or matrix factorization techniques (like LU decomposition), are used for efficiently solving equations that arise during model training and optimization. These methods are crucial for tasks such as linear regression, where they help compute the optimal coefficients quickly by solving the normal equations derived from the data.
- Gaussian Elimination with Backward Substitution
- Gaussian Elimination with Scaled Partial Pivoting
