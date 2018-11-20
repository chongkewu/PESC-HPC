#!/bin/bash
#python main.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/simples
exp_folder='toy-fast-slow'
Num=100
python /home/u32/chongkewu/PESC/Spearmint-PESC/spearmint/visualizations/progress_curve.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder 
xdg-open /home/u32/chongkewu/PESC/Spearmint-PESC/examples/$exp_folder/plots/error.pdf

