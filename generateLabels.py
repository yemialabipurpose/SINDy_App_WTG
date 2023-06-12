import pandas as pd
import numpy as np
import scipy.io as sio
import time

def generateLabels(yout, polyorder, usesine):
    yout_labels = ['1']

    for i in range(len(yout)):
        yout_labels.append(str(yout[i]))

    if polyorder >= 2:
        for i in range(len(yout)):
            for j in range(i, len(yout)):
                yout_labels.append(yout[i] + ' * ' + yout[j])

    if polyorder >= 3:
        for i in range(len(yout)):
            for j in range(i, len(yout)):
                for k in range(j, len(yout)):
                    yout_labels.append(yout[i] + ' * ' + yout[j] + ' * ' + yout[k])

    if usesine:
        for i in range(len(yout)):
            for k in range(1):
                yout_labels.append('sin(' + str(k) + ' * ' + yout[i] + ')')
                yout_labels.append('cos(' + str(k) + ' * ' + yout[i] + ')')

    return yout_labels