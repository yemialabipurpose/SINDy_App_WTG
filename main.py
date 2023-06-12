import pandas as pd
import numpy as np
import scipy.io as sio
import time



new_x_agg, new_x_agg_dot = load_data()
variables = ["AVf", "Cuj", "EQA", "ERV", "FhF", "Ghs", "IVk", "Itu", "JYA", "JlO", "LDF", "MVG", "MjO", "MrC", "MzJ", "NlO", "OwO", "OzL", "PhI", "Qwz", "SRl", "TUD", "Tiu", "UAR", "UOb", "WdL", "Xya", "YDe", "ZrZ", "apE", "bMV", "cYA", "cnS", "dsj", "eIa", "eVG", "fJL", "fvc", "hBP", "huP", "jVC", "jkj", "kfQ", "kkd", "lYx", "mPG", "nhc", "omk", "pXN", "qKR", "qdM", "rSk", "sQi", "tBC", "tUa", "usG", "vHT", "viG", "xGV", "xSa", "xVC", "xYV", "xnX", "yla", "zaX"]
start_time = time.time()
yout = poolData(new_x_agg, 3, True)
yout_labels = generateLabels(variables, 3, True)
Xi = STLS(yout, new_x_agg_dot, 0.1, 65)
elapsed_time = time.time() - start_time    
print(f"Program completed in {elapsed_time:.2f} seconds.")