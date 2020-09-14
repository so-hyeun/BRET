#! /bin/sh
python experiments/GAD/gad_prepro.py
python prepro_std.py --model bert-base-uncased --root_dir bert_data/canonical_data --task_def experiments/blue/blue_task_def.yml --do_lower_case $1
