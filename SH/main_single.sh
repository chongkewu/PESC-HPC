#!/bin/bash
###Author:Chongke Wu Date:Nov 15 University of Arizona
cd /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint
exp_folder="toy-fast-slow"
Num=100
Time=20
###cleanup experiment
#python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/cleanup.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder  
#sleep 3s
###run_exp
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/main.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder
###look_result
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/print_all_results.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder
################################################################################
###look_curve
echo "Check the current result, may be program still running"
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/visualizations/progress_curve.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder
sleep 3s
###open_curve
xdg-open /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder/plots/error.pdf


