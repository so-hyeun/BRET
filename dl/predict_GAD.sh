#! /bin/sh

DATA_DIR=$1


python dl/experiments/gad/prepro.py --data_dir ${DATA_DIR} --output_dir 'User_input/prepro_result/'
python dl/prepro_std.py --root_dir User_input/prepro_result/ --task_def experiments/gad/gad_task_def.yml 
python dl/predict.py --task_def experiments/gad/gad_task_def.yml --task gad --task_id 0 --prep_input "User_input/prepro_result/bert_base_uncased/gad_test.json" --score model_result/gad_result.json --checkpoint ckpt/GAD_finetuning/model_4.pt --with_label