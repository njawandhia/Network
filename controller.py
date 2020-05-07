# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:08:31 2020

@author: jawandhia
"""

#controller process
#read topology file
import os
def tellneigh(t,sid):
    if t%5 !=0:
        var=int(t/5);
        t=5*var;
    f=open('topology.txt','r');
    top=f.read();
    #print('top')
    f.close()
    i=0;neighbours=[];
    while(top.find('%s UP %s' %(t,sid),i,len(top)) != -1):
        z=top.find('%s UP %s' %(t,sid),i,len(top));
        #if top[z-1]=='\n' or z==0:
        #print(z)
        i=z+1;
        #j=j+1;
        if top[z-1]=='\n' or z==0:
            while(top[z]!='\n'):
                z=z+1
        #print(z)    
            neighbours.append(top[z-1])
        #j=j+1
    return neighbours

def findingmpr(t):
    node=0;
    while(node<=9):
        if os.path.exists('MPR%s.txt' %node):
                f=open('MPR%s.txt' %node,'r+')
                f.truncate(0);
                f.close();
        #finding 1 hop neighbour of node
        neighbour=tellneigh(t, node)
        #print(neighbour)
        #finding 2 hop neighbour of node
        secneigh=[];
        for i in neighbour:
            secneigh=secneigh+tellneigh(t,i);
        #print(secneigh)
        for i in secneigh:
            j=0;count=0;
            while j<len(secneigh):
                if i==secneigh[j]:
                    count=count+1;
                j=j+1;
            if count==1:
                #print('%s is an isolated 2 hop neighbour of %s' %(i,node));
                mprneigh=tellneigh(t,i)
                f=open('MPR%s.txt' %node,'a');
                f.write('%s' %list(set(mprneigh).intersection(neighbour)));f.write('\n');
                f.close();
                #secneigh.remove(i);
        
        #finding the MPR for non isolated nodes.
        for i in secneigh:
            j=0;count=0;
            while(j<len(secneigh)):
                if i==secneigh[j]:
                    count=count+1;
                j=j+1;
            if count>1 and i != node:
                MPRneigh=tellneigh(t,i);
                x=list(set(MPRneigh).intersection(neighbour));
                f=open('MPR%s.txt' %node,'r');
                y=list(f.read());f.close();
                z=[];
                if list(set(x).intersection(y))==[]:
                    for k in x:
                        z.append(len(tellneigh(t,k)));
                    maxindex=z.index(max(z));
                    f=open('MPR%s.txt' %node,'a');
                    f.write('%s' %x[maxindex]);f.write('\n');
                    f.close();
        node=node+1            
                
                

def writetofile(sid,neigh):
    f=open('from%s.txt' %sid,'r')
    #read last line of the form_sid.txt file
    top=f.read()
    #print(top)
    f.close()
    i=len(top)-2;last_line='';
    while(top[i]!='\n'):
        i=i-1;
    for j in range(i+1,len(top)):
        last_line=last_line+top[j];
    #print('printing last line');print(last_line)    
    #last_line contains the recently added line in fromsid.txt
    #last_line first conatins the DID of packet and then the message.
    #Extracring message from last_line.
    msg=last_line[2:];
    #However controller will write the message in toneigh.txt files.
    f=open('to%s.txt' %neigh,'a');
    f.write('%s %s' %(sid,msg));f.write('\n');
    f.close();

def route(t,sid,did,kaarwan):
    checker='false'
    neighbour=tellneigh(t,sid);
    if did in neighbour:
        kaarwan.append(sid)
        kaarwan.append(did)
        return kaarwan
    else:
        kaarwan.insert(0,did)
        while checker !='true':
            #print(did)
            f=open('MPR%s.txt' %did, 'r');
            l=list(f.read());
            if list(set(l).intersection(neighbour))!=[]:
                kaarwan=list(set(l).intersection(neighbour))+kaarwan
                checker='true'
                kaarwan.insert(0,sid);
                #kaarwan.append(did)
                #kaarwan.append(DID)
                return kaarwan;
            else:
                for i in l:
                    if i!='\n' and i != '[' and i!=']' and i!=' ' and i!="'":
                        # kaarwan.insert(0,i);
                        return route(t,sid,i,kaarwan);

        
        

    