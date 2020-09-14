#! /bin/sh
python experiments/ddi/prepro.py --data_dir 'User_input/ori_input/DDI_test.tsv' --output_dir 'User_input/prepro_result/'
python prepro_std.py --root_dir User_input/prepro_result/canonical_data --task_def experiments/ddi/ddi_task_def.yml 