#!/usr/bin/python
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import setting
setting.init()
import findmap
file_dynmat=open(setting.file_dynmat,"r");
atom=setting.atom;
mode_num=atom*3;
line=file_dynmat.readline();
freq=[];
eigve=np.zeros((mode_num,mode_num),dtype=float);
mode_tick=0;
while line:
  if(line.find("FREQ")!=-1):
    for i in range(mode_num):
      freq.append(float(file_dynmat.readline()));
  elif(line.find("vibration")!=-1):
    for i in range(atom):
      line=file_dynmat.readline();
      line=line.split();
      for j in range(3):
        eigve[mode_tick][3*i+j]=float(line[j]);
    mode_tick=mode_tick+1;
  line=file_dynmat.readline();
tolerance=0.95
zero_tolerance=0.007;
for i in range(mode_num):
  tick=1;
  vector=eigve[i];
  for j in range(atom*1/5):
    for k in range(3):
      if(abs(vector[3*j+k])>zero_tolerance and abs(vector[3*0+k])>zero_tolerance and (vector[3*j+k]/vector[3*0+k]>tolerance and vector[3*j+k]/vector[3*0+k] < 1/tolerance)):
        tick=tick*1;
      elif(abs(vector[3*j+k])<zero_tolerance and abs(vector[3*0+k])<zero_tolerance):
        tick=tick*1;
      else:
        tick=tick*0;
  for j in range(atom*1/5,atom*2/5):
    for k in range(3):
      if(abs(vector[3*j+k])>zero_tolerance and abs(vector[3*atom*1/5+k])>zero_tolerance and (vector[3*j+k]/vector[3*atom*1/5+k]>tolerance and vector[3*j+k]/vector[3*atom*1/5+k] < 1/tolerance)):
        tick=tick*1;
      elif(abs(vector[3*j+k])<zero_tolerance and abs(vector[3*atom*1/5+k])<zero_tolerance):
        tick=tick*1;
      else:
        tick=tick*0;
  for j in setting.oxygen1:
    bench=setting.oxygen1[0];
    for k in range(3):
      if(abs(vector[3*j+k])>zero_tolerance and abs(vector[bench*3+k])>zero_tolerance and (vector[3*j+k]/vector[3*bench+k]>tolerance and vector[3*j+k]/vector[3*bench+k] < 1/tolerance)):
        tick=tick*1;
      elif(abs(vector[3*j+k])<zero_tolerance and abs(vector[3*bench+k])<zero_tolerance):
        tick=tick*1;
      else:
        tick=tick*0;
  for j in setting.oxygen2:
    bench=setting.oxygen2[0]
    for k in range(3):
      if(abs(vector[3*j+k])>zero_tolerance and abs(vector[bench*3+k])>zero_tolerance and (vector[3*j+k]/vector[bench*3+k]>tolerance and vector[3*j+k]/vector[bench*3+k] < 1/tolerance)):
        tick=tick*1;
      elif(abs(vector[3*j+k])<zero_tolerance and abs(vector[bench*3+k])<zero_tolerance):
        tick=tick*1;
      else:
        tick=tick*0;
  for j in setting.oxygen3:
    bench=setting.oxygen3[0];
    for k in range(3):
      if(abs(vector[3*j+k])>zero_tolerance and abs(vector[bench*3+k])>zero_tolerance and (vector[3*j+k]/vector[bench*3+k]>tolerance and vector[3*j+k]/vector[bench*3+k] < 1/tolerance)):
        tick=tick*1;
      elif(abs(vector[3*j+k])<zero_tolerance and abs(vector[bench*3+k])<zero_tolerance):
        tick=tick*1;
      else:
        tick=tick*0;
  if(tick==1):
    print "I got one mode: "+str(i+1)
print setting.oxygen1
print setting.oxygen2
print setting.oxygen3
