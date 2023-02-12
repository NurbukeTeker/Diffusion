import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

def diffusion_model(N, D, T, dx, dt):
    """Solve a 1D diffusion equation using finite difference method.

    Parameters:
    N -- number of grid points
    D -- diffusion coefficient
    T -- total time
    dx -- spatial step size
    dt -- time step size

    Returns:
    u -- solution array
    """
    # Create the coefficient matrix
    coef = D * dt / dx**2
    diagonals = [np.ones(N-1) * -coef, np.ones(N) * (1 + 2 * coef), np.ones(N-1) * -coef]
    offsets = [-1, 0, 1]
    A = diags(diagonals, offsets).toarray()

    # Initialize the solution array
    u = np.zeros((int(T/dt), N))
    u[0, :] = np.sin(np.pi * np.linspace(0, 1, N))

    # Solve the diffusion equation using finite difference method
    for i in range(1, int(T/dt)):
        b = u[i-1, :]
        u[i, :] = spsolve(A, b)

    return u
