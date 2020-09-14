import os
from sys import path
path.append(os.getcwd())
from data_utils.task_def import DataFormat

def load_gad(file, header=True, train=True):
    """Loading data of GAD
    """
    rows = []
    cnt = 0
    with open(file, encoding="utf8") as f:
        for line in f:
            if header:
                header = False
                continue
            blocks = line.strip().split('\t')
            if train:
                sample = {'uid': cnt, 'premise': blocks[0], 'label': blocks[1]}
            else:
                sample = {'uid': cnt, 'premise': blocks[1], 'label': blocks[2]}
            cnt += 1
            rows.append(sample)
    return rows