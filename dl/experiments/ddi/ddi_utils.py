import os
from sys import path
path.append(os.getcwd())
from data_utils.task_def import DataFormat

def load_ddi(file, header=True):
    """Loading data of ddi2013-type
    """
    rows = []
    cnt = 0
    with open(file, encoding="utf8") as f:
        for line in f:
            if header:
                header = False
                continue
            blocks = line.strip().split('\t')
            sample = {'uid': cnt, 'premise': blocks[1], 'label': blocks[2]}
            cnt += 1
            rows.append(sample)
    return rows
