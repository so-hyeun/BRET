import os
import argparse
from sys import path
path.append(os.getcwd())
from data_utils.task_def import DataFormat
from data_utils.log_wrapper import create_logger
from experiments.GAD.gad_utils import load_gad
from experiments.common_utils import dump_rows

def parse_args():
    parser = argparse.ArgumentParser(description='Preprocessing English GAD dataset.')
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--seed', type=int, default=13)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()
    return args

def main(args):
    data_dir = args.data_dir
    data_dir = os.path.abspath(data_dir)
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)

    Fold = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for number in Fold:
        train_path = os.path.join(data_dir, number+'/train.tsv')
        test_path = os.path.join(data_dir, number+'/test.tsv')

        gad_train_data = load_gad(train_path, header=False, train=True)
        gad_test_data = load_gad(test_path, header=True, train=False)

        canonical_data_root = args.output_dir
        if not os.path.isdir(canonical_data_root):
            os.mkdir(canonical_data_root)
        gad_train_fout = os.path.join(canonical_data_root, 'gad'+number+'_train.tsv')
        gad_test_fout = os.path.join(canonical_data_root, 'gad'+number+'_test.tsv')

        dump_rows(gad_train_data, gad_train_fout, DataFormat.PremiseOnly)
        dump_rows(gad_test_data, gad_test_fout, DataFormat.PremiseOnly)


if __name__ == '__main__':
    args = parse_args()
    main(args)