#!/home/jiahaoz/miniconda2/bin/python
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import setting
ph_file=open(setting.ph_file,"r");
line=ph_file.readline();
atom=setting.atom;
record=np.zeros((atom*3/5,3),dtype=float);
oxygen_map=np.zeros((atom*3/5,2),dtype=int);
while line:
	if(line.find("site n.  atom      mass           positions (alat units)")!=-1):
		mark=0;
		for i in range(atom):
			line=ph_file.readline();
			if(line.find("O")!=-1):
				line=line.split();
				record[mark][0]=float(line[-4]);
				record[mark][1]=float(line[-3]);
				record[mark][2]=float(line[-2]);
				oxygen_map[mark][0]=mark;
				oxygen_map[mark][1]=float(line[0]);
				mark=mark+1;
	line=ph_file.readline();
"""End reading process, starting to process information"""
"""O1=[0.25,0.25,0.0],O2=[0.0,0.25,0.25],O3=[0.25,0.0,0.25]"""
type1=[];
type2=[];
type3=[];
for i in range(atom*3/5):
	temp=[0.0,0.0,0.0];
	for j in range(2):
		for k in range(2):
			for l in range(2):
				temp[0]=record[i][0]+j*0.5;
				temp[1]=record[i][1]+k*0.5;
				temp[2]=record[i][2]+l*0.5;
				for m in range(3):
					temp[m]=temp[m]*4;
					temp[m]=round(temp[m]);
					temp[m]=temp[m]%4;
				if(temp[0]==1 and temp[1]==1 and temp[2]==0):
					type1.append(i);
				elif(temp[0]==0 and temp[1]==1 and temp[2]==1):
					type2.append(i);
				elif(temp[0]==1 and temp[1]==0 and temp[2]==1):
					type3.append(i);
setting.oxygen1=[];
setting.oxygen2=[];
setting.oxygen3=[];
for i in type1:
	setting.oxygen1.append(oxygen_map[i][1]-1);
for i in type2:
	setting.oxygen2.append(oxygen_map[i][1]-1);
for i in type3:
	setting.oxygen3.append(oxygen_map[i][1]-1);
