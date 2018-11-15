#!/bin/bash
cd /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint
exp_folder="simple"
Num=5
Time=20
###cleanup multiple experiments
#python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/cleanup_experiments.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder $Num 
#sleep 3s
###run_exp
#python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/main.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder
###look_result
#python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/print_all_results.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder

################################################################################

###repeat_exp
python ./run_experiments.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder $Num
echo "wait $Time seconds"
sleep $Time
###look_curve
echo "Check the current result, may be program still running"
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/visualizations/progress_curve.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder --repeat=$Num
sleep 3s
###open_curve
xdg-open /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder/plots/mean_error.pdf


