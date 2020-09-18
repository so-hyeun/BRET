#! /bin/sh

DATA_DIR=$1

python dl/experiments/chemprot_new/prepro.py --data_dir ${DATA_DIR} --output_dir 'User_input/prepro_result/'
python dl/prepro_std.py --root_dir User_input/prepro_result/ --task_def experiments/chemprot_new/chemprot_task_def.yml 
python dl/predict.py --task_def experiments/chemprot_new/chemprot_task_def.yml --task chemprot_new --task_id 0 --prep_input "User_input/prepro_result/bert_base_uncased/chemprot_test.json" --score model_result/chemprot_result.json --checkpoint ckpt/Chemprot_finetuning/model_4.pt --with_label
