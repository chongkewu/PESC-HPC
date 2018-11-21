# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:20:53 2018

@author: 44266
"""
import linecache
import matplotlib.pyplot as plt
def plot_EMFP(foldername):
    # plot Minimum Feasible Expected mean value w.r.t evaluate number
    EMFP = [] # expected mean with feasible probability 
    numlist = []
    EvID = []
    with open(foldername+"/main.log",'r') as file: 
        for (num,line) in enumerate(file):
            if line[0:16] == "Minimum expected":
                EMFP.append(float(line[-9:-1]))
                numlist.append(num)
    EMFP = EMFP[0:-1]
    numlist = numlist[0:-1]
    for num in numlist:
        for i in range(5):   # scan more lines 
            temp = linecache.getline(foldername+"/main.log",num-7-i)
            if temp[0:2] == "ID":
                EvID.append(float(temp[31:-1]))  
    # begin plot
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
def get_cost_axis(foldername):
    # get task execution sequence
    task_seq = []
    with open(foldername+"/main.log",'r') as file: 
        for line in file: 
            if line[0:2] == "ID":
                # find colon place:
                c_ind = line.find(':')
                task_seq.append(line[28:c_ind])
    # transfer it to cost
    cost = [1,1]
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
    return cost_axis

def match_cost(EvID,cost_axis):
    Ev_cost = [1]*len(EvID)
    for (num,ID) in enumerate(EvID):
        Ev_cost[num] = cost_axis[int(ID)]
    return Ev_cost
        
    
    
    
if __name__ == "__main__":
    plot_EMFP("output_rosen_d")