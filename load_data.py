import pandas as pd
import numpy as np
import scipy.io as sio
import time

def load_data():
    data = sio.loadmat('StringData_square_10_50_80_percent_fault_Variant_B.mat')
    return data['new_x_agg'], data['new_x_agg_dot']