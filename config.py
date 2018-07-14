"""program configuration

NUM_NODE: number of nodes
INIT_PORT: port number of the first node
		   (I assuem node ports are consecutive, you could 
		   	certainly choose whatever ports you like)
RECV_BUFFER: socket buffer size when receiving messages

"""


NUM_NODE = 10
INIT_PORT = 3000
NODE_PORT = [(INIT_PORT + i) for i in xrange(NUM_NODE)]
RECV_BUFFER = 4096
list = []
list.append({0:None,1:None,2:None,3:None})
list.append({1:None,4:None,7:None,3:None})
list.append({2:None,5:None,7:None,6:None})
list.append({3:None,5:None,9:None,0:None})
list.append({0:None,4:None,5:None,6:None})
list.append({1:None,5:None,8:None,4:None})
list.append({1:None,6:None,9:None,7:None})
list.append({0:None,7:None,8:None,9:None})
list.append({2:None,6:None,8:None,3:None})
list.append({2:None,4:None,9:None,5:None})
REQUEST_SETS = list