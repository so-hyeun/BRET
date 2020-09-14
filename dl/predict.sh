#! /bin/sh

DATA_DIR=$1

python dl/experiments/ddi/prepro.py --data_dir ${DATA_DIR} --output_dir 'User_input/prepro_result/'
python dl/prepro_std.py --root_dir User_input/prepro_result/ --task_def experiments/ddi/ddi_task_def.yml 
python dl/predict.py --task_def experiments/ddi/ddi_task_def.yml --task ddi --task_id 0 --prep_input User_input/prepro_result/bert_base_uncased/ddi_test.json --cuda false --score model_result/ddi_result.json --checkpoint ckpt/DDI_finetuning/model_4.pt --with_label
