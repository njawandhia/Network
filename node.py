# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:35:16 2020

@author: user
"""

import controller, time
def current_time(s):
    return int(time.time()-s)

def main():
    #n=input("Enter the number of nodes");
    sid=input("Enter Source ID");
    did=input("Enter destination id");
    msg=str(input("Enter your message"));
    t=int(input("Enter the time at which message must be sent"));
    #print(t)
    #start=time.time()
    #current=current_time(start);
    i=0;
    while i<120:
        if i%5==0:
            #flooding hello message
            node=0;
            while node<=9:
                #getting the list of neighbours of node
                neighbour=controller.tellneigh(i,node);
                print(neighbour)
                for j in neighbour:
                    f=open('from%s.txt' %node,'a');
                    #writing hello message to neighbour.
                    f.write('%s HELLO MESSAGE' %j);f.write('\n');
                    f.close();
                    #giving control to cintroller for writing in toX.txt files.
                    controller.writetofile(node,j);
                node=node+1;
                #Updating the MPR file for each node.
            controller.findingmpr(i);    
        #if t!=i:
         #   time.sleep(t-current_time(start));
        if t==i:
            print("Message can be sent now");
            #getting the route to deliver the message.
           # print(did)
            #raasta=controller.route(t,sid,did)
            #print(raasta)
            #f=open("from%s.txt" %sid, 'a');
            #f.write(did+' '+msg);f.write('\n')
            #f.close();
            
        i=i+1;
        time.sleep(1);
            
     
if __name__=='__main__':
    main()