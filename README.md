# PESC-HPC
updated 11/4/2018 chongke wu   
Refer to the readme in https://github.com/HIPS/Spearmint/blob/master/README.md  
In HPC, you not allowed to use -- fork and sudo.  

1. How to install python packets in HPC.   
Refers to https://docs.hpc.arizona.edu/display/UAHPC/Using+and+Installing+Python.   
Use virtualenv and Set the environment in .bashrc, then you can use pip to install packets and modules. Use “vi /.bashrc” to edit it.   

2. How to install Mongod in HPC.   
Download mongod red hat version. Unzip tgz and set the environment in .bashrc. See https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/ . Don’t use .rpm Packages install because we can use sudo command in HPC, instead, use tarballs.  

3. How to run program?  
Load python 2.7:  
Module load python/2.7  
create <path/to/logfile\> and <path/to/dbfolder\>:   
/data/db  
/data/log/mylog.log  
 
Open terminal and run :  
mongod --logpath <path/to/logfile\> --dbpath <path/to/dbfolder\>.  
i.e.,  
mongod --logpath ./data/log/mylog.log  --dbpath ./data/db  
Don’t close it, open a new terminal , change directory to main.py folder and run :  
python main.py \</path/to/experiment/directory\>.  
i.e.  
python main.py /home/u32/chongkewu/PESC/Spearmint-PESC/examples/simple  

4. to original code (PESC branch).  
Scipy.weave into weave.  
Sometimes, when plot the result, the main_file in progressive_curve.py will contain ‘.py’ suffix. And it will be an error. So I add a comment of main_file[:len(main_file)-3] to delete the suffix.   
