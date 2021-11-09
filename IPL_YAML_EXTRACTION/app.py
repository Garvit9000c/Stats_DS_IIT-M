import os
import yaml
import json
import pandas as pd 

directory = './ipl_yaml'
csv={'date':[], 'venue':[], 'innings':[], 'target':[], 'team':[], '0.1': [], '0.2': [], '0.3': [], '0.4': [], '0.5': [], '0.6': [], '0.7': [], '0.8': [], '0.9': [], '0.10': [], '0.11': [], '0.12': [], 'd1': [], 'r1': [], 'w1': [], '1.1': [], '1.2': [], '1.3': [], '1.4': [], '1.5': [], '1.6': [], '1.7': [], '1.8': [], '1.9': [], '1.10': [], '1.11': [], '1.12': [], 'd2': [], 'r2': [], 'w2': [], '2.1': [], '2.2': [], '2.3': [], '2.4': [], '2.5': [], '2.6': [], '2.7': [], '2.8': [], '2.9': [], '2.10': [], '2.11': [], '2.12': [], 'd3': [], 'r3': [], 'w3': [], '3.1': [], '3.2': [], '3.3': [], '3.4': [], '3.5': [], '3.6': [], '3.7': [], '3.8': [], '3.9': [], '3.10': [], '3.11': [], '3.12': [], 'd4': [], 'r4': [], 'w4': [], '4.1': [], '4.2': [], '4.3': [], '4.4': [], '4.5': [], '4.6': [], '4.7': [], '4.8': [], '4.9': [], '4.10': [], '4.11': [], '4.12': [], 'd5': [], 'r5': [], 'w5': [], '5.1': [], '5.2': [], '5.3': [], '5.4': [], '5.5': [], '5.6': [], '5.7': [], '5.8': [], '5.9': [], '5.10': [], '5.11': [], '5.12': [], 'd6': [], 'r6': [], 'w6': []}


def extract(inn):
   score={}
   Max=0
   key=['0','1','2','3','4','5']
   val=['.1','.2','.3','.4','.5','.6','.7','.8','.9','.10','.11','.12']
   data={}
   
   for i in inn['deliveries']:
       ball=list(i.keys())
       ball=ball[0]
       score[str(ball)]=[i[ball]['runs']['total'],0]
       Max+=i[ball]['runs']['total']
       try:
           i[k]['wicket']
           score[str(k)][1]=1
       except:
           pass
           
   for i in key:
       delivery,runs,wickets=0,0,0
       for j in val:
           index=i+j
           try:
               s=score[index]
               data[index]=s[0]
               delivery+=1
               runs+=s[0]
               wickets+=s[1]
           except:
               data[index]=''
       data['d'+str(int(i)+1)]=delivery
       data['r'+str(int(i)+1)]=runs
       data['w'+str(int(i)+1)]=wickets   
                  
   return data,Max

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    row1,row2={},{}
    if os.path.isfile(f):
        print('Processing : ',f)
        with open(f, 'r') as stream:
            data = yaml.safe_load(stream)
        row1['date']=row2['date']=data['info']['dates'][0]
        row1['venue']=row2['venue']=data['info']['venue']
        if len(data['innings'])==2:
            inn1=data['innings'][0]['1st innings']
            score1,target1=extract(inn1)
            row1['innings']=1
            row1['target']=''
            row1['team']=inn1['team']
            row1.update(score1)
            inn2=data['innings'][1]['2nd innings']
            score2,target2=extract(inn2)
            row2['innings']=2
            row2['target']=target2
            row2['team']=inn2['team']
            row2.update(score2)
            for i in csv:
                csv[i].append(row1[i])
                csv[i].append(row2[i])
  
df = pd.DataFrame(csv)
df.to_csv('ipl.csv') 

