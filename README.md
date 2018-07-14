# Maekawa
This project is an implementation of Maekawa Algorithm for distributed systems, where we have 10 sites which coordinate to access the critical section

Authors : Bouroudi Abdelmounaim (ea_bouroudi@esi.dz); Haneche Abderrahim (ea_haneche@esi.dz); Oukhenniche Abdelkrim(da_oukhenniche@esi.dz)

The request sets for each site are disgned to respect diffrents Maekawa conditions for running the algorithm.
Following is a proposition of the 10 request sets with 4 site in each request set :

S_1= {1,2,3,4}
S_2= {2,5,8,4}
S_3= {3,6,8,7}
S_4= {4,6,10,1}
S_5= {1,5,6,7}
S_6= {2,6,9,5}
S_7= {2,7,10,8}
S_8= {1,8,9,10}
S_9= {3,7,9,4}
S_10= {3,5,10,9}


This project has to part :
front-end :
  written in php and using boostrap in the front-end, we used php to read from a file the results returned by the algorithm in python
back-end :
  written in python and after some changes made to use the request sets we created we have based on https://github.com/longislandicetea/Maekawa-Mutex work that was really well concepted 

To communicate between the front and the office we used a folder in which we have a file for each message returned by the back-end written in a json format where we specify the global timestamp, the thread id, the source of the message, the message type, the local timestamp of the site and the message itself like it was sent.

For each message we have a file .txt where it's written and ones the front-side read that file and show the message on web page it delete it and pass to the next file and so on.


To run this project you should run the two parts : front and back end 
front-end : just start the php server (apache for exemple) and lunch the page : index.html
back-end : just type : $> python mutex.py 
