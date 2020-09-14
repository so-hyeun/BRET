import os
import argparse
from sys import path
path.append(os.getcwd())
from data_utils.task_def import DataFormat
from data_utils.log_wrapper import create_logger
from experiments.chemprot_new.chemprot_utils import load_chemprot
from experiments.common_utils import dump_rows
#logger = create_logger(__name__, to_disk=True, log_file='bert_chemprot_data_proc_512_cased.log')

def parse_args():
    parser = argparse.ArgumentParser(description='Preprocessing English chemprot dataset.')
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

    train_path = os.path.join(data_dir, 'trainingPosit_chem')
    dev_path = os.path.join(data_dir, 'developPosit_chem')
    test_path = os.path.join(data_dir, 'testPosit_chem')

    chemprot_train_data = load_chemprot(train_path)
    chemprot_dev_data = load_chemprot(dev_path)
    chemprot_test_data = load_chemprot(test_path)
    #logger.info('Loaded {} ChemProt train samples'.format(len(chemprot_train_data)))
    #logger.info('Loaded {} ChemProt dev samples'.format(len(chemprot_dev_data)))
    #logger.info('Loaded {} ChemProt test samples'.format(len(chemprot_test_data)))

    canonical_data_root = args.output_dir
    if not os.path.isdir(canonical_data_root):
        os.mkdir(canonical_data_root)
    chemprot_train_fout = os.path.join(canonical_data_root, 'chemprot_new_train.tsv')
    chemprot_dev_fout = os.path.join(canonical_data_root, 'chemprot_new_dev.tsv')
    chemprot_test_fout = os.path.join(canonical_data_root, 'chemprot_new_test.tsv')
    
    dump_rows(chemprot_train_data, chemprot_train_fout, DataFormat.PremiseOnly)
    dump_rows(chemprot_dev_data, chemprot_dev_fout, DataFormat.PremiseOnly)
    dump_rows(chemprot_test_data, chemprot_test_fout, DataFormat.PremiseOnly)
    #logger.info('done with ChemProt')


if __name__ == '__main__':
    args = parse_args()
    main(args)