import os
import argparse
from sys import path
path.append(os.getcwd())
import sys
sys.path.insert(1, 'dl/')
from data_utils.task_def import DataFormat
from data_utils.log_wrapper import create_logger
from experiments.ddi.ddi_utils import load_ddi
from experiments.common_utils import dump_rows
logger = create_logger(__name__, to_disk=True, log_file='bert_disease_data_proc_512_cased.log')

def parse_args():
    parser = argparse.ArgumentParser(description='DDI prepro')
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--seed', type=int, default=13)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()
    return args

def main(args):
    data_dir = args.data_dir
    #data_dir = os.path.abspath(data_dir)
    #if not os.path.isdir(data_dir):
    #    os.mkdir(data_dir)
    print(data_dir)
    #ddi_train_path = os.path.join(data_dir, 'ddi2013-type/train.tsv')
    #ddi_dev_path = os.path.join(data_dir, 'ddi2013-type/dev.tsv')
    #ddi_test_path = os.path.join(data_dir)
    ddi_test_path = "dl/"+data_dir
    #ddi_train_data = load_ddi(ddi_train_path)
    #ddi_dev_data = load_ddi(ddi_dev_path)
    ddi_test_data = load_ddi(ddi_test_path)
    #logger.info('Loaded {} ddi2013-type train samples'.format(len(ddi_train_data)))
    #logger.info('Loaded {} ddi2013-type dev samples'.format(len(ddi_dev_data)))
    logger.info('Loaded {} ddi2013-type test samples'.format(len(ddi_test_data))) 
    
    
    
    bert_root = "dl/"+args.output_dir
    #if not os.path.isdir(bert_root):
    #    os.mkdir(bert_root)
    
    #ddi_train_fout = os.path.join(bert_root, 'ddi_train.tsv')
    #ddi_dev_fout = os.path.join(bert_root, 'ddi_dev.tsv')
    ddi_test_fout = os.path.join(bert_root, 'ddi_test.tsv')
    
    #dump_rows(ddi_train_data, ddi_train_fout, DataFormat.PremiseOnly)
    #dump_rows(ddi_dev_data, ddi_dev_fout, DataFormat.PremiseOnly)
    dump_rows(ddi_test_data, ddi_test_fout, DataFormat.PremiseOnly)
    logger.info('done with ddi2013-type')
        
    


if __name__ == '__main__':
    args = parse_args()
    main(args)