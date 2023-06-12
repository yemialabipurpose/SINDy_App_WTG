import pandas as pd
import numpy as np
import scipy.io as sio
import time


def poolData(yin, polyorder, usesine):
    n = yin.shape[0]
    nVars = yin.shape[1]
    yout = [np.ones((n, 1))]

    for i in range(nVars):
        yout.append(yin[:, i].reshape(-1, 1))

    if polyorder >= 2:
        for i in range(nVars):
            for j in range(i, nVars):
                yout.append((yin[:, i] * yin[:, j]).reshape(-1, 1))

    if polyorder >= 3:
        for i in range(nVars):
            for j in range(i, nVars):
                for k in range(j, nVars):
                    yout.append((yin[:, i] * yin[:, j] * yin[:, k]).reshape(-1, 1))

    if usesine:
        for k in range(1):
            yout.append(np.sin(k * yin))
            yout.append(np.cos(k * yin))

    yout = np.concatenate(yout, axis=1)
    return yout
