Unix Machine used- cs1.utdallas.edu
Name- Nidhi Jawandhia NetID- NXJ190011

#The code is written in Python 3.7.3
Overview: 
Processed and arguments
A network having processes as nodes and files as channels is simulated. Maximum we can have 10 nodes in the network numbered from 0 to 9.
Each process takes following inputs:
1. id the source node.
2. destination id of the process to which the node should send data.
3. a string of arbitrary text that the node will send to the destination.
4. Time at which it should transfer the string to the destination.

There is a single program (taking assistance from controller). There is a process called controller.py. It is a special process which is described below.

Communication Model and Files:
A wireless network is modelled. Each node with id X opens two text files fromX.txt and toX.txt. When X sends a message it appends it to from.txt. Hence at the end of execution, fromX.txt contains all the messages sent by X.
Messages are seperated by a new line.

A node is not aware about its neighbours. Controller is the one which is aware of the entire topology at all times. 
Before execution a topology.txt file is created which contains the topology of the network. It contains lines in the following format:

time status node1 node2

If the status is UP then the link is active from node1 to node2. If a link is birectional at any time t, then two entries must be present in the topology.txt file as follows:
t UP node1 node2
t UP node2 node1

Please note that the topology.txt file needs to be sorted by node1.

Working of the code:
Routing of messages are done by the concepts of OLSR protocol.
As stated, controller is aware of the network topology at all times. So, controller sends a list of all the neighbours of a node whenever it is asked for. Every 5 seconds, a node sends a HELLO MESSAGE to all it's neighbours and append it to it's fromX.txt file. This means that if at time t, node Y is a neighbour to node X then Y receives a HELLO MESSAGE from X. X will append this entry in it's fromX.txt file. The format of the appended hello message in fromX.txt file is:

destinationID HELLO MESSAGE

Now the controller reads the file fromX.txt and writes the message to toY.txt file. The format for appended hello message in toY.txt file is:

sourceid HELLO MESSAGE

Every 5 seconds the topology of the network may also change. So after every 5 seconds the controller finds the MPRs for all the nodes and stores in their respective MPRX.txt files. MPRs are obtained by the following algorithm.

Step1: Controller finds all the isolated 2-hop neighbours of the source node. All 1-hop nighbours which are connected to isolated 2-hop neighbours become         the MPRs.
Step2: Controller then finds the 1-hop neighbour which is connected to maximum remaining 2-hop neighbours. Such 1-hop neighbours too become the MPRs of the         source node.


When a node needs to send data to any destination node, it sends an empty routing list to the controller asking for the route to the corresponding destination node. Controller finds the route to the destination using the MPRs and return it to the source node. Source node uses this route list to send the data to the destination. Source node writes the message in it's fromX.txt file in the following format:

destinationid Message

Then it asks the controller to carry the mesage to the destination i.e.. it asks the controller to write the message in the toX.txt files for all the relays as well as the destination.
In this way destination receives the message.s

 
