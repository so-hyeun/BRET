import os
from sys import path
path.append(os.getcwd())
from data_utils.task_def import DataFormat

def load_chemprot(file, header=True):
    """Loading data of ChemProt
    """
    rows = []
    cnt = 0
    with open(file, encoding="utf8") as f:
        for line in f:
            if header:
                header = False
                continue
            blocks = line.strip().split('\t')
            if blocks[3]== "":
                sample = {'uid': cnt, 'premise': blocks[1], 'label': "CPR:false"}
            else:
                sample = {'uid': cnt, 'premise': blocks[1], 'label': blocks[3]}
            cnt += 1
            rows.append(sample)
    return rows