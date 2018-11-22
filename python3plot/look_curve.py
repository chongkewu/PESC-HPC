# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:20:53 2018

@author: 44266
"""
import linecache
import matplotlib.pyplot as plt
import os
import branin_d
import rosen_d
from scipy import interpolate
import numpy as np
def plot_EMFP(foldername, getxy = False, getpltxy = False):
    # plot Minimum Feasible Expected mean value w.r.t evaluate number
    EMFP = [] # expected mean with feasible probability 
    numlist = []
    EvID = []
    xlist = []
    ylist = []
    with open(foldername+"/main.log",'r') as file: 
        for (num,line) in enumerate(file):
            if line[0:16] == "Minimum expected":
                EMFP.append(float(line[-9:-1]))
                numlist.append(num)
    EMFP = EMFP[0:-1]
    numlist = numlist[0:-1]
    for num in numlist:
        for i in range(7):   # scan more lines 
            temp = linecache.getline(foldername+"/main.log",num-7-i)
            if temp[0:2] == "ID":
                EvID.append(float(temp[31:-1])) 
            temp1 = linecache.getline(foldername+"/main.log",num-11-i)
            if temp1[0:21] == "Suggestion: task(s) f":
                tempx = linecache.getline(foldername+"/main.log",num-8-i)
                tempy = linecache.getline(foldername+"/main.log",num-7-i)
                xlist.append(tempx[-13:-5])
                ylist.append(tempy[-13:-5])
    if getxy == True:
        return xlist,ylist
    # begin plot
    if getpltxy == True:
        cost_axis = get_cost_axis(foldername)
        Ev_cost = match_cost(EvID,cost_axis)   
        return EvID,Ev_cost,EMFP        
    plt.figure()
    plt.subplot(1,2,1)
    plt.plot(EvID,EMFP)
    plt.xlabel('Number of evaluations')
    plt.ylabel('Minimum feasible expected mean')
    plt.title('PESC decoupled evaluation for '+ foldername[7:-2])
    # plot EMFP w.r.t cost
    plt.subplot(1,2,2)
    cost_axis = get_cost_axis(foldername)
    Ev_cost = match_cost(EvID,cost_axis)    
    plt.plot(Ev_cost,EMFP)
    plt.xlabel('Cost')
    plt.ylabel('Minimum feasible expected mean')
    plt.title('PESC decoupled evaluation for '+ foldername[7:-2])
def get_cost_axis(foldername, cost = [1,1], r_type = 'axis'):
    # get task execution sequence
    task_seq = []
    with open(foldername+"/main.log",'r') as file: 
        for line in file: 
            if line[0:2] == "ID":
                # find colon place:
                c_ind = line.find(':')
                task_seq.append(line[28:c_ind])
    # transfer it to cost
    cost_seq = [0]*len(task_seq)
    cost_axis = [0]*len(task_seq)
    for (num,t) in enumerate(task_seq):
        if t[0] == 'f':
            cost_seq[num] = cost[0]
        elif t[0:2] == 'c1':
            cost_seq[num] = cost[1]
        else:
            print("unkonw task name %s"%t)
    for num in range(len(task_seq)):
        cost_axis[num] = sum(cost_seq[0:num+1])
    if r_type == "axis":
        return cost_axis
    elif r_type == "seq":
        return cost_seq
    else:
        print("unknow r_type %s"%r_type)

def match_cost(EvID,cost_axis):
    Ev_cost = [1]*len(EvID)
    for (num,ID) in enumerate(EvID):
        try:
            Ev_cost[num] = cost_axis[int(ID)-1]
        except:
            print("what happen???")
            return
    return Ev_cost

def plot_util(foldername, func = 'rosen'):
    # read the objective value in .out file.
    task_list = get_cost_axis(foldername, cost = [0,1], r_type = 'seq')
    V_obj = []
    V_num = []
    obj_addr = []
    for file in os.listdir(foldername):
        if file.endswith(".out"):
            if task_list[int(file[-7:-4])-1] == 0:# the .out file is objective 
                V_num.append(int(file[-7:-4]))
                with open(foldername+'\\'+file,'r') as file1: 
                    for line in file1:
                        if line[0:10] == "Got result":
                            V_obj.append(float(line[24:-4])) 
    # get the utility
    tau = 300
    tol = 0.001
    xlist,ylist = plot_EMFP(foldername, getxy = True)
    V_obj = V_obj[len(V_obj)-len(xlist)-1:-1] #only plot after first feasible occurs
    V_num = V_num[len(V_num)-len(xlist)-1:-1]
    for num,value in enumerate(V_obj):
        if func == "branin":
            Obj = branin_d.true_func({'x': float(xlist[num]),'y': float(ylist[num])})
        elif func == "rosen":
            Obj = rosen_d.true_func({'x': float(xlist[num]),'y': float(ylist[num])})
        else:
            print("unknow func %s"%func)
            
        if Obj['c1'] < 0+tol:
            V_obj[num] = tau
        # Here tau use the definition in PESC,
        # if change tau definition, comment this branch
# =============================================================================
#         elif tau > V_obj[num]: 
#             tau = V_obj[num]
#             print(tau)
# =============================================================================
    plt.figure()
    plt.subplot(121)
    plt.plot(V_num,V_obj)
    plt.xlabel('Evaluation number')
    plt.ylabel('Utility')
    plt.title('PESC decouple evaluation for '+ func)
    # plot util w.r.t cost
    cost_axis = get_cost_axis(foldername, cost = [1,1], r_type = 'axis')
    Ev_cost = match_cost(V_num,cost_axis) 
    plt.subplot(122)
    plt.plot(Ev_cost,V_obj)
    plt.xlabel('cost')
    plt.ylabel('Utility')
    plt.title('PESC decouple evaluation for '+ func)
    
def plot_EMFP_repeat(foldername):
    # read the total number of repeat
    dirname = os.listdir(foldername)
    repeatdir = [x for x in dirname if 'output_repeat' in x]
    # for each output_repeat_* folder, read the plot data
    num_repeat = len(repeatdir)
    EvID = [1]*num_repeat
    Evcost = [1]*num_repeat
    EMFP = [1]*num_repeat
    for num in range(num_repeat):
        EvID[num],Evcost[num],EMFP[num] = plot_EMFP(foldername+'\\'+repeatdir[num]\
            ,getpltxy = True)
    # Count the total unique x points for all curves
    EMFP_cost = EMFP
    EvID_total = []
    Evcost_total = []
    for num in range(num_repeat):
        EvID_total = list(set(EvID_total + EvID[num]))
        Evcost_total = list(set(Evcost_total + Evcost[num]))
    plot_mean_err(EvID_total,EvID,EMFP,num_repeat)
    
def plot_mean_err(EvID_total,EvID,EMFP,num_repeat):
    # Now plot mean and error bar.
    Evmean = [[]]*len(EvID_total)
    Everr = [1]*len(EvID_total)
    for num,val in enumerate(EvID_total):
        for num1 in range(num_repeat):
            for num2 in range(len(EvID[num1])):
                if EvID_total[num] == EvID[num1][num2]:
                    Evmean[num] = Evmean[num]+[EMFP[num1][num2]]
                    break
        Everr[num] = np.std(np.array(Evmean[num], np.float))
        
        Evmean[num] = np.mean(np.array(Evmean[num], np.float))#update Evmean
        
    plt.figure()
    plt.errorbar(EvID_total, Evmean, yerr=Evmean, fmt='-o')
                    
if __name__ == "__main__":
    
# =============================================================================
#     Usage example:
#     funcname = "branin"
#     foldername = "output_" + funcname + "_d"
#     plot_util(foldername, func = funcname)
#     plot_EMFP(foldername)
# =============================================================================
    funcname = "branin"
    foldername = "output_" + funcname + "_d" + "_repeat"
    plot_EMFP_repeat(foldername)
    #plot_EMFP(foldername+'//'+'output_repeat_0')