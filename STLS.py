import numpy as np

def STLS(Theta, dXdt, lambda_val, n):
    Xi = np.linalg.lstsq(Theta, dXdt, rcond=None)[0]

    for _ in range(10):
        smallinds = np.abs(Xi) < lambda_val
        Xi[smallinds] = 0

        for ind in range(n):
            biginds = ~smallinds[:, ind]
            Xi[biginds, ind] = np.linalg.lstsq(Theta[:, biginds], dXdt[:, ind], rcond=None)[0]

    return Xi