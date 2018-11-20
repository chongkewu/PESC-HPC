#!/bin/bash
#python main.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/simples
cd /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/
exp_folder="rosen"
Num="100"
#python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/cleanup.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder
##cleanup multiple experiments
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/cleanup_experiments.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder $Num
